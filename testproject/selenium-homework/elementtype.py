from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/trickyelements.html")

    element1 = driver.find_element_by_id("element1")
    element2 = driver.find_element_by_id("element2")
    element3 = driver.find_element_by_id("element3")
    element4 = driver.find_element_by_id("element4")
    element5 = driver.find_element_by_id("element5")
    elements = [element1, element2, element3, element4, element5]
    print(elements)
    print(type(elements))

    for button in elements:
        if button == driver.find_element_by_css_selector("button"):
            button.click()
            result = driver.find_element_by_id("result")
            print(result.text)

            assert (result.text == f"{button.text} was clicked")
finally:
    driver.close()
