---
name: progress-state-morphing
description: "Loading ring morphs into progress bar. Use for: 'progress animation', 'download state', 'loading morphing', 'ring to bar transition'"
---

# Progress State Morphing Skill

Circular progress ring that unrolls into a horizontal progress bar, extracted from _code_and_chill_ reel DbV5HtBPZ5w.

## Technique: Ring → Bar Unroll (DbV5HtBPZ5w)

**Visual:** Ring rotates (0-50% progress) → morphs into horizontal bar (50-100% progress)

**Tech Stack:** SVG + CSS animations  
**Duration:** Ring phase 2s, morph 800ms, total bar 3-5s

**HTML:**

```html
<div class="progress-container">
  <!-- Ring Phase (0-50%) -->
  <svg class="progress-ring" viewBox="0 0 120 120">
    <circle class="progress-circle" cx="60" cy="60" r="50" stroke="currentColor" stroke-width="4" fill="none"/>
  </svg>

  <!-- Bar Phase (50-100%) -->
  <div class="progress-bar" style="width: 0%"></div>
</div>
```

**CSS:**

```css
.progress-container {
  position: relative;
  width: 100%;
  max-width: 400px;
  margin: 0 auto;
}

/* Ring Phase */
.progress-ring {
  width: 120px;
  height: 120px;
  margin: 0 auto;
  transform: rotate(-90deg);
  opacity: 1;
  transition: opacity 400ms ease-out 800ms;
}

.progress-ring.morphing {
  opacity: 0;
}

.progress-circle {
  fill: none;
  stroke: #3b82f6;
  stroke-width: 4;
  stroke-linecap: round;
  stroke-dasharray: 314.16; /* 2 * PI * 50 */
  stroke-dashoffset: 314.16;
}

/* Animate ring rotation + progress fill */
@keyframes rotateRing {
  to { transform: rotate(-90deg) rotateZ(360deg); }
}

.progress-ring {
  animation: rotateRing 2s linear infinite;
}

/* Update stroke-dashoffset for progress (0-100%) */
.progress-circle {
  transition: stroke-dashoffset 100ms linear;
}

/* Bar Phase */
.progress-bar {
  height: 8px;
  background: #3b82f6;
  border-radius: 4px;
  margin-top: 20px;
  width: 0%;
  transition: width 100ms linear;
  opacity: 0;
  animation: barFadeIn 400ms ease-out 800ms forwards;
}

@keyframes barFadeIn {
  to { opacity: 1; }
}

/* Success State */
.progress-bar.complete {
  width: 100%;
  background: #10b981;
}
```

**JavaScript:**

```javascript
const ring = document.querySelector('.progress-circle');
const bar = document.querySelector('.progress-bar');
const container = document.querySelector('.progress-container');

const circumference = 2 * Math.PI * 50; // radius = 50

function updateProgress(percentage) {
  // Ring phase (0-50%)
  if (percentage <= 50) {
    const ringProgress = percentage / 50;
    ring.style.strokeDashoffset = circumference * (1 - ringProgress);
    bar.style.width = '0%';
  } 
  // Bar phase (50-100%)
  else {
    ring.style.strokeDashoffset = 0;
    const barProgress = (percentage - 50) / 50;
    bar.style.width = (barProgress * 100) + '%';
  }

  // Success state
  if (percentage >= 100) {
    container.classList.add('morphing');
    ring.parentElement.classList.add('morphing');
    bar.classList.add('complete');
  }
}

// Example: Simulate upload progress
let progress = 0;
const interval = setInterval(() => {
  progress += Math.random() * 30;
  if (progress >= 100) progress = 100;
  updateProgress(progress);
  
  if (progress >= 100) clearInterval(interval);
}, 500);
```

---

## React Component

```jsx
import { useEffect, useState } from 'react';
import './ProgressMorphing.css';

export function ProgressMorphing({ progress = 0 }) {
  const circumference = 2 * Math.PI * 50;
  const offset = circumference * (1 - Math.min(progress, 100) / 100);

  const isRingPhase = progress <= 50;
  const barProgress = isRingPhase ? 0 : ((progress - 50) / 50) * 100;
  const isComplete = progress >= 100;

  return (
    <div className={`progress-container ${isComplete ? 'morphing' : ''}`}>
      {/* Ring Phase */}
      <svg className="progress-ring" viewBox="0 0 120 120" opacity={!isComplete ? 1 : 0}>
        <circle
          className="progress-circle"
          cx="60"
          cy="60"
          r="50"
          stroke="currentColor"
          strokeWidth="4"
          fill="none"
          style={{ strokeDashoffset: offset }}
        />
      </svg>

      {/* Bar Phase */}
      <div
        className={`progress-bar ${isComplete ? 'complete' : ''}`}
        style={{ width: `${barProgress}%` }}
      />
    </div>
  );
}
```

---

## Customization

### Colors
```css
:root {
  --progress-primary: #3b82f6;
  --progress-success: #10b981;
}

.progress-circle { stroke: var(--progress-primary); }
.progress-bar { background: var(--progress-primary); }
.progress-bar.complete { background: var(--progress-success); }
```

### Timing
- Ring rotation: `2s` → adjust for faster/slower spin
- Morph start: `800ms` → earlier/later transition point
- Bar animation: `100ms linear` → smooth or instant fill

---

**Reference Reel:** DbV5HtBPZ5w (ring → bar morph) from _code_and_chill_ IG batch.
