class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_count = {}

        # Step 1: build frequency map
        for winner, loser in matches:
            if winner not in loss_count:
                loss_count[winner] = 0

            if loser not in loss_count:
                loss_count[loser] = 0

            loss_count[loser] += 1

        zero_loss = []
        one_loss = []

        # Step 2: classify players
        for player in loss_count:
            if loss_count[player] == 0:
                zero_loss.append(player)
            elif loss_count[player] == 1:
                one_loss.append(player)

        return [sorted(zero_loss), sorted(one_loss)]