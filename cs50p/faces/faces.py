def main(): 
    typing = input("Typing:") 
    print (convert(typing))

def convert(typing):
    # typing = input("Typing:") 
    result = ""
    i = 0
    while i < len(typing):
        if (typing[i:i+2] == ":)"):
            result += "🙂"
            i = i + 2
        elif (typing[i:i+2] == ":("): 
            result += "🙁" 
            i = i + 2
        else: 
            result += typing [i]
            i = i + 1
    return result     

main ()


        