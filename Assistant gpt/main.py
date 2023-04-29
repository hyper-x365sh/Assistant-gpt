


''' Hellow dear its sandesh kumar created this system for the use of chat gpt integrated with python
Follow me on git hub (hyper-x365sh)'''





bg = str(input("your name:"))
import openai 
from playsound import playsound
from gtts import gTTS
import os
import time
from datetime import datetime
from englisttohindi.englisttohindi import EngtoHindi
from googletrans import Translator
# get api key from openai.com/api
openai.api_key = "paste you api key here:"
# creating a speak function which will speak the text we enter:
dir = os.getcwd()
def speak(text):
    language = "en" # you can change the language of the gtts model
    myobj = gTTS(text=text, lang=language, slow=False , tld = "us") # also can change the accent via gtts documentation (tld) as accent
    myobj.save(f"{dir}\Temp\main.mp3")
    playsound(f"{dir}\Temp\main.mp3")
    os.remove(f"{dir}\Temp\main.mp3") # will remove the dir after closing the speak





def speak2(text):
    language = "hi"
    myobj = gTTS(text=text, lang=language, slow=False )
    myobj.save(f"{dir}\Temp\main2.mp3")
    playsound(f"{dir}\Temp\main2.mp3")
    os.remove(f"{dir}\Temp\main2.mp3")

# main gpt
def gpt(query , lang):   # specify the query along with the language for hindi type gpt("your query" , "Hindi") for english gpt("your query" , "english")
        
    while True:
        speak("After reading press 0 to exit:")
        print("After reading press 0 to exit:")
     
       
        user_input = query
    
        print("--"*40)
        if lang == "Hindi" :
                hj = f"iam searching for {user_input}"
                mn = EngtoHindi(hj)
                print(mn.convert)
                speak2(mn.convert)
        else:
                print(f"searching for {user_input}")
                speak(f"searching for {user_input}")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content":
                "You are a helpful assistant."},
                {"role": "user", "content": user_input},
            ],
            temperature=0.5,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            n=1,
            stop=["\nUser:"],
        )

        bot_response = response["choices"][0]["message"]["content"]
    
    
        if lang == "Hindi"   :
            translater = Translator()
            res =  translater.translate(bot_response,  src="en", dest="hi")
            now = datetime.now() 
            date_time = now.strftime("%m/%d/%Y, %H:%M:%S")  
            with open(fr"{dir}\\history\\history.txt" , "a+" ) as mainfile:
                data = f'''\n----------------------------------------------------------------------
{bg} searched for {user_input} on   {date_time} \n 
Answer: {bot_response}
--------------------------------------------------------------------------\n'''
                mainfile.write(data)
                mainfile.close()
                print("--"*40)
            
    
            header = f"your answer for {user_input} is:"
            df = EngtoHindi(header)
            speak2(df.convert)
            print("\nAnswer:" , res.text)
            speak2(res.text)
            print("--"*40)
        else:
            now = datetime.now()   
            date_time = now.strftime("%m/%d/%Y, %H:%M:%S")  
            with open(fr"{dir}\\history\\history.txt" , "a+" ) as mainfile:
                data = f'''\n----------------------------------------------------------------------
{bg}  searched for {user_input} on   {date_time} \n 
Answer: {bot_response}
--------------------------------------------------------------------------\n'''
                mainfile.write(data)
                mainfile.close()
                print("--"*40)
            if len(user_input) >= 6:
                        speak("your answer for your question  is")
                        print("\nAnswer:" , bot_response)
                        speak(bot_response)
                        print("--"*40)
            else:
                                    speak(f"your answer for {user_input} is")
                                    print("\nAnswer:" , bot_response)
                                    speak(bot_response)
                                    print("--"*40)
        speak("for quit press 0 after reading you answer:")
        bg = int(input("quit:"))
        if bg == 0:
              break





speak("hellow user welcome to the program created by sandesh")
speak(" also if you consider this helpful then please show yoour love by following me at git hub above link provided")
def cf():
    try:
        while True:
            speak("to exit press 1: and for continue press 2:")
            print("to exit press 1: and for continue press 2:")
            user = int(input("choice:"))
            if user == 1:
                    speak("bye we will meet again:")
                    break
            elif user == 2:
                    speak("how can i help you:")
                    query = str(input("your query:"))
                    speak("to get results in hindi press 1: and for english press 2:")
                    language = int(input("lang:"))
                    if language == 1:
                            gpt(query, "Hindi")
                            speak("moving on:")
                            cf()
                    elif language == 2:
                           gpt(query , "english")
                           speak("moving on:")
                           cf()
                    else:
                           speak(f"wrong input {user}")
                           cf()
    except:
           time.sleep(2)
           print("please check the program")
           print("check if you added the api key or not:")
           print("check you are connected to internet:")
           time.sleep(4)
           os.system(fr'cmd /k "{dir}\re\repair.bat"')







