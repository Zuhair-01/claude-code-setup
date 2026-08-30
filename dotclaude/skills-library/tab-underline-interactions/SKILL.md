---
name: tab-underline-interactions
description: "Tab underline with light-reaching animation and slide-to effect. Use for: 'tab animation', 'underline indicator', 'nav interaction'"
---

# Tab Underline Interactions Skill

Animated tab indicator with gradient shimmer effect, extracted from _code_and_chill_ reel DcC_M4Rv1Zp.

## Technique: Light-Reaches-For-It Underline (DcC_M4Rv1Zp)

**Visual:** Underline slides to active tab with gradient shimmer traveling left→right across it.

**Tech Stack:** CSS animations + gradients  
**Duration:** 300ms slide + 400ms shimmer

**HTML:**

```html
<div class="tabs-container">
  <button class="tab active" data-tab="dashboard">Dashboard</button>
  <button class="tab" data-tab="reports">Reports</button>
  <button class="tab" data-tab="settings">Settings</button>
</div>
```

**CSS:**

```css
.tabs-container {
  display: flex;
  gap: 0;
  border-bottom: 2px solid #e5e7eb;
  position: relative;
}

.tab {
  padding: 12px 16px;
  font-weight: 500;
  color: #6b7280;
  background: none;
  border: none;
  cursor: pointer;
  transition: color 200ms ease-out;
  position: relative;
}

.tab:hover {
  color: #374151;
}

.tab.active {
  color: #3b82f6;
}

/* Underline - positioned absolutely beneath active tab */
.tab.active::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, transparent 0%, #3b82f6 50%, transparent 100%);
  background-size: 300% 100%;
  animation: slideUnderline 300ms cubic-bezier(0.4, 0, 0.2, 1) forwards,
             shimmer 400ms ease-out;
}

@keyframes slideUnderline {
  from {
    left: var(--from-x);
    width: var(--width);
  }
  to {
    left: 0;
    width: 100%;
  }
}

@keyframes shimmer {
  0% {
    background-position: -300% center;
  }
  100% {
    background-position: 300% center;
  }
}
```

**JavaScript:**

```javascript
const tabs = document.querySelectorAll('.tab');

tabs.forEach((tab) => {
  tab.addEventListener('click', () => {
    const wasActive = document.querySelector('.tab.active');
    
    // Calculate sliding distance for next underline
    if (wasActive && wasActive !== tab) {
      const fromX = wasActive.offsetLeft;
      const toX = tab.offsetLeft;
      tab.style.setProperty('--from-x', (fromX - toX) + 'px');
      tab.style.setProperty('--width', wasActive.offsetWidth + 'px');
    }

    // Update active state
    tabs.forEach((t) => t.classList.remove('active'));
    tab.classList.add('active');
  });
});
```

---

## React Component

```jsx
import { useState, useRef } from 'react';
import './TabUnderline.css';

export function TabNavigation() {
  const [activeTab, setActiveTab] = useState('dashboard');
  const [slideStyle, setSlideStyle] = useState({});
  const tabsRef = useRef({});

  const handleTabClick = (tabName) => {
    const activeTabEl = tabsRef.current[activeTab];
    const nextTabEl = tabsRef.current[tabName];

    if (activeTabEl) {
      const fromX = activeTabEl.offsetLeft - nextTabEl.offsetLeft;
      const width = activeTabEl.offsetWidth;
      setSlideStyle({
        '--from-x': `${fromX}px`,
        '--width': `${width}px`,
      });
    }

    setActiveTab(tabName);
  };

  const tabs = ['dashboard', 'reports', 'settings'];

  return (
    <div className="tabs-container">
      {tabs.map((tab) => (
        <button
          key={tab}
          ref={(el) => (tabsRef.current[tab] = el)}
          className={`tab ${activeTab === tab ? 'active' : ''}`}
          onClick={() => handleTabClick(tab)}
          style={activeTab === tab ? slideStyle : {}}
        >
          {tab.charAt(0).toUpperCase() + tab.slice(1)}
        </button>
      ))}
    </div>
  );
}
```

---

## Customization

### Colors
```css
:root {
  --tab-active: #3b82f6;
  --tab-inactive: #6b7280;
}

.tab { color: var(--tab-inactive); }
.tab.active { color: var(--tab-active); }
.tab.active::after { background: linear-gradient(90deg, transparent, var(--tab-active), transparent); }
```

### Speed
- Slide: `300ms` → `200ms` (faster) or `400ms` (slower)
- Shimmer: `400ms` → `300ms` or `500ms`

### Easing
- `cubic-bezier(0.4, 0, 0.2, 1)` — Material Design (recommended)
- `ease-in-out` — smooth both directions

---

**Reference Reel:** DcC_M4Rv1Zp (tab underline slide + shimmer) from _code_and_chill_ IG batch.
