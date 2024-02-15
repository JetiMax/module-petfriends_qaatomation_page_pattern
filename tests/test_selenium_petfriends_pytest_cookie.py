from pages.base import wait_for_animation, wait_for_ajax_loading
from pages.petfriends import MainPage

def test_petfriends(web_driver):
    """ Authorize to Petfriends via cookies and create a screenshot when the login page is successful. """

    page = MainPage(web_driver)
    page.scroll_down()
    page.go_to_all_pets_page()  # Перейдите на страницу всех домашних животных после добавления файлов cookie.
    # Make the screenshot of browser window:
    page._web_driver.save_screenshot('petfriends.png')

    # Close the web driver
    web_driver.quit()


def test_petfriends_js(web_driver):
    """ Authorize to Petfriends via cookies and create a screenshot when the login page is successful. """

    page = MainPage(web_driver)
    page.scroll_down()
    page.go_to_all_pets_page()

    # Используем BasePage для ожидания анимации и ajax загрузки
    wait_for_animation(web_driver, '.text-center.align-self-center.align-middle')  # Замените 'your_selector_for_animation' на ваш селектор
    wait_for_ajax_loading(web_driver, 'task2 fill')  # Замените 'your_class_name_for_ajax_loading' на ваш класс

    # Создаем скриншот окна браузера:
    page._web_driver.save_screenshot('petfriends.png')

    # Закрываем веб-драйвер
    web_driver.quit()
