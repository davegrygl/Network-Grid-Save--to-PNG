import os
import time
import glob
import pyautogui
import subprocess


folder_path = r"C:\Users\TwojUzytkownik\Desktop\ToeProjects"
toe_files = glob.glob(os.path.join(folder_path, "*.toe"))
for toe_file in toe_files:
    print(f"[INFO] Uruchamianie pliku: {toe_file}")
    
    td_exe = r"C:\Program Files\Derivative\TouchDesigner.exe"

    process = subprocess.Popen([td_exe, toe_file])
    
    time.sleep(10)
    screenshot_name = os.path.splitext(os.path.basename(toe_file))[0] + "toe_file_screenshot.png"
    screenshot_full_path = os.path.join(folder_path, screenshot_name)

    pyautogui.screenshot(screenshot_full_path)
    print(f"[INFO] Zrzut ekranu zapisany: {screenshot_full_path}")
    pyautogui.hotkey("alt", "f4")

    time.sleep(3)

print("[KONIEC] Wszystkie pliki *.toe przetworzone.")