#!/usr/bin/python3

'''
Test 03.

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
from time import sleep

from scraping_helpers import helpers  # does_xpath_exist_with_timeout
from print_helpers.helpers import print_fatal, print_info, set_log_level, INFO
from scraping_humanic.scraping_humanic import move_to_element

import config         # DRIVER_PATH
from test_03_xpath import URL, BUTTONS

##########################################################


def test_03():

    wait_min = 1

    driver = helpers.init_driver( config.DRIVER_PATH, config.BROWSER_BINARY )

    driver.get( URL )

    elems = helpers.find_elements_by_xpath_with_timeout( driver, BUTTONS, 5 )

    if len( elems ) != 3:
        print_fatal( f"cannot find 3 buttons, found {len( elems )} buttons" )
        exit()

    print_info( "found buttons, moving 1" )

    move_to_element(driver, elems[0])

    print_info( "found buttons, moving 2" )

    move_to_element(driver, elems[1])

    print_info( "found buttons, moving 3" )

    move_to_element(driver, elems[2])

    print_info( "done" )

##########################################################

def main():

    set_log_level( INFO )
    test_03()

##########################################################

if __name__ == "__main__":
   main()

##########################################################
