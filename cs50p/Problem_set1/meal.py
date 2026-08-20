def main():
    time = input("What's time is it? ")
    # breakfast 7:00 - 8:00
    if 7 <= convert(time) <= 8 :
        print ("breakfast time")
    elif 12 <= convert(time) <= 13:
        print ("lunch time")
    elif 18 <= convert (time) <= 19:
        print ("dinner time")

def convert(time):

    hour, minute = time.split(":")
    time_convert = int(hour) + int(minute)/60 
    return time_convert 

if __name__ == "__main__":
    main()
