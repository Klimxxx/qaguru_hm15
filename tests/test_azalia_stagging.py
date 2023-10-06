from selene import have, browser
from selene.support.shared import browser


# 1. проверить что избранное пустое
def test_check_empty_favorites():
    browser.open('')
    browser.element('[data-testid="banner-mobile-app-close"]').click()  # close advertisment
    browser.all('[data-testid="favorites"]')[1].click()  # TODO NATALIE FILTER VISIBLE
    browser.element('[class^="Favorites_empty__title__"]').should(have.exact_text('Здесь пока пусто'))

# 2. проверить что есть 2 города на главной странице
def test_check_2_cities():
    browser.open('https://staging.azalianow.shop/')
    browser.element('[data-testid="banner-mobile-app-close"]').click()  # close advertisment
    browser.element('[data-testid="geo-toggler"]').click()  #click listbox cities
    browser.all('[data-testid="geo-item"]')[0].should(have.text('Москва и Московская область'))
    browser.all('[data-testid="geo-item"]')[1].should(have.text('Нижний Новгород и Нижегородская область'))

# 3. проверить что корзина пустая
def test_check_bin():
    browser.open('https://staging.azalianow.shop/')
    browser.element('[data-testid="banner-mobile-app-close"]').click()  # close advertisment
    browser.all('[data-testid="checkout"]')[1].click()  # click bin
    browser.element('[class^="Favorites_empty__title__"]').should(have.text('В корзине пусто'))

# 4. проверить что пользователь на авторизован
def test_check_user_not_authorised():
    browser.open('')
    browser.element('[data-testid="banner-mobile-app-close"]').click()  # close advertisment
    browser.all('[data-testid="open-login-modal"]')[1].should(have.text('Войти'))

# 5. проверить что поиск работает
def test_check_search_rozi():
    browser.open('')
    browser.element('[data-testid="banner-mobile-app-close"]').click()  # close advertisment
    browser.element('[inputmode="search"]').type("Розы").press_enter()
    browser.element('[class^="SearchCatalog_title__').should(have.text('розы'))
    browser.all('[class^="ProductCard_name__"]')[1].should(have.text("роз"))

# 6. добавить товар в корзину и проверить что он добавлен
def test_add_to_bin():
    browser.open('')
    browser.element('[data-testid="banner-mobile-app-close"]').click()  # close advertisment
    browser.all('[class^="ProductCard_cartButton__"]')[0].click()
    browser.all('[class ^="ProductsListItem_wrapper__"]')[0].should(have.text('1'))




