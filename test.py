__author__ = 'MarX'

from CFObject import *
from CFMethods import *

# Methods not tested yet
TO_TEST = """
contest_list,
contest_standings,
contest_status,
problemset_recentStatus,
user_ratedList,
user_rating
"""

def main():
    testing = user_info(["otero1991", "jcg", "marX"])
    print(testing.url())
    data = testing.get()
    for i in data:
        print()
        for j, k in i.get_all():
            print(j, k)


if __name__ == "__main__":
    main()
    