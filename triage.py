# --- Tuscany Triage System - International Edition - Version 0.3.7 ---
# Major Release: Integrated Advanced Clinical Analyzer
# Features: 
# - GCS (Glasgow Coma Scale) Module
# - Chief Complaint Keyword Analysis
# - Vital Signs Cross-Check (HR, SpO2)
# - Live Ward Dashboard & Persistent Session Counters
# - Professional Input Validation & Safety Overrides
def get_valid_score(prompt, min_val, max_val, legend=None):
    if legend:
        print(f"  Reference: {legend}")
    while True:
        try:
            score = int(input(prompt))
            if min_val <= score <= max_val:
                return score
            else:
                print(f"  (!) Out of range ({min_val}-{max_val}).")
        except ValueError:
            print("  (!) Error: Please enter a number.")

def main():
    triage_counters = {"RED": 0, "ORANGE": 0, "GREEN/AZURE": 0}
    all_patients = []
    
    while True:
        print("\n" + "="*75)
        print(" TUSCANY TRIAGE SYSTEM v0.3.7-EN - ADVANCED CLINICAL ANALYZER ")
        print("="*75)

        patient_id = input("Patient Name or ID (or type 'exit' to quit): ")
        if patient_id.lower() == 'exit':
            break

        # 1. CHIEF COMPLAINT ANALYSIS
        print("\n[CHIEF COMPLAINT / ADMISSION REASON]")
        symptom = input("  Main symptom or sign: ").lower()
        
        # 2. VITAL SIGNS
        print("\n[VITAL SIGNS]")
        hr  = get_valid_score("  Heart Rate (BPM): ", 20, 220)
        sp2 = get_valid_score("  Oxygen Saturation (%): ", 50, 100)
        
        # 3. GCS (NEUROLOGICAL ASSESSMENT)
        print("\n[NEUROLOGICAL ASSESSMENT (GCS)]")
        e = get_valid_score("  Eyes (1-4): ", 1, 4, "4:Spontaneous, 3:Voice, 2:Pain, 1:None")
        v = get_valid_score("  Verbal (1-5): ", 1, 5, "5:Oriented, 4:Confused, 3:Inapprop., 2:Sounds, 1:None")
        m = get_valid_score("  Motor (1-6): ", 1, 6, "6:Obeys, 5:Localizes, 4:Flexion, 3:Abnormal, 2:Extension, 1:None")
        gcs_score = e + v + m

        # 4. DECISION ENGINE (Expanded Symptoms + Vital Signs)
        suggested_pathway = "Standard Observation"
        assigned_code = "GREEN/AZURE"

        # --- CRITICAL SYMPTOMS LOGIC ---
        # IMMEDIATE RED CODE FOR EXTREME SYMPTOMS
        if any(x in symptom for x in ["arrest", "coma", "shock", "massive hemorrhage", "airway obstruction"]):
            assigned_code = "RED"
            suggested_pathway = "RESUSCITATION AREA (SHOCK ROOM)"
        
        # SPECIFIC CLINICAL PATHWAYS
        elif any(x in symptom for x in ["chest pain", "angina", "myocardial"]):
            assigned_code = "ORANGE"
            suggested_pathway = "CARDIAC PATHWAY (ECG < 10 min)"
        elif any(x in symptom for x in ["stroke", "ictus", "deficit", "paralysis", "speech", "fas"]):
            assigned_code = "RED"
            suggested_pathway = "STROKE UNIT PATHWAY"
        elif any(x in symptom for x in ["trauma", "accident", "fall", "injury"]):
            assigned_code = "ORANGE"
            suggested_pathway = "TRAUMA PATHWAY"
            if "major" in symptom or "high dynamics" in symptom:
                assigned_code = "RED"
        elif any(x in symptom for x in ["hemorrhage", "bleeding", "melaena", "hematemesis"]):
            assigned_code = "ORANGE"
            suggested_pathway = "HEMORRHAGIC / SURGICAL PATHWAY"
        elif any(x in symptom for x in ["psychiatric", "agitation", "self-harm", "suicide"]):
            assigned_code = "ORANGE"
            suggested_pathway = "PSYCHIATRIC SAFETY PATHWAY"
        elif any(x in symptom for x in ["birth", "contractions", "pregnancy", "labor"]):
            assigned_code = "ORANGE"
            suggested_pathway = "OBSTETRIC-GYNECOLOGICAL PATHWAY"
        elif any(x in symptom for x in ["burn", "fire", "scald"]):
            assigned_code = "ORANGE"
            suggested_pathway = "BURN UNIT PATHWAY"
        elif any(x in symptom for x in ["poisoning", "overdose", "intoxication"]):
            assigned_code = "RED"
            suggested_pathway = "TOXICOLOGY PATHWAY / ANTIDOTE"

        # --- CROSS-CHECK WITH VITAL SIGNS ---
        # Vitals can upgrade the code, never downgrade it
        if gcs_score <= 8 or sp2 < 90 or hr > 140 or hr < 40:
            assigned_code = "RED"
        elif (9 <= gcs_score <= 12) or (90 <= sp2 < 94) or (110 <= hr <= 140):
            if assigned_code != "RED":
                assigned_code = "ORANGE"

        # 5. LOG UPDATE
        triage_counters[assigned_code] += 1
        patient_summary = f"Patient: {patient_id} | CODE: {assigned_code} | Symptom: {symptom[:15]}... | GCS: {gcs_score} | HR: {hr}"
        all_patients.append(patient_summary)

        # 6. CURRENT SUMMARY
        print("\n" + "-"*55)
        print(f" TRIAGE RESULT FOR: {patient_id}")
        print(f" ASSIGNED CODE: {assigned_code}")
        print(f" SUGGESTED PATHWAY: {suggested_pathway}")
        print("-"*55)

        # 7. LIVE DASHBOARD
        print("\n[ WARD STATUS - WORKLOAD ]")
        for color, count in triage_counters.items():
            print(f"  {color}: {count} patient(s)")
        
        print("\n--- VISITED PATIENTS LOG ---")
        for p in all_patients:
            print(f" > {p}")
        
        input("\nPress Enter for next patient...")

    print("\n" + "="*55)
    print("SESSION CLOSED - Final Summary:")
    for color, count in triage_counters.items():
        print(f"  {color}: {count}")
    print("\nGreat work in the ward today. Now rest well, warrior.")

if __name__ == "__main__":
    main()
