from calculator import Calculator

if __name__ == "__main__":
    filepath = "data/football.dat"
    columns = ["Team", "P", "W", "L", "D", "F", "A", "Pts"]
    calc = Calculator(filepath, columns, skip_lines=1,
                      col1="F", col2="A", key_col="Team")
    team, diff = calc.execute()
    print(f"Team {team} has the smallest goal difference of {diff}")
