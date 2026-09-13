class Solution:
    def rankTeams(self, votes):
        n = len(votes[0])
        count = {team: [0] * n for team in votes[0]}

        for vote in votes:
            for i, team in enumerate(vote):
                count[team][i] += 1

        teams = list(votes[0])

        teams.sort(key=lambda team: ([-x for x in count[team]], team))

        return ''.join(teams)