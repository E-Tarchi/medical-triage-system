# 🏥 Tuscany Triage System — International Edition
### *Version 0.4.1 — Clinical Decision Support System*

![Version](https://img.shields.io/badge/Version-0.4.1--EN-red)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)

An advanced **Clinical Decision Support System (CDSS)** designed to assist healthcare professionals in patient prioritization, following the official 5‑color (6‑level) protocol of the **Tuscany Region (Italy)**.

---

## 🚀 What's New in v0.4.1
This release marks the evolution from a simple data collector to a true clinical reasoning engine.

### 🧠 Clinical Decision Engine
* **Full Regional Hierarchy:** Integration of all 6 triage codes (White, Azure, Green, Yellow, Orange, Red).
* **GCS Module:** Automated calculation of the Glasgow Coma Scale.
* **NRS Pain Integration:** Pain treated as the 5th Vital Sign.

### ⚡ “X+1” Pain Logic
If a patient reports severe pain (**NRS ≥ 7**), the system automatically suggests upgrading the priority to the next level in the hierarchy (e.g., Green → Yellow).

### ⚠️ Safety Alerts: Clinical Congruency
A **Dubious Clinical Congruency Alert** cross‑checks high pain scores with stable vital signs (Heart Rate and Blood Pressure), prompting the operator to reassess psychophysical stress or potential malingering.


### 📊 Decision Workflow
```mermaid
graph TD
    A[Patient Arrival] --> B[Vital Signs & GCS]
    B --> C{Critical Symptoms?}
    C -- Yes --> D[RED Code / Shock Room]
    C -- No --> E[Assess Pain NRS]
    E --> F{NRS >= 7?}
    F -- Yes --> G[Apply X+1 Upgrade]
    F -- No --> H[Standard Protocol]
    G --> I[Final Confirmation]
    H --> I[Final Confirmation]
    I --> J[Admission to Ward]
```

## 🛠 Features & Normalization

|Feature | Description |
| :--- | :--- |
| **Data Integrity** | Patient names stored in lowercase for database consistency. |
| **UI Rendering** | Professional display using .title() formatting. |
| **Vital Cross‑Check** | Automatic Red Code trigger for SpO₂ < 90% or GCS ≤ 8. |
| **Live Dashboard** | Real‑time monitoring of ward workload by color code. |

---

## 📋 Triage Hierarchy Reference
Official **Tuscany Centro** priority scale:

1. 🔴 **RED** — Resuscitation / Immediate life‑threatening
2. 🟠 **ORANGE** — High risk / Evolutional urgency
3. 🟡 **YELLOW** — Mediated urgency
4. 🟢 **GREEN** — Deferred urgency
5. 🔵 **AZURE** — Minor urgency
6. ⚪ **WHITE** — Non‑urgent

---

## 📄 License

This project is licensed under the **GNU General Public License v3.0**.  
This means the software is, and will always remain, **Free and Open Source**. 

**Why GPL v3?** As a healthcare professional, I believe clinical logic should be a shared asset. This license ensures that any improvements or derivative works made by others must also be shared with the community under the same terms, preventing the "privatization" of this logic by proprietary entities.

See the [LICENSE](LICENSE) file for the full legal text.

---
> ⚠️ Medical Disclaimer
> [!IMPORTANT]
> **This software is for educational and simulation purposes only.** It is NOT a certified Medical Device and should NOT be used to make actual clinical decisions in a real-world healthcare setting. The author is not responsible for any misuse or clinical outcomes resulting from the use of this code.
---

**Maintained by:** [Emanuele Tarchi](https://www.linkedin.com/in/emanuele-tarchi-it/)
---
**Maintained by:** [Emanuele Tarchi](https://www.linkedin.com/in/tuo-profilo-linkedin)  
*Healthcare Professional & Aspiring Software Engineer* "Building tools to support those on the frontline." 🏥💻
