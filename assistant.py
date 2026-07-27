from pynput import mouse
from pynput import keyboard
from pynput.keyboard import Key
import time
import sys
import pyperclip
from google import genai
from dotenv import load_dotenv
load_dotenv()
def copy():
    with keyboard_controller.pressed(Key.ctrl):
        keyboard_controller.press("c")
        keyboard_controller.release("c")
        time.sleep(0.5)
def get_text():
        parse_to_llm=pyperclip.paste()
        return parse_to_llm
def calling_llm(parse_to_llm):
        interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input=f"if a mathematical equation is given , give its solution , if a word is given give its definition and if question is asked just answer it here is your statement --  {parse_to_llm}" 
     )
        return (interaction.output_text)
client = genai.Client()
a,b=None,None
c,d=None,None
keyboard_controller = keyboard.Controller()
'''here start the  work '''

try:
    def on_hotkeyactivate():
       print("hot key activated")
       def on_click(x, y, button, pressed):
          global a,b,c,d
          if pressed :
            a,b=x,y
          else:
            c,d=x,y
            if a-c ==0 and d-b==0:
              return "you didnt even select anything"
            else :
              print(f"text selected successfully !!")
              copy()
              get_text()
              calling_llm(get_text())
            return False
          
       listener= mouse.Listener(
                      on_click=on_click,
                   ) 
       listener.start()
  
                
    def for_canonical(f): # pattern gets clearance
      return lambda k: f(l.canonical(k))

    hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<ctrl>+<alt>+h'), # hotkey defined 
    on_hotkeyactivate)
    l= keyboard.Listener(
        on_press=for_canonical(hotkey.press),
        on_release=for_canonical(hotkey.release)) 
    l.start()
    on_hotkeyactivate()
    time.sleep(20)
except (AttributeError,KeyboardInterrupt):
   sys.exit()
