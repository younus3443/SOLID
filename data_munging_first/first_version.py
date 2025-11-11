
min_spread = float('inf')
min_day = None

with open("data/weather.dat") as f:
    lines = f.readlines()[2:-1]  # skip headers and footers
    for line in lines:
        parts = line.split()
        if len(parts) < 3:
            continue
        day = parts[0]
        try:
            max_t = int(parts[1])
            min_t = int(parts[2])
        except ValueError:
            continue

        spread = abs(max_t - min_t)
        if spread < min_spread:
            min_spread = spread
            min_day = day

print(f"Day {min_day} has the smallest temperature spread of  {min_spread}°F")


min_diff = float('inf')
min_team = None

with open("data/football.dat") as file:
    lines = file.readlines()[1:]
    for line in lines:
        line = line.strip()
        if not line or line.startswith('-'):
            continue

        line = line.replace(" - ", " ")

        parts = line.split()
        if len(parts) < 8:
            continue

        team = parts[0]
        try:
            f_goals = int(parts[5])
            a_goals = int(parts[6])
        except ValueError:
            continue

        diff = abs(f_goals - a_goals)
        if diff < min_diff:
            min_diff = diff
            min_team = team

print(f"Team {min_team} has the smallest goal difference of {min_diff}")
