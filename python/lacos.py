HP_MAX = 50
DAMAGE = 7
POTION_PRICE = 25
POTION_HEAL = 15
POTION_THRESHOLD = 40

hp = HP_MAX
gold = 70
day = 0


while hp > 0:
    hp -= DAMAGE
    day += 1

    if hp <= 0:
        print(f"Morreu no dia {day}.")
    elif hp > POTION_THRESHOLD:
        print(f"Dia {day}: {hp} HP.")
    else:
        if gold >= POTION_PRICE:
            gold -= POTION_PRICE
            hp = min(hp + POTION_HEAL, HP_MAX)
            print(f"Dia {day}: Poção! HP {hp}, ouro {gold}.")
        else:
            print(f"Dia {day}: Sem ouro para poção! HP {hp}.")
