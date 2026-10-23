LOG_PATH = "/var/log/pacman.log"
DATE_POSITION = 0
TAG_POSITION = 1
ACTION_POSITION = 2
ACTIONS = ["installed", "upgraded", "removed"]
TOP_DAYS = 5
LAST_WARNINGS = 5


def total_lines(tag: str) -> int:
    total_lines = [line for line in LOG if get_tag(line) == tag]
    return len(total_lines)


def get_date(line: str) -> str:
    date = line.split()[DATE_POSITION]
    return date[1:11]


def total_action(action: str) -> int:
    total_actions = [
        line for line in LOG if is_alpm(line) and get_action(line) == action
    ]
    return len(total_actions)


def get_tag(line: str) -> str:
    return line.split()[TAG_POSITION]


def is_alpm(line: str) -> bool:
    return line.split()[TAG_POSITION] == "[ALPM]"


def get_action(line: str) -> str:
    return line.split()[ACTION_POSITION]


def count_dates(log):
    dates = [get_date(line) for line in log]
    count = {}
    for date in dates:
        count[date] = count.get(date, 0) + 1
    return count


def has_warning(line: str) -> bool:
    return "warning:" in line or "error:" in line


with open(LOG_PATH) as f:
    LOG = f.read().splitlines()

tags = sorted({get_tag(line) for line in LOG})
valid_log = [line for line in LOG if len(line.split()) > ACTION_POSITION]
date_count = count_dates(valid_log)
top_dates = sorted(date_count, key=lambda date: date_count[date], reverse=True)[
    :TOP_DAYS
]
list_warning = sorted([line for line in valid_log if has_warning(line)])

print("----------------")

print(f"Total lines on log: {len(LOG)}.")
print(f"Total valid lines on log: {len(valid_log)}.")
print(f"Diff: {len(LOG) - len(valid_log)}.")

print("----------------")

print(f"Tags: {', '.join(tags)}.")
for tag in tags:
    print(f"Total lines in tag {tag}: {total_lines(tag)}.")

print("----------------")

print(f"{TOP_DAYS} days with more entries:")
for day, date in enumerate(top_dates, start=1):
    print(f"Day {day}: {date} with {date_count[date]} entries.")

print("----------------")

for action in ACTIONS:
    print(f"Packages {action}: {total_action(action)}.")

print("----------------")

print(f"Total lines with warnings: {len(list_warning)}.")
print(f"Last {LAST_WARNINGS} warning lines:")
for i, line in enumerate(list_warning[-LAST_WARNINGS:], start=1):
    print(f"Warning {i}: {line}.")

print("----------------")
