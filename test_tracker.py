
from elite_ai_agency.token_tracker import TokenCostTracker
import json

def main():
    print("=== Initializing Elite AI Agency: Token Cost Tracker ===")
    tracker = TokenCostTracker(model_name="gemini-pro")
    tracker.add_usage(input_tokens=15000, output_tokens=4500)
    tracker.add_usage(input_tokens=25000, output_tokens=8000)
    report = tracker.export_report("cost_report.json")
    print("\n--- Cost Report Result ---")
    print(json.dumps(report, indent=4))

if __name__ == "__main__":
    main()
