import allure
from selene import have, browser, be


@allure.title("Проверка что избранное пустое изначально")
def test_check_empty_favorites():
    with allure.step("Открываем браузер"):
        browser.open('')
    with allure.step("Закрываем рекламу"):
        browser.element('[data-testid="banner-mobile-app-close"]').click()
    with allure.step("Открываем избранное"):
        browser.all('[data-testid="favorites"]').filtered_by(be.visible).first.click()
    with allure.step("Проверяем что в избранном нет товаров"):
        browser.element('[class^="Favorites_empty__title__"]').should(have.exact_text('Здесь пока пусто'))


@allure.title("Проверка что есть 2 города на главной странице")
def test_check_2_cities():
    with allure.step("Открываем браузер"):
        browser.open('')
    with allure.step("Закрываем рекламу"):
        browser.element('[data-testid="banner-mobile-app-close"]').click()
    with allure.step("Нажимаем на листбокс городов"):
        browser.all('[data-testid="geo-toggler"]').filtered_by(be.visible).first.click()
    with allure.step("Проверка что в листбоксе есть Москва и обл."):
        browser.all('[data-testid="geo-item"]').filtered_by(be.visible).first.should(
        have.text('Москва и Московская область'))
    with allure.step("Проверка что в листбоксе есть Нижний Новгород и обл."):
        browser.all('[data-testid="geo-item"]').filtered_by(be.visible).second.should(
        have.text('Нижний Новгород и Нижегородская область'))


@allure.title("Проверка что корзина изначально пустая")
def test_check_bin():
    with allure.step("Открываем браузер"):
        browser.open('')
    with allure.step("Закрываем рекламу"):
        browser.element('[data-testid="banner-mobile-app-close"]').click()
    with allure.step("Открываем корзину"):
        browser.all('[data-testid="checkout"]').filtered_by(be.visible).first.click()
    with allure.step("Проверяем что в корзине пусто"):
        browser.element('[class^="Favorites_empty__title__"]').should(have.text('В корзине пусто'))


@allure.title("Проверка что пользователь изначально не авторизован")
def test_check_user_not_authorised():
    with allure.step("Открываем браузер"):
        browser.open('')
    with allure.step("Закрываем рекламу"):
        browser.element('[data-testid="banner-mobile-app-close"]').click()
    with allure.step("Нажать на кнопку войти на главной странице"):
        browser.all('[data-testid="open-login-modal"]')[0].click()
    with allure.step("Проверка что в окне появился текст 'Введите телефон, чтобы войти'"):
        browser.element('[class^="login-modal_title__"]').should(have.text('Введите телефон, чтобы войти'))


@allure.title("Проверка что поиск работает и ищет")
def test_check_search_rozi():
    with allure.step("Открываем браузер"):
        browser.open('')
    with allure.step("Закрываем рекламу"):
        browser.element('[data-testid="banner-mobile-app-close"]').click()
    with allure.step("В поиске вводим текст Розы"):
        browser.element('[inputmode="search"]').type("Розы").press_enter()
    with allure.step("Проверяем что открывается страница с результатами Розы"):
        browser.element('[class^="SearchCatalog_title__').should(have.text('розы'))


@allure.title("Добавление любого товара в корзину и проверка что он добавлен")
def test_add_to_bin():
    with allure.step("Открываем браузер"):
        browser.open('')
    with allure.step("Закрываем рекламу"):
        browser.element('[data-testid="banner-mobile-app-close"]').click()
    with allure.step("Добавляем товар с главной страницы в корзину"):
        browser.all('[class^="ProductCard_cartButton__"]')[0].click()
    with allure.step("Проверяем что только 1 товар добавлен в корзину"):
        browser.all('[class ^="ProductsListItem_wrapper__"]')[0].should(have.text('1'))
