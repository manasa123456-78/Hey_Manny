import json
import random as rand
import time
from datetime import datetime
from speech import speak, take_user_input
from funcs import *
from automation import action_centre

with open('data.json', 'r') as fp:
    qdb = json.load(fp)
all_ques = list(qdb.keys())

def greet_user(USERNAME="Manasa"):
    hour = datetime.now().hour
    if 6 <= hour < 12:
        speak(f"Good Morning {USERNAME}")
        speak("I am very happy to see you Mam")
        time.sleep(0.5)
        speak("Oh wait, actually I cannot see you Mam as you didn't give me access to your webcam")
    elif 12 <= hour < 16:
        speak(f"Good Afternoon {USERNAME}")
        speak("Did you have your lunch Mam?")
        time.sleep(0.5)
        speak("Sometimes I feel like eating real food too, Mam")
    elif hour >= 16:
        speak(f"Good Evening {USERNAME}")
        speak("Hope your day went as planned Mam")
    else:
        speak("Good to see you awake, Mam")
        time.sleep(0.5)
        speak("I thought I am the only one awake")

while True:
    query = take_user_input().lower()

    if 'hello nova' in query or 'hey nova' in query:
        greet_user()
        while True:
            query_1 = take_user_input().lower()

            if query_1 in all_ques:
                response = rand.choice(qdb[query_1])
                print(response)
                speak(response)
                continue

            if query_1 == 'dodo':
                speak("Yes Mam")
                continue

            if 'search' in query_1 and 'google' in query_1:
                idx1 = query_1.index('search')
                idx2 = query_1.index('on')
                res = query_1[idx1 + len('search') + 1: idx2].strip()
                search_on_google(res)
                continue

            if 'play' in query_1 and 'on' in query_1:
                idx1 = query_1.index('play')
                idx2 = query_1.index('on')
                res = query_1[idx1 + len('play') + 1: idx2].strip()
                play_on_youtube(res)
                continue

            elif 'play' in query_1:
                play_on_youtube(query_1.split('play')[1].strip())
                continue

            if 'show desktop' in query_1:
                show_desktop()
                continue

            if 'close tab' in query_1:
                close_tab()
                continue

            if 'when i say' in query_1:
                if q_and_a_train(query_1):
                    with open('data.json', 'r') as fp:
                        qdb = json.load(fp)
                    all_ques = list(qdb.keys())
                    speak("Added to my database, Mam")
                continue

            if 'hotspot' in query_1:
                action_centre(2)
                continue
            if 'bluetooth' in query_1:
                action_centre(1)
                continue
            if 'night light' in query_1:
                action_centre(3)
                continue

            if 'take rest' == query_1:
                speak("Thank you Mam. But I'm always ready.")
                break

            if 'full screen' in query_1:
                pyautogui.press('f')
                continue
            if 'pause' in query_1 or 'resume' in query_1:
                pyautogui.press('space')
                continue

    if 'go home' in query:
        speak("Thanks for letting me sleep Mam. Bye.")
        break
