#!/usr/bin/python3

'''
Scraping Humanic.

Copyright (C) 2024 Dr. Sergey Kolevatov

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

'''

import math
from selenium.webdriver.common.action_chains import ActionChains

##########################################################

def calc_delay(duration_sec: int, step_angle: int ) -> float:

    assert duration_sec > 0
    assert step_angle > 0

    num_steps = int(360 / step_angle)
    delay = float( duration_sec / num_steps )
    return delay

##########################################################


def wheel_around_element(driver, element, radius: int, duration_sec: int = 2) -> None:

    assert radius > 0

    step_angle = 10

    delay = calc_delay(duration_sec, step_angle)

    # Create an Actions object
    actions = ActionChains(driver)

    # Define the center coordinates of the circle (relative to the element)
    center_x = element.location["x"] + element.size["width"] / 2
    center_y = element.location["y"] + element.size["height"] / 2

    # Simulate movement points around the circle
    for angle in range(0, 360, step_angle):  # Adjust angle step size for smoother motion
        # Calculate x and y coordinates for the current angle
        x_offset = radius * math.cos(math.radians(angle))
        y_offset = radius * math.sin(math.radians(angle))

        # Move to the calculated point relative to the center
        actions.move_to_element_with_offset(element, int(x_offset), int(y_offset))

        # Add a short pause to simulate human-like movement (optional)
        actions.pause(delay)  # Adjust pause duration as needed

    # Perform the built actions
    actions.perform()

"""
Performs a wheel movement around an element specified by the given XPath.

Args:
    driver (WebDriver): The WebDriver instance used to interact with the browser.
    xpath (str): The XPath expression to locate the element.
    radius (int): The radius of the circle to move around.
    duration_sec (int, optional): The duration of the wheel movement in seconds. Defaults to 2.

Returns:
    None: This function does not return anything.

Raises:
    NoSuchElementException: If the element specified by the XPath cannot be found.

"""
def wheel_around_xpath(driver, xpath: str, radius: int, duration_sec: int = 2) -> None:

    # Get the element to start the movement from
    element = driver.find_element( 'xpath', xpath )

    wheel_around_element( driver, element, radius, duration_sec )


def move_to_element(driver, element, duration_sec: int = 1) -> None:

    # Create an Actions object
    actions = ActionChains(driver)

    # Build the action: move from start element to end element
    actions. \
        pause(duration_sec).\
        move_to_element(element).\
        perform()


def move_to_xpath(driver, xpath: str, duration_sec: int = 1) -> None:

    # Get the element to start the movement from
    element = driver.find_element( 'xpath', xpath )

    move_to_element( driver, element, duration_sec )


def move_from_element_to_element(driver, element_from, element_to , duration_sec: int = 1) -> None:

    # Create an Actions object
    actions = ActionChains(driver)

    # Build the action: move from start element to end element
    actions.move_to_element(element_from).\
        pause(duration_sec).\
        move_to_element(element_to).\
        perform()


def move_from_xpath_to_xpath(driver, xpath_from: str, xpath_to: str , duration_sec: int = 1) -> None:

    # Get the element to start the movement from
    element_from    = driver.find_element( 'xpath', xpath_from )
    element_to      = driver.find_element( 'xpath', xpath_to )

    move_from_xpath_to_xpath( driver, element_from, element_to , duration_sec )


##########################################################
