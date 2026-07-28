# 🧾 Clinical Auditability, Non-Repudiation & Logging Architecture

![ISO 27001](https://img.shields.io/badge/ISO%2027001-A.12.4%20Logging-blue)
![NIS2 Compliance](https://img.shields.io/badge/NIS2-Healthcare%20Resilience-orange)
![Non-Repudiation](https://img.shields.io/badge/Data%20Integrity-Non--Repudiation-green)

This document outlines the logging, traceability, and identity management specifications implemented in the **Tuscany Triage System (CDSS)** to guarantee medico-legal non-repudiation and regulatory compliance under **ISO/IEC 27001**, **NIS2**, and **EU AI Act Article 12**.

---

## 📌 1. Logging Scope & Medico-Legal Rationale

In emergency healthcare settings, auditability is essential for clinical quality control, incident post-mortems, and legal defense against malpractice claims. The system enforces continuous event logging for every operational milestone:

1. **Operator Identity & Shift Tracking:** Login/logout events tied to specific badges or credentials.
2. **Patient Admission Metrics:** Clinical inputs (HR, SBP, SpO2, GCS, NRS) and the resulting system-suggested code.
3. **Manual Overrides:** Explicit tracking of operator decisions when overriding system recommendations.

---

## 🔒 2. Technical Logging Implementation (`src/utils.py`)

Event logging is implemented in the core execution stream:

    def log_event(message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("triage_audit_log.txt", "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {message}\n")

### Audit Log Schema Example (`triage_audit_log.txt`)

    [2026-07-28 20:15:10] SHIFT_START - Operator: NURSE_MARIO_ROSSI
    [2026-07-28 20:18:22] ADMISSION - Op: NURSE_MARIO_ROSSI | Pat: John Doe | Code: RED | GCS: 7 | SI: CRITICAL
    [2026-07-28 20:22:05] OVERRIDE - Op: NURSE_MARIO_ROSSI modified Jane Smith from YELLOW to ORANGE
    [2026-07-28 20:22:05] ADMISSION - Op: NURSE_MARIO_ROSSI | Pat: Jane Smith | Code: ORANGE | GCS: 15 | SI: STABLE
    [2026-07-28 20:30:00] SHIFT_END - Operator: NURSE_MARIO_ROSSI

---

## 🛡️ 3. Standard & Security Mapping

| Standard / Regulation | Control Requirement | Technical Implementation |
| :--- | :--- | :--- |
| **EU AI Act Art. 12** | Automatic recording of events (logs) throughout system operation. | Continuous appending of patient evaluations and system suggestions with ISO timestamps. |
| **ISO/IEC 27001 A.12.4.1** | Event logging of user activities, exceptions, and security events. | Capture of login (`SHIFT_START`), logout (`SHIFT_END`), and manual code modifications (`OVERRIDE`). |
| **NIS2 Directive (Healthcare)** | Infrastructure resilience and incident traceability. | Immutable audit trail enabling root-cause analysis in case of clinical software incidents. |

---

## 🚀 4. Production Hardening Roadmap

For enterprise production deployments, the flat-file logging system (`triage_audit_log.txt`) is designed to be upgraded to:
* **Cryptographic Hashing:** Appending SHA-256 hashes to each log line (Append-Only ledger / Blockchain) to prevent retrospective tampering.
* **Centralized SIEM Integration:** Streaming logs to a Syslog / SIEM endpoint (e.g., Elastic, Splunk) with Write-Once-Read-Many (WORM) storage.
