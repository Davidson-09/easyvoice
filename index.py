import speech_recognition as sr
import json
from types import SimpleNamespace
import re

r = sr.Recognizer()

Microphones = sr.Microphone.list_microphone_names()
my_mic = sr.Microphone(device_index=1)

# with sr.AudioFile(filename) as source:
#     # listen for the data (load audio to memory)
#     audio_data = r.record(source)
#     # recognize (convert from speech to text)
#     text = r.recognize_google(audio_data)
#     print(text)

with my_mic as source:
    print("Say now!!!!")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

# print(r.recognize_google(audio))
# print(audio)

textObject = r.recognize_google(audio, language = 'en-IN', show_all = True )
extract = json.dumps(textObject)
print(extract)
text = json.loads(extract,object_hook=lambda d: SimpleNamespace(**d)).alternative[0].transcript


# now to text recognition
pattern = "[a-zA-Z0-9]+ [0-9]+:[0-9]+"
secondPattern = "[a-zA-Z0-9]+ [0-9]+:[0-9]+\(-)[0-9]"

if (re.search(pattern, text)):
    print('valid input')
else:
    print('invalid input or wrong pattern')