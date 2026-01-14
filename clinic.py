# File: clinic.py

def calculate_gcs(e, v, m):
    """Computes the total Glasgow Coma Scale score (3-15)."""
    return e + v + m

def check_shock_index(hr, sbp):
    """Calculates Heart Rate / Systolic BP ratio to detect occult shock."""
    if sbp <= 0: return False
    index = round(hr / sbp, 2)
    # Mostriamo a video il calcolo per trasparenza clinica
    print(f"\n[📊] HEMODYNAMICS: Shock Index = {index}")
    if index > 0.9:
        print("⚠️  CRITICAL ALERT: High Shock Index (>0.9). Potential instability!")
        return True
    return False

def evaluate_clinical_priority(symptom, gcs_score, hr, sp2, sbp, nrs_score, is_unstable):
    """
    Advanced Decision Engine v0.6.1:
    - Maps symptoms to pathways
    - Cross-checks Vitals for safety
    - Validates Clinical Congruency (Pain vs Vitals)
    """
    assigned_code = "GREEN"
    suggested_pathway = "STANDARD CLINICAL PATHWAY"
    triage_order = ["WHITE", "AZURE", "GREEN", "YELLOW", "ORANGE", "RED"]

    # --- 1. PATHWAY & SYMPTOM LOGIC ---
    if any(x in symptom for x in ["arrest", "coma", "shock", "massive hemorrhage", "airway"]):
        assigned_code = "RED"
        suggested_pathway = "RESUSCITATION AREA (SHOCK ROOM)"
    elif any(x in symptom for x in ["stroke", "ictus", "deficit", "paralysis", "speech"]):
        assigned_code = "RED"
        suggested_pathway = "STROKE UNIT PATHWAY"
    elif any(x in symptom for x in ["chest pain", "angina", "myocardial"]):
        assigned_code = "ORANGE"
        suggested_pathway = "CARDIAC PATHWAY (ECG < 10 min)"
    elif any(x in symptom for x in ["trauma", "accident", "fall", "injury"]):
        assigned_code = "YELLOW"
        suggested_pathway = "TRAUMA PATHWAY"
        if any(x in symptom for x in ["major", "high dynamics"]):
            assigned_code = "RED"
    elif any(x in symptom for x in ["poisoning", "overdose", "intoxication"]):
        assigned_code = "RED"
        suggested_pathway = "TOXICOLOGY PATHWAY / ANTIDOTE"
    elif any(x in symptom for x in ["psychiatric", "agitation", "suicide"]):
        assigned_code = "ORANGE"
        suggested_pathway = "PSYCHIATRIC SAFETY PATHWAY"

    # --- 2. VITAL SIGNS CROSS-CHECK (Safety Upgrades) ---
    if gcs_score <= 8 or sp2 < 90 or hr > 140 or hr < 40:
        assigned_code = "RED"
    elif (9 <= gcs_score <= 12) or (90 <= sp2 < 94) or (110 <= hr <= 140) or is_unstable:
        # Se il codice attuale è più basso di ORANGE, fai l'upgrade
        if triage_order.index(assigned_code) < triage_order.index("ORANGE"):
            assigned_code = "ORANGE"

    # --- 3. CLINICAL CONGRUENCY ALERT ---
    congruency_alert = False
    if nrs_score >= 7 and (60 <= hr <= 85) and (110 <= sbp <= 140):
        congruency_alert = True

    # --- 4. PAIN-BASED UPGRADE (X + 1 Logic) ---
    if nrs_score >= 7:
        current_idx = triage_order.index(assigned_code)
        if current_idx < len(triage_order) - 1:
            assigned_code = triage_order[current_idx + 1]

    return assigned_code, suggested_pathway, congruency_alert