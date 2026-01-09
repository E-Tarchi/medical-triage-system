# --- Tuscany Triage System - International Edition - Version 0.4.1 ---
# Major Release: NRS Pain Module & Full Regional Hierarchy
# Features: 
# - Normalized Patient Database (lower case storage, .title() display)
# - Full 6-Code Hierarchy (White to Red)
# - NRS Module with Clinical Congruency Alert
# - Pain-Based Priority Upgrade (X + 1 Logic)

# Official Triage Hierarchy (Tuscany Region Protocol)
TRIAGE_CODES = ["WHITE", "AZURE", "GREEN", "YELLOW", "ORANGE", "RED"]

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

def display_nrs_legend():
    print("\n" + "-"*45)
    print("      PAIN SCALE REFERENCE (NRS)")
    print("-"*45)
    print(" 0      : No Pain")
    print(" 1 - 3  : Mild Pain")
    print(" 4 - 6  : Moderate Pain")
    print(" 7 - 10 : SEVERE PAIN (⚠️ Priority Upgrade)")
    print("-"*45)

def main():
    triage_counters = {color: 0 for color in TRIAGE_CODES}
    all_patients = []
    
    while True:
        print("\n" + "="*75)
        print(" TUSCANY TRIAGE SYSTEM v0.4.1-EN - ADVANCED CLINICAL ANALYZER ")
        print("="*75)

        raw_name = input("Patient Name or ID (or type 'exit' to quit): ")
        if raw_name.lower() == 'exit':
            break
        
        # Data Normalization
        patient_db_id = raw_name.lower()  # For database consistency
        display_name = raw_name.title()    # For professional UI display

        # 1. CHIEF COMPLAINT
        print("\n[CHIEF COMPLAINT / ADMISSION REASON]")
        symptom = input("  Main symptom or sign: ").lower()
        
        # 2. VITAL SIGNS
        print("\n[VITAL SIGNS]")
        hr  = get_valid_score("  Heart Rate (BPM): ", 20, 220)
        sp2 = get_valid_score("  Oxygen Saturation (%): ", 50, 100)
        sbp = get_valid_score("  Systolic Blood Pressure (mmHg): ", 40, 300)
        
        # 3. GCS (NEUROLOGICAL ASSESSMENT)
        print("\n[NEUROLOGICAL ASSESSMENT (GCS)]")
        e = get_valid_score("  Eyes (1-4): ", 1, 4, "4:Spontaneous, 3:Voice, 2:Pain, 1:None")
        v = get_valid_score("  Verbal (1-5): ", 1, 5, "5:Oriented, 4:Confused, 3:Inapprop., 2:Sounds, 1:None")
        m = get_valid_score("  Motor (1-6): ", 1, 6, "6:Obeys, 5:Localizes, 4:Flexion, 3:Abnormal, 2:Extension, 1:None")
        gcs_score = e + v + m

        # 4. PAIN ASSESSMENT (NRS)
        display_nrs_legend()
        nrs_score = get_valid_score("  Enter NRS Score (0-10): ", 0, 10)

        # 5. DECISION ENGINE
        suggested_pathway = "Standard Observation"
        assigned_code = "GREEN" # Baseline

        # --- PATHWAY & SYMPTOM LOGIC ---
        if any(x in symptom for x in ["arrest", "coma", "shock", "massive hemorrhage"]):
            assigned_code = "RED"
            suggested_pathway = "RESUSCITATION AREA"
        elif any(x in symptom for x in ["chest pain", "angina", "myocardial"]):
            assigned_code = "ORANGE"
            suggested_pathway = "CARDIAC PATHWAY (ECG < 10 min)"
        elif any(x in symptom for x in ["stroke", "ictus", "deficit", "speech"]):
            assigned_code = "RED"
            suggested_pathway = "STROKE UNIT PATHWAY"
        elif any(x in symptom for x in ["trauma", "accident", "fall"]):
            assigned_code = "YELLOW"
            suggested_pathway = "TRAUMA PATHWAY"

        # --- VITAL SIGNS CROSS-CHECK ---
        if gcs_score <= 8 or sp2 < 90 or hr > 140 or hr < 40:
            assigned_code = "RED"
        elif (9 <= gcs_score <= 12) or (90 <= sp2 < 94) or (110 <= hr <= 140):
            if TRIAGE_CODES.index(assigned_code) < TRIAGE_CODES.index("YELLOW"):
                assigned_code = "YELLOW"

        # --- CLINICAL CONGRUENCY ALERT (v0.4.0) ---
        if nrs_score >= 7 and (60 <= hr <= 85) and (110 <= sbp <= 140):
            print("\n[!] ⚠️  SYSTEM ALERT: DUBIOUS CLINICAL CONGRUENCY")
            print(f"--> Severe pain reported (NRS: {nrs_score}), but vital signs are stable.")
            print("--> Assess for psychophysical stress, anxiety, or malingering.")
            print("--> Visual reassessment required before confirming the code.")

        # --- PAIN-BASED UPGRADE (X + 1 Logic) ---
        if nrs_score >= 7:
            current_idx = TRIAGE_CODES.index(assigned_code)
            if current_idx < len(TRIAGE_CODES) - 1:
                assigned_code = TRIAGE_CODES[current_idx + 1]
                print(f"\n[CLINICAL INFO] Pain-based priority upgrade to: {assigned_code}")

        # 6. FINAL REVIEW & CONFIRMATION
        print("\n" + "-"*55)
        print(f" TRIAGE SUMMARY FOR: {display_name}")
        print(f" FINAL PROPOSED CODE: {assigned_code}")
        print(f" SUGGESTED PATHWAY: {suggested_pathway}")
        print("-"*55)
        
        conf = input(f"Confirm assignment for {display_name}? (y/n): ").lower()
        if conf != 'y':
            assigned_code = input(f"Select manual code {TRIAGE_CODES}: ").upper()

        # 7. LOGGING & DASHBOARD
        triage_counters[assigned_code] += 1
        all_patients.append(f"Patient: {display_name} | CODE: {assigned_code} | NRS: {nrs_score} | GCS: {gcs_score}")

        print("\n[ WARD STATUS - LIVE DASHBOARD ]")
        for color in TRIAGE_CODES:
            if triage_counters[color] > 0:
                print(f"  {color}: {triage_counters[color]} patient(s)")
        
        input("\nPress Enter to admit next patient...")

    print("\n" + "="*55)
    print("SESSION CLOSED - Final Ward Report:")
    for color, count in triage_counters.items():
        print(f"  {color}: {count}")
    print("\nShift ended. Excellent management, Mr. Anderson.")

if __name__ == "__main__":
    main()
