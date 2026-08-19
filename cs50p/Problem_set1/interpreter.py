def main(): 
    cal = input("Expression: ").split()
    x = int(cal[0])
    z = int(cal[2])
    y = cal[1]

    # start interpret 
    match y: 
        case "+": 
            print (f"{(x + z):.1f}")
        case "-":
            print (f"{(x - z):.1f}")
        case "*": 
            print (f"{(x * z):.1f}")
        case "/":
            print (f"{(x / z):.1f}")
        case _:
            print ("only cal +,-,*,/")

main()