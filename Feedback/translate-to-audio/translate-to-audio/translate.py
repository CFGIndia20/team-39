from googletrans import Translator
from text_to_speech.text_to_speech import text_to_speech

def translate_to_audio(text, source, destination):
    trans = Translator()
    t = trans.translate(
        text, src = source , dest=destination
    )

    # print(f'Source:{t.src}')
    # print(f'Destination: {t.dest}')
    # print(f'{t.origin} ->{t.text}')

    text_to_speech(t.text,"out.mp3",t.dest)

if __name__ == "__main__":
    text = 'Hello, how are you doing?'
    initial = 'en'
    final = 'hi'
    translate_to_audio(text,initial,final)