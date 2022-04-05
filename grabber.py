import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib

os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome()
driver.get("https://enrollmentconnect.umich.edu/portal/campus_day_lsa")
driver.implicitly_wait(10)


dateList = [8, 11, 16, 18]
# can be any number i just ran this so that it would find only LSA dates


recipient = "" # my email address
message = "https://enrollmentconnect.umich.edu/portal/campus_day_lsa "


def SendEmail(recipient , message):
    server = smtplib.SMTP("smtp.gmail.com" , 587)
    server.ehlo()
    server.starttls()
    server.login("mail@mail.com" , "password")  
    server.sendmail("mail@mail.com" , recipient , message)
    server.close() 


def tour():
	for number in dateList:

		rgb = driver.find_element_by_xpath('//*[@id="register_datepicker"]/div/table/tbody//a[.=' + str(number) + ']/parent::*').value_of_css_property('background-color')

		if (rgb == "rgba(134, 199, 67, 1)"):
			SendEmail(recipient , message + str(number))   
			return("green")
		else:
			time.sleep(10)

	time.sleep(60)
	tour()

tour()