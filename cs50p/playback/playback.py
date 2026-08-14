def playback():
    speech = input ("His speech:")
    # split first
    speech_sep = speech.split()
    print (speech_sep)
    # join again with "..."
    new_speech = '...'.join(speech_sep)
    print (new_speech)
playback()
