from pydub import AudioSegment
import os


def silencio (duration=3000, file="audios/silence.mp3"):
    silence = AudioSegment.silent(duration)
    silence.export(file, format="mp3")


# creamos 3 audios de silencios con duracion 1,2,3 segundos
s1 = silencio (2000, file="audios/s1.mp3")
#s2 = silencio (1000, file="audios/s2.mp3")
#s3 = silencio (2000, file="audios/s3.mp3")


# Extraemos audios los archivos de audio
a1 = AudioSegment.from_mp3("audios/0.mp3")
a2 = AudioSegment.from_mp3("audios/1.mp3")
a3 = AudioSegment.from_mp3("audios/2.mp3")
a4 = AudioSegment.from_mp3("audios/3.mp3")
a5 = AudioSegment.from_mp3("audios/4.mp3")
a6 = AudioSegment.from_mp3("audios/5.mp3")
a7 = AudioSegment.from_mp3("audios/6.mp3")
a8 = AudioSegment.from_mp3("audios/7.mp3")
t1 = AudioSegment.from_mp3("audios/s1.mp3")

# Concatenamos los audios
final_audio = a1 + t1 + a2 + t1 + a3 + t1 + a4 + t1 + a5 + t1 + a6 + t1 + a7 + t1 + a8
#final_audio.export("audios/clima2.mp3", format="mp3")
final_audio.export("audios/hobbies1.opus", format="opus", bitrate="16k")


# speak("The cat sat on the table", "audios/0.wav", 2)
# silencio (2000, "audios/1.wav")
# speak("Did the dog sit on the table?", "audios/2.wav", 2)
# silencio (2000, "audios/3.wav")
# speak("No, the cat sat on the table", "audios/4.wav", 2)
# silencio (2000, "audios/5.wav")
# speak("Where did the cat sit?", "audios/6.wav", 2)
# silencio (2000, "audios/7.wav")
# speak("The cat sat on the table", "audios/8.wav", 2)
# silencio (2000, "audios/9.wav")
# speak("Did the cat sit on the chair?", "audios/10.wav", 2)
# silencio (2000, "audios/11.wav")
# speak("No, the cat sat on the table.", "audios/12.wav", 2)
# silencio (2000, "audios/13.wav")
# speak("What did the cat do on the table?", "audios/14.wav", 2)
# silencio (2000, "audios/15.wav")
# speak("The cat sat on the table.", "audios/16.wav", 2)
# silencio (8000, "audios/17.wav")

# speak("Did the dog sit on the table?", "audios/0.wav", 2)
# silencio (2000, "audios/1.wav")

# x = 1

# list = []
# for i in range(x):
#     list.append(AudioSegment.from_wav(f"audios/{i}.wav"))

# final_audio = AudioSegment.empty()
# for i in range(x):
#     final_audio += list[i]

# final_audio.export("a2.mp3", format="mp3")