def main(): 
    greeting = input("Greeting: ")
    if result(greeting)[0:5] == "hello":
        print("$0")
    elif result(greeting)[0] == "h":
        print("$20")
    else: 
        print("$100")

#function convert input to low case and no pre_space
def result(say):
    new_say = say.lower().split()
    result =  " ".join(new_say)
    return result 

main()