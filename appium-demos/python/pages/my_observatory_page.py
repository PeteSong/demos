import time

from appium.webdriver.common.appiumby import AppiumBy

from .action_bot import ActionBot
from .date_utils import get_next_day_labels


class MyObservatoryPage:
    my_observatory_icon_by = (AppiumBy.ACCESSIBILITY_ID, "MyObservatory")

    my_observatory_title_by = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("MyObservatory")')

    navigate_up_by = (AppiumBy.ACCESSIBILITY_ID, "Navigate up")
    forecast_menu_item_by = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Forecast & Warning Services")')
    nine_day_forecast_menu_item_by = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("9-Day Forecast").instance(1)',
    )
    nine_day_forecast_list_view_by = (AppiumBy.ID, "hko.MyObservatory_v1_0:id/mainAppSevenDayView")
    # nine_day_forecast_list_view_items_by = (AppiumBy.CLASS_NAME, 'android.widget.LinearLayout')

    nine_day_forecast_list_view_scrollable_by_value = (
        'new UiScrollable(new UiSelector().resourceId("hko.MyObservatory_v1_0:id/mainAppSevenDayView"))'
    )
    nine_day_forecast_list_view_scrollable_by = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        nine_day_forecast_list_view_scrollable_by_value,
    )

    def build_one_day_forecast_list_item_by_value(self, day_label: str) -> str:
        return f'new UiSelector().className("android.widget.LinearLayout").descriptionStartsWith("{day_label}")'

    def build_one_day_forecast_list_item_by(self, day_label: str) -> tuple:
        return (
            AppiumBy.ANDROID_UIAUTOMATOR,
            self.build_one_day_forecast_list_item_by_value(day_label),
        )

    def build_scroll_to_item_in_nine_day_forecast_list_view(self, day_label: str) -> tuple:
        """
        Scroll to the element using the Android UIAutomator.
        """
        val = (
            f"{self.nine_day_forecast_list_view_scrollable_by_value}"
            f".scrollIntoView("
            f"{self.build_one_day_forecast_list_item_by_value(day_label)})"
        )
        return (AppiumBy.ANDROID_UIAUTOMATOR, val)

    def __init__(self, driver):
        self.driver = driver
        self.bot: ActionBot = ActionBot(driver)

    def launch(self):
        """
        Launch the app by clicking the app icon since the app is installed from the Play Store.
        There is no "appActivity" to launch directly.
        """
        self.bot.click(self.my_observatory_icon_by)
        time.sleep(5)

    def navigate_up(self):
        self.bot.click(self.navigate_up_by)

    def click_forecase_services_menu_item(self):
        self.bot.click(self.forecast_menu_item_by)

    def click_nine_day_forecast_menu_item(self):
        self.bot.click(self.nine_day_forecast_menu_item_by)

    def scroll_to_one_day_forecast_list_item(self, day_label: str):
        self.bot.element_located(self.build_scroll_to_item_in_nine_day_forecast_list_view(day_label))

    def get_nine_day_forecast_data(self):
        print("getting nine day forecast data ... \n")

        list_view = self.bot.element_located(self.nine_day_forecast_list_view_scrollable_by)
        item_descriptions = list()
        for day_label in get_next_day_labels():
            self.scroll_to_one_day_forecast_list_item(day_label)
            item_element = self.bot.element_located_in_element(
                list_view, self.build_one_day_forecast_list_item_by(day_label)
            )
            item_desc = item_element.get_attribute("contentDescription")
            item_descriptions.append(item_desc)
            print(item_desc)

        print()

        return item_descriptions
