import csv
from collections import Counter
from datetime import datetime

# Event IDs to analyze
FAILED_EVENT = '4625'
SUCCESS_EVENT = '4624'
PROCESS_EVENT = '4688'

failed_logins = []
successful_logins = []
process_creations = []
failed_events = []

# Read the Security CSV log
with open('logs/sample_security_logs.csv', 'r', encoding='utf-8') as file:
  reader = csv.DictReader(file)

  for row in reader:
    event_id = row.get('EventID')

    # Failed login attempts
    if event_id == FAILED_EVENT:
      failed_logins.append(row.get('AccountName'))
      failed_events.append({
        'user': row.get('AccountName'),
        'ip': row.get('IPAddress'),
        'time': row.get('TimeCreated')
      })

    # Successful logins
    if event_id == SUCCESS_EVENT:
      successful_logins.append(row.get('AccountName'))

    # Process creation events
    if event_id == PROCESS_EVENT:
      process_creations.append(row.get('ProcessName'))

print('==== LOG SUMMARY ====')
print(f'Total Failed Logins: {len(failed_logins)}')
print(f'Total Successful Logins: {len(successful_logins)}')
print(f'Total Process Creations: {len(process_creations)}')

print('\nTop Failed Login Accounts:')
for account, count in Counter(failed_logins).most_common(5):
  print(f'{account}: {count}')

print('\nTop Executed Processes:')
for proc, count in Counter(process_creations).most_common(5):
  print(f'{proc}: {count}')

# ==== BRUTE FORCE DETECTION ====
print('\n ==== BRUTE FORCE ATTEMPT DETECTION ====')
bruteforce_threshold = 3 # Number of failed attempts considered suspicious

failed_counts = Counter(failed_logins)

# Final accounts with repeated failed login attempts
for account, count in failed_counts.items():
  if count >= bruteforce_threshold:
    print(f"Possible brute-force attack detected: User '{account}' had {count} failed login attempts.")
    
# ==== BRUTE FORCE DETECTION BY IP ADDRESS ====
print('\n ==== BRUTE FORCE BY IP ADDRESS ====')
ip_failures = Counter()

# Building counts for each IP associated with failed logins
with open('logs/sample_security_logs.csv', 'r', encoding='utf-8') as file:
  reader = csv.DictReader(file)

  for now in reader:
    if now.get('EventID') == FAILED_EVENT:
      ip = now.get('IPAddress')
      if ip:
        ip_failures[ip] += 1

# Print suspicious IPs
for ip, count in ip_failures.items():
  if count >= bruteforce_threshold:
    print(f'Possible brute-force source detected: IP {ip} had {count} failed login attempts.')

# ==== TIME-WINDOW BRUTE FORCE DETECTION ====
print('\n ==== TIME-WINDOW BRUTE FORCE DETECTION ====')

window_seconds = 60

# Convert timestamps to datetime objects
for event in failed_events:
  try:
    event['time'] = datetime.fromisoformat(event['time'])
  except:
      pass

# Group by IP and User
from collections import defaultdict
events_by_ip = defaultdict(list)
events_by_user = defaultdict(list)

for e in failed_events:
  if e['ip']:
    events_by_ip[e['ip']].append(e['time'])
  if e['user']:
    events_by_user[e['user']].append(e['time'])

def check_time_window(events, label_type):
  for label, times in events.items():
    times.sort()
    for i in range(len(times)):
      count = 1
      for j in range(i + 1, len(times)):
        if (times[j] - times[i]).total_seconds() <= window_seconds:
          count += 1
        else:
          break
      if count >= 5:
        print(f"{label_type} '{label}' made {count} failed attempts within {window_seconds} seconds.")
        break

# Check IPs
check_time_window(events_by_ip, 'IP')

# Check Users
check_time_window(events_by_user, 'User')