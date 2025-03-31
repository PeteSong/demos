import time

from pages.my_observatory_page import MyObservatoryPage


def test_nine_day_forecast_data(appium_service, android_driver):
    driver = android_driver

    # KEYCODE_HOME
    driver.press_keycode(3)
    time.sleep(2)

    my_observatory_page = MyObservatoryPage(driver)
    my_observatory_page.launch()
    my_observatory_page.navigate_up()
    my_observatory_page.click_forecase_services_menu_item()
    my_observatory_page.click_nine_day_forecast_menu_item()
    forecast_data = my_observatory_page.get_nine_day_forecast_data()
    assert len(forecast_data) == 9
