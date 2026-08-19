
import sys
import os
import json
import importlib.util
from typing import Dict, Any

class EnvironmentVerifier:
    def __init__(self, required_python_version: tuple = (3, 11)):
        self.required_python_version = required_python_version
        self.report: Dict[Any, Any] = {}

    def check_python_version(self) -> bool:
        current_version = sys.version_info
        is_valid = current_version >= self.required_python_version
        self.report["python_version"] = {
            "required": f"{self.required_python_version[0]}.{self.required_python_version[1]}",
            "current": f"{current_version.major}.{current_version.minor}.{current_version.micro}",
            "status": "PASS" if is_valid else "FAIL"
        }
        return is_valid

    def check_package(self, package_name: str) -> bool:
        spec = importlib.util.find_spec(package_name)
        exists = spec is not None
        if "packages" not in self.report:
            self.report["packages"] = {}
        self.report["packages"][package_name] = {
            "status": "PASS" if exists else "FAIL"
        }
        return exists

    def check_env_variable(self, var_name: str) -> bool:
        exists = var_name in os.environ
        if "environment_variables" not in self.report:
            self.report["environment_variables"] = {}
        self.report["environment_variables"][var_name] = {
            "status": "PASS" if exists else "FAIL"
        }
        return exists

    def run_full_audit(self, packages: list, env_vars: list, output_filename: str = "audit_report.json") -> Dict[Any, Any]:
        self.check_python_version()
        for pkg in packages:
            self.check_package(pkg)
        for var in env_vars:
            self.check_env_variable(var)
        
        # حفظ التقرير تلقائياً كملف JSON
        with open(output_filename, "w", encoding="utf-8") as f:
            json.dump(self.report, f, indent=4, ensure_ascii=False)
            
        print(f"--- Audit report successfully saved to {output_filename} ---")
        return self.report
