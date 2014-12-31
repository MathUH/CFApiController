__author__ = 'MarX'

from CFObject import *
import urllib.request
import json

def class_name(t):
    name = str(type(t))[8: -2]
    name = name.split('.')[-1]
    name = name.replace('_', '.')
    return name

URL_PREFIX = "http://codeforces.com/api/"
# URL_PREFIX = ""

def mystr(s):
    ans = ""
    if (isinstance(s,list)):
        # LIST TYPE
        for i in range(len(s)):
            ans += s[i]
            if (i + 1 != len(s)):
                ans += ";"
    else:
        ans = str(s)

    return ans

class CFAbstractMethod:
    def __init__(self, **kargs):
        self.params = kargs

    def url(self):
        url =  URL_PREFIX + class_name(self)
        start = True

        for i in self.params:

            if (self.params[i] == None):
                continue

            if start:
                start = False
                url += '?'
            else:
                url += '&'

            url += "%s=%s"%(str(i), mystr(self.params[i]))

        return url

    def data(self):
        f = urllib.request.urlopen( self.url() )
        ans = f.read()
        f.close()
        return ans.decode()

    def data1(self):
        return '{"status":"OK","result":[{"handle":"marX","firstName":"Marcelo","lastName":"Fornet","country":"Cuba","city":"Havana City","organization":"Havana University","contribution":0,"rank":"candidate master","rating":1816,"maxRank":"master","maxRating":2006,"lastOnlineTimeSeconds":1419894432,"registrationTimeSeconds":1394451183},{"handle":"jcg","firstName":"José Carlos","lastName":"Gutiérrez","country":"Cuba","city":"Havana","organization":"Havana University","contribution":0,"rank":"expert","rating":1603,"maxRank":"expert","maxRating":1684,"lastOnlineTimeSeconds":1419272399,"registrationTimeSeconds":1322853953}]}'

    def take(self):
        my_data = json.loads(self.data())

        if (my_data["status"] == "OK"):
            return (True, my_data["result"])
        else:
            return (False, my_data["comment"])

    def get(self):
        status, ans = self.take()
        if (status):
            return ans
        else:
            print("FAILED")
            return ans

class contest_hacks(CFAbstractMethod):
    """
    Returns list of hacks in the specified contests. Full information about hacks is available only after some time after the contest end. During the contest user can see only own hacks.
    contestId    Id of the contest. It is not the round number. It can be seen in contest URL. For example: /contest/374/status
    Return value: Returns a list of Hack objects.
    Example: http://codeforces.com/api/contest.hacks?contestId=374
    """

    def __init__(self, contestId):
        params = {"contestId":contestId}
        super().__init__(**params)

    def get(self):
        status, ans = self.take()
        if status:
            return [CFHack(i) for i in ans]
        else:
            print(ans)


class contest_list(CFAbstractMethod):
    """
    Returns information about all available contests.
    gym    Boolean. If true — than gym contests are returned. Otherwide, regular contests are returned.
    Return value: Returns a list of Contest objects. If this method is called not anonymously, then all available contests for a calling user will be returned too, including mashups and private gyms.
    Example: http://codeforces.com/api/contest.list?gym=true
    """

    def __init__(self, gym = None):
        params = {"gym":gym}
        super().__init__(**params)

    def get(self):
        status, ans = self.take()
        if status:
            return [CFContest(i) for i in ans]
        else:
            print(ans)


class contest_standings(CFAbstractMethod):
    """
    Returns the description of the contest and the requested part of the standings.
    contestId         Id of the contest. It is not the round number. It can be seen in contest URL. For example: /contest/374/status
    From              1-based index of the standings row to start the ranklist.
    count             Number of standing rows to return.
    handles           Semicolon-separated list of handles. No more than 10000 handles is accepted.
    room              If specified, than only participants from this room will be shown in the result. If not — all the participants will be shown.
    showUnofficial    If true than all participants (virtual, out of competition) are shown. Otherwise, only official contestants are shown.
    Return value: Returns object with three fields: "contest", "problems" and "rows". Field "contest" contains a Contest object. Field "problems" contains a list of Problem objects. Field "rows" contains a list of RanklistRow objects.
    Example: http://codeforces.com/api/contest.standings?contestId=374&from=1&count=5&showUnofficial=true
    """

    def __init__(self, contestId, From = None, count = None, handles = None, room = None, showUnofficial = None):
        params = {"contestId":contestId, "from":From, "count":count, "handles":handles, "room":room, "showUnofficial":showUnofficial}
        super().__init__(**params)

    def get(self):
        status, ans = self.take()
        if status:
            contest = ans["contest"]
            problems = ans["problems"]
            rows = [CFRanklistRow(i) for i in ans["rows"]]
            return (contest, problems, rows)
        else:
            print(ans)


class contest_status(CFAbstractMethod):
    """
    Returns submissions for specified contest. Optionally can return submissions of specified user.
    contestId    Id of the contest. It is not the round number. It can be seen in contest URL. For example: /contest/374/status
    handle       Codeforces user handle.
    From         1-based index of the first submission to return.
    count        Number of returned submissions.
    Return value: Returns a list of Submission objects, sorted in decreasing order of submission id.
    Example: http://codeforces.com/api/contest.status?contestId=374&from=1&count=10
    """

    def __init__(self, contestId, handle = None, From = None, count = None):
        params = {"contestId":contestId, "handle":handle, "from":From, "count":count}
        super().__init__(**params)

    def get(self):
        status, ans = self.take()
        if status:
            return [CFSubmission(i) for i in ans]
        else:
            print(ans)


class problemset_problems(CFAbstractMethod):
    """
    Returns all problems from problemset. Problems can be filtered by tags.
    tags    Semicilon-separated list of tags.
    Return value: Returns two lists. List of Problem objects and list of ProblemStatistics objects.
    Example: http://codeforces.com/api/problemset.problems?tags=implementation
    """

    def __init__(self, tags = None):
        params = {"tags":tags}
        super().__init__(**params)

    def get(self):
        status, ans = self.take()
        if status:
            return ans
        else:
            print(ans)


class problemset_recentStatus(CFAbstractMethod):
    """
    Returns recent submissions.
    count    Number of submissions to return. Can be up to 1000.
    Return value: Returns a list of Submission objects, sorted in decreasing order of submission id.
    Example: http://codeforces.com/api/problemset.recentStatus?count=10
    """

    def __init__(self, count):
        params = {"count":count}
        super().__init__(**params)

    def get(self):
        status, ans = self.take()
        if status:
            return [CFSubmission(i) for i in ans]
        else:
            print(ans)


class user_info(CFAbstractMethod):
    """
    Returns information about one or several users.
    handles    Semicolon-separated list of handles. No more than 10000 handles is accepted.
    Return value: Returns a list of User objects for requested handles.
    Example: http://codeforces.com/api/user.info?handles=DmitriyH;Fefer_Ivan
    """

    def __init__(self, handles):
        params = {"handles":handles}
        super().__init__(**params)

    def get(self):
        status, ans = self.take()
        if status:
            return [CFUser(i) for i in ans]
        else:
            print(ans)


class user_ratedList(CFAbstractMethod):
    """
    Returns the list of all rated users.
    activeOnly    Boolean. If true then only users, who participated in rated contest during the last month are returned. Otherwise, all users with at least one rated contest are returned.
    Return value: Returns a list of User objects, sorted in decreasing order of rating.
    Example: http://codeforces.com/api/user.ratedList?activeOnly=true
    """

    def __init__(self, activeOnly = None):
        params = {"activeOnly":activeOnly}
        super().__init__(**params)

    def get(self):
        status, ans = self.take()
        if status:
            return [CFUser(i) for i in ans]
        else:
            print(ans)


class user_rating(CFAbstractMethod):
    """
    Returns rating history of the specified user.
    handle    Codeforces user handle.
    Return value: Returns a list of RatingChange objects for requested user.
    Example: http://codeforces.com/api/user.rating?handle=Fefer_Ivan
    """

    def __init__(self, handle):
        params = {"handle":handle}
        super().__init__(**params)

    def get(self):
        status, ans = self.take()
        if status:
            return [CFRatingChange(i) for i in ans]
        else:
            print(ans)


class user_status(CFAbstractMethod):
    """
    Returns submissions of specified user.
    handle    Codeforces user handle.
    From      1-based index of the first submission to return.
    count     Number of returned submissions.
    Return value: Returns a list of Submission objects, sorted in decreasing order of submission id.
    Example: http://codeforces.com/api/user.status?handle=Fefer_Ivan&from=1&count=10
    """

    def __init__(self, handle, From = None, count = None):
        params = {"handle":handle, "from":From, "count":count}
        super().__init__(**params)

    def get(self):
        status, ans = self.take()
        if status:
            return [CFSubmission(i) for i in ans]
        else:
            print(ans)

CFMethodList = [contest_hacks,
                contest_list,
                contest_standings,
                contest_status,
                problemset_problems,
                problemset_recentStatus,
                user_info,
                user_ratedList,
                user_rating,
                user_status
]