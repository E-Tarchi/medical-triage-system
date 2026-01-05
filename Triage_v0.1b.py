# --- Basic Medical Triage - Version 0.1 Beta ---
# Initial prototype: focus on blood pressure and respiratory/cardiac symptoms

# Clinical list for cardiac symptoms
cardiac_symptoms = ["chest pain", "arrhythmia", "palpitations"]

while True:
    print("\n--- NEW TRIAGE ADMISSION ---")
    patient_name = input("Patient Name (or type 'exit'): ").title()

    if patient_name == "Exit":
        print("Shift ended. System closing. Rest well, warrior!")
        break

    # Input vital signs
    oxygen_saturation = int(input("Oxygen Saturation (SpO2 %): "))
    systolic_pressure = int(input("Systolic Blood Pressure (mmHg): "))
    main_symptom = input("Main Symptom: ").lower().strip()

    # Logic Flag for Blood Gas Analysis (BGA/EGA)
    bga_needed = False
    if oxygen_saturation <= 93:
        print(">>> ALERT: Perform BGA (EGA) and administer Oxygen")
        bga_needed = True

    # Priority Categorization (Triage Logic)
    if systolic_pressure >= 180:
        print(f">>> RED CODE: Immediate danger for {patient_name}!")
    elif bga_needed == True:
        print(f">>> YELLOW CODE for {patient_name} (Respiratory Failure)")
    elif main_symptom in cardiac_symptoms:
        print(f"Forward {patient_name} to Cardiology department.")
    elif 140 <= systolic_pressure < 180:
        print(f">>> YELLOW CODE for {patient_name}")
    else:
        print(f">>> Patient {patient_name} waiting for general examination.")
