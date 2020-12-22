import time


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_to_basket_button(browser):
    button = None
    try:
        browser.get(link)
        # time.sleep(10)  # 10 секунд на проверку надписи вполне достаточно

        button = browser.find_element_by_css_selector('.btn-add-to-basket')
    finally:
        assert button is not None, 'There is on "Add to basket" button on this page!'
