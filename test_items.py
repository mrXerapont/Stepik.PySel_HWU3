import time
from selenium import webdriver


def test_add_to_card_btn_shld_exst(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.implicitly_wait(10)

    browser.get(link)

#    btn = browser.find_element_by_css_selector("#add_to_basket_form .btn-add-to-baske")
    print (browser.find_element_by_css_selector("#add_to_basket_form .btn-add-to-basket").size)
    #time.sleep(10)
    #assert ???, "Error! 'Add to basket' button not found!"