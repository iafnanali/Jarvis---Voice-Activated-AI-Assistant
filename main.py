import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
from groq import Groq
from pytube import YouTube

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi= "12000105ba62ec14214adfba6ba1a18b893333"
weatherapi = "cefffe091f5f4a4bde95e173205241111"
city = "bahawalpur"
music = {
    "shape of you":"https://www.youtube.com/watch?v=JGwWNGJdvx8&list=PLPSCssPYXhWTTcpNZwYoEQWt8Wc8KO0NV",
    "let her go":"https://www.youtube.com/watch?v=RBumgq5yVrA&list=PLPSCssPYXhWTTcpNZwYoEQWt8Wc8KO0NV&index=10"
}

def speak(text):
    engine.say(text) 
    engine.runAndWait() 

def process_ai(command):
    GROQ_API_KEY = "gsk_555zXLrhlA3LtY5v80LHa2WGdyb3FYGIjCEtqKqY2aHa9JGmBLjAIbbbb"
    client = Groq(api_key=GROQ_API_KEY)

    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": command,
        }
    ],
    model="llama3-8b-8192",
    )

    return (chat_completion.choices[0].message.content)

def process_command(command):
    if "open youtube" in command.lower():
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")
    elif "open google" in command.lower():
        speak("Opening Google.")
        webbrowser.open("https://www.google.com/")
    elif "open netflix" in command.lower():
        speak("Opening Netflix.")
        webbrowser.open("https://www.netflix.com/")
    elif "open linkedin" in command.lower():
        speak("Opening Linkedin.")
        webbrowser.open("https://www.linkedin.com/")
    elif "play" in command.lower():
        song = command.lower().split("play", 1)[1].strip()
        speak(f"Searching for {song} on YouTube.")
        search_query = f"https://www.youtube.com/results?search_query={'+'.join(song.split())}"
        webbrowser.open(search_query)
    elif "news" in command.lower():
        speak("Fetching the latest news.")
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            if articles:
                for article in articles[:5]:
                    title = article['title']
                    speak(title)
            else:
                speak("Sorry, I couldn't find any news articles.")
        else:
            speak("Failed to fetch news.")
    elif "weather" in command.lower():
        speak("Fetching weather")
        r = requests.get(f"http://api.weatherapi.com/v1/current.json?key={weatherapi}&q={city}")
        if r.status_code == 200:
            data = r.json()
            location = data['location']['name']
            region = data['location']['region']
            country = data['location']['country']
            temp_celsius = data['current']['temp_c']
            condition = data['current']['condition']['text']
            feels_like_celsius = data['current']['feelslike_c']
            speak(f"Weather in {location}, {region}, {country}:")
            speak(f"Temperature: {temp_celsius}°C")
            speak(f"Condition: {condition}")
            speak(f"Feels Like: {feels_like_celsius}°C")
        else:
            speak(f"Failed to fetch weather data. Status code: {r.status_code}")
    else:
        output = process_ai(command)
        speak(output)

if __name__ == "__main__":
    speak("Hey I am Jarvis")
    while True:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:   
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)   
            if (word.lower()=="jarvis"):
                speak("Yeah")
                with sr.Microphone() as source:
                    print("JARVIS ACTIVE")
                    audio= r.listen(source)
                    command= r.recognize_google(audio)
                    process_command(command)
        except sr.WaitTimeoutError:
            print("[speak again]")
        except sr.UnknownValueError:
            print("Could not understand the audio")
        except OSError:
            print("Microphone not found or not working.")

