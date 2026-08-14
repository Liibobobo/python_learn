# python method
def playback():
    speech = input ("His speech:")
    #replace space with \t
    new_speech = speech.replace(" ","\t")
   # new_speech = speech.expandtabs()
    print (new_speech.expandtabs(3))
playback()


