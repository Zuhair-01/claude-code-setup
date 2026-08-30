---
name: upload-widget-interactions
description: "Drag-drop file upload with retry state animations. Use for: 'upload animation', 'drag drop state', 'retry animation', 'file progress'"
---

# Upload Widget Interactions Skill

File upload animations with retry state transitions, extracted from _code_and_chill_ reel Da0iDR4vl5M.

## When to Use

- File upload components (documents, images, videos)
- Drag-drop zones with visual feedback
- Retry logic for failed uploads
- Progress indication during processing

## Technique: Drag-Drop + Retry State (Da0iDR4vl5M)

**Visual Flow:**
1. User drags file → zone highlights
2. File drops → appears in queue with thumbnail
3. Processing → progress ring spins
4. Error (or success) → state reflects with icon + button

**Tech Stack:** Tailwind + CSS animations + SVG progress  
**Duration:** Depends on upload speed (user-driven)

**HTML Structure:**

```html
<div class="upload-widget">
  <!-- Drag zone (shown when empty) -->
  <div class="drag-zone" id="dragZone">
    <svg class="upload-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
      <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M17 8l-5-5-5 5M12 3v12" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
    <p class="text-gray-600">Drag files here or click to browse</p>
  </div>

  <!-- File queue (shown when files present) -->
  <div class="file-queue" id="fileQueue" style="display: none;">
    <!-- File items inserted here dynamically -->
  </div>
</div>
```

**CSS:**

```css
.upload-widget {
  width: 100%;
  max-width: 600px;
  margin: 0 auto;
}

/* Drag Zone */
.drag-zone {
  border: 2px dashed #d1d5db;
  border-radius: 12px;
  padding: 40px;
  text-align: center;
  cursor: pointer;
  transition: all 200ms ease-out;
  background: #fafafa;
}

.drag-zone:hover {
  border-color: #3b82f6;
  background: #eff6ff;
}

.drag-zone.drag-over {
  border-color: #3b82f6;
  background: #eff6ff;
  transform: scale(1.02);
}

.upload-icon {
  width: 48px;
  height: 48px;
  color: #6b7280;
  margin-bottom: 12px;
  animation: bounceIcon 2s ease-in-out infinite;
}

@keyframes bounceIcon {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-8px); }
}

/* File Queue */
.file-queue {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-top: 20px;
}

/* Individual File Item */
.file-item {
  display: flex;
  gap: 12px;
  align-items: center;
  padding: 12px;
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  transition: all 300ms ease-out;
}

/* File Thumbnail */
.file-thumbnail {
  width: 56px;
  height: 56px;
  border-radius: 6px;
  background: #e5e7eb;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  flex-shrink: 0;
  overflow: hidden;
}

.file-thumbnail img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* File Info */
.file-info {
  flex: 1;
  min-width: 0;
}

.file-name {
  font-weight: 500;
  color: #1f2937;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  margin-bottom: 4px;
}

.file-size {
  font-size: 12px;
  color: #6b7280;
}

/* Progress Ring (SVG) */
.progress-ring {
  width: 48px;
  height: 48px;
  transform: rotate(-90deg);
  flex-shrink: 0;
}

.progress-ring-circle {
  fill: none;
  stroke: #3b82f6;
  stroke-width: 4;
  stroke-linecap: round;
  stroke-dasharray: 282.74;
  stroke-dashoffset: 282.74;
  animation: spin 2s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Error State */
.file-item.error {
  opacity: 0.6;
  border-color: #fca5a5;
  background: #fef2f2;
}

.file-item.error .file-thumbnail {
  background: #fee2e2;
}

.file-item.error .progress-ring {
  display: none;
}

.error-icon {
  width: 24px;
  height: 24px;
  color: #dc2626;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.error-message {
  font-size: 12px;
  color: #dc2626;
  margin-top: 4px;
}

/* Retry Button */
.retry-btn {
  padding: 6px 12px;
  background: #dc2626;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 12px;
  cursor: pointer;
  transition: all 200ms ease-out;
  animation: slideInUp 300ms cubic-bezier(0.34, 1.56, 0.64, 1);
}

.retry-btn:hover {
  background: #b91c1c;
}

@keyframes slideInUp {
  from {
    opacity: 0;
    transform: translateY(8px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Success State */
.file-item.success {
  border-color: #86efac;
  background: #f0fdf4;
}

.file-item.success .progress-ring {
  animation: none;
}

.success-icon {
  width: 24px;
  height: 24px;
  color: #10b981;
  flex-shrink: 0;
}
```

**JavaScript:**

```javascript
const dragZone = document.getElementById('dragZone');
const fileQueue = document.getElementById('fileQueue');
const uploadWidget = document.querySelector('.upload-widget');

// Drag events
dragZone.addEventListener('dragover', (e) => {
  e.preventDefault();
  dragZone.classList.add('drag-over');
});

dragZone.addEventListener('dragleave', () => {
  dragZone.classList.remove('drag-over');
});

dragZone.addEventListener('drop', (e) => {
  e.preventDefault();
  dragZone.classList.remove('drag-over');
  handleFiles(e.dataTransfer.files);
});

// Click to browse
dragZone.addEventListener('click', () => {
  const input = document.createElement('input');
  input.type = 'file';
  input.multiple = true;
  input.addEventListener('change', () => handleFiles(input.files));
  input.click();
});

function handleFiles(files) {
  dragZone.style.display = 'none';
  fileQueue.style.display = 'flex';

  Array.from(files).forEach((file) => {
    const fileItem = createFileItem(file);
    fileQueue.appendChild(fileItem);
    uploadFile(file, fileItem);
  });
}

function createFileItem(file) {
  const item = document.createElement('div');
  item.className = 'file-item';
  
  // Thumbnail
  const thumbnail = document.createElement('div');
  thumbnail.className = 'file-thumbnail';
  if (file.type.startsWith('image/')) {
    const reader = new FileReader();
    reader.onload = (e) => {
      thumbnail.innerHTML = `<img src="${e.target.result}" />`;
    };
    reader.readAsDataURL(file);
  } else {
    thumbnail.textContent = '📄';
  }

  // Info
  const info = document.createElement('div');
  info.className = 'file-info';
  info.innerHTML = `
    <div class="file-name">${file.name}</div>
    <div class="file-size">${formatBytes(file.size)}</div>
  `;

  // Progress ring (SVG)
  const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
  svg.setAttribute('class', 'progress-ring');
  const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
  circle.setAttribute('class', 'progress-ring-circle');
  circle.setAttribute('cx', '24');
  circle.setAttribute('cy', '24');
  circle.setAttribute('r', '20');
  svg.appendChild(circle);

  item.appendChild(thumbnail);
  item.appendChild(info);
  item.appendChild(svg);

  return item;
}

async function uploadFile(file, fileItem) {
  try {
    // Simulate upload (replace with actual API call)
    await new Promise((resolve) => setTimeout(resolve, 3000));

    // Success state
    fileItem.classList.add('success');
    const svg = fileItem.querySelector('svg');
    svg.innerHTML = '<circle cx="24" cy="24" r="24" fill="#10b981"/><text x="24" y="32" text-anchor="middle" fill="white" font-size="20">✓</text>';
  } catch (error) {
    // Error state
    fileItem.classList.add('error');
    const errorMsg = document.createElement('div');
    errorMsg.className = 'error-message';
    errorMsg.textContent = 'Upload failed';
    fileItem.querySelector('.file-info').appendChild(errorMsg);

    const retryBtn = document.createElement('button');
    retryBtn.className = 'retry-btn';
    retryBtn.textContent = 'Retry';
    retryBtn.onclick = () => uploadFile(file, fileItem);
    fileItem.appendChild(retryBtn);

    const svg = fileItem.querySelector('svg');
    svg.innerHTML = '<circle cx="24" cy="24" r="24" fill="none"/><text x="24" y="32" text-anchor="middle" fill="#dc2626" font-size="20">✕</text>';
  }
}

function formatBytes(bytes) {
  if (bytes === 0) return '0 Bytes';
  const k = 1024;
  const sizes = ['Bytes', 'KB', 'MB', 'GB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return Math.round(bytes / Math.pow(k, i) * 100) / 100 + ' ' + sizes[i];
}
```

---

## React Component

```jsx
import { useState } from 'react';
import './UploadWidget.css';

export function UploadWidget() {
  const [files, setFiles] = useState([]);
  const [isDragging, setIsDragging] = useState(false);

  const handleDragOver = (e) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = () => setIsDragging(false);

  const handleDrop = (e) => {
    e.preventDefault();
    setIsDragging(false);
    handleFiles(e.dataTransfer.files);
  };

  const handleFiles = (fileList) => {
    setFiles(Array.from(fileList).map((file) => ({
      file,
      id: Math.random(),
      status: 'uploading',
      progress: 0,
    })));
  };

  return (
    <div className="upload-widget">
      {files.length === 0 ? (
        <div
          className={`drag-zone ${isDragging ? 'drag-over' : ''}`}
          onDragOver={handleDragOver}
          onDragLeave={handleDragLeave}
          onDrop={handleDrop}
        >
          <svg className="upload-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M17 8l-5-5-5 5M12 3v12" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
          </svg>
          <p>Drag files here or click to browse</p>
        </div>
      ) : (
        <div className="file-queue">
          {files.map((item) => (
            <div key={item.id} className={`file-item ${item.status}`}>
              <div className="file-thumbnail">
                {item.file.type.startsWith('image/') ? '🖼️' : '📄'}
              </div>
              <div className="file-info">
                <div className="file-name">{item.file.name}</div>
                <div className="file-size">{(item.file.size / 1024).toFixed(1)} KB</div>
              </div>
              {item.status === 'uploading' && (
                <svg className="progress-ring" viewBox="0 0 48 48">
                  <circle className="progress-ring-circle" cx="24" cy="24" r="20"/>
                </svg>
              )}
              {item.status === 'success' && <div className="success-icon">✓</div>}
              {item.status === 'error' && <button className="retry-btn">Retry</button>}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
```

---

## Customization

### Colors
```css
:root {
  --upload-primary: #3b82f6;
  --upload-success: #10b981;
  --upload-error: #dc2626;
  --upload-border: #d1d5db;
}
```

### Animation Speed
- Ring spin: `2s` → `1s` (faster) or `3s` (slower)
- Retry slide: `300ms cubic-bezier(0.34, 1.56, 0.64, 1)` → adjust duration

---

## Related Skills

- `progress-state-morphing` — alternative progress animations
- `frontend-design` — visual polish for upload zones

---

**Reference Reel:** Da0iDR4vl5M (drag-drop + retry) from _code_and_chill_ IG batch.
