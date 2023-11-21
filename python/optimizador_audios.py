from pydub import AudioSegment

x = 2

if x == 1:
    # convert all files mp3 to opus compressed file
    for i in range(0,8):
        name = "au_"
        test = AudioSegment.from_mp3("audios/"+name+str(i)+".mp3")
        test.export("audios/convertidos/"+name+str(i)+".opus", format="opus", bitrate="16k")


if x == 2:
    lista = ["Play board game","bike","hike","run","exercise","watch TV","read","go to the movies","listen to music","Play video games"]
    # convert all the files in the list to opus compressed files
    for item in lista:
        filename = f"audios/{item}.mp3"
        output_filename = f"audios/convertidos/{item}.opus"
        # Convert the file to opus format
        audio = AudioSegment.from_mp3(filename)
        audio.export(output_filename, format="opus", bitrate="16k")