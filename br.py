from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import os
import sys

def main(password):
  options = Options()
  options.add_argument("--headless")
  browser = webdriver.Firefox(firefox_options=options)
  url = "http://admin:%s@10.11.12.1/ADV_home2.htm" % password
  browser.get(url) #navigate to the page
  browser.find_element_by_id("reboot").click()
  time.sleep(2)
  browser.switch_to_alert().accept();
  time.sleep(5)
  os.system("/usr/bin/sudo /sbin/ip route del 0/0")
  time.sleep(90)
  browser.quit()

if __name__ == '__main__':
  # 60 seconds to allow setting up network on reboot
  time.sleep(60)
  while True:
    main(sys.argv[1])
    time.sleep(60*60) # 1 hour
