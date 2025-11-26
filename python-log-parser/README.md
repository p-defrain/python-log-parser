# Python Security Log Analyzer
A Python-based tool for analyzing Windows Security Event Logs to detect suspicious login behavior, brute-force attacks, and process execution activity.  
Designed as a portfolio-friendly cybersecurity project that demonstrates real SOC analysis skills.

---

## 🔍 Overview

This project parses Windows-style CSV security logs and automatically identifies:

- Failed and successful login attempts  
- Suspicious authentication patterns  
- Repeated login failures by user  
- Brute-force attempts by IP address  
- High-frequency failures within a time window  
- Commonly executed processes on the system  

The tool simulates real SIEM-style detections similar to Splunk, Elastic, Sentinel, and QRadar.

---

## ⚙️ Features

### ✔ Event Log Parsing
Extracts:
- **4625** – Failed logon  
- **4624** – Successful logon  
- **4688** – Process creation  

### ✔ Summary Statistics
Displays:
- Total failed logins  
- Total successful login

### ✔ Brute-Force Detection (IP-Level)
Identifies brute-force sources:

### ✔ Time-Window Detection (Advanced)
Identifies rapid login failures within 60 seconds:

---

## 📁 Project Structure
python-log-parser/
│
├── parser.py
├── README.md
├── LICENSE (optional)
│
├── logs/
│ └── sample_security_logs.csv
│
└── screenshots/
└── output.png

---

## ▶️ Running the Tool

### 1. Clone the repository
```bash
git clone https://github.com/p-defrain/python-log-parser.git
cd python-log-parser

2. Run the parser
python parser.py

3. View the analysis output

Example:
==== LOG SUMMARY ====
Total Failed Logins: 13
Total Successful Logins: 2
Total Process Creations: 4

==== BRUTE FORCE ATTEMPT DETECTION ====
Possible brute-force attack detected: User 'jdoe' had 8 failed login attempts.

==== BRUTE FORCE BY IP ADDRESS ====
Possible brute-force source detected: IP 192.168.1.22 had 8 failed login attempts.

==== TIME-WINDOW BRUTE FORCE DETECTION ====
IP '192.168.1.22' made 8 failed attempts within 60 seconds.

🧪 Sample Log Data

The logs/sample_security_logs.csv file includes synthetic Windows Event Log entries used for testing.
This ensures consistent, repeatable results for anyone cloning the project.

📸 Screenshots

Add a screenshot of your terminal output here:
/screenshots/output.png
(Recommended: include one clear terminal screenshot for recruiters.)
```

🛠 Skills Demonstrated
This project highlights key cybersecurity competencies:
  - Log analysis & parsing
  - Threat detection logic
  - Windows Event ID interpretation
  - Python automation
  - Brute-force attack detection
  - Time-window correlation (SIEM-style detection)
  - Working with structured datasets (CSV logs)
  - Creating clean GitHub portfolio projects

🚀 Future Enhancements
Planned improvements:
  - Add JSON output option
  - Add command-line arguments for thresholds
  - Add suspicious process detection
  - Export alerts to CSV
  - Visual dashboard (Grafana or Python plots)

🤝 Contributing
Contributions and ideas are welcome!
Feel free to submit a pull request.

📄 License

This project is licensed under the MIT License.
