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

import config         # DRIVER_PATH

##########################################################


def test_01():

    wait_min = 1

    driver = helpers.init_driver( config.DRIVER_PATH, config.BROWSER_BINARY )

    driver.get( "https://www.google.de" )

    helpers.sleep( wait_min * 60 )

##########################################################

def main():

    test_01()

##########################################################

if __name__ == "__main__":
   main()

##########################################################
