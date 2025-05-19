import pyautogui
import keyboard
import time
import pygetwindow as gw
import subprocess
import os

# file path (change this path to match the location of the ChatGPT app on your computer)
GPT_EXECUTABLE_PATH = r"C:\Program Files\WindowsApps\OpenAI.ChatGPT-Desktop_1.2025.125.0_x64__2p2nqsd0c76g0\app\ChatGPT.exe"
# window title
GPT_WINDOW_TITLE = "ChatGPT"

def is_gpt_running():
    windows = gw.getAllTitles()
    return any(GPT_WINDOW_TITLE in title for title in windows)

def launch_gpt_app():
    if not os.path.exists(GPT_EXECUTABLE_PATH):
        print("Uygulama yolu yanlis, Dosya bulunamadı.")
        return False
    subprocess.Popen(GPT_EXECUTABLE_PATH)
    print("ChatGPT baslatiliyor...")
    return True

def bring_gpt_to_front():
    for _ in range(20):  # 10 saniyeye kadar dene
        windows = gw.getWindowsWithTitle(GPT_WINDOW_TITLE)
        if windows:
            win = windows[0]
            win.activate()
            return True
        time.sleep(0.5)
    print("Pencere bulunamadi.")
    return False

def send_selected_text_to_gpt():
    # Seçili metni kopyala
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.3)

    # GPT çalışmıyorsa başlat
    if not is_gpt_running():
        if not launch_gpt_app():
            return
        time.sleep(3)  # Uygulamanın açılması için zaman tanı

    # Öne getir
    if bring_gpt_to_front():
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')

print("Hazır: Metni seç ve 'p' tuşuna bas.")
while True:
    if keyboard.is_pressed('p'):
        send_selected_text_to_gpt()
        time.sleep(0.5)