---
name: navbar-glass-effects
description: "Glass-morphism navbar with refraction & chromatic aberration. Use for: 'glass nav', 'refraction effect', 'chromatic navbar'. From Instagram reel (DbXiNGVvUQA)"
---

# Navbar Glass Effects Skill

Real-glass refraction navbar with backdrop-filter + optional chromatic aberration, extracted from _code_and_chill_ reel DbXiNGVvUQA.

## Technique: Glass Navbar Refraction (DbXiNGVvUQA)

**Visual:** Navbar appears frosted glass over page. Subtle color split (chromatic aberration) on hover.

**Tech Stack:** CSS `backdrop-filter` + optional React Three Fiber for advanced refraction

### Simple Version (CSS Only)

```css
.navbar {
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 40;
  backdrop-filter: blur(12px) saturate(180%);
  background: linear-gradient(
    180deg,
    rgba(255, 255, 255, 0.8),
    rgba(255, 255, 255, 0.6)
  );
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
  -webkit-backdrop-filter: blur(12px) saturate(180%);
  will-change: backdrop-filter;
}

.nav-link {
  position: relative;
  transition: all 200ms ease-out;
}

.nav-link:hover {
  filter: drop-shadow(0 0 6px rgba(59, 130, 246, 0.4));
}

.nav-link::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(
    circle at var(--mouse-x, 50%) var(--mouse-y, 50%),
    rgba(255, 255, 255, 0.1) 0%,
    transparent 70%
  );
  opacity: 0;
  transition: opacity 300ms ease-out;
}

.nav-link:hover::before {
  opacity: 1;
}
```

**HTML:**

```html
<nav class="navbar">
  <a href="/" class="nav-link">Home</a>
  <a href="/features" class="nav-link">Features</a>
  <a href="/pricing" class="nav-link">Pricing</a>
</nav>
```

### Advanced Version (Chromatic Aberration via JavaScript)

```javascript
const navLinks = document.querySelectorAll('.nav-link');

navLinks.forEach(link => {
  link.addEventListener('mousemove', (e) => {
    const rect = link.getBoundingClientRect();
    const x = ((e.clientX - rect.left) / rect.width) * 100;
    const y = ((e.clientY - rect.top) / rect.height) * 100;
    
    link.style.setProperty('--mouse-x', `${x}%`);
    link.style.setProperty('--mouse-y', `${y}%`);
    
    // Chromatic aberration on hover
    const xOffset = (x - 50) * 0.1;
    const yOffset = (y - 50) * 0.1;
    
    link.style.textShadow = `
      ${xOffset}px ${yOffset}px 0 rgba(255, 0, 0, 0.5),
      -${xOffset}px -${yOffset}px 0 rgba(0, 0, 255, 0.5)
    `;
  });

  link.addEventListener('mouseleave', () => {
    link.style.textShadow = 'none';
  });
});
```

### React Component

```jsx
export function GlassNavbar() {
  return (
    <nav className="navbar">
      <div className="nav-logo">Logo</div>
      <div className="nav-links">
        {['Home', 'Features', 'Pricing', 'Docs'].map(link => (
          <a key={link} href={`/${link.toLowerCase()}`} className="nav-link">
            {link}
          </a>
        ))}
      </div>
    </nav>
  );
}
```

---

## Customization

### Blur Strength
- Light (subtle): `blur(8px)`
- Medium (default): `blur(12px)`
- Heavy (opaque): `blur(20px)`

### Colors
```css
background: linear-gradient(
  180deg,
  rgba(255, 255, 255, 0.8),  /* Top opacity */
  rgba(255, 255, 255, 0.6)   /* Bottom opacity */
);
border-bottom: 1px solid rgba(255, 255, 255, 0.2); /* Border */
```

### Saturation
- Natural: `saturate(100%)`
- Vibrant (default): `saturate(180%)`
- Ultra-vibrant: `saturate(200%)`

---

## Browser Support

- **backdrop-filter:** 95%+ (all modern browsers)
- **-webkit prefix:** iOS Safari 9+
- **Fallback:** Background color still renders if blur not supported

---

**Reference Reel:** DbXiNGVvUQA (glass navbar + refraction) from _code_and_chill_ IG batch.
