# 🏥 Tuscany Triage System - International Edition
### *Version 0.4.1 - Clinical Decision Support System*

![Version](https://img.shields.io/badge/Version-0.4.1--EN-red)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

An advanced **Clinical Decision Support System (CDSS)** developed to assist healthcare professionals in patient prioritization, following the official 5-color (6-level) protocol of the **Tuscany Region (Italy)**.

---

## 🚀 What's New in v0.4.1

This update marks the transition from a simple data collector to an intelligent clinical analyzer.

### 🧠 Clinical Decision Engine
* **Full Regional Hierarchy:** Integrated all 6 codes (White, Azure, Green, Yellow, Orange, Red).
* **GCS Module:** Automated calculation of the Glasgow Coma Scale.
* **NRS Pain Integration:** Treatment of pain as the *5th Vital Sign*.

### ⚡ The "X+1" Pain Logic
If a patient reports severe pain (**NRS ≥ 7**), the system automatically suggests a priority upgrade to the next level in the hierarchy (e.g., Green → Yellow).

### ⚠️ Safety Alerts: Clinical Congruency
The system features a **Dubious Clinical Congruency Alert**. It cross-references high pain scores with stable vital signs (Heart Rate and Blood Pressure) to prompt the operator for a visual reassessment of psychophysical stress or potential malingering.



---

## 🛠 Features & Normalization

| Feature | Description |
| :--- | :--- |
| **Data Integrity** | Patient names are stored in `lowercase` for database consistency. |
| **UI Rendering** | Professional display using `.title()` capitalization (e.g., `MARIO ROSSI` -> `Mario Rossi`). |
| **Vital Cross-Check** | Automatic Red Code trigger for SpO2 < 90% or GCS ≤ 8. |
| **Live Dashboard** | Real-time tracking of ward workload by color code. |

---

## 📋 Triage Hierarchy Reference

The system operates on the official **Tuscany Centro** priority scale:

1.  🔴 **RED**: Resuscitation / Immediate life-threatening.
2.  🟠 **ORANGE**: High risk / Evolutional urgency.
3.  🟡 **YELLOW**: Mediated urgency.
4.  🟢 **GREEN**: Deferred urgency.
5.  🔵 **AZURE**: Minor urgency.
6.  ⚪ **WHITE**: Non-urgent.

---

🛡 Disclaimer
IMPORTANT: This software is a simulation tool for educational and decision-support purposes. It does not replace professional clinical judgment or official hospital protocols. ALWAYS TRUST YOUR CLINICAL EYES.
