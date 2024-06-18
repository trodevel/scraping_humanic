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


def round_around_xpath(driver, xpath: str, radius: int, duration_sec: int = 2) -> None:

    assert radius > 0

    step_angle = 10

    delay = calc_delay(duration_sec, step_angle)

    # Get the element to start the movement from
    element = driver.find_element( 'xpath', xpath )

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

##########################################################
