# File: utils.py
import datetime

def get_valid_score(prompt, min_val, max_val, legend=None):
    """Handles user input with range validation and error catching."""
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
            print("  (!) Error: Please enter a numeric value.")

def log_event(message):
    """Writes system events to a secure log file for clinical audit."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open("triage_audit_log.txt", "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {message}\n")
    except Exception as e:
        print(f"❌ Logging Error: {e}")

def display_nrs_legend():
    """Displays the Numeric Rating Scale for pain assessment."""
    print("\n" + "-" * 45)
    print("      PAIN SCALE REFERENCE (NRS)")
    print("-" * 45)
    print(" 0      : No Pain")
    print(" 1 - 3  : Mild Pain")
    print(" 4 - 6  : Moderate Pain")
    print(" 7 - 10 : SEVERE PAIN (⚠️ Priority Upgrade)")
    print("-" * 45)