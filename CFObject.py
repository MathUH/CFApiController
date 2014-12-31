__author__ = 'MarX'

import json

class CFObject:
    attr = ""
    def __init__(self, s = None):
        self.attrs = self.attr.split(',')
        for i in self.attrs:
            self.__setattr__(i, None)

        if (s != None):
            self.load(s)

    def get_all(self):
        for i in self.attrs:
            cur = self.__getattribute__(i)
            if (cur == None):
                continue
            yield (i, cur)

    def dumps(self):
        data = {}
        for i, j in self.get_all():
            data.update( {i : j} )
        return json.dumps(data)

    def load(self, s):
        """ Load object from dictionary
        """
        for i in s:
            self.__setattr__(i, s[i])

    def loads(self, data):
        """ Load object from json
        """
        self.__init__()
        data_p = json.loads(data)
        self.load(data_p)


class CFUser(CFObject):
    attr = "handle,email,vkId,openId,firstName,lastName,country,city,organization,contribution,rank,rating,maxRank,maxRating,lastOnlineTimeSeconds,registrationTimeSeconds"
    __doc__ = """
-----------------------------
Represents a Codeforces user.
-----------------------------
handle                     String. Codeforces user handle.
email                      String. Shown only if user allowed to share his contact info.
vkId                       String. User id for VK social network. Shown only if user allowed to share his contact info.
openId                     String. Shown only if user allowed to share his contact info.
firstName                  String. Localized. Can be absent.
lastName                   String. Localized. Can be absent.
country                    String. Localized. Can be absent.
city                       String. Localized. Can be absent.
organization               String. Localized. Can be absent.
contribution               Integer. User contribution.
rank                       String. Localized.
rating                     Integer.
maxRank                    String. Localized.
maxRating                  Integer.
lastOnlineTimeSeconds      Integer. Time, when user was last seen online, in unix format.
registrationTimeSeconds    Integer. Time, when user was registered, in unix format.
"""

class CFRatingChange(CFObject):
    attr = "contestId,contestName,rank,ratingUpdateTimeSeconds,oldRating,newRating"
    __doc__ = """
----------------------------------------------------
Represents a participation of user in rated contest.
----------------------------------------------------
contestId                  Integer.
contestName                String. Localized.
rank                       Integer. Place of the user in the contest. This field contains user rank on the moment of rating update. If afterwards rank changes (e.g. someone get disqualified), this field will not be update and will contain old rank.
ratingUpdateTimeSeconds    Integer. Time, when rating for the contest was update, in unix-format.
oldRating                  Integer. User rating before the contest.
newRating                  Integer. User rating after the contest.
"""

class CFContest(CFObject):
    attr = "id,name,type,phase,frozen,durationSeconds,startTimeSeconds,relativeTimeSeconds,preparedBy,websiteUrl,description,difficulty,kind,icpcRegion,country,city,season"
    __doc__ = """
-----------------------------------
Represents a contest on Codeforces.
-----------------------------------
id                     Integer.
name                   String. Localized.
type                   Enum: CF, IOI, ICPC. Scoring system used for the contest.
phase                  Enum: BEFORE, CODING, PENDING_SYSTEM_TEST, SYSTEM_TEST, FINISHED.
frozen                 Boolean. If true, then the ranklist for the contest is frozen and shows only submissions, created before freeze.
durationSeconds        Integer. Duration of the contest in seconds.
startTimeSeconds       Integer. Can be absent. Contest start time in unix format.
relativeTimeSeconds    Integer. Can be absent. Number of seconds, passed after the start of the contest. Can be negative.
preparedBy             String. Can be absent. Handle of the user, how created the contest.
websiteUrl             String. Can be absent. URL for contest-related website.
description            String. Localized. Can be absent.
difficulty             Integer. Can be absent. From 1 to 5. Larger number means more difficult problems.
kind                   String. Localized. Can be absent. Human-readable type of the contest from the following categories: Official ACM-ICPC Contest, Official School Contest, Opencup Contest, School/University/City/Region Championship, Training Camp Contest, Official International Personal Contest, Training Contest.
icpcRegion             String. Localized. Can be absent. Name of the ICPC Region for official ACM-ICPC contests.
country                String. Localized. Can be absent.
city                   String. Localized. Can be absent.
season                 String. Can be absent.
"""

class CFParty(CFObject):
    attr = "contestId,members,participantType,teamId,teamName,ghost,room,startTimeSeconds"
    __doc__ = """
-----------------------------------------------
Represents a party, participating in a contest.
-----------------------------------------------
contestId           Integer. Id of the contest, in which party is participating.
members             List of Member objects. Members of the party.
participantType     Enum: CONTESTANT, PRACTICE, VIRTUAL, MANAGER, OUT_OF_COMPETITION.
teamId              Integer. Can be absent. If party is a team, then it is a unique team id. Otherwise, this field is absent.
teamName            String. Localized. Can be absent. If party is a team or ghost, then it is a localized name of the team. Otherwise, it is absent.
ghost               Boolean. If true then this party is a ghost. It participated in the contest, but not on Codeforces. For example, Andrew Stankevich Contests in Gym has ghosts of the participants from Petrozavodsk Training Camp.
room                Integer. Can be absent. Room of the party. If absent, then the party has no room.
startTimeSeconds    Integer. Can be absent. Time, when this party started a contest.
"""

class CFMember(CFObject):
    attr = "handle"
    __doc__ = """
-------------------------------
Represents a member of a party.
-------------------------------
handle    String. Codeforces user handle.
"""

class CFProblem(CFObject):
    attr = "contestId,index,name,type,points,tags"
    __doc__ = """
---------------------
Represents a problem.
---------------------
contestId    Integer. Id of the contest, containing the problem.
index        String. Usually a letter of a letter, followed by a digit, that represent a problem index in a contest.
name         String. Localized.
type         Enum: PROGRAMMING, QUESTION.
points       Floating point number. Can be absent. Maximum ammount of points for the problem.
tags         String list. Problem tags.
"""

class CFProblemStatistics(CFObject):
    attr = "contestId,index,solvedCount"
    __doc__ = """
--------------------------------------------
Represents a statistic data about a problem.
--------------------------------------------
contestId      Integer. Id of the contest, containing the problem.
index          String. Usually a letter of a letter, followed by a digit, that represent a problem index in a contest.
solvedCount    Integer. Number of users, who solved the problem.
"""

class CFSubmission(CFObject):
    attr = "id,contestId,creationTimeSeconds,relativeTimeSeconds,problem,author,programmingLanguage,verdict,testset,passedTestCount,timeConsumedMillis,memoryConsumedBytes"
    __doc__ = """
------------------------
Represents a submission.
------------------------
id                     Integer.
contestId              Integer.
creationTimeSeconds    Integer. Time, when submission was created, in unix-format.
relativeTimeSeconds    Integer. Number of seconds, passed after the start of the contest (or a virtual start for virtual parties), before the submission.
problem                Problem object.
author                 Party object.
programmingLanguage    String.
verdict                Enum: FAILED, OK, PARTIAL, COMPILATION_ERROR, RUNTIME_ERROR, WRONG_ANSWER, PRESENTATION_ERROR, TIME_LIMIT_EXCEEDED, MEMORY_LIMIT_EXCEEDED, IDLENESS_LIMIT_EXCEEDED, SECURITY_VIOLATED, CRASHED, INPUT_PREPARATION_CRASHED, CHALLENGED, SKIPPED, TESTING, REJECTED. Can be absent.
testset                Enum: SAMPLES, PRETESTS, TESTS, CHALLENGES, TESTS1, ..., TESTS10. Testset used for judging the submission.
passedTestCount        Integer. Number of passed tests.
timeConsumedMillis     Integer. Maximum time in milliseconds, consumed by solution, for one test.
memoryConsumedBytes    Integer. Maximum memory in bytes, consumed by solution, for one test.
"""

class CFHack(CFObject):
    attr = "id,creationTimeSeconds,hacker,defender,verdict,problem,test,judgeProtocol"
    __doc__ = """
------------------------------------------------
Represents a hack, made during Codeforces Round.
------------------------------------------------
id                     Integer.
creationTimeSeconds    Integer. Hack creation time in unix format.
hacker                 Party object.
defender               Party object.
verdict                Enum: HACK_SUCCESSFUL, HACK_UNSUCCESSFUL, INVALID_INPUT, GENERATOR_INCOMPILABLE, GENERATOR_CRASHED, IGNORED, TESTING, OTHER. Can be absent.
problem                Problem object. Hacked problem.
test                   String. Can be absent.
judgeProtocol          Object with three fields: "manual", "protocol" and "verdict". Field manual can have values "true" and "false". If manual is "true" then test for the hack was entered manually. Fields "protocol" and "verdict" contain human-readable description of judge protocol and hack verdict. Localized. Can be absent.
"""

class CFRanklistRow(CFObject):
    attr = "party,rank,points,penalty,successfulHackCount,unsuccessfulHackCount,problemResults,lastSubmissionTimeSeconds"
    __doc__ = """
--------------------------
Represents a ranklist row.
--------------------------
party                        Party object. Party that took a corresponding place in the contest.
rank                         Integer. Party place in the contest.
points                       Floating point number. Total ammount of points, scored by the party.
penalty                      Integer. Total penalty (in ICPC meaning) of the party.
successfulHackCount          Integer.
unsuccessfulHackCount        Integer.
problemResults               List of ProblemResult objects. Party results for each problem. Order of the problems is the same as in "problems" field of the returned object.
lastSubmissionTimeSeconds    Integer. For IOI contests only. Time in seconds from the start of the contest to the last submission that added some points to the total score of the party.
"""

class CFProblemResult(CFObject):
    attr = "points,penalty,rejectedAttemptCount,type"
    __doc__ = """
----------------------------------------------------------
Represents a submissions results of a party for a problem.
----------------------------------------------------------
points                  Floating point number.
penalty                 Integer. Penalty (in ICPC meaning) of the party for this problem.
rejectedAttemptCount    Integer. Number of incorrect submissions.
type                    Enum: PRELIMINARY, FINAL. If type is PRELIMINARY then points can decrease (if, for example, solution will fail during system test). Otherwise, party can only increase points for this problem by submitting better solutions.
"""

CFObjectList = [CFUser,
                CFRatingChange,
                CFContest,
                CFParty,
                CFMember,
                CFProblem,
                CFProblemStatistics,
                CFSubmission,
                CFHack,
                CFRanklistRow,
                CFProblemResult
]