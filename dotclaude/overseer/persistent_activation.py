#!/usr/bin/env python3
"""
Persistent Activation: Ensures unified system stays active across all sessions
Heartbeat mechanism + session recovery
"""

import json
from pathlib import Path
from datetime import datetime, timedelta

class PersistentActivation:
    """Maintains system activation across sessions and tasks"""

    def __init__(self):
        self.status_file = Path.home() / ".claude/overseer/system-status.json"
        self.heartbeat_interval = 300  # 5 minutes
        self.initialize()

    def initialize(self):
        """Initialize or restore system status"""
        if self.status_file.exists():
            try:
                with open(self.status_file) as f:
                    status = json.load(f)
                    if self._is_healthy(status):
                        return  # System already active
            except:
                pass

        # Create fresh status. This records local health only; it does not
        # prove that Claude Code routed a task through every advertised layer.
        self.status_file.write_text(json.dumps({
        "version": "2026-08-17",
            "activated": datetime.now().isoformat(),
            "system": "unified",
            "status": "ACTIVE",
            "components": {
                "overseer": "ready",
                "bundles": "ready",
                "smart_selector": "ready",
                "skill_router": "ready",
                "omniroute": "ready",
                "quality_gates": "ready",
            },
            "metrics": {
                "sessions_active": 1,
                "tasks_processed": 0,
                "avg_tokens_saved": None,
                "avg_cost_saved": None,
            }
        }, indent=2))

    def _is_healthy(self, status: dict) -> bool:
        """Check if system is healthy and active"""
        if status.get("status") != "ACTIVE":
            return False

        # Check heartbeat (should be recent)
        last_heartbeat = status.get("last_heartbeat")
        if last_heartbeat:
            try:
                last_time = datetime.fromisoformat(last_heartbeat)
                age = datetime.now() - last_time
                if age > timedelta(seconds=self.heartbeat_interval * 2):
                    return False  # Too old
            except:
                return False

        return True

    def heartbeat(self):
        """Update heartbeat to show system is alive"""
        try:
            with open(self.status_file) as f:
                status = json.load(f)
        except:
            self.initialize()
            return

        status["last_heartbeat"] = datetime.now().isoformat()
        status["status"] = "ACTIVE"
        self.status_file.write_text(json.dumps(status, indent=2))

    def log_task_completion(self, task_id: str, metrics: dict):
        """Log metrics for completed task"""
        try:
            with open(self.status_file) as f:
                status = json.load(f)
        except:
            self.initialize()
            return

        status["metrics"]["tasks_processed"] = status["metrics"].get("tasks_processed", 0) + 1
        if "last_task" not in status["metrics"]:
            status["metrics"]["last_task"] = {}
        status["metrics"]["last_task"] = {
            "id": task_id,
            "completed": datetime.now().isoformat(),
            "metrics": metrics,
        }

        self.status_file.write_text(json.dumps(status, indent=2))

    def get_status(self) -> dict:
        """Get current system status"""
        if not self.status_file.exists():
            self.initialize()

        with open(self.status_file) as f:
            return json.load(f)

    def ensure_active(self) -> bool:
        """Ensure system is active, restart if needed"""
        status = self.get_status()

        if status.get("status") != "ACTIVE":
            # Reactivate
            self.initialize()
            return True

        # Update heartbeat
        self.heartbeat()
        return True


# Global instance
_activation = None


def get_activation() -> PersistentActivation:
    global _activation
    if not _activation:
        _activation = PersistentActivation()
    return _activation


def on_session_start():
    """Called when Claude Code session starts"""
    activation = get_activation()
    activation.ensure_active()
    return activation.get_status()


def on_task_end(task_id: str, metrics: dict):
    """Called when task completes"""
    activation = get_activation()
    activation.log_task_completion(task_id, metrics)


if __name__ == "__main__":
    activation = get_activation()

    # On session start
    status = on_session_start()
    print("Session Start Status:")
    print(json.dumps(status, indent=2))

    # Simulate task completion
    on_task_end("task_001", {
        "bundle_used": "BUNDLE-F-video-media",
        "tokens_used": 28,
        "tokens_saved": 52,
        "compression": "65%",
        "quality_score": 8.8,
        "duration_ms": 1200,
    })

    # Check status
    final_status = activation.get_status()
    print("\nFinal Status:")
    print(f"Tasks processed: {final_status['metrics']['tasks_processed']}")
    print(f"System status: {final_status['status']}")
