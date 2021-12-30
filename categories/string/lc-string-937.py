class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letLog = []
        digLog = []

        for log in logs:
            splitedLog = log.split()
            if splitedLog[1].isalpha():
                letLog.append(log)
            else:
                digLog.append(log)

        letLog.sort(key=lambda x: (x.split()[1:], x[0]))

        return [*letLog, *digLog]