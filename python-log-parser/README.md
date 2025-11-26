Python Security Log Analyzer

A Python-based tool for analyzing Windows Security Event Logs to detect suspicious activity, brute-force attacks, and process execution behavior.

This project is designed to simulate real SOC (Security Operations Center) workflows using synthetic log data, making it ideal for cybersecurity students and professionals building a portfolio.

🚀 Features
🔍 Log Event Parsing

Parses Windows-style CSV logs and extracts:

Failed logins (Event ID 4625)

Successful logins (Event ID 4624)

Process creation events (Event ID 4688)

📊 Summary Statistics

Displays:

Total failed login attempts

Total successful login attempts

Total processes executed

Top failed login accounts

Top executed processes

🔐 Brute-Force Detection (User-Level)

Flags accounts with repeated failed login attempts:
Possible brute-force attack detected: User 'jdoe' had 8 failed login attempts.

🌐 Brute-Force Detection (IP-Level)

Identifies brute-force attempts originating from a specific IP:
Possible brute-force source detected: IP 192.168.1.22 had 8 failed login attempts.

⏱ Time-Window Brute-Force Detection (Advanced)

Detects whether multiple failed logins occurred within a short period (default: 60 seconds):
IP '192.168.1.22' made 8 failed attempts within 60 seconds.
User 'jdoe' made 8 failed attempts within 60 seconds.

This mimics real SIEM correlation rules used in tools like Splunk, Sentinel, and Elastic.

📁 Project Structure
python-log-parser/
│
├── parser.py                  # Main Python script
│
├── logs/
│   └── sample_security_logs.csv   # Synthetic log file used for testing
│
└── README.md                  # Project documentation

📦 Installation
1. Clone the Repository
git clone https://github.com/<your-username>/python-log-parser.git
cd python-log-parser

2. Ensure Python 3 Is Installed

Check your version:
python --version

3. Install Dependencies

This project uses only Python standard libraries, so no external installations are required.

▶️ Usage

Run the log analyzer:
python parser.py

You will see output like:
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

The project includes a synthetic dataset (sample_security_logs.csv) representing realistic Windows Event Log entries for:

Failed logins

Successful logins

Process executions

This ensures consistent and reproducible testing.

💡 Why This Project Matters

This tool demonstrates:

Python automation

Log analysis

Security event correlation

Threat detection logic

Understanding of Windows Security Events

Ability to build SOC-style detection tools

These are high-value skills for roles such as:

SOC Analyst (Tier 1 / Tier 2)

Cybersecurity Analyst

Incident Response Analyst

Threat Hunter

📸 Screenshots

Add screenshots of your terminal output here.

Example:
/screenshots/output.png

🛠 Future Enhancements

Planned improvements include:

JSON output

Suspicious process detection

Exporting alerts to a CSV/JSON

Command-line argument support

Dashboard visualization

🤝 Contributing

Pull requests, ideas, and enhancements are welcome!

📄 License

This project is licensed under the MIT License.