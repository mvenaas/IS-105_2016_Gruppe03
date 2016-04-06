# This code is borrowed from user "sfcgeorge", link: https://gist.github.com/sfcgeorge/0e4d2977ebcdd050927c

# There is a river with a boat and a bank on each side; that's how rivers work.
# On the left bank is a farmer with their wolf, goat and a cabbage.
# The farmer keeps the peace, they're like a horse whisperer but for goats.
# If the farmer is not around then the goat will eat the cabbage,
# and the wolf will eat the goat. They must not be paired up alone.
# Only the farmer can row the boat; cabbages don't have arms.
# The boat has just 2 spaces because it's cheap, one for farmer one for object.
# The farmer may be in the boat alone but other items must not be left in alone.
# The farmer wants to get all his items to the other bank.

class WGC:
    F, W, G, C = 0, 1, 2, 3

    start, goal = [[F, W, G, C], [], []]  ,  [[], [], [F, W, G, C]]

    def __init__(self, state = None):
        self.state = state or self.start[:]

    def won(self): return self.state == self.goal

    def successors(self):
        for move in [[0, 1], [1, 0], [1, 2], [2, 1]]:
            for possibility in self.move_source_dest(*move):
                if not self.invalid(possibility): yield WGC(possibility)

    def move_source_dest(self, s, d):
        source_orig = self.state[s][:]
        if WGC.F in source_orig: # move one
            state = self.state[:]
            state[s], state[d] = self.state[s][:], self.state[d][:]
            state[s].remove(WGC.F)
            state[d].insert(0, WGC.F)
            yield state
        if WGC.F in source_orig and len(source_orig) >= 2: # move two
            source_orig.remove(WGC.F)
            for i in range(len(source_orig)):
                state = self.state[:]
                state[s], state[d] = source_orig[:], self.state[d][:]
                state[d] += [WGC.F, state[s].pop(i)]
                state[d].sort()
                yield state

    def invalid(self, s):
        # boat has two max
        if len(s[1]) > 2: return True
        for i in range(3):
            # goat must not be left alone with cabbage
            if WGC.G in s[i] and WGC.C in s[i] and not WGC.F in s[i]:
                return True
            # wolf must not be left alone with goat
            if WGC.W in s[i] and WGC.G in s[i] and not WGC.F in s[i]:
                return True


class Run:
    history, won = [], False

    def go(self, problem):
        self.next(problem, 0)
        return self.history

    def next(self, problem, depth):
        self.history.append(problem.state)
        if problem.won():
            self.won = True
        else:
            for s in problem.successors():
                if not self.won:
                    self.history = self.history[:depth+1]
                    if not s.state in self.history: self.next(s, depth+1)


#for s in Run().go(WGC()): print s


class WGCPrinter:
    def __init__(self, n):
        with open(n) as f: self.symbols = f.read().split('\n\n')
        for i in range(len(self.symbols)):
            self.symbols[i] = self.symbols[i].split('\n')
            self.symbols[i].reverse()

    def width(self, symbol):
        return max(len(s) for s in symbol)

    def total_width(self):
        return sum(self.width(s) +2 for s in self.symbols)

    def max_height(self):
        return max(len(s) for s in self.symbols)

    def print_state(self, state):
        lines = []
        for i in range(-1, self.max_height()+1): # each row of ascii prints out
            row = ""
            for p in range(len(state)): # position of the state (bank, boat...)
                pos = ""
                g = '-' if (i == -1 or i == self.max_height()) and (p != 0 and p != len(state)-1) else ' '
                for sym in state[p]: # symbol in the position (wolf, goat...)
                    s = self.symbols[sym]
                    pos += g+(s[i] if s[i:i+1] else '').ljust(self.width(s),g)+g
                row += g * (self.total_width() - len(pos)) + pos
                br = '/' if i == 0 else ('\\' if i == self.max_height()-1 else ('~' if i == -1 or i == self.max_height() else '|'))
                bl = '\\' if i == 0 else ('/' if i == self.max_height()-1 else ('~' if i == -1 or i == self.max_height() else '|'))
                if p == len(state)-2: row += br + "~("
                if p == 0: row += ")~" + bl
            lines.insert(0, row)
        for line in lines: print line


printer = WGCPrinter('wgc_ascii.txt')
for s in Run().go(WGC()): printer.print_state(s)