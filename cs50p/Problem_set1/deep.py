def main(): 
    # separate input to resolve corner case of 42 (space around 42)"
    question_sep = input("Great Question of Life, the Universe and Everything?").split()
    print (question_sep)
    question = " ".join(question_sep)
    print (question)

    # resolve case-insensitively for 2 left input, lower all the input 
    question_lower = question.lower()
    if (question_lower == "42" or question_lower == "forty-two" or question_lower == "forty two"):
        print("Yes")
    else: 
        print("No")

main()
