from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.kapucziner.hu")

div_id = driver.find_element_by_id("div id")
div_id.send_keys("nemlétezik")





