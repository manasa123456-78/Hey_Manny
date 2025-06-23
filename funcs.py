import webbrowser
import pyautogui
import time
import json

def search_on_google(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")

def play_on_youtube(query):
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

def show_desktop():
    pyautogui.hotkey('win', 'd')

def close_tab():
    pyautogui.hotkey('ctrl', 'w')

def q_and_a_train(query):
    try:
        if "when i say" in query and "you say" in query:
            parts = query.split("you say")
            question = parts[0].replace("when i say", "").strip()
            answer = parts[1].strip()

            with open('data.json', 'r') as f:
                data = json.load(f)

            if question in data:
                if answer not in data[question]:
                    data[question].append(answer)
            else:
                data[question] = [answer]

            with open('data.json', 'w') as f:
                json.dump(data, f, indent=4)

            return True
        return False
    except Exception as e:
        print(f"[ERROR] q_and_a_train failed: {e}")
        return False
