class DFA:
    def __init__(self, delta, q0, F):
        self.delta = delta
        self.q0 = q0
        self.F = F

    def run(self, word):
        q = self.q0
        L = [q]
        while word != "":

            q = self.delta[(q, word[0])]
            L.append(q)
            word = word[1:]

        if q not in self.F:
            return L, False
        else:
            return L, True


class NFA:
    def __init__(self, delta, q0, F):
        self.delta = delta
        self.q0 = q0
        self.F = F

    def run(self, word):
        ok = False
        D = []

        def wordCheck(word, q, L=[]):
            L.append(q)
            nonlocal ok
            nonlocal D
            if word == "":
                if q in self.F:
                    ok = True
                    D.append(L)
            else:
                if (q, word[0]) in self.delta:
                    for state in self.delta[(q, word[0])]:
                        l1 = L[::]
                        wordCheck(word[1:], state, l1)
        wordCheck(word, self.q0)
        return D, ok



f = open("automata.in", 'r')
g = open("words.in", 'r')
q0 = int(f.readline())
F = [int(x) for x in f.readline().split()]
delta = {}
for l in f:
    l = l.split()
    if (int(l[0]), l[1]) in delta:
        delta[(int(l[0]), l[1])].append(int(l[2]))
    else:
        delta[(int(l[0]), l[1])] = [int(l[2])]
        
        
automata = NFA(delta, q0, F)


for word in g:
    word = word.strip()
    L, ok = automata.run(word)
    if ok == True:
        print(f"\nThe word --{word}-- has been accepted and the paths are:")
        for path in L:
            print(*path,sep="-")
    else:
        print(f"\nThe word --{word}-- has been rejected.")
f.close()
g.close()