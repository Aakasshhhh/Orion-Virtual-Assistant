from core.speaker import speak
from core.listener import take_command
from brain.command_handler import handle_command

def run_orion():
    # Initial Greeting
    speak("Initializing ORION. System check complete.")
    
    while True:
        # Step 1: Listen for voice (High-Accuracy version)
        query = take_command()
        
        # Step 2: If the listener failed, skip to next loop
        if query == "none":
            continue
            
        # Step 3: Pass the text to the Brain
        status = handle_command(query)
        
        # Step 4: Check if the Brain decided to shut down
        if status == "stop":
            break
import datetime
import webbrowser
# CRITICAL: We must import the speak function from our core
from core.speaker import speak 

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
        # Here, the 'f' string passes the actual time into the speaker
        speak(f"The current time is {strTime}")

    # WEB TASKS
    elif 'open google' in query:
        speak("Opening Google for you now.")
        webbrowser.open("https://www.google.com")

    elif 'exit' in query or 'stop' in query:
        speak("Shutting down. Systems offline.")
        return "stop"

    return "continue"
    
if __name__ == "__main__":
    run_orion()