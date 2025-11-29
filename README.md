🛡️ python-log-parser
Windows Security Log Parser & Brute-Force Attack Detector
A Python-based CLI tool that analyzes Windows Security event logs (CSV export from Event Viewer) to detect brute-force attacks, suspicious login activity, and abnormal authentication patterns.
This project is designed to simulate real SOC analyst workflows: parsing security logs, grouping authentication failures, analyzing timestamps, scanning for repeated failures, and generating actionable alerts.
----
🚀 Features
 - Brute-force detection by user account
    - Identifies accounts with repeated failed logins
  - Brute-force detection by IP address
    - Flags source addresses generating excessive failures
  - Sliding time-window analysis
    - Detects bursts of activity (e.g., 5 failed logins within 60 seconds)
  - Process creation monitoring
    - Summaries of Event ID 4688 executions
  - Configurable thresholds and time windows
    - --threshold and --window CLI options
  - Structured, modular codebase
    - Detectors, helpers, examples, and CLI entrypoint
  - Clear summary reporting
    - Top failed accounts, top executed processes, total counts
----
📁 Project Structure
python-log-parser/
│
├── log_parser/
│   ├── main.py
│   ├── detectors/
│   │   └── brute_force_detector.py
│   ├── utils/
│   │   ├── parser_helpers.py
│   │   └── file_loader.py
│   └── examples/
│       └── sample_security_logs.csv
│
└── README.md
----
🧠 MITRE ATT&CK Mapping
| Detection Type                      | MITRE Technique                   | Description                                          |
| ----------------------------------- | --------------------------------- | ---------------------------------------------------- |
| Repeated failed logins (by user/IP) | **T1110 – Brute Force**           | Adversary attempts multiple passwords to gain access |
| Successful login after failures     | **T1078 – Valid Accounts**        | Compromised account used after brute-force attempts  |
| Rapid-fire failures in time window  | **T1110.001 – Password Guessing** | High-frequency authentication failures               |
Adding ATT&CK mapping helps align this tool with real SOC analysis and industry frameworks.
----
🛠️ Usage
Basic command
python log_parser/main.py --input logs/security.csv
With thresholds and time window
python log_parser/main.py \
    --input logs/security.csv \
    --threshold 5 \
    --window 60
----
CLI Arguments
| Flag          | Description                                      | Default  |
| ------------- | ------------------------------------------------ | -------- |
| `--input`     | Path to Windows Security log in CSV format       | required |
| `--threshold` | Minimum number of failures before alerting       | 3        |
| `--window`    | Sliding time window for rapid attempts (seconds) | 60       |
----
📌 Example Output
==== LOG SUMMARY ====
Total Failed Logins: 42
Total Successful Logins: 5
Total Process Creations: 120

Top Failed Login Accounts:
administrator: 15
user1: 9
sqladmin: 7

Top Executed Processes:
cmd.exe: 30
powershell.exe: 22
regsvr32.exe: 5

==== BRUTE FORCE ATTEMPT DETECTION ====
Possible brute-force attack detected: User 'administrator' had 15 failed attempts.

==== BRUTE FORCE BY IP ADDRESS ====
Suspicious IP detected: 203.0.113.55 had 18 failed login attempts.

==== TIME-WINDOW BRUTE FORCE DETECTION ====
IP '203.0.113.55' made 5 failed attempts within 60 seconds.
User 'administrator' made 6 failed attempts within 60 seconds.
----
🧩 How It Works (Detection Logic)
1. Parse Windows Security CSV logs
  - Event IDs used:
    - 4625 = Failed logon
    - 4624 = Successful logon
    - 4688 = Process creation
2. Group events by:
  - Username
  - Source IP
  - Timestamp
3. Check detection rules:
  - A user/IP with ≥ threshold failed logins
  - An IP generating abnormal volume of failures
  - 5+ failures within a 60-second sliding window
4. Output findings to the console
  - Clear, SOC-style alerts
----
📈 Roadmap (Future Enhancements)
  - JSON/CSV export for SIEM ingestion
  - Real-time streaming mode (tail -f style)
  - Additional detectors (RDP logs, account lockouts, service creation)
  - Visualization notebook (failed logins over time)
  - Integration with packet analyzer project (Project B)
----
✨ Author
Paul DeFrain
Cybersecurity Graduate Student • Security Automation & Detection Engineering Enthusiast
