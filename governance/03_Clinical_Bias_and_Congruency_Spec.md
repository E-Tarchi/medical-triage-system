# 🔬 Clinical Bias Mitigation & Algorithmic Congruency Specification

![Clinical Safety](https://img.shields.io/badge/Clinical%20Safety-High%20Priority-red)
![Bias Mitigation](https://img.shields.io/badge/Algorithmic%20Bias-Mitigated-green)
![EU AI Act](https://img.shields.io/badge/EU%20AI%20Act-Art.%2010%20%26%2014-blue)

This document specifies the technical and clinical mechanisms implemented in the **Tuscany Triage System (CDSS)** to prevent algorithmic bias, mitigate automation bias, and cross-validate clinical input congruency.

---

## 📌 1. Algorithmic Bias in Emergency Triage

In acute clinical decision systems, bias can lead to under-triage (underestimating a critical condition) or over-triage (misallocating emergency resources). The system targets two major sources of potential bias:

1. **Subjective Pain Bias:** Over-reliance on patient-reported pain scores (NRS scale) without objective autonomic/hemodynamic validation.
2. **Silent Shock Misses:** Under-triaging hemodynamically unstable patients who maintain normal blood pressure due to compensatory mechanisms.

---

## 🛡️ 2. Algorithmic Safety Controls (`src/clinic.py`)

### 2.1 Occult Shock Detection (Shock Index)
Younger patients or athletes in early septic or hemorrhagic shock often present with normal Systolic Blood Pressure (SBP) despite significant tissue hypoperfusion.

    def check_shock_index(hr, sbp):
        if sbp <= 0: return False
        index = round(hr / sbp, 2)
        if index > 0.9:
            return True # Critical Alert

* **Clinical Rationale:** The Shock Index (Heart Rate / SBP ratio > 0.9) overrides standard threshold checks, flagging occult instability early and mitigating demographic bias related to compensatory physiological mechanisms.

### 2.2 Clinical Congruency Cross-Check (NRS vs. Vitals)
To address potential malingering, acute anxiety, or subjective inflation of pain scores, the system executes an automated congruency cross-check:

    congruency_alert = False
    if nrs_score >= 7 and (60 <= hr <= 85) and (110 <= sbp <= 140):
        congruency_alert = True

* **Clinical Rationale:** Severe pain (NRS >= 7) typically triggers a sympathetic nervous system response (tachycardia and hypertension). Severe reported pain with completely resting vital signs triggers a `DUBIOUS CLINICAL CONGRUENCY` alert, forcing the operator to conduct a targeted reassessment rather than blindly upgrading the triage code.

---

## ⚖️ 3. Regulatory Alignment

* **EU AI Act Article 10 (Data Quality & Bias):** The deterministic cross-checks prevent systematically biased decisions driven by single subjective parameters.
* **MDR Annex I (General Safety & Performance Requirements):** Ensures that decision-support algorithms incorporate clinical safety nets against false positives and false negatives.
