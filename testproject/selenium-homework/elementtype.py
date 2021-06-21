from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost:9999/trickyelements.html")

product = driver.find_element_by_id("product")
product.send_keys()
quantity = driver.find_element_by_id("quantity")
quantity.send_keys()
price = driver.find_element_by_id()
price.send_keys()

add_button = driver.find_element_by_id("add")
add_button.click()