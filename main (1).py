import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
# for visual and user interface 
from tkinter import *
from PIL import Image,ImageTk
import tkinter as tk
def one_f():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
   # print(voices[1].id)
   # 2 is female voice and 1 /3 is male voice 
    engine.setProperty('voice', voices[1].id)


    def speak(audio):
       engine.say(audio)
       engine.runAndWait()

  
    def wishMe():
       hour = int(datetime.datetime.now().hour)
       if hour>=0 and hour<12:
        speak("Good Morning!")

       elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

       else:
        speak("Good Evening!")  

       speak("Hello I am Siya. Please tell me how may I help you")       

    def takeCommand():
      #It takes microphone input from the user and returns string output

      r = sr.Recognizer()
      with sr.Microphone() as source:
          print("Listening...")
    #pause for 1 second before execution.
          r.pause_threshold = 1
          audio = r.listen(source)

      try:
          print("Recognizing...")    
          query = r.recognize_google(audio, language='en-in')
          print(f"User said: {query}\n")

      except Exception as e:
          # print(e)    
          #print("Say that again please....")
          speak("Say that again please....") 
          return "None"
      return query

    def sendEmail(to, content):
      server = smtplib.SMTP('smtp.gmail.com', 587)
      server.ehlo()
      server.starttls()
      server.login('youremail@gmail.com', 'your-password')
      server.sendmail('youremail@gmail.com', to, content)
      server.close()

    if __name__ == "__main__":
      wishMe()
      #while True:
      if 1:
          query = takeCommand().lower()

          # Logic for executing tasks based on query
          if 'wikipedia' in query:
              speak('Ok please wait')
              query = query.replace("wikipedia", "")
              results = wikipedia.summary(query, sentences=2)
              speak("According to Wikipedia")
              webbrowser.open(results)
              print(results)
              speak(results)

          elif 'youtube' in query:
              webbrowser.open("youtube.com")

          elif 'who are you' in query:
              speak("My name is siya and I am a virtual Assistant backbenchers  made me with the help of python language")

          elif 'google' in query:
              webbrowser.open("google.com")
              
          elif 'take me to my bank' in query:
              webbrowser.open("https://v1.hdfcbank.com/assets/popuppages/netbanking.htm")    
              
          elif 'take me to my College' in query:
              webbrowser.open("https://www.umit.ac.in/")

          elif 'stack overflow' in query:
              webbrowser.open("stackoverflow.com")

          elif 'world' in query:
              webbrowser.open('https://edition.cnn.com/world')

          elif 'open new' in query:
              webbrowser.open('https://timesofindia.indiatimes.com/?from=mdr')
            
          elif 'food' in query:
              webbrowser.open("zomato.com")

          elif 'Swiggy' in query:
              webbrowser.open("swiggy.com")

          elif 'open spotify' in query:
              webbrowser.open("https://open.spotify.com/?nd=1")

          elif 'open whatsapp' in query:
              webbrowser.open("https://web.whatsapp.com/")

          elif 'book my ticket' in query:
              webbrowser.open("https://in.bookmyshow.com")

          elif 'Netflix' in query:
              webbrowser.open("netflix.com")
        
          elif 'instagram' in query:
              webbrowser.open("https://www.instagram.com/")

          elif 'I want to shopping' in query:
              webbrowser.open("https://www.amazon.com/") 


          elif 'play my favourite song' in query:
              music_dir = 'D:\songs'
              songs = os.listdir(music_dir)
              print(songs)    
              os.startfile(os.path.join(music_dir, songs[0]))

          elif 'what is the time' in query:
              strTime = datetime.datetime.now().strftime("%H:%M:%S")    
              speak(f"the time is {strTime}")

          elif 'open code' in query:
              codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
              os.startfile(codePath)

          elif 'mail to Shruti' in query:
              try:
                  speak("What should I say?")
                  content = takeCommand()
                  to = "shrutibharati21@gmail.com"    
                  sendEmail(to, content)
                  speak("Email has been sent!")
              except Exception as e:
                  print(e)
                  speak("Sorry my friend Shruti. I am not able to send this email")
def close():
    screen1.destroy()
#TKIENER code below
global screen1
screen1 = Tk()
width = screen1.winfo_screenwidth()
height = screen1.winfo_screenheight()
screen1.geometry(f'{width}x{height}')
#bg=PhotoImage(file="E:\images\cort.png")
screen1.title("Siya")
path = "aishaa.png"
#panel = tk.Label(window, image = img)
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(screen1, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
screen1['bg'] = "cornflowerblue"
#b4 = Button(screen1, text="personal Assistant", font=('Helvetica', 40),borderwidth=5,relief=SUNKEN)
#b4.place(x=550,y=15)
#1st button for start
b5 = Button(screen1, text="Hello Siya !!", fg='Red', bg="black", font=('Helvetica', 40),borderwidth=8, command=one_f,relief=FLAT)
b5.place( x=150,y=530)
#2nd button close
b6 = Button(screen1, text="See You ", fg='Red', bg="black", font=('Helvetica', 40),borderwidth=8, command=close,relief=FLAT)
b6.place( x=180,y=660)
screen1.mainloop()


