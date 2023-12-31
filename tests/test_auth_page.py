import pickle
import time
from pytest_html.extras import url
from selenium.webdriver.common.by import By


def test_petfriends(web_driver):
    """ Search some phrase in google and make a screenshot of the page. """

    # Open PetFriends base page:
    web_driver.get("https://petfriends.skillfactory.ru/")

    time.sleep(10)  # Just for demonstration purposes, do NOT repeat it on real projects!

    # Find the field for search text input:
    btn_newuser = web_driver.find_element(By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]")
    btn_newuser.click()

    btn_exist_acc = web_driver.find_element(By.LINK_TEXT, "У меня уже есть аккаунт")
    btn_exist_acc.click()

    field_email = web_driver.find_element(By.ID, "email")
    field_email.click()
    field_email.clear()
    field_email.send_keys("jetimax@yandex.ru")

    field_pass = web_driver.find_element(By.ID, "pass")
    field_pass.click()
    field_pass.clear()
    field_pass.send_keys("1725maksim")

    btn_submit = web_driver.find_element(By.XPATH, "//button[@type='submit']")
    btn_submit.click()

    assert web_driver.current_url == 'https://petfriends.skillfactory.ru/all_pets'


    # Save cookies of the browser after the login
    with open('my_cookies.pkl', 'wb') as cookies:
        pickle.dump(web_driver.get_cookies(), cookies, protocol=pickle.HIGHEST_PROTOCOL)

    # Make the screenshot of browser window:
    web_driver.save_screenshot('result_petfriends.png')


def test_petfriends1(web_driver):
    """Search some phrase in google and make a screenshot of the page."""

    # Open PetFriends base page:
    web_driver.get("https://petfriends.skillfactory.ru/")

    # Нажатие кнопки открывает новую вкладку
    # Получить текущий дескриптор окна (чтобы вернуться позже)
    main_window = web_driver.current_window_handle

    # Выполните действия, которые откроют здесь новую вкладку/окно
    # Переключиться на новую вкладку (при условии, что открыта вторая вкладка)
    web_driver.switch_to.window(web_driver.window_handles[1])

    # Подтверждение URL
    assert web_driver.current_url == 'https://petfriends.skillfactory.ru/all_pets'

    # Вернуться в главное окно
    web_driver.switch_to.window(main_window)