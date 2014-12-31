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

INFO = {"handle":"DmitriyH","firstName":"Dmitriy","lastName":"Khodyrev","country":"Russia","city":"Moscow","organization":"KL","contribution":135,"rank":"master","rating":1941,"maxRank":"master","maxRating":1947,"lastOnlineTimeSeconds":1420021608,"registrationTimeSeconds":1268570311}

def main():
    user = CFUser()
    user.load(INFO)
    for i, j in user.get_all():
        print(i, j)

    print(user.dumps())
    print(str(user.dumps()))

if __name__ == "__main__":
    main()
    