def indoor_voice():
    voice = input("Your sentence:")
    #use function case fold: transfer string to lower case
    voice = voice.casefold()
    print("Your indoor voice:",voice)
indoor_voice()
