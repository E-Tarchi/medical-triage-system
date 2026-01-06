# --- Medical Triage System - Version 0.2 ---
# Prototype update: Added Green and White codes for full categorization

cardiac_symptoms = ["chest pain", "arrhythmia", "palpitations", "shortness of breath"]

while True:
    print("\n--- EMERGENCY ROOM ADMISSION SYSTEM v0.2 ---")
    patient_name = input("Patient Name (or type 'exit'): ").title()

    if patient_name == "Exit":
        print("System closing. Great job today, warrior!")
        break

    # Input vital signs
    oxygen_saturation = int(input("Oxygen Saturation (SpO2 %): "))
    systolic_pressure = int(input("Systolic Blood Pressure (mmHg): "))
    main_symptom = input("Main Symptom: ").lower().strip()

    # Priority Logic (Triage)
    if systolic_pressure >= 180 or oxygen_saturation < 90:
        print(f">>> RED CODE: Immediate intervention for {patient_name}!")
        
    elif (140 <= systolic_pressure < 180) or (90 <= oxygen_saturation <= 93) or (main_symptom in cardiac_symptoms):
        print(f">>> YELLOW CODE for {patient_name} (Urgent)")
        if oxygen_saturation <= 93:
            print(">>> CLINICAL NOTE: Perform BGA/EGA and administer Oxygen.")
            
    elif 120 <= systolic_pressure < 140:
        print(f">>> GREEN CODE for {patient_name} (Low Priority)")
        
    else:
        print(f">>> WHITE CODE for {patient_name} (Non-Urgent/General Exam)")
