import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from elite_ai_agency.tasks import AgencyTaskManager

def main():
    print('========================================')
    print('    ELITE AI AUTOMATION AGENCY v1.0     ')
    print('========================================')
    
    manager = AgencyTaskManager()
    
    while True:
        print('\nSelect Agency Service:')
        print('1. Generate Client Onboarding Plan')
        print('2. Generate Lead Generation Funnel Plan')
        print('3. Exit')
        
        choice = input('\nEnter your choice (1-3): ').strip()
        
        if choice == '1':
            client = input('Enter client name (e.g., Nexus Corp): ').strip()
            if client:
                print('\n[Agency] Processing Onboarding Plan...')
                manager.generate_and_save_onboarding_plan(client)
                print(f'[Agency] Done! Report saved in reports/ folder.')
        elif choice == '2':
            niche = input('Enter business niche (e.g., Real Estate Agency): ').strip()
            if niche:
                print('\n[Agency] Processing Lead Generation Plan...')
                manager.generate_and_save_lead_gen_plan(niche)
                print(f'[Agency] Done! Report saved in reports/ folder.')
        elif choice == '3':
            print('Exiting Elite AI Agency. Goodbye!')
            break
        else:
            print('Invalid choice. Please choose 1, 2, or 3.')

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)