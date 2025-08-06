# 🧠 Jarvis: Voice-Activated AI Assistant in Python

A voice-controlled virtual assistant inspired by real-world AIs like Siri and Alexa. "Jarvis" listens for voice commands and performs a variety of tasks — from fetching real-time weather and news to opening websites and answering custom questions using Groq’s LLaMA 3 model.

---

## 🚀 Features

- 🎤 **Wake Word Activation** – Listens for the keyword `Jarvis` before activating.
- 🔊 **Offline Text-to-Speech** – Talks back using `pyttsx3`.
- 🌐 **Web Automation** – Opens YouTube, Google, Netflix, LinkedIn, and more.
- 🎵 **Music Search** – Searches and plays songs on YouTube.
- 🌤️ **Live Weather Updates** – Gets real-time weather via [WeatherAPI](https://www.weatherapi.com/).
- 📰 **Breaking News** – Reads out business headlines via [NewsAPI](https://newsapi.org/).
- 🤖 **Smart AI Answers** – Sends general questions to Groq’s **LLaMA 3 AI model** and responds intelligently.

---

## 🛠️ Tech Stack

| Technology     | Purpose                            |
|----------------|-------------------------------------|
| Python 3.11     | Core programming language          |
| SpeechRecognition | Voice input & speech recognition |
| PyAudio        | Microphone access                  |
| pyttsx3        | Offline speech synthesis (TTS)     |
| Requests       | API communication (weather/news)   |
| Groq SDK       | LLaMA 3 intelligent chatbot        |
| Webbrowser     | Open URLs in default browser       |
| Pytube         | (Optional) YouTube video handling  |

---

## 🧪 How It Works

1. The assistant listens for the wake word “**Jarvis**”.
2. Once activated, it listens for your command.
3. Based on the command, it:
   - 🔗 Opens a website
   - 🎶 Plays a song on YouTube
   - 🌦️ Gives weather info
   - 📰 Reads out the latest news
   - 🧠 Or sends your command to Groq LLaMA 3 AI for a response.

---

## 📦 Installation

1. **Clone this repository:**
```bash
git clone https://github.com/yourusername/jarvis-voice-ai-assistant.git
cd jarvis-voice-ai-assistant
