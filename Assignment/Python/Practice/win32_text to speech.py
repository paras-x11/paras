import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

# Change the rate (-10 to 10; default is 0)
speaker.Rate = 2  # Speaks faster

# Change the volume (0 to 100)
speaker.Volume = 80  # Set volume to 80%

# List available voices
voices = speaker.GetVoices()
print("Available Voices:")
for i, voice in enumerate(voices):
    print(f"{i}: {voice.GetDescription()}")

speaker.Voice = voices[1]  

speaker.Speak("This is a customized text-to-speech example.")
