import datetime # Line 1
import webbrowser # Line 2
from core.speaker import speak # Line 3
import wikipedia # Line 4

def handle_command(query):
    # GREETING
    if 'hello' in query or 'hi' in query:
        # We don't just print, we call speak()
        speak("Hello! ORION system is online. How can I help you?")

    # IDENTITY
    elif 'who are you' in query:
        speak("I am ORION, your intelligent assistant.")

    # TIME
    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%I:%M %p")
    # RIGHT:
        speak(f"The current time is {strTime}") 
    
    # WRONG (if you only did this):
    # print(f"The time is {strTime}")

    # WEB TASKS
    elif 'open google' in query:
        speak("Opening Google for you now.")
        webbrowser.open("https://www.google.com")

    elif 'exit' in query or 'stop' in query:
        speak("Shutting down. Systems offline.")
        return "stop"
    
    elif 'wikipedia' in query or 'who is' in query or 'what is' in query or 'tell me about' in query or 'why' in query:
       speak("Searching Wikipedia...")
       query = query.replace("wikipedia", "").replace("who is", "").replace("what is", "").replace("tell me about", "").replace("why", "")
       results = wikipedia.summary(query, sentences=2)
       speak("According to Wikipedia...")
       speak(results)

    elif 'what can you do' in query or 'your features' in query:
       speak("I can tell you the time, open Google or YouTube, and soon, I will be able to recognize your face for secure access.")

    return "continue"