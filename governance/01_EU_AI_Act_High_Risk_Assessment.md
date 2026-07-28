# 🇪🇺 EU AI Act Compliance Assessment & High-Risk System Classification

![EU AI Act Status](https://img.shields.io/badge/EU%20AI%20Act-High--Risk%20System-red)
![Classification](https://img.shields.io/badge/Class-Annex%20III%20%2F%20Healthcare-blue)
![Human Oversight](https://img.shields.io/badge/Oversight-Human--in--the--Loop%20(Art.%2014)-green)

This document provides a formal Regulatory Compliance Assessment for the **Tuscany Triage System (CDSS)** under **European Union Regulation (EU) 2024/1689 (EU Artificial Intelligence Act)**.

---

## 📌 1. System Qualification & Risk Categorization

### 1.1 Legal Categorization
Under Article 6 and **Annex III (Section 5 - Essential Public Services & Healthcare)** of Regulation (EU) 2024/1689, software systems used for emergency triage, clinical prioritization, and resource allocation in emergency healthcare settings are classified as **High-Risk AI / Decision Systems**.

### 1.2 System Purpose & Clinical Scope
The system operates as a **Clinical Decision Support System (CDSS)** designed to evaluate patient vital signs, Glasgow Coma Scale (GCS), Shock Index, and reported pain (NRS scale) to suggest an emergency code priority and clinical pathway.

---

## 🛡️ 2. Mapping Requirements to Code Architecture

The table below maps the mandatory requirements for High-Risk AI Systems under Chapter II of the EU AI Act directly to the Python implementation of the Tuscany Triage System:

| EU AI Act Article | Mandatory Requirement | Implementation in Python Architecture (`src/`) | Compliance Status |
| :--- | :--- | :--- | :---: |
| **Article 9** | **Risk Management System** | `clinic.py` -> `evaluate_clinical_priority()`<br>• Automated safety upgrades for critical vitals (SpO2 < 90%, GCS <= 8, Shock Index > 0.9).<br>• Clinical Congruency Alert cross-checks pain vs. autonomic response. | 🟢 COMPLIANT |
| **Article 10** | **Data Quality & Governance** | `utils.py` -> `get_valid_score()`<br>• Input range validation and exception handling prevent malformed or out-of-bounds physiological data entry. | 🟢 COMPLIANT |
| **Article 12** | **Record-Keeping & Logging** | `utils.py` -> `log_event()`<br>• Continuous audit trail recording operator login, shift events, admission metrics, and clinical overrides in `triage_audit_log.txt`. | 🟢 COMPLIANT |
| **Article 13** | **Transparency & Explainability** | `clinic.py` & `main.py`<br>• Deterministic logic tree.<br>• Real-time display of calculated parameters (Shock Index, GCS total) and clinical rationale before code assignment. | 🟢 COMPLIANT |
| **Article 14** | **Human Oversight (Human-in-the-Loop)** | `main.py` -> Section 6 (Manual Override)<br>• System proposals are non-binding.<br>• Mandatory operator confirmation required.<br>• Forced audit logging when an operator overrides a suggested code. | 🟢 COMPLIANT |

---

## 🔬 3. Deep Dive: Human Oversight Architecture (Art. 14)

Article 14 of the EU AI Act mandates that High-Risk systems must be designed so that natural persons can oversee their functioning, prevent automation bias, and override system outputs.

### 3.1 Override Workflow
The system explicitly enforces Human-in-the-Loop (HITL) governance in `main.py`:

    # System output generation
    suggested_code, pathway, alert = evaluate_clinical_priority(...)

    print(f">>> RECOMMENDED CODE: {final_code}")
    conf = input(f"Confirm {final_code}? (y/n): ").lower()

    # Operator override decision
    if conf != 'y':
        actual_code = input(f"Select Manual Code {TRIAGE_CODES}: ").upper()
        # Log override for medico-legal accountability
        log_event(f"OVERRIDE - Op: {operator_id} modified {display_name} from {final_code} to {actual_code}")

### 3.2 Mitigation of Automation Bias
* **Clinical Congruency Warning:** If a patient reports severe pain (NRS >= 7) but vital signs show normal hemodynamics (HR 60-85, SBP 110-140), the system raises an explicit alert (`DUBIOUS CLINICAL CONGRUENCY`) forcing the triage nurse to reassess for anxiety or malingering rather than blindly trusting the pain score.

---

## 🧾 4. Auditability & Non-Repudiation (Art. 12)

All events logged via `utils.log_event()` include UTC/local ISO timestamps and operator identifiers to ensure medico-legal non-repudiation:

    [2026-07-28 20:15:10] SHIFT_START - Operator: NURSE_MARIO_ROSSI
    [2026-07-28 20:18:22] ADMISSION - Op: NURSE_MARIO_ROSSI | Pat: John Doe | Code: RED | GCS: 7 | SI: CRITICAL
    [2026-07-28 20:22:05] OVERRIDE - Op: NURSE_MARIO_ROSSI modified Jane Smith from YELLOW to ORANGE
    [2026-07-28 20:22:05] ADMISSION - Op: NURSE_MARIO_ROSSI | Pat: Jane Smith | Code: ORANGE | GCS: 15 | SI: STABLE

---

## ⚖️ 5. Conclusion & Regulatory Readiness

The **Tuscany Triage System** demonstrates that algorithmic clinical decision tools can be engineered with embedded compliance. By coupling deterministic clinical protocols with mandatory human oversight, input sanitization, and structured audit logging, the system fulfills the core requirements of the **EU AI Act for High-Risk Systems**.
