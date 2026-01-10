# =================================================================
# Tuscany Triage System v0.5.7
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

import datetime

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


def check_shock_index(hr, sbp):
    """Calculates Heart Rate / Systolic BP ratio to detect occult shock."""
    if sbp <= 0: return False
    index = round(hr / sbp, 2)
    print(f"\n[📊] HEMODYNAMICS: Shock Index = {index}")
    if index > 0.9:
        print("⚠️  CRITICAL ALERT: High Shock Index (>0.9). Potential instability!")
        return True
    return False


def log_event(message):
    """Secure logging for clinical audit and accountability."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open("triage_audit_log.txt", "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {message}\n")
    except Exception as e:
        print(f"❌ Logging Error: {e}")


def display_nrs_legend():
    print("\n" + "-" * 45)
    print("      PAIN SCALE REFERENCE (NRS)")
    print("-" * 45)
    print(" 0      : No Pain")
    print(" 1 - 3  : Mild Pain")
    print(" 4 - 6  : Moderate Pain")
    print(" 7 - 10 : SEVERE PAIN (⚠️ Priority Upgrade)")
    print("-" * 45)


def main():
    print("\n" + "=" * 75)
    print(" TUSCANY TRIAGE SYSTEM v0.5.7 - CLINICAL AUDIT EDITION ")
    print("=" * 75)

    # 1. OPERATOR LOGIN
    operator_id = input("Operator ID (Name or Badge Number) to start shift: ").strip().upper()
    if not operator_id: operator_id = "ANONYMOUS_USER"

    log_event(f"SHIFT_START - Operator: {operator_id}")
    print(f"\nWelcome, Operator {operator_id}. System ready for admissions.")

    triage_counters = {color: 0 for color in TRIAGE_CODES}

    while True:
        print("\n" + "-" * 55)
        raw_name = input("Patient Name/ID (or type 'exit' to logout): ")
        if raw_name.lower() == 'exit':
            break

        display_name = raw_name.title()

        # 2. ASSESSMENT INPUTS
        print(f"\n[ASSESSMENT FOR: {display_name}]")
        symptom = input("  Chief Complaint: ").lower()
        hr = get_valid_score("  Heart Rate (BPM): ", 20, 220)
        sbp = get_valid_score("  Systolic BP (mmHg): ", 40, 300)

        # Hemodynamic Check (Shock Index)
        is_unstable = check_shock_index(hr, sbp)

        # 3. INTERACTIVE GCS
        print("\n[NEUROLOGICAL ASSESSMENT (GCS)]")
        e = get_valid_score("  Eyes (1-4): ", 1, 4, "4:Spontaneous, 3:Voice, 2:Pain, 1:None")
        v = get_valid_score("  Verbal (1-5): ", 1, 5, "5:Oriented, 4:Confused, 3:Inapprop., 2:Sounds, 1:None")
        m = get_valid_score("  Motor (1-6): ", 1, 6, "6:Obeys, 5:Localizes, 4:Flexion, 3:Abnormal, 2:Extension, 1:None")
        gcs_score = e + v + m
        print(f"  >>> Computed GCS Total: {gcs_score}/15")

        # 4. PAIN ASSESSMENT
        display_nrs_legend()
        nrs_score = get_valid_score("  Enter NRS Score (0-10): ", 0, 10)

        # 5. DECISION ENGINE
        suggested_code = "GREEN"

        # Symptom-based priority
        if any(x in symptom for x in ["arrest", "coma", "shock", "hemorrhage", "bleeding"]):
            suggested_code = "RED"
        elif any(x in symptom for x in ["chest pain", "angina"]):
            suggested_code = "ORANGE"

        # Neurological / Hemodynamic Hard-Stops
        if gcs_score <= 8:
            suggested_code = "RED"
        elif is_unstable:
            suggested_code = "ORANGE"
            print("  [SYSTEM ACTION] High Shock Index forced priority to ORANGE.")

        # Pain-based upgrade (X + 1 Logic)
        final_code = suggested_code
        if nrs_score >= 7:
            idx = TRIAGE_CODES.index(suggested_code)
            if idx < len(TRIAGE_CODES) - 1:
                final_code = TRIAGE_CODES[idx + 1]
                print(f"  [CLINICAL UPGRADE] High pain intensity. Recommended: {final_code}")

        # 6. AUDIT & OVERRIDE
        print(f"\n>>> RECOMMENDED CODE: {final_code}")
        conf = input(f"Confirm {final_code}? (y/n): ").lower()

        actual_code = final_code
        if conf != 'y':
            actual_code = input(f"Select Manual Code {TRIAGE_CODES}: ").upper()
            if actual_code not in TRIAGE_CODES: actual_code = final_code
            # LOG MANUAL OVERRIDE
            log_event(f"OVERRIDE - Op: {operator_id} modified {display_name} from {final_code} to {actual_code}")

        # 7. FINALIZATION & LOGGING
        triage_counters[actual_code] += 1
        si_status = "CRITICAL" if is_unstable else "STABLE"
        log_event(
            f"ADMISSION - Op: {operator_id} | Pat: {display_name} | Code: {actual_code} | GCS: {gcs_score} | SI: {si_status}")

        print(f"\nPatient {display_name} admitted with code {actual_code}.")

    log_event(f"SHIFT_END - Operator: {operator_id}")
    print("\nShift ended. Audit log secured. Goodbye!")


if __name__ == "__main__":
    main()
