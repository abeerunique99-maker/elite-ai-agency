
import sys
import json
from elite_ai_agency.environment_verifier import EnvironmentVerifier
from elite_ai_agency.token_tracker import TokenCostTracker
from elite_ai_agency.prompt_manager import PromptManager

def show_banner():
    print("==========================================")
    print("     ELITE AI AGENCY: COMMAND CENTER      ")
    print("==========================================")

def main():
    show_banner()
    print("1. Run Environment Audit")
    print("2. Run Token Cost Simulation")
    print("3. Run Prompt Manager Catalog")
    
    choice = input("\nSelect an option (1, 2, or 3): ").strip()
    
    if choice == "1":
        print("\n--- Running Environment Verifier ---")
        verifier = EnvironmentVerifier()
        report = verifier.run_full_audit(
            packages=["langgraph", "langchain", "pydantic"],
            env_vars=["GEMINI_API_KEY", "OPENAI_API_KEY"]
        )
        print(json.dumps(report, indent=4))
        
    elif choice == "2":
        print("\n--- Running Token Cost Tracker ---")
        tracker = TokenCostTracker(model_name="gemini-pro")
        tracker.add_usage(input_tokens=20000, output_tokens=5000)
        report = tracker.export_report("cost_report.json")
        print(json.dumps(report, indent=4))

    elif choice == "3":
        print("\n--- Running Prompt Manager ---")
        pm = PromptManager()
        pm.register_template("greeting", "Hello {name}, welcome to Elite AI Agency!")
        rendered = pm.render_template("greeting", {"name": "Enterprise Client"})
        print(f"Rendered Prompt: {rendered}")
        pm.export_templates("prompts_catalog.json")
        
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
