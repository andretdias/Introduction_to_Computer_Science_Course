class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self,other):
        newself = self.vals.copy()
        for element in self.vals:
            if other.member(element) == False:
                newself.remove(element)
        newlist = intSet()
        for element in newself:
            newlist.insert(element)
        return newlist

    def __len__(self):
        return len(self.vals)

setA = intSet()
setA.insert(-19)
setA.insert(-16)
setA.insert(-8)
setA.insert(-4)
setA.insert(-1)
setA.insert(5)
setA.insert(7)
setA.insert(12)
setA.insert(12)
setB = intSet()
setB.insert(-17)
setB.insert(-16)
setB.insert(-15)
setB.insert(-14)
setB.insert(-11)
setB.insert(-5)
setB.insert(4)
setB.insert(7)
setB.insert(8)

print(setA.intersect(setB))
print(setA.len())
print(intSet.len(setA))
