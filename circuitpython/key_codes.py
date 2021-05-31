# Keys => Codes

keys_ch_de = {
	"a":[4], #a
	"b":[5], #b
	"c":[6], #c
	"d":[7], #d
	"e":[8], #e
	"f":[9], #f
	"g":[10], #g
	"h":[11], #h
	"i":[12], #i
	"j":[13], #j
	"k":[14], #k
	"l":[15], #l
	"m":[16], #m
	"n":[17], #n
	"o":[18], #o
	"p":[19], #p
	"q":[20], #q
	"r":[21], #r
	"s":[22], #s
	"t":[23], #t
	"u":[24], #u
	"v":[25], #v
	"w":[26], #w
	"x":[27], #x
	"y":[29], #y
	"z":[28], #z

	"A":[225,4], #A
	"B":[225,5], #B
	"C":[225,6], #C
	"D":[225,7], #D
	"E":[225,8], #E
	"F":[225,9], #F
	"G":[225,10], #G
	"H":[225,11], #H
	"I":[225,12], #I
	"J":[225,13], #J
	"K":[225,14], #K
	"L":[225,15], #L	
	"M":[225,16], #M
	"N":[225,17], #N
	"O":[225,18], #O
	"P":[225,19], #P
	"Q":[225,20], #Q
	"R":[225,21], #R
	"S":[225,22], #S
	"T":[225,23], #T
	"U":[225,24], #U
	"V":[225,25], #V
	"W":[225,26], #W
	"X":[225,27], #X
	"Y":[225,29], #Y
	"Z":[225,28], #Z

	"0":[39], #0
	"1":[30], #1
	"2":[31], #2
	"3":[32], #3
	"4":[33], #4
	"5":[34], #5
	"6":[35], #6
	"7":[36], #7
	"8":[37], #8
	"9":[38], #9

	"=":[225,39],
	"+":[225,30],
	"*":[225,32],
	"ç":[225,33],
	"%":[225,34],
	"&":[225,35],
	"/":[225,36],
	"(":[225,37],
	")":[225,38],
	
	" ":[44],
	"$":[50],
	"ö":[51],
	"ä":[52],
	"ü":[47],
	"?":[225,45],
	"§":[53],
	",":[54],
	".":[55],
	":":[225,55],
	"-":[56],
	"_":[225,56],
	"°":[225,53],

	# none visible / special commands
	"APOSTROPH":[225,31],
	"HOME":[74], #Home (often moves to beginning of line)
	"END":[77], #End (often moves to end of line)
	"ENTER":[40], #Enter (Return)
	"RETURN":[40], #Alias for ENTER
	"INSERT":[73], #Insert
	"DELETE":[76], #Delete forward
	"TAB":[43], #Tab and Backtab
	"BACKSPACE":[42], #Delete backward (Backspace)
	"POUND":[225,50], ## and ~ (Non-US keyboard)

	"PAGE_DOWN":[78], #Go forward one page
	"PAGE_UP":[75], #Go back one page

	"PAUSE":[72], #Pause (Break)
	"PRINT_SCREEN":[70], #Print Screen (SysRq)
	"ESCAPE":[41], #Escape
	"CAPS_LOCK":[57],
	"SCROLL_LOCK":[71], #Scroll Lock

	"ALT":[226], #Alias for LEFT_ALT; Alt is also known as Option (Mac)
	"APPLICATION":[101], #Application: also known as the Menu key (Windows)
	"COMMAND":[227], #Labeled as Command on Mac keyboards], with a clover glyph
	"CONTROL":[224], #Alias for LEFT_CONTROL
	"GUI":[227], #Alias for LEFT_GUI; GUI is also known as the Windows key], Command (Mac)], or Meta
	"WINDOWS":[227], #Labeled with a Windows logo on Windows keyboards
	"SHIFT":[225], #Alias for LEFT_SHIFT
	"OPTION":[226], #Labeled as Option on some Mac keyboards

	"POWER":[102], #Power (Mac)
	
	"UP_ARROW":[82], #Move the cursor up
	"DOWN_ARROW":[81], #Move the cursor down
	"RIGHT_ARROW":[79], #Move the cursor right
	"LEFT_ARROW":[80], #Move the cursor left
	
	"F1":[58], #Function key F1
	"F10":[67], #Function key F10
	"F11":[68], #Function key F11
	"F12":[69], #Function key F12
	"F13":[104], #Function key F13 (Mac)
	"F14":[105], #Function key F14 (Mac)
	"F15":[106], #Function key F15 (Mac)
	"F16":[107], #Function key F16 (Mac)
	"F17":[108], #Function key F17 (Mac)
	"F18":[109], #Function key F18 (Mac)
	"F19":[110], #Function key F19 (Mac)
	"F2":[59], #Function key F2
	"F3":[60], #Function key F3
	"F4":[61], #Function key F4
	"F5":[62], #Function key F5
	"F6":[63], #Function key F6
	"F7":[64], #Function key F7
	"F8":[65], #Function key F8
	"F9":[66], #Function key F9

	"KEYPAD_ZERO":[98], #Keypad 0 and Ins
	"KEYPAD_ONE":[89], #Keypad 1 and End
	"KEYPAD_TWO":[90], #Keypad 2 and Down Arrow
	"KEYPAD_THREE":[91], #Keypad 3 and PgDn
	"KEYPAD_FOUR":[92], #Keypad 4 and Left Arrow
	"KEYPAD_FIVE":[93], #Keypad 5
	"KEYPAD_SIX":[94], #Keypad 6 and Right Arrow
	"KEYPAD_SEVEN":[95], #Keypad 7 and Home
	"KEYPAD_EIGHT":[96], #Keypad 8 and Up Arrow
	"KEYPAD_NINE":[97], #Keypad 9 and PgUp

	"KEYPAD_ASTERISK":[85], #Keypad *
	"KEYPAD_BACKSLASH":[100], #Keypad \ and | (Non-US)
	"KEYPAD_ENTER":[88], #Keypad Enter
	"KEYPAD_EQUALS":[103], #Keypad":[(Mac)
	"KEYPAD_FORWARD_SLASH":[84], #Keypad /
	"KEYPAD_MINUS":[86], #Keyapd -
	"KEYPAD_PLUS":[87], #Keypad +
	"KEYPAD_NUMLOCK":[83], #Num Lock (Clear on Mac)
	"KEYPAD_PERIOD":[99], #Keypad . and Del

	"LEFT_ALT":[226], #Alt modifier left of the spacebar
	"RIGHT_ALT":[230], #Alt modifier right of the spacebar

	# double presse => ""
	"RIGHT_BRACKET":[48], #] and }

	"LEFT_CONTROL":[224], #Control modifier left of the spacebar
	"RIGHT_CONTROL":[228], #Control modifier right of the spacebar

	"LEFT_GUI":[227], #GUI modifier left of the spacebar
	"RIGHT_GUI":[231], #GUI modifier right of the spacebar

	"LEFT_SHIFT":[225], #Shift modifier left of the spacebar
	"RIGHT_SHIFT":[229] #Shift modifier right of the spacebar
}