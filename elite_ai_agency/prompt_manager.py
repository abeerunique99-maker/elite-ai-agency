
import json
from typing import Dict, Any

class PromptManager:
    def __init__(self):
        self.templates: Dict[str, str] = {}

    def register_template(self, name: str, template_str: str):
        self.templates[name] = template_str
        print(f"--- Prompt template [{name}] registered successfully ---")

    def render_template(self, name: str, context: Dict[str, Any]) -> str:
        if name not in self.templates:
            raise ValueError(f"Template '{name}' not found.")
        
        template = self.templates[name]
        try:
            return template.format(**context)
        except KeyError as e:
            raise ValueError(f"Missing context variable for template: {e}")

    def export_templates(self, filename: str = "prompts_catalog.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.templates, f, indent=4, ensure_ascii=False)
        print(f"--- Prompts catalog successfully exported to {filename} ---")
        return self.templates
