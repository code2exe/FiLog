from time import sleep
from selenium import webdriver
import configparser
import sys
import pyautogui as auto

pwd = configparser.ConfigParser()
pwd.read('config.ini')
user = pwd['Credentials']['username']
pas = pwd['Credentials']['password']

def main():
	options = webdriver.FirefoxOptions
	# options.set_headless(True)
	global driver
	driver = webdriver.Chrome(chrome_options=options)
	driver.get('https://www.fiverr.com')
	sleep(5)
	# LOGIN
	sign_in = driver.find_element_by_css_selector('#main-wrapper-header > header > div.header-row > nav > ul > li.header-login > a')
	# sleep(1)
	sign_in.click()
	# END LOGIN
	sleep(2)
# 	Pyauto
	auto.moveTo(489, 437, duration=0.25)
	auto.click(489, 437, clicks=1, button='left')
	auto.typewrite(user)
	sleep(2)
	auto.moveTo(410, 503, duration=0.25)
	auto.click(410, 503, clicks=1, button='left')
	auto.typewrite(pas)
	sleep(2)
	auto.moveTo(410, 503, duration=0.25)
	auto.click(410, 503, clicks=1, button='left')
	sleep(1)


def runUntilExit():
	try:
		main()
	except:
		exit_condition = False
		while not exit_condition:
			print("An error occured")
			ec = input("Type (e) to exit or (r) to restart \n")
			if ec == "e":
				print("you typed", ec)
				exit_condition = True
			elif ec == "r":
				driver.close()
				print("Restarting program")
				# exit_condition = False  # unnecessary but for better understanding
			else:
				print("Command misunderstood")

if __name__ == '__main__':
	for i in range(1):
		runUntilExit()
		while True:
			pass
