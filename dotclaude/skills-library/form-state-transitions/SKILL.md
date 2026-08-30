---
name: form-state-transitions
description: "Card-flip & form state animations from Instagram reels. Use for: 'form state transition', 'card flip', 'auth page animation', 'modal transitions'"
---

# Form State Transitions Skill

Smooth form state transitions extracted from _code_and_chill_ reels — login↔signup card flip, field focus animations, modal slide-in/out.

## When to Use This Skill

- Login ↔ Signup toggle (one form → other)
- Multi-step form flows (step 1 → 2 → 3)
- Modal open/close animations
- Switching between different form views (view, edit, confirm)

## Technique: Login↔Signup Card Flip (Db7fSM1v8Yg)

**Visual:** Current form slides left off-screen, next form enters from right. Pure horizontal translate, no 3D rotation.

**Tech Stack:** CSS transitions + transform  
**Duration:** 400ms per transition

**Copy-Paste Code:**

```html
<!-- HTML Structure -->
<div class="form-wrapper">
  <div class="forms-container">
    <!-- Login Form -->
    <form class="form login-form">
      <h2>Login</h2>
      <input type="email" placeholder="Email" />
      <input type="password" placeholder="Password" />
      <button type="submit">Login</button>
      <p class="toggle-link">Need an account? <a href="#" data-form="signup">Sign up</a></p>
    </form>

    <!-- Signup Form -->
    <form class="form signup-form">
      <h2>Create Account</h2>
      <input type="text" placeholder="Full Name" />
      <input type="email" placeholder="Email" />
      <input type="password" placeholder="Password" />
      <input type="password" placeholder="Confirm Password" />
      <button type="submit">Sign Up</button>
      <p class="toggle-link">Already have an account? <a href="#" data-form="login">Login</a></p>
    </form>
  </div>
</div>
```

```css
/* Wrapper handles overflow (hide forms sliding out) */
.form-wrapper {
  position: relative;
  overflow: hidden;
  width: 400px;
  max-width: 100%;
  margin: 0 auto;
  border-radius: 12px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
}

/* Container slides to reveal forms */
.forms-container {
  display: flex;
  width: 200%;
  transition: transform 400ms cubic-bezier(0.4, 0, 0.2, 1);
  will-change: transform;
}

/* Each form takes 50% of container width */
.form {
  width: 50%;
  flex-shrink: 0;
  padding: 40px;
  background: white;
}

/* Default: show login (translateX 0) */
.forms-container.show-login {
  transform: translateX(0%);
}

/* Show signup: shift left by 50% (second form enters from right) */
.forms-container.show-signup {
  transform: translateX(-50%);
}

/* Smooth stagger for form fields */
.form input,
.form button {
  opacity: 1;
  transition: opacity 200ms ease-out;
}

/* Fade out fields during slide (optional polish) */
.forms-container.transitioning .form input,
.forms-container.transitioning .form button {
  opacity: 0.7;
}

/* Focus state animations */
.form input:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
  transition: all 200ms ease-out;
}
```

```javascript
// Simple toggle between login/signup
const container = document.querySelector('.forms-container');
const toggleLinks = document.querySelectorAll('[data-form]');

toggleLinks.forEach((link) => {
  link.addEventListener('click', (e) => {
    e.preventDefault();
    const targetForm = e.currentTarget.dataset.form;
    container.classList.remove('show-login', 'show-signup');
    container.classList.add(`show-${targetForm}`);
  });
});

// Optional: Add transitioning class for field fade
container.addEventListener('click', () => {
  container.classList.add('transitioning');
  setTimeout(() => container.classList.remove('transitioning'), 200);
});
```

---

## Advanced: Multi-Step Form

For 3+ step forms, stack forms vertically or extend horizontal:

```html
<!-- 3-Step Form -->
<div class="forms-container" style="width: 300%;">
  <form class="form step-1"><!-- Step 1 --></form>
  <form class="form step-2"><!-- Step 2 --></form>
  <form class="form step-3"><!-- Step 3 --></form>
</div>
```

```css
.forms-container.step-1 { transform: translateX(0%); }
.forms-container.step-2 { transform: translateX(-33.33%); }
.forms-container.step-3 { transform: translateX(-66.66%); }
```

```javascript
function goToStep(stepNumber) {
  const width = 100 / (document.querySelectorAll('.form').length);
  const offset = width * (stepNumber - 1);
  container.style.transform = `translateX(-${offset}%)`;
}

nextButton.addEventListener('click', () => goToStep(2));
prevButton.addEventListener('click', () => goToStep(1));
```

---

## Customization

### Speed
- **Fast:** `200ms cubic-bezier(0.4, 0, 0.2, 1)`
- **Medium (Default):** `400ms cubic-bezier(0.4, 0, 0.2, 1)`
- **Slow:** `600ms cubic-bezier(0.4, 0, 0.2, 1)`

### Easing
- `cubic-bezier(0.4, 0, 0.2, 1)` — Material Design (recommended)
- `ease-in-out` — smooth both directions
- `ease-out` — feels faster (good for user interaction)

### Colors & Styling
```css
.form {
  background: var(--form-bg); /* Customize background */
  border-radius: var(--form-radius, 12px);
}

.form input {
  border: 2px solid var(--form-border, #e5e7eb);
  border-radius: var(--form-input-radius, 8px);
  padding: var(--form-input-padding, 12px);
}

.form input:focus {
  border-color: var(--form-focus, #3b82f6);
  box-shadow: 0 0 0 3px var(--form-focus-ring, rgba(59, 130, 246, 0.1));
}
```

---

## React Component Example

```jsx
import { useState } from 'react';
import './FormTransitions.css';

export function AuthForm() {
  const [view, setView] = useState('login');

  return (
    <div className="form-wrapper">
      <div
        className={`forms-container show-${view}`}
      >
        {/* Login Form */}
        <form className="form login-form" onSubmit={(e) => e.preventDefault()}>
          <h2>Login</h2>
          <input type="email" placeholder="Email" />
          <input type="password" placeholder="Password" />
          <button type="submit">Login</button>
          <button
            type="button"
            onClick={() => setView('signup')}
            className="toggle-link"
          >
            Need an account? Sign up
          </button>
        </form>

        {/* Signup Form */}
        <form className="form signup-form" onSubmit={(e) => e.preventDefault()}>
          <h2>Create Account</h2>
          <input type="text" placeholder="Full Name" />
          <input type="email" placeholder="Email" />
          <input type="password" placeholder="Password" />
          <input type="password" placeholder="Confirm Password" />
          <button type="submit">Sign Up</button>
          <button
            type="button"
            onClick={() => setView('login')}
            className="toggle-link"
          >
            Already have an account? Login
          </button>
        </form>
      </div>
    </div>
  );
}
```

---

## Browser Support

- **CSS Transforms:** 100% (all browsers)
- **CSS Transitions:** 100%
- **Will-change:** 95%+ (optional, for performance)

No polyfills needed.

---

## Performance Tips

1. **Use `will-change`** on `.forms-container` to hint browser for GPU acceleration
2. **Lock form width** to prevent layout shift during animation
3. **Overflow hidden** on wrapper to hide sliding forms
4. **Test on mobile** — verify smooth animation at 60fps

---

## Related Skills

- `auth-micro-animations` — OTP state animations (complements this)
- `tab-underline-interactions` — similar sliding pattern for nav
- `frontend-design` — visual polish for form layouts

---

**Reference Reel:** Db7fSM1v8Yg (login card-flip) from _code_and_chill_ IG batch.
