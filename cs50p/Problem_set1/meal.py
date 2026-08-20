def main():
    time = input("What's time is it? ").split(":")
    # breakfast 7:00 - 8:00
    print(convert(time))

def convert(time):
    hour = int(time[0]) + int(time[1])/60 
    return hour

if __name__ == "__main__":
    main()