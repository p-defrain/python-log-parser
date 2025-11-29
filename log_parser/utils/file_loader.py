import csv

FAILED_EVENT = '4625'
SUCCESS_EVENT = '4624'
PROCESS_EVENT = '4688'

def load_security_log(path):
  failed_logins = []
  successful_logins = []
  process_creations = []
  failed_events = []

  with open(path, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:
      event_id = row.get('EventID')

      if event_id == FAILED_EVENT:
        failed_logins.append(row.get('AccountName'))
        failed_events.append({
          'user': row.get('AccountName'),
          'ip': row.get('IPAddress'),
          'time': row.get('TimeCreated')
        })

      if event_id == SUCCESS_EVENT:
        successful_logins.append(row.get('AccountName'))

      if event_id == PROCESS_EVENT:
        process_creations.append(row.get('ProcessName'))

  return failed_events, failed_logins, successful_logins, process_creations


                                         
