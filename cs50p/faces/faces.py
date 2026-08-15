def convert():
    typing = input("Typing:") 
    result = ""
    for i in range(len(typing)):
        if (typing[i:i+2] == ":)"):
            result += "🙂"
            i = i + 1
            # result += typing [i]
            print (result)
        elif (typing[i:i+2] == ":("): 
            result += "🙁" 
            # i = i + 1
            # result += typing [i]
        else: 
            result += typing [i]
            print (result)
        print (result)
        
convert() 
        