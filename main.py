people = []
avail = []

class Person:
    def __init__(self,name,cple = None):
        self.name = name
        self.cple = cple
        self.has = None

def listPeople():
    for p in people: print(p.name,p.cple)
    for a in avail: print(a)

def funcMap(p):
    if p.has is None: return p.name

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
    return map(funcMap,people)

def writeResults():
    for p in people:
        with open(f'{p.name}.txt','w+') as writer:
            writer.write(f'{p.name} has {p.has}')
        writer.close()

def doMagic():
    pass

if __name__ == "__main__":
    avail = initPeople()
    doMagic()
    # listPeople()
