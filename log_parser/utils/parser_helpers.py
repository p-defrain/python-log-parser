from datetime import datetime

def parse_timestamp(ts):
  try:
    return datetime.fromisoformat(ts)
  except Exception:
    return None

def group_events_by_key(events, key):
  grouped = {}
  for event in events:
    val = event.get(key)
    if val:
      grouped.setdefault(val, []).append(event['time'])
  return grouped

def sort_times(grouped):
  for key in grouped:
    grouped[key] = sorted(grouped[key])
  return grouped
