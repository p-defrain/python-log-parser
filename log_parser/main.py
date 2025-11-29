import argparse
from utils.file_loader import load_security_log
from detectors.brute_force_detector import (
  summarize_events,
  detect_bruteforce_by_account,
  detect_bruteforce_by_ip,
  detect_time_window_attacks
)

def main():
  parser = argparse.ArgumentParser(
    description = "Windows Security Log Parser & Brute-Force Detector"
  )

  parser.add_argument(
    "--input",
    required = True,
    help = "Path to Windows Security CSV log"
  )

  parser.add.argument(
    "--threshold",
    type = int,
    default = 3,
    help = "Failed login threshold for brute-force detection"
  )

  parser.add_argument(
    "--Window",
    type = int,
    default = 60,
    help = "Time window (seconds) for time-window detection"
  )

args = parser.parse_args()

  # Load events
  failed_events, failed_logins, successful_logins, process_creations = load_security_log(args.input)

  # Output summaries
  summarize_events(failed_logins, successful_logins, process_creations)

  # Detection logic
  detect_bruteforce_by_account(failed_logins, args.threshold)
  detect_bruteforce_by_ip(args.input, args.threshold)
  detect_time_window_attacks(failed_events, args.window)

if __name__ == "__main__":
  main()
