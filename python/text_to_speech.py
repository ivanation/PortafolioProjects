"""
Basic example of edge_tts usage.
"""

import asyncio

import edge_tts

from pydub import AudioSegment

VOICES = ["en-US-AnaNeural", "en-US-AriaNeural", "en-US-ChristopherNeural", "en-US-EricNeural", "en-US-GuyNeural", "en-US-JennyNeural", "en-US-MichelleNeural"]


# TEXT = "The girls are reading"
# VOICE = VOICES[2] # de 0 a 6
# OUTPUT_FILE = "audios/tobe1.mp3" # donde se guarda el audio
# SPEECH_RATE = "-30%" # Velocidad de la voz / "-30%" disminuye / "+50%" aumenta / "+0%" defecto)

# async def _main() -> None:
#     communicate = edge_tts.Communicate(TEXT, VOICE, rate=SPEECH_RATE)
#     await communicate.save(OUTPUT_FILE)


# if __name__ == "__main__":
#     asyncio.get_event_loop().run_until_complete(_main())


################ iteractuando con array

frases = ["What do you like to do?","I like to play video games", "What do you do for fun?","I like to swim","What music do you like?","I like pop music","Do you play video games?","No, I don't. I play board games"]

name = "au_"

for i,value in enumerate(frases):
    TEXT = value
    VOICE = VOICES[4] # de 0 a 6 
    OUTPUT_FILE = "audios/"+name+str(i)+".mp3" # donde se guarda el audio
    #OUTPUT_FILE = "audios/"+value+".mp3" # donde se guarda el audio
    SPEECH_RATE = "-30%" # Velocidad de la voz / "-30%" disminuye / "+50%" aumenta / "+0%" defecto)

    async def _main() -> None:
        communicate = edge_tts.Communicate(TEXT, VOICE, rate=SPEECH_RATE)
        await communicate.save(OUTPUT_FILE)
        test = AudioSegment.from_mp3(OUTPUT_FILE)
        test.export("audios/convertidos/"+name+str(i)+".opus", format="opus", bitrate="16k")


    if __name__ == "__main__":
        asyncio.get_event_loop().run_until_complete(_main())