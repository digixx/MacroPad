# Trinket M0 CodePad

import board
import busio
import time
from digitalio import DigitalInOut, Direction, Pull
from adafruit_hid.keyboard import Keyboard
from key_codes import keys_ch_de as keymap
from cmd_maps import *

cmd_bankswitch = "BANK"

# Built in red LED
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# Used if we do HID output
kbd = Keyboard()
kbd_layout = keymap

# Serial connection to Nextion
uart = busio.UART(board.TX, board.RX, stop=1, baudrate=115200, timeout=0.1)

# send data to Nextion, send end of message tail too
def send(msg):
    buf = bytearray(msg)
    uart.write(buf)
    uart.write(b'\xff\xff\xff')

# set caption and background color of buttons on Nextion
def set_button(id, name, color):
    if color == "": color = "50712" # if not defined set color to grey
    send(id + '.txt="' + name + '"')
    send(id + '.bco=' + color)

# set text and color of buttons on nextion for selected bank
def build_ui(bank_name):
    bank = banks[bank_name] # Dict
    for buttons in bank:
        for btn_id in buttons: # Dict
            elements = buttons[btn_id]
            btn_name = elements[0]
            btn_color = elements[1]
            btn_cmds = elements[2]
            set_button(btn_id, btn_name, btn_color)
            buttons_cmds[btn_id] = btn_cmds

# send ascii text (check keyboard map for correct keys)
def send_text(text):
    for char in text:
        c = kbd_layout.get(char.upper())
        print("char:", c)
        if c is not None:
            if char == char.upper(): # send upper case value
                kbd.press(kbd_layout.get("SHIFT"))
                kbd.press(c)
            else:
                kbd.press(c)
            kbd.release_all()

# separate different keystrokes and delay some time after sending
def do_delay(t):
    delay = t * 0.1
    time.sleep(delay)

# get command string for pressed button and execute commands
def send_keys(btn):
    cmds = buttons_cmds.get(btn)
    if cmds is not None:
        print("cmds=", cmds)
        for cmd in cmds:
            print("cmd=", cmd)
            
            # check for string or interger value
            if isinstance(cmd, int):
                # print ("cmd: Delay found=", cmd)
                kbd.release_all()
                do_delay(cmd)

            elif isinstance(cmd, str):
                # check for static commands
                if cmd == cmd_bankswitch:
                    build_ui(next(current_bank))

                else:
                    # check for known keywords
                    kw = kbd_layout.get(cmd)
                    if kw is not None:
                        # keyword found
                        # print("kw=", kw)
                        for kwc in kw:
                            kbd.press(kwc)

                    else:
                        # keyword not found / send as ascii string
                        for s in cmd:
                            c = kbd_layout.get(s)
                            if c is not None:
                                # print("s/c=", s, c)
                                for kc in c:
                                    # print("kc=", kc)
                                    kbd.press(kc)
                                    # print("kc=", kc)
                                kbd.release_all()
        print("-----------")

# switch to next defined bank
def roll_bank():
    while True:
        for bank in banks:
            yield bank

######################### INIT ###################################
print("Start")
current_bank = roll_bank() # get first bank in definition
build_ui(next(current_bank)) # set Nextion buttons for bank text and color

######################### MAIN LOOP ##############################
while True:
    if uart.in_waiting:
        data = uart.readline()
        button_pressed = "".join(chr(x) for x in data)
        led.value = 1
        send_keys(button_pressed)
        led.value = 0
