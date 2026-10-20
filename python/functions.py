def apply_damage(hp: int, damage: int) -> int:
    return max(hp - damage, 0)


def is_critical(hp: int, max_hp: int, critical_ratio: float) -> bool:
    return (hp / max_hp) < critical_ratio


MAX_HP = 50
DAMAGE = 7
CRITICAL_RATIO = 0.3

hp = 42

for day in range(7):
    hp = apply_damage(hp, DAMAGE)
    day += 1

    if is_critical(hp, MAX_HP, CRITICAL_RATIO):
        prefix = "Critical! "
    else:
        prefix = ""

    print(f"{prefix}Day {day}: Hit for {DAMAGE}, HP {hp}/{MAX_HP}.")
