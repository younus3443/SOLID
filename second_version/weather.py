from calculator import Calculator

if __name__ == "__main__":
    filepath = "data/weather.dat"
    columns = ["Day", "MxT", "MnT", "AvT", "HDDay"]
    calc = Calculator(filepath, columns, skip_lines=1,
                      col1="MxT", col2="MnT", key_col="Day")
    day, diff = calc.execute()
    print(f"Day {day} has the smallest temperature spread of {diff}°C")
