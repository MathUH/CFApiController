__author__ = 'MarX'

from CFObject import *
from CFMethods import *

# Methods not tested yet
TO_TEST = """
contest_list,
contest_standings,
contest_status,
problemset_problems,
problemset_recentStatus,
user_info,
user_ratedList,
user_rating
"""

def main():
    testing = contest_hacks(200)
    data = testing.get()
    for i in data:
        print("CUR HACK")
        for j, t in i.get_all():
            print(j, t)


if __name__ == "__main__":
    main()
    