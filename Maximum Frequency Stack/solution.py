class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.freqStacks = defaultdict(list)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        freq = self.freq[val]
        self.freqStacks[freq].append(val)
        self.maxFreq = max(self.maxFreq, freq)

    def pop(self) -> int:
        val = self.freqStacks[self.maxFreq].pop()
        self.freq[val] -= 1
        if not self.freqStacks[self.maxFreq]:
            self.maxFreq -= 1
        return val