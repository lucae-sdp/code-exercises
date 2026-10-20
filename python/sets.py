monday = ["gym", "read", "code", "read", "meditate"]
tuesday = ["code", "walk", "read", "code"]

set_monday = set(monday)
set_tuesday = set(tuesday)

print(f"Number of tasks on monday: {len(set_monday)}.")
print(f"Same tasks made on both days: {', '.join(set_monday & set_tuesday)}.")
print(f"Tasks made only on monday: {', '.join(set_monday - set_tuesday)}.")
print(f"Different tasks made in the week: {', '.join(set_monday | set_tuesday)}.")
