from collections import Counter
from datetime import datetime
from utils.parser_helpers import parse_timestamp, group_events_by_key, sort_times
import csv

FAILED_EVENT = '4625'

# ==========================
#   SUMMARY REPORTING
# ==========================

def summarize_events(failed_logins, successful_logins, process_creations):
  print("==== LOG SUMMARY ====")
  print(f"Total Failed Logins: {len(failed_logins)}")
  print(f"Total Successful Logins: {len(successful_logins)}")
  print(f"Total Process Creations: {len(process_creations)}")

  print("\nTop Failed Login Accounts:")
  for account, count in Counter(failed_logins).most_common(5):
    print(f"{account}: {count}")

  print("\nTop Executed Processes:")
  for proc, count in Counter(process_creations).most_common(5):
    print(f"{proc}: {count}")

# ==========================
#   BRUTE FORCE DETECTION
# ==========================

def detect_bruteforce_by_account(failed_logins, threshold):
  print("\n==== BRUTE FORCE ATTEMPT DETECTION ====")

  failed_counts = Counter(failed_logins)

  for account, count in failed_counts.items():
    if count >= threshold:
      print(f"Possible brute-force attack dettected: User '{account}' had {count} failed attempts.")

def detect_bruteforce_by_ip(path, threshold):
  print("\n==== BRUTE FORCE BY IP ADDRESS ====")

  ip_counts = Counter()

  with open(path, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:
      if row.get("EventID") == FAILED_EVENT:
        ip = row.get("IPAddress")
        if ip:
          ip_counts[ip] +=

  for ip, count in ip_counts.items():
    if count >= threshold:
      print(f"Suspicious IP detected: {ip} had {count} failed login attempts.")

# ==========================
#   TIME WINDOW DETECTION
# ==========================

def detect_time_window_attacks(failed_events, windown_seconds):
  print("\n==== TIME-WINDOW BRUTE FORCE DETECTION ====")

  # Parse Timestamps
  for event in failed_events:
    event['time'] = parse_timestamp(event['time'])

  # Group events
  events_by_ip = sort_times(group_events_by_key(failed_events, 'ip'))
  events_by_user = sort_times(group_events_by_key(failed_events, 'user'))

  # Apply sliding-window logic
  def check(group, label):
    for key, times in group.items():
      for i in range(len(times)):
        count = 1
        for j in range(i + 1, len(times)):
          if (times[j] - times[i].total_seconds() <= window_seconds:
            count += 1
          else:
            break

        if count >= 5:
          print(f"{label} '{key}' made {count} failed attempts within {window_seconds} seconds.")
          break

  check(events_by_ip, "IP")
  check(events_by_user, "User")
