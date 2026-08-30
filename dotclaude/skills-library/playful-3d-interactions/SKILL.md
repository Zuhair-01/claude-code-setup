---
name: playful-3d-interactions
description: "Playful 3D click-to-interact animations (soda can, Easter eggs). Use for: '3D easter egg', 'playful interaction', 'click-to-open'. From Instagram reel (DbAzYoVvFu7)"
---

# Playful 3D Interactions Skill

Playful 3D objects with spring physics, extracted from _code_and_chill_ reel DbAzYoVvFu7 (soda can click-to-open).

## Technique: Soda Can Click-to-Open (DbAzYoVvFu7)

**Visual:** Click can → tips over, lid flies up with arc trajectory, color floods in, springs physics on bounce.

**Tech Stack:** Three.js + React Three Fiber + simple gravity simulation

**React Component:**

```jsx
import { Canvas, useFrame } from '@react-three/fiber';
import { useRef, useState } from 'react';
import * as THREE from 'three';

export function PlayfulSodaCan() {
  const [isOpened, setIsOpened] = useState(false);

  return (
    <div className="playful-can-container">
      <Canvas camera={{ position: [0, 0, 4], fov: 50 }}>
        <ambientLight intensity={0.8} />
        <directionalLight position={[5, 5, 5]} intensity={1} />
        <SodaCan isOpened={isOpened} onOpen={() => setIsOpened(true)} />
      </Canvas>
    </div>
  );
}

function SodaCan({ isOpened, onOpen }) {
  const canRef = useRef();
  const lidRef = useRef();
  const liquidRef = useRef();
  const timeRef = useRef(0);
  const liquidColorRef = useRef(new THREE.Color(0x000));

  useFrame(() => {
    if (!isOpened) return;

    timeRef.current += 0.016; // ~60fps delta

    // Lid physics
    if (lidRef.current && timeRef.current < 1.5) {
      const t = timeRef.current;
      const gravity = 9.8;
      let velocity = 8 - gravity * t;
      
      lidRef.current.position.y = 1.2 + velocity * 0.016 * t;
      lidRef.current.position.z += 0.05;
      
      if (lidRef.current.position.y < -2) {
        velocity *= -0.7; // Bounce
      }
    }

    // Can tip over
    if (canRef.current && timeRef.current < 0.3) {
      canRef.current.rotation.z = (timeRef.current / 0.3) * Math.PI / 6;
    }

    // Liquid reveal
    if (liquidRef.current && timeRef.current < 0.8) {
      liquidRef.current.material.opacity = (timeRef.current / 0.8);
      const hue = timeRef.current / 0.8; // Color shift
      liquidColorRef.current.setHSL(hue * 0.1 + 0.05, 1, 0.5);
      liquidRef.current.material.color = liquidColorRef.current;
    }
  });

  return (
    <group>
      {/* Can Body */}
      <mesh
        ref={canRef}
        onClick={onOpen}
        style={{ cursor: 'pointer' }}
      >
        <cylinderGeometry args={[0.4, 0.4, 1.2, 32]} />
        <meshPhongMaterial color="#ef4444" />
      </mesh>

      {/* Can Lid */}
      {isOpened && (
        <mesh ref={lidRef} position={[0, 1.2, 0]}>
          <cylinderGeometry args={[0.5, 0.5, 0.1, 32]} />
          <meshPhongMaterial color="#333" />
        </mesh>
      )}

      {/* Liquid Inside */}
      {isOpened && (
        <mesh ref={liquidRef} position={[0, -0.2, 0]}>
          <cylinderGeometry args={[0.35, 0.35, 0.8, 32]} />
          <meshPhongMaterial
            color={0xff6b00}
            transparent
            opacity={0}
          />
        </mesh>
      )}
    </group>
  );
}
```

**CSS:**

```css
.playful-can-container {
  width: 100%;
  height: 400px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 12px;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: transform 200ms ease-out;
}

.playful-can-container:hover {
  transform: scale(1.02);
}

.playful-can-container canvas {
  display: block;
}
```

---

## Customization

### Can Color
Change `color="#ef4444"` to any hex value

### Liquid Color
Modify the hue range in color shift:
```javascript
liquidColorRef.current.setHSL(
  hue * 0.1 + 0.05,  // Hue (0-1)
  1,                  // Saturation
  0.5                 // Lightness
);
```

### Gravity/Physics
```javascript
const gravity = 9.8;    // Adjust for slower/faster fall
const bounceStr = 0.7;  // Change from 0.7 to adjust bounce
```

### Duration
- Can tip: `timeRef.current < 0.3` (300ms)
- Lid flight: `timeRef.current < 1.5` (1500ms)
- Liquid reveal: `timeRef.current < 0.8` (800ms)

---

## Advanced: Particle Confetti

Add confetti burst on open:

```jsx
function ConfettiParticles() {
  const particlesRef = useRef([]);

  useFrame(() => {
    particlesRef.current.forEach(p => {
      p.position.y -= p.velocity;
      p.rotation.z += 0.05;
    });
  });

  return (
    <group>
      {Array.from({ length: 20 }).map((_, i) => (
        <mesh key={i} position={[Math.random() - 0.5, 0, 0]}>
          <boxGeometry args={[0.1, 0.1, 0.1]} />
          <meshPhongMaterial color={Math.random() * 0xffffff} />
        </mesh>
      ))}
    </group>
  );
}
```

---

**Reference Reel:** DbAzYoVvFu7 (soda can 3D click-to-open) from _code_and_chill_ IG batch.
