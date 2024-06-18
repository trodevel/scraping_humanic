#!/usr/bin/python3

'''
Test 01.

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

from scraping_helpers import helpers  # does_xpath_exist_with_timeout
from print_helpers.helpers import print_fatal, print_info, set_log_level, INFO
from scraping_humanic.scraping_humanic import wheel_around_xpath

import config         # DRIVER_PATH
from test_01_xpath import URL, BANNER, PATH

##########################################################


def test_01():

    wait_min = 1

    driver = helpers.init_driver( config.DRIVER_PATH, config.BROWSER_BINARY )

    driver.get( URL )

    banner = helpers.find_element_by_xpath_with_timeout( driver, BANNER, 5 )

    if not banner:
        print_fatal( "cannot find banner" )
        exit()

    print_info( "found banner, clicking" )

    helpers.wait_till_clickable_and_click( banner, 5 )

    if not helpers.does_xpath_exist_with_timeout(driver, PATH, 10):
        print_fatal( "broken xpath" )
        exit()

    print_info( "found xpath, rotating" )

    wheel_around_xpath( driver, PATH, 100 )

    print_info( "done" )

##########################################################

def main():

    set_log_level( INFO )
    test_01()

##########################################################

if __name__ == "__main__":
   main()

##########################################################
