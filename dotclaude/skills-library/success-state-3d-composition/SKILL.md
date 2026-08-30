---
name: success-state-3d-composition
description: "3D success animations (delivery truck, confetti). Use for: 'export success', 'render complete', '3D success state', 'celebration animation'. From Instagram reel (Db_bxUZvz2n)"
---

# Success State 3D Composition Skill

3D animated success states using Three.js + React Three Fiber, extracted from _code_and_chill_ reel Db_bxUZvz2n.

## When to Use

- Export/render completion animations
- Success confirmations with 3D elements
- Celebratory scenes (delivery truck, objects in motion)
- After-action feedback with visual reward

## Technique: Delivery Truck Scene (Db_bxUZvz2n)

**Visual:** Button click → form fades, 3D scene renders (delivery truck drives left→right), celebrates completion.

**Tech Stack:** Three.js + React Three Fiber (or Babylon.js)  
**Duration:** Scene 3s total (0.5s fade-in, 2s truck, 0.5s fade-out)

**React Component:**

```jsx
import { Canvas } from '@react-three/fiber';
import { useFrame, useLoader } from '@react-three/fiber';
import * as THREE from 'three';
import { useState } from 'react';

export function SuccessScene({ isVisible }) {
  const [animation, setAnimation] = useState(0);

  return (
    <div className={`success-scene ${isVisible ? 'visible' : ''}`}>
      {isVisible && (
        <Canvas camera={{ position: [0, 0, 5], fov: 50 }}>
          <ambientLight intensity={0.8} />
          <directionalLight position={[5, 5, 5]} intensity={1} />
          
          <DeliveryTruck />
          <Ground />
        </Canvas>
      )}
    </div>
  );
}

function DeliveryTruck() {
  const meshRef = useRef();
  const wheelRefs = useRef([]);
  
  useFrame(({ clock }) => {
    const t = clock.getElapsedTime();
    
    if (t < 0.5) {
      // Fade in
      meshRef.current.material.opacity = t / 0.5;
    } else if (t < 2.5) {
      // Drive across
      const progress = (t - 0.5) / 2;
      meshRef.current.position.x = -8 + progress * 16;
      
      // Rotate wheels
      wheelRefs.current.forEach(w => {
        w.rotation.z += 0.1;
      });
    } else {
      // Fade out
      meshRef.current.material.opacity = Math.max(0, 1 - (t - 2.5) / 0.5);
    }
  });

  return (
    <group ref={meshRef}>
      {/* Cargo box */}
      <mesh position={[0, 0.5, 0]}>
        <boxGeometry args={[2, 1, 1]} />
        <meshPhongMaterial color="#ef4444" />
      </mesh>
      
      {/* Wheels */}
      {[[-0.6, -0.3, 0.5], [-0.6, -0.3, -0.5], [0.6, -0.3, 0.5], [0.6, -0.3, -0.5]].map((pos, i) => (
        <mesh key={i} position={pos} ref={(el) => wheelRefs.current[i] = el}>
          <cylinderGeometry args={[0.3, 0.3, 0.1, 16]} />
          <meshPhongMaterial color="#000" />
        </mesh>
      ))}
    </group>
  );
}

function Ground() {
  return (
    <mesh position={[0, -1, 0]}>
      <planeGeometry args={[20, 2]} />
      <meshPhongMaterial color="#bfdbfe" />
    </mesh>
  );
}
```

**CSS:**

```css
.success-scene {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 50;
  opacity: 0;
  transition: opacity 300ms ease-out;
  pointer-events: none;
  background: rgba(255, 255, 255, 0.9);
}

.success-scene.visible {
  opacity: 1;
}

.success-scene canvas {
  display: block;
}
```

**Usage:**

```jsx
const [showSuccess, setShowSuccess] = useState(false);

const handleExportComplete = () => {
  setShowSuccess(true);
  setTimeout(() => setShowSuccess(false), 3000);
};

return (
  <>
    <SuccessScene isVisible={showSuccess} />
    <button onClick={handleExportComplete}>Export</button>
  </>
);
```

---

## Customization

### Colors
- Truck: change `#ef4444` (red)
- Ground: change `#bfdbfe` (light blue)
- Background: change `rgba(255, 255, 255, 0.9)`

### Duration
- Fade-in: change `0.5` in time check
- Truck drive: change `2s` duration
- Fade-out: change `0.5s`

### Camera
- Zoom: adjust `fov: 50` (lower = zoom in)
- Position: adjust `camera={{ position: [0, 0, 5] }}`

---

**Reference Reel:** Db_bxUZvz2n (delivery truck scene) from _code_and_chill_ IG batch.
