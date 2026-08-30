---
name: auth-micro-animations
description: "OTP input micro-animations (verified ring, seal fusion) extracted from Instagram reels. Use for: 'OTP animation', 'verified badge animation', 'auth flow polish'"
---

# Auth Micro-Animations Skill

Real micro-animations for OTP input flows, extracted from _code_and_chill_ Instagram reels (Hasibul Hasan).

## When to Use This Skill

- Building OTP verification flows (email, SMS, 2FA)
- Polishing login/auth pages with delightful state transitions
- Creating verified badges or checkmark animations
- Adding motion to multi-step auth forms

## Two Techniques

### 1. OTP Ring (DbxxWJnoR2L) — Last Digit Curls Into Verified Ring

**Visual:** User types 4th digit → box transforms 3D into spinning ring with checkmark.

**Tech Stack:** CSS 3D transforms (no JS required)  
**Duration:** 600ms total (400ms curl + 200ms spin setup)

**Copy-Paste CSS:**
```css
/* OTP boxes container */
.otp-container {
  display: flex;
  gap: 8px;
}

/* Individual OTP box */
.otp-input {
  width: 48px;
  height: 48px;
  border: 2px solid #d1d5db;
  border-radius: 8px;
  text-align: center;
  font-size: 24px;
  font-weight: bold;
  perspective: 1000px;
}

/* On all 4 filled, add this to last box */
.otp-input.completed {
  animation: curlIntoRing 600ms cubic-bezier(0.68, -0.55, 0.265, 1.55) forwards;
  border: none;
  background: #10b981;
  color: white;
}

@keyframes curlIntoRing {
  0% {
    transform: rotateY(0deg);
    border-color: #d1d5db;
    background: transparent;
  }
  100% {
    transform: rotateY(180deg) scale(1.1);
    background: #10b981;
    border: none;
  }
}

/* Checkmark appears in the ring */
.otp-input.completed::after {
  content: '✓';
  position: absolute;
  font-size: 28px;
  color: white;
  font-weight: bold;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  animation: checkmarkFade 600ms ease-out forwards;
}

@keyframes checkmarkFade {
  0% { opacity: 0; scale: 0.5; }
  60% { opacity: 0; }
  100% { opacity: 1; scale: 1; }
}

/* Continuous spin after formation */
@keyframes spinRing {
  to { transform: rotateY(180deg) rotateZ(360deg); }
}

.otp-input.completed {
  animation: curlIntoRing 600ms cubic-bezier(0.68, -0.55, 0.265, 1.55) forwards,
             spinRing 1.2s linear 600ms infinite;
}
```

**Trigger:** JavaScript detects all 4 boxes filled
```javascript
const inputs = document.querySelectorAll('.otp-input');
const lastInput = inputs[3];
if (inputs.every(i => i.value)) {
  lastInput.classList.add('completed');
  // Or trigger API call
}
```

---

### 2. OTP Seal (DbbNr-SvJkK) — Boxes Fuse Into Violet→Aqua Seal

**Visual:** All 4 OTP boxes collapse to center, fuse into spinning gradient seal, color shifts violet → aqua.

**Tech Stack:** CSS transforms + gradients (pure CSS animation)  
**Duration:** 1000ms total

**Copy-Paste CSS:**
```css
/* Container for OTP boxes that will fuse */
.otp-container.sealing {
  position: relative;
  width: 64px;
  height: 64px;
  margin: 0 auto;
}

/* Boxes during fusion */
.otp-container.sealing .otp-input {
  position: absolute;
  width: 48px;
  height: 48px;
  animation: fuseToCenter 600ms ease-in-out forwards;
}

/* Each box moves to center point */
@keyframes fuseToCenter {
  0% {
    opacity: 1;
    transform: translate(0, 0);
  }
  100% {
    opacity: 0;
    transform: translate(-20px, -20px) scale(0);
  }
}

/* Seal pseudo-element replaces boxes */
.otp-container.sealing::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 64px;
  height: 64px;
  border-radius: 50%;
  background: linear-gradient(135deg, #8b5cf6 0%, #06b6d4 100%);
  animation: sealBirth 400ms cubic-bezier(0.34, 1.56, 0.64, 1) 200ms forwards,
             sealPulse 2s ease-in-out 600ms infinite;
  opacity: 0;
}

/* Seal grows from nothing */
@keyframes sealBirth {
  0% {
    opacity: 0;
    scale: 0;
  }
  100% {
    opacity: 1;
    scale: 1;
  }
}

/* Seal pulses subtly */
@keyframes sealPulse {
  0%, 100% { scale: 1; }
  50% { scale: 1.08; }
}

/* Checkmark inside seal */
.otp-container.sealing::before {
  content: '✓';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 36px;
  color: white;
  font-weight: bold;
  opacity: 0;
  animation: checkmarkAppear 300ms ease-out 600ms forwards;
  z-index: 1;
}

@keyframes checkmarkAppear {
  0% {
    opacity: 0;
    scale: 0.3;
  }
  100% {
    opacity: 1;
    scale: 1;
  }
}
```

**Trigger:**
```javascript
const container = document.querySelector('.otp-container');
if (allFieldsFilled()) {
  container.classList.add('sealing');
}
```

---

## Implementation Guide

### 1. Setup

```html
<!-- OTP Input Form -->
<div class="otp-container">
  <input type="text" class="otp-input" maxlength="1" data-index="0" />
  <input type="text" class="otp-input" maxlength="1" data-index="1" />
  <input type="text" class="otp-input" maxlength="1" data-index="2" />
  <input type="text" class="otp-input" maxlength="1" data-index="3" />
</div>
```

### 2. Add All CSS from Above

Copy both technique's `@keyframes` and class definitions into your component or global CSS.

### 3. JavaScript Logic

```javascript
const inputs = document.querySelectorAll('.otp-input');
const container = document.querySelector('.otp-container');

inputs.forEach((input, index) => {
  input.addEventListener('input', (e) => {
    if (e.target.value.length === 1) {
      // Auto-focus next input
      if (index < inputs.length - 1) {
        inputs[index + 1].focus();
      } else {
        // All filled — choose animation
        triggerVerification();
      }
    }
  });

  input.addEventListener('keydown', (e) => {
    if (e.key === 'Backspace' && !input.value && index > 0) {
      inputs[index - 1].focus();
    }
  });
});

function triggerVerification() {
  // Option A: Ring animation on last box
  inputs[3].classList.add('completed');
  
  // Option B: Seal fusion on all
  // container.classList.add('sealing');
  
  // Then submit or validate
  submitOTP();
}
```

---

## Customization

### Colors
Replace `#10b981` (emerald ring) and `#8b5cf6` / `#06b6d4` (seal violet/aqua) with your brand colors:

```css
:root {
  --otp-success: #10b981;
  --seal-primary: #8b5cf6;
  --seal-secondary: #06b6d4;
}

.otp-input.completed { background: var(--otp-success); }
.otp-container.sealing::after { 
  background: linear-gradient(135deg, var(--seal-primary) 0%, var(--seal-secondary) 100%);
}
```

### Speed
Adjust animation durations:
- Ring curl: change `600ms` to `400ms` (faster) or `800ms` (slower)
- Seal fusion: adjust `600ms` in `fuseToCenter` keyframe
- Spin loop: modify `1.2s` in `spinRing`

### Easing
Common eases for OTP animations:
- `cubic-bezier(0.68, -0.55, 0.265, 1.55)` — bouncy, playful
- `cubic-bezier(0.4, 0, 0.2, 1)` — Material Design standard
- `ease-out` — simple decelerate
- `ease-in-out` — smooth both ways

---

## Live Example (React)

```jsx
import { useEffect, useRef } from 'react';

export function OTPInput() {
  const inputsRef = useRef([]);
  const containerRef = useRef(null);

  const handleInput = (index) => {
    if (inputsRef.current[index].value.length === 1) {
      if (index < 3) {
        inputsRef.current[index + 1].focus();
      } else {
        // All filled
        containerRef.current.classList.add('sealing');
      }
    }
  };

  return (
    <div ref={containerRef} className="otp-container">
      {[0, 1, 2, 3].map((i) => (
        <input
          key={i}
          ref={(el) => (inputsRef.current[i] = el)}
          type="text"
          maxLength="1"
          className="otp-input"
          onInput={() => handleInput(i)}
        />
      ))}
    </div>
  );
}
```

**Include CSS separately** (in your global stylesheet or component module):

```css
/* Paste all @keyframes and classes from above */
```

---

## Browser Support

- **CSS 3D Transforms:** 95%+ (all modern browsers)
- **backdrop-filter:** Not needed here, safe to use
- **Gradient animation:** 100% supported

No polyfills required.

---

## Related Skills

- `form-state-transitions` — card-flip for login/signup toggle
- `progress-state-morphing` — progress ring animation (extends this concept)
- `frontend-design` — aesthetic decisions for auth pages

---

**Reference Reel:** DbxxWJnoR2L (OTP ring), DbbNr-SvJkK (OTP seal) from _code_and_chill_ IG batch.
