import random
import copy

people = []
avail = []

class Person:
    def __init__(self,name,cple = None):
        self.name = name
        self.cple = cple
        self.has = None

def listPeople():
    for p in people:
        # if p.name.lower() == 'tanner':
        print(p.name + ' has ' + str(p.has))
    print('\n')
    # for a in avail: print(a.name)

def reset():
    for p in people: p.has = None
    global avail
    avail = copy.copy(people)
    mix()

def initPeople():
    # couples = input('Enter semicolon separated couples: \n(Ex: person1 person2; person3 person4 ) ').split(';')
    # singles = input('Enter everyone else: ').split()
    couples = 'jt macahl; parker kylie; taylor megan'.split(';')
    singles = 'tanner davis alyssa nate'.split()
    for c in couples:
        c = c.split()
        people.append(Person(c[0].strip(),c[1].strip()))
        people.append(Person(c[1].strip(),c[0].strip()))
    for s in singles: people.append(Person(s))
    reset()

def writeResults(doit):
    try:
        with open('files/master.txt','w+') as final:
            if not doit: final.close()
            for p in people:
                file = p.name + '.txt'
                try:
                    with open('files/'+file,'w+') as writer:
                        writer.write(p.name + ' has ' + p.has)
                    writer.close()
                except: print('Failed to open ' + file)
                if doit: final.write(p.name + ' has ' + p.has +'\n')
            final.close()
    except: print('Failed to open master.txt')

def mix():
    for r in range(len(people)): random.shuffle(people)
    for a in range(len(avail)): random.shuffle(avail)

def doMagic():
    done = False
    while not done:
        broke = False
        for p in people:
            if p.has is None:
                rnd = random.randrange(len(avail))
                p.has = avail[rnd].name
                if p.name == p.has or p.has == p.cple:
                    broke = True
                    break
                avail.pop(rnd)
        s = sum(p.has is None for p in people)
        if s != 0 or broke:
            broke = True
            reset()
        good = True
        if not broke:
            for p in people:
                if p.name == p.has or p.cple == p.has:
                    good = False
                    reset()
                    break
        if good and not broke: done = True

if __name__ == "__main__":
    # for x in range(5):
    initPeople()
    doMagic()
    writeResults(True)
    # listPeople()
