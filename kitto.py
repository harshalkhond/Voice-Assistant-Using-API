import pyttsx3           #convert text to speech
import speech_recognition as sr     #take input as speech
import datetime
import wikipedia
import webbrowser            #gives access to bbrowser
import os
import smtplib               #use to send mails
import googlesearch           #use t9 search using earth
from googlesearch import search
import requests
import wolframalpha



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)




def speak(audio):              #speak anything that you want it to speak
    engine.say(audio)
    engine.runAndWait()

def wishme():                  #wishes you according to time
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour==12:
        speak("good morning!")
    elif hour>12 and hour<=18:
        speak("good afternon!")
        speak("how can i help you")
    else:
        speak("hello how are you going,")
        speak('how are you harshal sir')

def search_please(url):             #takes you to chrome         #search any url on google chrome
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

def takecommand():                  #takes command through microphone
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.......")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing.....")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said {query}\n")
    except Exception as e:
        print("say that again please.....")
        return "None"
    return query

#def sentemail(to,content):                   #send email to anyone
    #server=smtplib.SMTP('smtp.gmail.com',587)
    #server.ehlo()
    #server.starttls()
    #server.login('khondharsha26@gmail.com','')
    #server.sendmail('khondharsha26@gmail.com',to,content)
    #server.close()
    
def ask_google(string):                            #it gives us list of website which are most recently serached related to your query
    website_list=list(search(query, tld="co.in", num=3, stop=3, pause=2))
    for i in range(len(website_list)):
        if "youtube" in website_list[i]:
            pass
        elif():
            search_please(website_list[i])
            break
        else:
            search_please(website_list[0])
            break

def weatherr(city):                    #shows you the weather using weaather map API
        url="https://api.openweathermap.org/data/2.5/weather?q={}&appid=a31656e7a1012c423c9f66c3ba59268b&units=metric".format(city)
        res=requests.get(url)
        data=res.json()
        temp=data["main"]["temp"]
        wind_speed=data["wind"]["speed"]
    
        description=data["weather"][0]["description"]
        mini=data["main"]["temp_min"]
        maxim=data["main"]["temp_max"]
        presseure=data["main"]["pressure"]
        humid=data["main"]["humidity"]
        visibile=data["visibility"]
        speak("showing you the weather")
        speak(f"the temperature of {city} is {temp} degree celsius and it would like to have a {description} ")
        if 'rain' or 'cloud' in description:
            speak ("you should have an umbrella with you when you go out!")
        speak("Do you want some more info....")
        reply=takecommand()
        if reply=="yes" or reply=="s":
            speak('alright showing some more info')
            speak(f"the wind speed will be {wind_speed} metres per second, air pressure is approximately {presseure} pascal, the humidity will be {humid} while the visibility is {visibile} and the temperature ranges from {mini} to {maxim} degrees celsius")

def play_song():
            speak("please tell me which song you want to play")
            song_name=takecommand()
            A=song_name.split()
            original_link='https://gaana.com/song/'
            b='-'
            links=b.join(A)
            links1=original_link+links
            links2=original_link+links+'-1'
            speak(f"playing {song_name} from ganna.com")
            search_please(links1)
            speak("are you able to listen that song?")
            user_input=takecommand()
            if user_input=="yes" or user_input=="s":
                                pass
            elif user_input=="no":
                speak("sorry i will try one more time")
                search_please(links2)
                speak("are you able to listen that song now?")
            again_user_input=takecommand()
            if again_user_input=="yes" or  again_user_input=="s":
                pass
            elif again_user_input=="no":
                speak("have you entered the song correctly!")
                user_input2=takecommand()
                if user_input2=="yes" or user_input2=="s":
                    speak("sorry, i am not able to play that song due to some technical issues")
                elif user_input2=="no":
                    speak("Tell me one more time which song you want me to play")
                    again_user_input=takecommand()
                    speak("please tell me which song you want to play")
                    song_name=takecommand()
                    A=song_name.split()
                    original_link='https://gaana.com/song/'
                    b='-'
                    links=b.join(A)
                    links1=original_link+links
                    links2=original_link+links+'-1'
                    speak(f"playing {song_name} from ganna.com")
                    search_please(links1)
                    speak("are you able to listen that song?")
                    user_input=takecommand()
                    if user_input=="yes" or user_input=="s":
                                        pass
                    elif user_input=="no":
                        speak("sorry i will try one more time")
                        search_please(links2)

listt=('what','when','where','which','who','whom','Whose','why','how')
def ask_any_question(questionss):
    app_id="TWURHH-93E3Q6HYJL"
    client = wolframalpha.Client(app_id)
    res = client.query(questionss)
    answer = next(res.results).text
    print(answer)
    speak(answer)




if __name__== "__main__" :
    wishme()
    while True:
        query=takecommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia.......')
            query=query.replace('wikipedia',"")
            results=wikipedia.summary(query,sentences=4)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            ("opening youtube for you")
            search_please('youtube.com')

        elif 'open whatsapp' in query:
            speak("opening whatsapp from web")
            search_please('https://web.whatsapp.com/')

        elif 'open facebook' in query:
            speak("opening facebook for you")
            search_please('facebook.com')

        elif 'open google' in query:
            speak("opening google search box")
            search_please('google.com')

        elif 'open code' in query:
            speak("opening visual studio code")
            codepath=r"C:\Users\Vaishnavi khond\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codepath)
        
        elif 'send email'in query:
            try:
                speak('what should i say')
                content=takecommand()
                to="vaishnavikhondg@gmail.com"
                sentemail(to,content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry bhai email has not been sent")

        elif 'weather' in query:
            string1=query.split()
            if string1[-1]!='weather':
                weatherr(string1[-1])
            else:
                speak("tell me the name of city please")
                city1=takecommand()
                weatherr(city1)

        elif "book a cab" in query:
            speak("taking you to ola auto")
            search_please('https://www.olacabs.com/')               

        elif 'play'in query:
            play_song()

        elif [i for i in listt if i in query]:
            count=0
            speak("i can anser to any question you want")
            if "minus" or "twice" or "upon" or "into" in query:
                new_query=query.replace("minus","-")
                new_query=new_query.replace("twice","2")
                new_query=new_query.replace("upon","divided by")
                new_query=new_query.replace("into","*")
                ask_any_question(new_query)
                print(new_query)
                count+=1
            else:
                ask_any_question(query)   
           
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"the time is {strTime} ")

        elif "take me to" in query:
            a=query.split()
            b=a.index("to")
            speak(f"taking you to {a[b+1:]}")
            ask_google(a[b+1:])
        elif "images" in query:
            a=query.split()
            if "of" in query:
                b=a.index("of")
                search_please(f"https://www.google.com/search?q={a[b+1:]}+images&rlz=1C1CHBF_enIN893IN893&sxsrf=ALeKk03wHKSr-L0j20-68-5U031CBavGHg:1596211599710&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjD-ovL7_fqAhVSfSsKHQY6BsoQ_AUoAXoECA4QAw&biw=1536&bih=722")
            else:
                b=a.index("for")
                search_please(f"https://www.google.com/search?q={a[b+1:]}+images&rlz=1C1CHBF_enIN893IN893&sxsrf=ALeKk03wHKSr-L0j20-68-5U031CBavGHg:1596211599710&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjD-ovL7_fqAhVSfSsKHQY6BsoQ_AUoAXoECA4QAw&biw=1536&bih=722")

        #elif 'play music' in query:
            #music_dir="C:\Users\Vaishnavi khond\Music\songs"
            #songs=os.listdir(music_dir)
            #print(songs)
            #os.startfile(os.path.join(music_dir,songs[0]))

        #elif len(query)!=0:

            #ask_google(query)
        elif "buy" in query:
            search_list=query.split()
            plus="+"
            thing=plus.join(search_list)
            speak("select one from amazon.in")
            search_please(f"https://www.amazon.in/s?k={thing}&ref=nb_sb_noss_2")

        elif "stop" or "done" or "bye" in query:
            break
        


    






