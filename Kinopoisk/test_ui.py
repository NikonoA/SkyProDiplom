from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import allure


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(50)
    yield driver
    driver.quit()


@allure.id("UI-1")
@allure.title("Проверка поиска фильма с корректным названием")
def test_ui_search_by_name(driver):
    with allure.step("UI.Открыть сайт"):
        driver.get("https://www.kinopoisk.ru/")
    with allure.step("UI.Ввести название фильма"):
        driver.find_element(By.NAME, "kp_query").send_keys("Гарри Поттер")
    assert driver.find_element(By.ID, "suggest-item-film-689").is_displayed()


@allure.id("UI-2")
@allure.title("Проверка поиска фильма по фильтрам")
def test_ui_search_with_filters(driver):
    with allure.step("UI.Открыть сайт"):
        driver.get("https://www.kinopoisk.ru/")
    with allure.step("UI.Зайти в фильтр и указать значение для поиска"):
        driver.find_element(By.CSS_SELECTOR,
                            ".styles_advancedSearch__uwvnd").click()
        driver.find_element(By.CSS_SELECTOR,
                            "#find_film").send_keys("Благословение")
    with allure.step("UI.Нажать поиск"):
        driver.find_element(By.CSS_SELECTOR, ".el_18.submit."
                            "nice_button").click()
    assert driver.find_element(By.CSS_SELECTOR, "a[href='/film/"
                               "2043475/sr/1/']").is_displayed()


@allure.id("UI-3")
@allure.title("Проверка поиска рандомного фильма")
def test_ui_random_film(driver):
    with allure.step("UI.Открыть сайт"):
        driver.get("https://www.kinopoisk.ru/")
    with allure.step("UI.Нажать на поиск рандомного фильма"):
        driver.find_element(By.CSS_SELECTOR,
                            "button.styles_root__CUh_v."
                            "styles_submit__2AIpj").click()
    with allure.step("UI.Ввести Критерии для подбора"):
        driver.find_element(By.CSS_SELECTOR, "#genreListTitle").click()
        driver.find_element(By.CSS_SELECTOR, ".genre_1750.selectItem").click()
        driver.find_element(By.CSS_SELECTOR, "#genreListTitle").click()
    wait1 = WebDriverWait(driver, 15)
    wait1.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".button"))
            )
    with allure.step("UI.Нажать поиск"):
        driver.find_element(By.CSS_SELECTOR, ".button").click()
    assert driver.find_element(By.CSS_SELECTOR, ".right").is_displayed()


@allure.id("UI-4")
@allure.title("Проверка поиска фильма в подборке")
def test_ui_the_list_of_films(driver):
    with allure.step("UI.Открыть сайт"):
        driver.get("https://www.kinopoisk.ru/")
    with allure.step("UI.Нажать на подборку 250 лучших фильмов"):
        driver.find_element(By.CSS_SELECTOR, 'a.styles_root__7mPJN.'
                            'styles_lightThemeItem__BSbZW'
                            '[href="/lists/categories/movies/1/"]').click()
        driver.find_element(By.XPATH, '//span[contains(text(),'
                            '"250 лучших фильмов")]').click()
    with allure.step("UI.Найти фильм на странице"):
        driver.find_element(By.XPATH, '//div[@data-tid="173d6058"]'
                            '/a[last()]').click()
    assert driver.find_element(By.XPATH, '//span[contains(text(),'
                               '"Достать ножи")]').is_displayed()


@allure.id("UI-5")
@allure.title("Проверка поиска фильма "
              "с некорректным названием")
def test_ui_search_by__wrong_name(driver):
    with allure.step("UI.Открыть сайт"):
        driver.get("https://www.kinopoisk.ru/")
    with allure.step("UI.Ввести ошибочное назввание "
                     "(набор букв или символов)"):
        fall = driver.find_element(By.NAME, "kp_query")
        fall.send_keys("ППППППППППППППППППППППП")
        fall.send_keys(Keys.RETURN)
    assert driver.find_element(By.CSS_SELECTOR, "h2."
                               "textorangebig").is_displayed()
