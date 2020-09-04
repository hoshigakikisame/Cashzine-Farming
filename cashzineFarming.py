import pyautogui
import time

scrolling_times = 10

while 1:
	for scroll in range(scrolling_times):
		pyautogui.scroll(-1)
		time.sleep(7)
	pyautogui.click(528,72)
	time.sleep(1)
	pyautogui.click(605, 177)