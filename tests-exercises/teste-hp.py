nome = "Luca"
hp_txt = "42"
hp_max_txt = "50"
gold_txt = "17.456"

hp = int(hp_txt)
hp_max = int(hp_max_txt)
hp_ratio = hp / hp_max
gold = float(gold_txt)

print(f"{nome}: {hp}/{hp_max} HP ({hp_ratio:.0%}), {gold:.2f} gold")

if hp <= 0:
    print("Morto. Perdeu um nível.")
elif hp_ratio < 0.3:
    if gold < 25:
        print("Crítico! Sem ouro para poção.")
    else:
        print("Crítico! Toma uma poção.")
elif hp_ratio <= 0.7:
    print("Ferido.")
else:
    print("Saudável.")
