import pyttsx3 as audio
import PyPDF2 as pdf


def ia():
    droid=audio.init()
    droid.say("bonjour yannick, je vais lire un fichier pdf, écoute attentivement!")
    fichier=open('COURS SIAD.pdf','rb')
    lecture= pdf.PdfReader(fichier)
    pages = len(lecture.pages)
    print(pages)
    i=0
    while i<pages:
        texte = lecture.pages[i]
        lire = texte.extract_text()
        droid.say(lire)
        i+=1

    #droid.say(lire)
    droid.runAndWait()
ia()