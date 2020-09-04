import pyautogui
import time

# while 1:
# 	pyautogui.click(605, 177)
# 	time.sleep(6)
# 	pyautogui.click(528,72)
# 	time.sleep(1)
scrolling_times = 7

while 1:
	for scroll in range(scrolling_times): 
		pyautogui.scroll(-5)
		time.sleep(3)
		pyautogui.scroll(5)
		time.sleep(4)
	pyautogui.click(528, 72)
	time.sleep(1)
	pyautogui.click(605, 177)