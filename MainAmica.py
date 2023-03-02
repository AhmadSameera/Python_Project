import random
import json
import torch
from Brain import NeuralNet
from NeuralNetwork import bag_of_words,tokenize


device=torch.device('cuda' if torch.cuda.is_available() else'cpu')
with open("intents.json",'r') as json_data:
    intents=json.load(json_data)

FILE="traindata.pth"
data=torch.load(FILE)

input_size=data["input_size"]
hidden_size=data["hidden_size"]
output_size=data["output_size"]
all_words=data["all_words"]
tags=data["tags"]
model_state=data["model_state"]

model=NeuralNet(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()

#----------------------- Main Coding-------------------------#
from Speak import listen,speak
from tasks import function
from tasks import functionInput
import datetime

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour <12:
        speak("Hello,Good Morning. How can i help you.")
    elif hour >= 12 and hour < 18:
        speak("Hello,Good Afternoon. It's Amica here.")
    elif hour >= 18 and hour < 24:
        speak("Hello,Good Evening")
wishMe()
def main1():
    sentence=listen()
    result=str(sentence)

    if 'stop' in sentence or 'bye' in sentence:
        speak("Byee, Hope you have a good day.")
        exit()

    sentence=tokenize(sentence)
    x=bag_of_words(sentence,all_words)
    x=x.reshape(1,x.shape[0])
    x=torch.from_numpy(x).to(device)

    output=model(x)

    _ ,predicted=torch.max(output,dim=1)
    tag=tags[predicted.item()]
    probs=torch.softmax(output,dim=1)
    prob=probs[0][predicted.item()]

    if prob.item()>0.75:
        for intent in intents['intents']:
            if tag==intent["tag"]:
                reply=random.choice(intent["responses"])

                if "time" in reply:
                    function(reply)
                elif "date" in reply:
                    function(reply)
                elif "screenshot" in reply:
                    function(reply)
                elif "notepad" in reply:
                    function(reply)
                elif "spotify" in reply:
                    function(reply)
                elif "weatherReports" in reply:
                    functionInput(reply,result)
                elif "information" in reply:
                    functionInput(reply,result)
                elif "google" in reply:
                    functionInput(reply,result)
                elif "play" in reply:
                    functionInput(reply,result)
                elif "jokes" in reply:
                    functionInput(reply,result)
                elif "open gmail" in reply:
                    functionInput(reply,result)
                elif "open google" in reply:
                    functionInput(reply,result)
                elif "news" in reply:
                    functionInput(reply,result)
                elif "camera" in reply:
                    functionInput(reply,result)
                # elif "note" in reply:
                #     functionInput(reply,result)
                # elif "alarm" in reply:
                #     functionInput(reply, result)
                elif "stop" in reply:
                    exit()
                else:
                    speak(reply)
try:
    while True:
        main1()
except:
    pass

finally:
    speak('facing some issues. Please try to speak again Maam.')
