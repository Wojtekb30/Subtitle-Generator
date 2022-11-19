import speech_recognition as sr
import librosa
import time
from googletrans import Translator
translator = Translator()

r = sr.Recognizer()
wynik=""
dlugosc = 3
ofset=0

movie = sr.AudioFile('movie.wav')
dlugoscvid = int(librosa.get_duration(filename='movie.wav'))
print(dlugoscvid)
if dlugoscvid > librosa.get_duration(filename='movie.wav'):
    dlugoscvid=dlugoscvid-1
print(dlugoscvid)
while dlugoscvid%dlugosc!=0:
    dlugoscvid=dlugoscvid-1
print(dlugoscvid)
while ofset+dlugosc<=dlugoscvid:
    try:
        with movie as source:
            audio = r.record(source, offset=float(ofset), duration=float(dlugosc))
            tempwynik = str(r.recognize_google(audio))
            print("TEMP odczyt: "+tempwynik)
            
            czas = str(time.strftime('%H:%M:%S', time.gmtime(ofset)))
            czass = str(time.strftime('%H:%M:%S', time.gmtime(ofset+dlugosc)))
            
            tlumacz = translator.translate(tempwynik, dest='pl')
            tempwynik = tlumacz.text



                
            wynik = wynik + czas+".000,"+czass+'.000'+'\n'
            wynik = wynik + tempwynik + " " +"\n" + '\n'
            #print("TEMP wynik: "+wynik)
            
    except:
        print("ERROR")
    ofset=ofset+dlugosc
filetowrite = open("subtitles.srt", "w")
filetowrite.write(wynik)
filetowrite.close()
print("DONE")
