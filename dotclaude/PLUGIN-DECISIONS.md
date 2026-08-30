# Plugin Decisions

Plugins remain disabled by default until they pass a Windows smoke test and
have a non-overlapping responsibility.

| Plugin | Decision | Reason |
| --- | --- | --- |
| `claude-mem@thedotmack` | Disabled | Overlaps auto memory, telemetry, history, and Second Brain; its hooks are Unix-heavy and broad |
| `andrej-karpathy-skills@karpathy-skills` | Disabled | Its guidance is already represented in global instructions and live skills |
| `superpowers@claude-plugins-official` | Disabled | Overlaps GSD workflow and guard surfaces |
| `vercel@claude-plugins-official` | Disabled | Enable only for a project that actively uses Vercel tooling |

Enable one explicitly after testing:

```powershell
claude plugin enable <plugin-name> --scope user
```

Do not enable Claude-Mem globally until memory ownership and retention policy
are approved. Do not enable multiple broad lifecycle-hook plugins together.
