def convert():
    typing = input("Typing:") 
    result = ""
    i = 0
    while i < len(typing):
        if (typing[i:i+2] == ":)"):
            result += "🙂"
            i = i + 2
            # result += typing [i]
            print (result)
        elif (typing[i:i+2] == ":("): 
            result += "🙁" 
            i = i + 2
            # result += typing [i]
        else: 
            result += typing [i]
            i = i + 1
            print (result)
        print (result)
        
convert() 


        