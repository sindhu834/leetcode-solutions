class Solution:
    def bagOfTokensScore(self, tokens, power):
        tokens.sort()
        score = max_score = 0
        low, high = 0, len(tokens) - 1

        while low <= high:
            # Play smallest token face-up if possible
            if power >= tokens[low]:
                power -= tokens[low]
                score += 1
                low += 1
                max_score = max(max_score, score)
            # Otherwise, play largest token face-down to gain power
            elif score > 0:
                power += tokens[high]
                score -= 1
                high -= 1
            else:
                break  # can't do anything
        return max_score
