nome = "Luca"
hp_txt = "42"
hp_max_txt = "50"
gold_txt = "17.456"

hp = int(hp_txt)
hp_max = int(hp_max_txt)
hp_ratio = hp / hp_max
gold = float(gold_txt)

print(f"{nome}: {hp}/{hp_max} HP ({hp_ratio:.0%}), {gold:.2f} gold")
