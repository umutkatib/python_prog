import pyautogui

# Çözünürlüğü
screenWidth, screenHeight = pyautogui.size()
print("Ekran Çözünürlüğü :", screenWidth, screenHeight)

# Fare
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)