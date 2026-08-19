import logging
from typing import List, Dict, Any

class TaskManager:
    def __init__(self):
        self.tasks: List[Dict[str, Any]] = []

    def create_task(self, title: str, description: str = "") -> Dict[str, Any]:
        """
        إنشاء مهمة جديدة وإضافتها لقائمة مهام الوكالة
        """
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "description": description,
            "status": "pending"  # pending, in_progress, completed
        }
        self.tasks.append(task)
        logging.info(f"تم إنشاء المهمة رقم {task['id']}: {title}")
        return task

    def get_pending_tasks(self) -> List[Dict[str, Any]]:
        """
        استرجاع المهام التي لم تُنفذ بعد
        """
        return [t for t in self.tasks if t["status"] == "pending"]

    def update_task_status(self, task_id: int, status: str):
        """
        تحديث حالة المهمة
        """
        for t in self.tasks:
            if t["id"] == task_id:
                t["status"] = status
                logging.info(f"تم تحديث حالة المهمة {task_id} إلى: {status}")
                return True
        return False