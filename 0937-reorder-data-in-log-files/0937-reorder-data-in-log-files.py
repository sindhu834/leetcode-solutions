class Solution:
    def reorderLogFiles(self, logs):
        letter_logs = []
        digit_logs = []

        for log in logs:
            identifier, rest = log.split(" ", 1)
            if rest[0].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append((rest, identifier, log))

        # Sort letter logs by content, then identifier
        letter_logs.sort()

        # Extract original logs
        result = [log[2] for log in letter_logs] + digit_logs
        return result
