from googletrans import Translator

def translate_docs(text, source, destination):
    fh = open('text.txt',"w")
    trans = Translator()
    t = trans.translate(
        text, src = source , dest=destination
    )
    fh.write(t.text)

    print(f'Source: {t.src}')
    print(f'Destination: {t.dest}')
    print(f'{t.origin} ->{t.text}')

    # text_to_speech(t.text,"out.mp3",t.dest)
    fh.close()

if __name__ == "__main__":
    text = 'Hello, how are you doing?'
    initial = 'en'
    final = 'de'
    translate_docs(text,initial,final)