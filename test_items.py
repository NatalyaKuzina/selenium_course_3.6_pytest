import time
from selenium.webdriver.common.by import By
 
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
 
def test_guest_should_see_button_for_add_to_basket(browser):
    browser.get(link)
    #time.sleep(30)
    button_name = browser.find_elements(By.CSS_SELECTOR, "button[class='btn btn-lg btn-primary btn-add-to-basket']")
    assert len(button_name) == 1, "button for add to basket not found on page"