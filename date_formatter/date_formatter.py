import numpy as np
import re

import pandas as pd
from datetime import datetime


class DateFormatter:

    def __init__(self, dt_, USE_FULL_MONTH_NAME, USE_HYPHEN_AS_SPACER, REGION_FORMAT):

        self.dt_: str = dt_
        self.USE_FULL_MONTH_NAME: bool = USE_FULL_MONTH_NAME
        self.USE_HYPHEN_AS_SPACER: bool = USE_HYPHEN_AS_SPACER
        self.REGION_FORMAT: str = None

    def dateFormat(dt_: str, USE_FULL_MONTH_NAME: bool, USE_HYPHEN_AS_SPACER: bool, REGION_FORMAT: str = None):

        def is_nan_true_or_false(x):
            return (x is np.nan or x != x)

        def test_for_existence_of_month_key(month_dict, name_key, month_digit_int):

            try:

                month_dict[name_key][month_digit_int]

                return True

            except:

                return False

        if not is_nan_true_or_false(REGION_FORMAT):

            if REGION_FORMAT == 'US':

                # format is "2018-18-12" ("YYYY-DD-MM")

                day_string_regex = r"([0-9]{2})\-[0-9]{2}\-[0-9]{4}"
                month_string_regex = r"[0-9]{2}\-([0-9]{2})\-[0-9]{4}"

            else:

                # format is "2018-12-18" "YYYY-MM-DD"

                month_string_regex = r"([0-9]{2})\-[0-9]{2}\-[0-9]{4}"
                day_string_regex = r"[0-9]{2}\-([0-9]{2})\-[0-9]{4}"

        else:

            # format is "2018-12-18" "YYYY-MM-DD"

            month_string_regex = r"([0-9]{2})\-[0-9]{2}\-[0-9]{4}"
            day_string_regex = r"[0-9]{2}\-([0-9]{2})\-[0-9]{4}"

        def check_for_correct_starting_string_format(regex_main, dt_):

            try:

                re.findall(regex_main, dt_)[0]

                return True

            except:

                return False

        # parameters:
        # dt_: pandas datetime object
        # USE_FULL_MONTH_NAME: BOOL: True | False: if True, uses the month's full name; if False, uses three letter abbreviation
        # USE_HYPHEN_AS_SPACER: BOOL: True | False: if True, uses '-' as spacer; if False uses " "
        # REGION_FORMAT: str: if "US", assumes format of "2018-18-12" ("YYYY-DD-MM"); if not or None, assumes format of "2018-12-18" ("YYYY-MM-DD")

        if is_nan_true_or_false(dt_) or len(str(dt_)) < 10:

            return dt_

        else:

            dt_ = str(dt_)

            if USE_FULL_MONTH_NAME:

                name_key = 1

            else:

                name_key = 0

            if USE_HYPHEN_AS_SPACER:

                SPACER = "-"

            else:

                SPACER = " "

            month_dict = {
                0: {
                    1: 'Jan',
                    2: 'Feb',
                    3: 'Mar',
                    4: 'Apr',
                    5: 'May',
                    6: 'Jun',
                    7: 'Jul',
                    8: 'Aug',
                    9: 'Sep',
                    10: 'Oct',
                    11: 'Nov',
                    12: 'Dec'
                },
                1: {
                    1: 'January',
                    2: 'February',
                    3: 'March',
                    4: 'April',
                    5: 'May',
                    6: 'June',
                    7: 'July',
                    8: 'August',
                    9: 'September',
                    10: 'October',
                    11: 'November',
                    12: 'December'
                },
            }

            # match pattern '2014-12-18' with regex

            regex_main = r"[0-9]{2}\-[0-9]{2}\-[0-9]{4}"

            if check_for_correct_starting_string_format(regex_main, dt_):

                main_date_string = re.findall(regex_main, dt_)[0]

            else:

                return dt_

            year_string_regex = r"[0-9]{2}\-[0-9]{2}\-([0-9]{4})"

            year_digit_int = int(re.findall(
                year_string_regex, main_date_string)[0])
            month_digit_int = int(re.findall(
                month_string_regex, main_date_string)[0])
            day_digit_int = int(re.findall(
                day_string_regex, main_date_string)[0])

            if USE_FULL_MONTH_NAME:

                YEAR_STRING = str(year_digit_int)

            else:

                YEAR_STRING = str(year_digit_int)[-2:]

            if test_for_existence_of_month_key(month_dict, name_key, month_digit_int):

                readableDateString = str(
                    day_digit_int) + SPACER + month_dict[name_key][month_digit_int] + SPACER + YEAR_STRING

                return readableDateString

            else:

                return dt_
