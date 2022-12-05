import requests


class Solution:
    def getNumDraws(self, year):

        # Write your code here
        res = 0
        maximum_score = 10

        for i in range(maximum_score+1):
            r = requests.get(
                f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1goals={i}&team2goals={i}')
            res += r.json()['total']

        return res


print(Solution().getNumDraws(2011))
