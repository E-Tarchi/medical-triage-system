# 🏥 MDR UE 2017/745 Rule 11 — Software as a Medical Device (SaMD) Qualification

![MDR Status](https://img.shields.io/badge/MDR-UE%202017%2F745-blue)
![Classification](https://img.shields.io/badge/Class-Class%20IIa%20(Rule%2011)-orange)
![Standard](https://img.shields.io/badge/Lifecycle-IEC%2062304-green)

This document provides a formal Regulatory Qualification and Classification Assessment for the **Tuscany Triage System (CDSS)** under the **European Medical Device Regulation (MDR EU 2017/745)**.

---

## 📌 1. Medical Device Qualification (MDR Article 2)

### 1.1 Legal Definition
Under MDR Article 2(1), software intended by the manufacturer to be used for human beings for specific medical purposes (including diagnosis, prevention, monitoring, prediction, prognosis, treatment, or alleviation of disease) qualifies as **Medical Device Software (MDSW)** / **Software as a Medical Device (SaMD)**.

### 1.2 Intended Purpose
The **Tuscany Triage System** is designed for use in Hospital Emergency Departments to:
* Calculate physiological risk scores (Glasgow Coma Scale, Shock Index).
* Process real-time patient vital signs (Heart Rate, Blood Pressure, SpO2) and symptoms.
* Provide clinical decision support by recommending standardized triage urgency codes (White, Azure, Green, Yellow, Orange, Red) and clinical pathways (e.g., Stroke Unit, Shock Room).

Because the software directly influences clinical prioritization and diagnostic decision-making in acute healthcare settings, it **qualifies as a Medical Device**.

---

## ⚖️ 2. Classification Analysis under Rule 11 (Annex VIII)

Annex VIII, Section 3.3 (**Rule 11**) of Regulation (EU) 2017/745 explicitly governs software intended to provide information used to take decisions for diagnostic or therapeutic purposes:

| Rule 11 Criteria | Regulatory Analysis for Tuscany Triage System | Resulting Class |
| :--- | :--- | :---: |
| **Base Rule 11** | Software intended to provide information which is used to take decisions for diagnostic or therapeutic purposes. | **Class IIa** |
| **High Impact Exception** | Software intended to take decisions that may cause death or an irreversible deterioration of a person's state of health. | *Not applicable* (System enforces mandatory Human Oversight / Override, preventing autonomous life-critical actions). |
| **Medium Impact Exception** | Software intended to monitor physiological processes in critical conditions. | **Class IIa / Class IIb** depending on real-time continuous monitoring scope. |

### Final Classification
* **Assigned Class:** **Class IIa** (MDR Annex VIII, Rule 11).
* **Rationale:** The system provides actionable information to triage healthcare professionals to guide clinical prioritization. Because final authority remains with the qualified triage nurse (Human-in-the-Loop), the software acts as a decision support system rather than an autonomous diagnostic device.

---

## 🛡️ 3. Mapping Clinical Logic to MDR Requirements

The table below demonstrates how the clinical modules in `src/clinic.py` align with medical device software performance requirements:

| Clinical Module (`src/clinic.py`) | Clinical Calculation | MDR Performance & Safety Focus |
| :--- | :--- | :--- |
| `check_shock_index()` | Heart Rate / Systolic Blood Pressure ratio | Early detection of occult hemodynamic instability (SI > 0.9). Mitigates risk of under-triage in internal bleeding. |
| `calculate_gcs()` | Summation of Eye, Verbal, and Motor responses | Standardized neurological impairment rating (GCS <= 8 triggers immediate Red Code escalation). |
| `evaluate_clinical_priority()` | Multi-parametric decision engine | Cross-references vital signs against chief complaints to prevent clinical misclassification. |

---

## 📜 4. Applicable Standards & Quality Management Roadmap

To maintain full compliance as a Class IIa Medical Device Software, the system architecture aligns with the following international standards:

1. **EN ISO 13485:** Medical devices - Quality management systems - Requirements for regulatory purposes.
2. **IEC 62304 / EN 62304:** Medical device software - Software life cycle processes (Class B software safety classification).
3. **EN ISO 14971:** Medical devices - Application of risk management to medical devices.
4. **IEC 82304-1:** Health software - Part 1: General requirements for product safety.

---

## ⚖️ 5. Conclusion

The **Tuscany Triage System** is formally qualified as a **Class IIa Medical Device Software (SaMD)** under MDR (EU) 2017/745 Rule 11. By combining strict input validation, deterministic algorithms, and transparent decision rationale, the software fulfills the clinical safety and performance requirements expected of emergency healthcare technology.
