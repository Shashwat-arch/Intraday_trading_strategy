import numpy as np

class FindExtremum:
    def __init__(self,
                 high:list,
                 low:list):
        self.high = high
        self.low = low

    def find_extremum(self):
        extremum = []

        # Check extremum values in 'high' array
        for i in range(1, len(self.high) - 1):
            if self.high[i] > self.high[i - 1] and self.high[i] > self.high[i + 1]:
                extremum.append(self.high[i])

        # Check extremum values in 'low' array
        for i in range(1, len(self.low) - 1):
            if self.low[i] < self.low[i - 1] and self.low[i] < self.low[i + 1]:
                extremum.append(self.low[i])

        extremum_values = np.array(extremum).reshape(-1, 1)

        return extremum_values