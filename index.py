import pyttsx3

droid=pyttsx3.init()
droid.say("bonjour yannick, que puis-je faire pour toi?")
message="je veux que tu telechage une musique"
droid.say("ok, quelle est le nom de la musique?")
droid.runAndWait()