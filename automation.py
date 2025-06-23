from pywinauto import Desktop
from pywinauto.keyboard import send_keys
import time

def action_centre(option):
    options = {
        1: "Bluetooth",
        2: "Mobile hotspot",
        3: "Night light"
    }

    if option not in options:
        print("Invalid option.")
        return

    toggle_name = options[option]

    try:
        send_keys("{VK_LWIN down}a{VK_LWIN up}")
        time.sleep(1.5)

        desktop = Desktop(backend="uia")
        quick_settings = desktop.window(title_re=".*", control_type="Window")

        for btn in quick_settings.descendants():
            if toggle_name.lower() in btn.window_text().lower():
                btn.click_input()
                print(f"[INFO] Toggled {toggle_name}")
                break

        send_keys("{VK_LWIN down}a{VK_LWIN up}")

    except Exception as e:
        print(f"[ERROR] Action centre automation failed: {e}")
