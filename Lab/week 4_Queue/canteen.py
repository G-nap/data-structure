class Queue:
    def __init__(self):
        self.q = []

    def push(self, lst):
        for val in self.q[-1::-1]:
            if lst[0] == val[0]:
                if self.q.index(val) == self.size() - 1:
                    break
                self.q.insert(self.q.index(val) + 1, lst)
                return
        self.q.append(lst)

    def pop(self):
        if self.size() != 0:
            return self.q.pop(0)  
        else :
            return 'Empty'

    def size(self):
        return len(self.q)

    def __str__(self):
        return ', '.join(str(data) for data in self.q) if self.size() != 0 else 'Empty'

n = input('Enter Input : ').split('/')
d = {}
q = Queue()

for e in n[0].split(','):
    e = e.split()
    d[e[1]] = d.get(e[1], e[0])

for e in n[1].split(','):
    e = e.split()
    if len(e) == 1:
        pop = q.pop()
        print(pop if pop == 'Empty' else int(pop[1]))
    else:
        e[0] = d[e[1]]
        q.push(e)