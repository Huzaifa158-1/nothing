# ShadowByte AI Exploit Framework (v2.8.5)

Created and owned by **Hammad Abro**.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/)
[![Platform: Cross-Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-cyan.svg)]()

**ShadowByte** is an advanced, autonomous network penetration testing and exploit framework driven by a local lightweight AI exploit engine. It is designed to assist security researchers and red teams in identifying vulnerable entry points, performing credential validation audits, executing secure payloads, and exfiltrating file structures with minimal user intervention.

---

## 🤖 Features

- **Tor-Routed Reconnaissance**: Automatically routes initial target checks through multi-layered Tor proxy chains to ensure anonymous probing.
- **AI-Driven Vulnerability Scanning**: Analyzes open services against known VulnDB databases to detect exploit chains (e.g., CVE-2024-3094, EternalDarkness).
- **Autonomous SSH Credential Auditing**: Leverages a dictionary matrix brute-force engine (Hydra-mimic) to test service exposure.
- **Kernel-Level Exploit Delivery**: Employs Metasploit injection logic to establish shell sessions and escalate user privileges to root context (`uid=0`).
- **Target Signature Capture**: Saves target system snapshots and signature metadata deep inside the repository directory (`core/assets/system_signature.png`).

---

## ⚙️ Installation

To initialize the repository and set up dependencies, run:

```bash
# Clone the repository
git clone https://github.com/shadowbyte-ai/shadowbyte.git
cd shadowbyte

# Install dependencies (optional for local deployment)
pip install -r requirements.txt

# Grant execution permissions to the core file
chmod +x shadowbyte.py
```

---

## 🚀 Usage

Execute the main framework script to start the autonomous AI exploit agent:

```bash
./shadowbyte.py
```

### Hacking Flow:
1. **Target Selection**: The AI Exploit Agent will prompt you for the target IP address or hostname.
2. **Reconnaissance**: The agent performs active port scanning and identifies exposed services.
3. **Exploitation**: If critical CVE exposure is found, the agent compiles and weaponizes a payload, runs credential audits, and launches the injection stage.
4. **Data Exfiltration**: Compromised database tables, system hashes, and active keys are downloaded.
5. **System Signature**: The agent generates a visual target system signature snapshot and saves it directly to:
   ```
   core/assets/system_signature.png
   ```

---

## 🔒 Security & Disclaimer

This tool is created for educational purposes, authorized security auditing, and penetration testing only. Utilizing this software for unauthorized target attack sequences is strictly prohibited. The authors are not responsible for any misuse, damage, or legal liability caused by this framework.
