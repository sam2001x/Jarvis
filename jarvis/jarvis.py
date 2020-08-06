import pyttsx3
from json import loads
import requests
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia 
import os
import smtplib
import psutil
import shutil
from weather_forecast import weather
import re
import time


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# This function checks the cpu usage and returns true if the usage is less than 75 %. 
def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75  

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    # Replace <gmail-id> with you gmail id and <pass-word> with your orignal password
    server.login('<gmail-id>','<pass-word>')   
    server.sendmail('santaudaipur@gmail.com', to, content)
    server.close()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# This function reads the newspaper headlines
def read_news():
    speak("Todays headlines are")
    url = # enter your newsapi link here.
    news = requests.get(url).text
    news = json.loads(news)
    arts = news['articles']
    for articles in arts:
        speak(articles['title'])
        speak("next news")
        time.sleep(2)
        
def Flip_coin():
     coin = ["head","tail"]
     coin = rm.choice(coin)
     playsound("<PATH>") # Replace <PATH> with the path of mp3 sound you want to play while flipping coin
     speak(f"{coin}")
                       

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir!")
    elif hour >=12 and hour < 18:
        speak("Good afternoon sir!")
    else:
        speak("Good Evening sir!")
    speak("please tell me how may i help you")


# This function extracts the number from a string
def find_number(string):
    temp = re.findall(r'\d+',string)
    return(list(map(int, temp)))

def takecommand():
    """ It takes microphone input from user and 
    returns string output"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return("None")
    return query    


if __name__ == "__main__":
    WishMe()
    while True:
        query = takecommand().lower()
        

        #logic for exccuting task based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia..")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2) #sentence=2 means taking 2 lines from wikipedia
            speak("According to wikipedia..")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            
            webbrowser.open("google.com")

        elif 'open hackerrank' in query:
            webbrowser.open("hackerrank.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")        

        elif 'send email' in query:
                try:
                    speak("what should i say")
                    content = takecommand()
                    sendemail(to, content)
                    speak("your email has been sent!")
                except Exception as e:
                    print(e)
                    print("soory sir i could not send email")

        elif 'play music' in query:
                    music_dir = #path to the folder
                    song = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, song[randint(1,10)]))
        
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"sir, the time is {strtime}")

        elif 'open  vs code' in query:
            codepath = "C:\\Users\\saket\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
       
        elif 'check cpu usage' in query:
            if check_cpu_usage():
                speak("Everything is fine sir. Your cpu usage is less than 75 percent.")
            else:
                speak("your cpu usage is more then 75 percent")

        elif "today's headlines" in query:
            read_news()

        elif "today's weather" in query:
            w_F = weather()
            speak(w_F)
            print(w_F)
        
        elif "add" in query:
            res = find_number(query)
            speak(f" the result is {sum(res)}")

        elif "wait" in query:
            sl = find_number(query)
            for i in sl:
                time.sleep(i)

        elif 'quit' or 'exit' or "jarvis shutdown"  in query:          
            exit()
            
        
        elif "toss a coin" or "flip a coin" in query:
                Flip_coin()    
            
        
        




