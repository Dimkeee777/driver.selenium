def test_search_example(driver):


    driver.get("https://www.google.com")

    search_input = driver.find_element('name', 'q')

    search_input.clear()
    search_input.send_keys('22222222222222222222222222')

    search_button = driver.find_element('name', 'btnK')
    search_button.submit()

    driver.save_screenshot('result.png')