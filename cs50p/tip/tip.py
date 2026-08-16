def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    bill = float(d.removeprefix("$"))
    return bill

def percent_to_float(p):
    # convert input and remove %
    tip_expect = float(p.removesuffix("%"))
    # convert to final number
    result = tip_expect / 100
    return result

main()