
import json
from elite_ai_agency.environment_verifier import EnvironmentVerifier

def main():
    print("=== Initializing Elite AI Agency: Environment Verifier ===")
    verifier = EnvironmentVerifier(required_python_version=(3, 11))
    
    # قائمة الحزم ومتغيرات البيئة المراد التحقق منها
    target_packages = ["langgraph", "langchain", "pydantic"]
    target_env_vars = ["GEMINI_API_KEY", "OPENAI_API_KEY"]
    
    report = verifier.run_full_audit(target_packages, target_env_vars)
    
    print("\n--- Audit Report Result ---")
    print(json.dumps(report, indent=4))

if __name__ == "__main__":
    main()
