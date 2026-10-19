DAMAGE = 15
player = {"name": "Luca", "hp": 42, "hp_max": 50, "gold": 17.456, "level": 12}

print(
    f"{player['name']} (lvl {player['level']}): {player['hp']}/{player['hp_max']} HP, {player['gold']:.2f} gold."
)

for _ in range(3):
    hit = min(DAMAGE, player["hp"])
    player["hp"] -= hit
    print(f"Hit for {hit} damage! HP: {player['hp']}.")

player["class"] = "warrior"
print(f"Class selected: {player['class']}.")

print(f"Player mana: {player.get('mana', 0)}.")

for key, value in player.items():
    print(f"{key}: {value}.")
