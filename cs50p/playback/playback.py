# python method
# def playback():
#     speech = input ("His speech:")
#     #replace space with \t
#     new_speech = speech.replace(" ","\t")
#    # new_speech = speech.expandtabs()
#     print (new_speech.expandtabs(3))
# playback()

# again
def playback():
    speech = input ("His speech:")
    # split first
    speech_sep = speech.split()
    print (speech_sep)
    for i in speech_sep:
        print (i)
playback()
