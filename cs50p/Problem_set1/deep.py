def main(): 
    question = input("Great Question of Life, the Universe and Everything?")
    question_lower = question.lower()
    if (question_lower == "42" or question_lower == "forty-two" or question_lower == "forty two"):
        print("Yes")
    else: 
        print("No")

main()
