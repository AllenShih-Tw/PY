from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="/Users/shijiaxiang/Desktop/Python/selenium/chromedriver")  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/');
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(2) # Let the user actually see something!
driver.quit()
driver.close()
