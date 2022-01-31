import time

from selenium.webdriver.remote.webdriver import WebDriver
from typing import List

class BookingFiltration():
    def __init__(self, driver:WebDriver):
        self.driver = driver

    # * add many args to parameter
    def apply_star_rating(self, *star_values):
        star_filter_box = self.driver.find_element_by_css_selector('div[data-filters-group="class"]')
        star_child_elements = star_filter_box.find_elements_by_css_selector('*')

        for star_value in star_values:
            for star_element in star_child_elements:
                if(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars':
                    star_element.click()
                    time.sleep(1)

    def sort_by_lowest_price(self):
        element = self.driver.find_element_by_css_selector('li[data-id="price"]')
        element.click()