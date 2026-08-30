#!/usr/bin/env node
/**
 * PostToolUse hook (Write|Edit|MultiEdit) — build-time security lint.
 *
 * Reads the just-written code from the hook payload and flags high-signal
 * insecure patterns so they get fixed in the same session, not shipped.
 * Advisory only: prints findings to stderr, never blocks. Fast, no deps.
 */
"use strict";

let raw = "";
process.stdin.setEncoding("utf8");
process.stdin.on("data", (c) => (raw += c));
process.stdin.on("end", () => {
  let payload;
  try { payload = JSON.parse(raw); } catch { return; }

  const ti = payload.tool_input || payload.toolInput || {};
  const path = ti.file_path || ti.path || "";
  // skip non-code files
  if (path && !/\.(js|jsx|ts|tsx|py|rb|go|java|php|cs|sql|env|yml|yaml|json|astro|svelte|vue)$/i.test(path)) return;
  if (/\.(test|spec)\./i.test(path) || /[\\/](test|tests|__tests__|spec)[\\/]/i.test(path)) return;

  let code = "";
  if (typeof ti.content === "string") code += ti.content + "\n";
  if (typeof ti.new_string === "string") code += ti.new_string + "\n";
  if (Array.isArray(ti.edits)) for (const e of ti.edits) if (e && typeof e.new_string === "string") code += e.new_string + "\n";
  if (!code.trim()) return;

  const findings = [];
  const add = (msg) => findings.push(msg);

  // --- secrets ---
  if (/(?:api[_-]?key|secret|password|passwd|token|client[_-]?secret|private[_-]?key)\s*[:=]\s*["'][A-Za-z0-9_\-\/+]{12,}["']/i.test(code)
      && !/process\.env|os\.environ|import\.meta\.env|getenv|Deno\.env|config\.|example|placeholder|your[_-]?key|xxx/i.test(code)) {
    add("possible hardcoded secret — move to env / secret store, never commit");
  }
  if (/(?:sk_live_|pk_live_|AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{36}|xox[baprs]-)/.test(code)) {
    add("live credential / provider token literal detected — rotate it and use env");
  }

  // --- SQL injection ---
  if (/(?:SELECT|INSERT|UPDATE|DELETE)\s+.*(?:\+\s*(?:req|request|params|query|body|input|user)|\$\{(?:req|params|query|body|input|user|id|name|email)|%\s*\((?:req|user|id))/is.test(code)
      || /(?:query|execute|raw)\s*\(\s*[`"'][^`"']*(?:SELECT|INSERT|UPDATE|DELETE)[^`"']*\$\{/is.test(code)) {
    add("SQL built with string interpolation of input — use parameterized queries / ORM bindings");
  }

  // --- XSS ---
  if (/dangerouslySetInnerHTML|v-html|\.innerHTML\s*=|insertAdjacentHTML\s*\(|document\.write\s*\(/.test(code)
      && !/DOMPurify|sanitize/i.test(code)) {
    add("raw HTML injection sink without sanitizer — DOMPurify or avoid; keep framework escaping");
  }

  // --- CORS ---
  if (/Access-Control-Allow-Origin["'\s:]+\*/.test(code) && /credentials|Allow-Credentials|withCredentials|cookie/i.test(code)) {
    add("CORS '*' with credentials — use an explicit origin allow-list");
  }
  if (/cors\(\s*\)/.test(code) || /origin\s*:\s*true/.test(code)) {
    add("permissive CORS (all origins) — scope to known origins if this endpoint is authenticated");
  }

  // --- command injection ---
  if (/(?:child_process|exec|execSync|spawn|os\.system|subprocess\.(?:call|run|Popen)|Runtime\.getRuntime)\b/.test(code)
      && /(?:\+\s*(?:req|params|query|body|input|user)|\$\{(?:req|params|query|body|input|user)|shell\s*[:=]\s*true|shell=True)/i.test(code)) {
    add("shell command with interpolated input — execFile + args array + allow-list, no shell");
  }

  // --- webhook signature ---
  if (/webhook|\/hooks?\/|stripe|paddle|lemonsqueezy|razorpay|paypal/i.test(code)
      && /(?:app\.(post|put)|router\.(post|put)|export (async )?function (POST|PUT)|@app\.(post|route))/i.test(code)
      && !/constructEvent|verify(Signature|Header|Webhook)?|hmac|createHmac|signature|svix|X-Hub-Signature|stripe-signature/i.test(code)) {
    add("webhook/payment POST handler with no visible signature verification — verify before trusting the body");
  }

  // --- auth / access control smell ---
  if (/(?:app\.(get|post|put|delete|patch)|router\.(get|post|put|delete|patch)|@(app|router)\.(get|post|put|delete))/i.test(code)
      && /(?:findById|findOne|findUnique|SELECT .* WHERE id|get\(id\)|\.get\(.*id)/i.test(code)
      && !/(?:userId|user_id|org_id|orgId|tenant_id|tenantId|owner|session\.|req\.user|ctx\.user|current_user|auth\.)/i.test(code)) {
    add("resource fetched by id with no owner/tenant/session scoping visible — possible IDOR");
  }

  // --- fail-open / stack trace leak ---
  if (/catch\s*\([^)]*\)\s*\{\s*(?:res|response)\.(?:status\([^)]*\)\.)?(?:send|json)\s*\(\s*(?:err|error|e)\b/i.test(code)) {
    add("error object sent to the client — leaks stack/internals; return a generic message, log server-side");
  }

  // --- md5/sha for passwords ---
  if (/(?:createHash\(\s*["'](?:md5|sha1|sha256)["']|hashlib\.(?:md5|sha1|sha256))/i.test(code) && /password|passwd|pwd/i.test(code)) {
    add("fast hash used on a password — use argon2id or bcrypt");
  }

  if (findings.length) {
    process.stderr.write(
      "\n[secure-write-scan] advisory — review before continuing" +
      (path ? "  (" + path + ")" : "") + ":\n" +
      findings.map((f) => "  • " + f).join("\n") +
      "\n  → load `secure-by-default` and fix in this diff; run `security-audit` Phase 0 before shipping.\n"
    );
  }
});
