def main(): 
    camel_word = input("camelCase: ")
    snake_case = ""
    for char in camel_word: 
        if 65 <= ord(char) <= 90:
            char = chr(ord(char) + 32)
            snake_case += f"_{char}"
        else: 
            snake_case += char
    print (snake_case)

main()