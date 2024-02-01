class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        
        minTimeTaken = []

        j = 0
        for i in range(0, len(tasks), 4):
            timeTaken = []
            timeTaken.append(processorTime[j] + tasks[i])
            timeTaken.append(processorTime[j] + tasks[i+1])
            timeTaken.append(processorTime[j] + tasks[i+2])
            timeTaken.append(processorTime[j] + tasks[i+3])

            minTimeTaken.append(max(timeTaken))
            j = j + 1

        return max(minTimeTaken)
      