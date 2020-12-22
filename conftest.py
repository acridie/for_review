import pytest
from selenium import webdriver


# функция-обработчик опции командной строки
def pytest_addoption(parser):
    # добавили опцию browser_name в командную строку (по умолчанию chrome)
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose browser: chrome or firefox')
    # добавили опцию language в командную строку (по умолчанию ru)
    parser.addoption('--language', action='store', default='ru',
                     help='Choose browser language')


# фикстура запуска и закрытия браузера
@pytest.fixture(scope='function')
def browser(request):
    # запрашиваем значение параметра (тип браузера) переданного в cmd
    browser_name = request.config.getoption('browser_name')
    # заправшиваем значение параметра (язык) переданного в cmd
    user_language = request.config.getoption('language')
    if browser_name == 'chrome':
        print('\n initializing Chrome browser...')
        options = webdriver.ChromeOptions()
        # опция, которая убирает всякую дичь, типа DevTools из консоли при запуске теста
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # опция, которая передает в хидер "accept_languages" язык браузера (можно через запятую)
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        print('\n initializing Firefox browser...')
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    browser.set_window_size(1920, 1080)
    browser.implicitly_wait(10)
    yield browser
    print('\n closing browser...')
    browser.quit()
