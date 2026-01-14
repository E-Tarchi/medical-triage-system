# =================================================================
# Tuscany Triage System v0.6.2
# Copyright (C) 2026 Emanuele Tarchi
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
# =================================================================

from clinic import check_shock_index, calculate_gcs, evaluate_clinical_priority
from utils import get_valid_score, log_event, display_nrs_legend

# Global Triage Hierarchy
TRIAGE_CODES = ["WHITE", "AZURE", "GREEN", "YELLOW", "ORANGE", "RED"]

def main():
    print("\n" + "=" * 75)
    print(" TUSCANY TRIAGE SYSTEM v0.6.1 - MODULAR CLINICAL ENGINE ")
    print("=" * 75)

    # 1. OPERATOR LOGIN & SHIFT INITIALIZATION
    operator_id = input("Operator ID (Name or Badge Number) to start shift: ").strip().upper()
    if not operator_id:
        operator_id = "ANONYMOUS_USER"

    log_event(f"SHIFT_START - Operator: {operator_id}")
    print(f"\nWelcome, Operator {operator_id}. System ready for admissions.")

    # Initialize session counters
    triage_counters = {color: 0 for color in TRIAGE_CODES}

    while True:
        print("\n" + "-" * 55)
        raw_name = input("Patient Name/ID (or type 'exit' to logout): ")
        if raw_name.lower() == 'exit':
            break

        # UI Normalization
        display_name = raw_name.title()

        # 2. CLINICAL ASSESSMENT INPUTS
        print(f"\n[ASSESSMENT FOR: {display_name}]")
        symptom = input("  Chief Complaint: ").lower()
        hr = get_valid_score("  Heart Rate (BPM): ", 20, 220)
        sp2 = get_valid_score("  Oxygen Saturation (%): ", 50, 100)
        sbp = get_valid_score("  Systolic BP (mmHg): ", 40, 300)

        # Hemodynamic status check
        is_unstable = check_shock_index(hr, sbp)

        # 3. NEUROLOGICAL ASSESSMENT (GCS)
        print("\n[NEUROLOGICAL ASSESSMENT (GCS)]")
        e = get_valid_score("  Eyes (1-4): ", 1, 4, "4:Spontaneous, 3:Voice, 2:Pain, 1:None")
        v = get_valid_score("  Verbal (1-5): ", 1, 5, "5:Oriented, 4:Confused, 3:Inapprop., 2:Sounds, 1:None")
        m = get_valid_score("  Motor (1-6): ", 1, 6, "6:Obeys, 5:Localizes, 4:Flexion, 3:Abnormal, 2:Extension, 1:None")
        gcs_score = calculate_gcs(e, v, m)
        print(f"  >>> Computed GCS Total: {gcs_score}/15")

        # 4. PAIN ASSESSMENT (NRS)
        display_nrs_legend()
        nrs_score = get_valid_score("  Enter NRS Score (0-10): ", 0, 10)

        # 5. CLINICAL DECISION ENGINE
        # Passing all parameters to the clinical module to get code, pathway, and congruency alert
        suggested_code, pathway, alert = evaluate_clinical_priority(
            symptom, gcs_score, hr, sp2, sbp, nrs_score, is_unstable
        )

        # Handle Clinical Congruency Alert (Pain vs Vitals)
        if alert:
            print("\n[!] ⚠️  SYSTEM ALERT: DUBIOUS CLINICAL CONGRUENCY")
            print("    --> Severe pain reported, but vital signs are stable.")
            print("    --> Assess for anxiety or malingering before confirmation.")

        print(f"\n>>> SUGGESTED PATHWAY: {pathway}")

        # 6. CLINICAL AUDIT & MANUAL OVERRIDE
        final_code = suggested_code
        print(f">>> RECOMMENDED CODE: {final_code}")

        conf = input(f"Confirm {final_code}? (y/n): ").lower()

        actual_code = final_code
        if conf != 'y':
            actual_code = input(f"Select Manual Code {TRIAGE_CODES}: ").upper()
            if actual_code not in TRIAGE_CODES:
                actual_code = final_code
            # Log override for accountability
            log_event(f"OVERRIDE - Op: {operator_id} modified {display_name} from {final_code} to {actual_code}")

        # 7. ADMISSION FINALIZATION & DASHBOARD UPDATE
        triage_counters[actual_code] += 1
        si_status = "CRITICAL" if is_unstable else "STABLE"

        # Comprehensive event logging
        log_event(
            f"ADMISSION - Op: {operator_id} | Pat: {display_name} | Code: {actual_code} | GCS: {gcs_score} | SI: {si_status}"
        )

        print(f"\nPatient {display_name} admitted with code {actual_code}.")

    log_event(f"SHIFT_END - Operator: {operator_id}")
    print("\nShift ended. Audit log secured. Goodbye!")


if __name__ == "__main__":
    main()