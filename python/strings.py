LOG = [
    "[2026-10-20T18:01:21-0300] [ALPM] upgraded python (3.14.5-1 -> 3.14.6-1)",
    "[2026-10-20T18:01:22-0300] [ALPM] installed ruff (0.14.2-1)",
    "[2026-10-20T18:01:22-0300] [PACMAN] synchronizing package lists",
    "[2026-10-20T18:05:40-0300] [ALPM] removed nano (8.6-1)",
    "[2026-10-20T18:05:41-0300] [ALPM] upgraded neovim (0.12.3-1 -> 0.12.4-1)",
]


def get_action(line: str) -> str:
    return line.split()[2]


def get_package(line: str) -> str:
    return line.split()[3]


def is_alpm(line: str) -> bool:
    return line.split()[1] == "[ALPM]"


for line in LOG:
    if is_alpm(line):
        print(f"{get_action(line)}: {get_package(line)}.")

upgraded = [
    get_package(line)
    for line in LOG
    if is_alpm(line) and get_action(line) == "upgraded"
]

pairs = {get_package(line): get_action(line) for line in LOG if is_alpm(line)}

print("--------------------")
print(f"Pares: {pairs}")
print(f"Packages upgraded: {', '.join(upgraded)}.")
