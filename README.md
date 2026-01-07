# Tuscany Triage System - International Edition (v0.3.7)

### 🏥 Context & Vision
Developed by a healthcare professional, this project bridges the gap between frontline clinical experience and Cloud Engineering. It is a decision-support tool designed to streamline the triage process, following the logic of the **Tuscany Region (Italy) Triage Protocols (Delibera 444/2019)** but localized for international environments.

> **Note on Versioning:** Versions 0.3.0 through 0.3.6 were used for internal development, focusing on refining GCS logic, stress-testing input validation, and perfecting the integration between clinical symptoms and vital signs before this public release (v0.3.7).

### 🚀 Key Features
- **Integrated Clinical Logic:** Automatically cross-checks symptoms with vital signs.
- **GCS Calculator:** Full Glasgow Coma Scale assessment with built-in reference legends.
- **Smart Keyword Analysis:** Recognizes critical symptoms (e.g., *Chest Pain*, *Stroke*, *Trauma*) and suggests specialized clinical pathways.
- **Safety-First Validation:** Professional input handling ensures that vital signs (HR, SpO2) and scores remain within realistic clinical ranges.
- **Live Ward Dashboard:** Real-time tracking of patient workload and color-code distribution during the triage session.

### 🛠 Tech Stack
- **Language:** Python 3.10+
- **Platform:** Designed for cross-platform use and optimized for **Raspberry Pi** deployment.
- **Principles:** Modular programming, Clean Code, and DRY (Don't Repeat Yourself) architecture.

### 📊 Triage Logic Applied
The system prioritizes patient safety by assigning a code based on the "Worst Case Scenario":
1. **RED (Emergency):** Critical vitals (SpO2 < 90%, GCS ≤ 8, extreme HR) or immediate life-threat symptoms.
2. **ORANGE (Urgent):** Compromised vitals or high-risk clinical pathways (Cardiac, Stroke, Major Trauma).
3. **GREEN/AZURE (Stable):** Normal vital signs and non-urgent symptoms.

### 📈 Future Roadmap
- [ ] Persistent Data Storage (CSV/JSON/SQL).
- [ ] Pain Scale (NRS) Integration.
- [ ] Time-to-Treatment tracking for each priority code.
- [ ] Integration with hardware sensors (Pulse Oximeter via GPIO).

---
*Created by a Cloud Engineering Student & Healthcare Professional.*
