DAMAGES = [7, 3, 12, 0, 9, 15, 4]
DAMAGE_THRESHOLD = 10

bad_days = []

for day, damage in enumerate(DAMAGES, start=1):
    print(f"Day {day}: {damage} damage.")

    if damage > DAMAGE_THRESHOLD:
        bad_days.append(day)

print(f"Days without taking damage: {DAMAGES.count(0)}.")
print(f"Most damage taken in a single day: {max(DAMAGES)}.")
print(f"Total damage of the week: {sum(DAMAGES)}.")
print(f"Bad days: {', '.join(str(day) for day in bad_days)}.")
