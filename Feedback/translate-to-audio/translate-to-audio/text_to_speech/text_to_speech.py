from gtts import gTTS
import os
def text_to_speech(filename, fout, lngg):
    # fh = open(filename,"r")
    mytext = filename #fh.read().replace("\n", " ")
    
    language = lngg

    output = gTTS(text = mytext, lang=language, slow=False)

    output.save(fout)
    # fh.close()

if __name__ == "__main__":
    textfile = "text.txt"
    fout = "output.mp3"
    lang = 'en'
    text_to_speech(textfile, fout, lang)
#to play the file from os perspective
#os.system("start output.mp3")