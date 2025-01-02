import pyautogui
import time
import pyperclip
import cohere

co = cohere.Client("LVwy0jXt62EqxQ5pSpwDrW1rrL6EPAY4TZL4mkxg")  # Replace with your API key

'''
Warning: No extra apps should be active rather than the ones that are on taskbar. Can disturb the icon pointer
Target: Wanda Maximoff -- Whatsapp web
Icon pointer: 1204, 1046
starting co-ordinate: 685, 270
ending co-ordinate: 1843, 900
'''

pyautogui.click(1204, 1046)
time.sleep(1)

pyautogui.moveTo(685, 270)
pyautogui.dragTo(1843, 900, duration=1.0, button='left') 
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)
chat_history = pyperclip.paste()
chat_history = pyperclip.paste()
print(chat_history)
# First prompt
response1 = co.generate(
    model="command-xlarge-nightly",
    prompt="You are a person named Taslim Ansari who speaks hindi as well as english. You are from India and you are a coder. You analyze chat history and roast people in a funny way. Output should be the next chat response (text message only)",
    max_tokens=50
)
result1= response1.generations[0].text
print("Response 1:", result1)

# Second prompt
response2 = co.generate(
    model="command-xlarge-nightly",
    prompt=chat_history,
    max_tokens=50
)
result2= response2.generations[0].text
print("\nResponse 2:", result2)
pyperclip.copy(result2)

pyautogui.click(844, 954)
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.press('enter')