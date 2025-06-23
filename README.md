# Manny – Your Personal Voice Assistant 

Manny is a Python-based desktop voice assistant that recognizes natural speech, responds via text-to-speech, executes system-level actions, and learns custom Q&A responses dynamically. It supports over **20 unique voice commands** for hands-free workflows, desktop automation, and web interaction.

---

##  Features
-  **Voice Command Recognition:** Real-time speech-to-text processing using `SpeechRecognition` with ambient noise calibration.
-  **Dynamic Q&A Learning:** Train Manny on custom questions and answers via natural language prompts.
-  **Text-to-Speech Feedback:** Audio responses powered by `pyttsx3` for seamless interaction.
-  **Web Automation:** Google searches, YouTube playback, and web navigation with voice commands.
-  **System Control:** Automates tasks like showing desktop, closing tabs, fullscreen control, and pausing/resuming media.
-  **Windows Action Center Automation:** Toggle Bluetooth, Hotspot, and Night Light using `pywinauto` for reliable UI automation.
-  **Modular Architecture:** Supports future integrations and easy expansion of commands and features.

---

##  Project Structure
```text
manny-voice-assistant/
├── main.py              # Core voice assistant loop
├── speech.py            # Speech recognition and TTS
├── funcs.py             # Utility functions: search, play, Q&A training, system controls
├── automation.py        # Windows Action Center automation via pywinauto
├── data.json            # Dynamic knowledge base (Q&A pairs)
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
