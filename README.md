# MacroPad
Sending scripted keystrokes over USB

This is a small project to send predefined keystrokes over USB to a PC or other HRD devices.

It uses a Nextion-Display to show an array of buttons which can be paged for more commands.
The button on the Nextion are named "b0" ... "b15". "b15" is the button to swap through pages.

In this first version you can choose the title of the buttom, its background color and the command sequence

{"b0": ("CTRL-C","WHITE",["CONTROL","C"])}

"b0": is the name of the button within the page
"CTRL-C" ist the text displayed on the button
"WHITE" is the color of its background
["CONTROL","C"] is the code sended to the serial USB connection



