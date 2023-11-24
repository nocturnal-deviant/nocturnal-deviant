

#PDF to Speech model 
#importing neccessary modules 
import pyttsx3
import PyPDF2

#location of the pdf file 
read_file=PyPDF2.PdfReader(open('Projects /Img_to_speech/ML_algorithms.pdf','rb'))

#initializin the speech engine 
engine=pyttsx3.init()

#initializing the iteration to read each pages from the pdf one after another 
for pagenumber in range(len(read_file.pages)): 
    voices=engine.getProperty('voices')  #changig the default voice 
    engine.setProperty('voice',voices[2].id) 
    engine.setProperty('rate',120)  #adjusting the speed 
    engine.setProperty('volume',2.5)  #adjusting the volume 
    text=read_file._get_page(pagenumber).extract_text() #extracting the text from pdf file 
    engine.say(text)
    print(text)
    engine.save_to_file(text,'audio.mp3')
    engine.runAndWait()


engine.stop()
engine.runAndWait()
