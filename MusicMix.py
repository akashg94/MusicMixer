from pygame import mixer

mixer.__init__() #start the mixer

mixer.music.load("amiparboi.mp3") #load the song
mixer.music.set_volume (0.7) # set the volume
mixer.music.play() #play the music

while True:
    print("press 'p' to pause 'r' to resume ")
    print("press 'e' to exit the program ")
    query = input(">>> ")

    if query == 'p':
        mixer.music.pause()
    elif query == 'r':
        mixer.music.unpause()
    elif query == 'e':
        mixer.music.stop()
        break

