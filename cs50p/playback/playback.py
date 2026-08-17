# def playback():
#     speech = input ("His speech:")
#     # split first
#     speech_sep = speech.split()
#     print (speech_sep)
#     # join again with "..."
#     new_speech = '...'.join(speech_sep)
#     print (new_speech)
# playback()

# method 2: assign lan luot for new sentence, use concatenate
def playback_2():
    speech = input ("His speech:")
    new_speech = ""
    for i in range(len(speech)):
        if (speech[i] != " "):
            new_speech += speech[i]
        else:
            new_speech += "..."
    print (new_speech)


playback_2()

    # j = 0
    # for i in range(len(speech)):
    #     if (speech[i] != " "):
    #         new_speech[j] = speech[i]
    #         j += 1
    #     else:
    #         new_speech[j:j+2] = "."
    #         j += 3
    # print (new_speech)
