import time
from selenium.common.exceptions import NoSuchElementException


def test_add_to_card_btn_should_exist(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.implicitly_wait(10)
    browser.get(link)
    time.sleep(30)

    # Не знаю какой вариант оставить, оставлю этот тут для себя
    # btn_pre = browser.find_elements_by_css_selector("#add_to_basket_form .btn-add-to-basket")

    try:
        browser.find_element_by_css_selector("#add_to_basket_form .btn-add-to-basket")
        btn_present = True
    except NoSuchElementException:
        btn_present = False

    assert btn_present, "Error! 'Add to basket' button not found!"
    # assert len(btn_pre) > 0, "Error! 'Add to basket' button not found!"
