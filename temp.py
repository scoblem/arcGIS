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

    def __len__(self):
        return len(self.vals)

    def intersect(self, obj):
        """Returns a intSet object containing the intersecting values of self & obj"""
        x = set(self.vals)
        y = set(obj.vals)
        z = x & y

        intersect = intSet()

        for i in z:
            intersect.insert(i)

        return intersect


# setA: {-18,-17,-14,-13,-10,9,11,13,15}
# setB: {-15,-8,-7,-1,1,3,14}
# setA.intersect(setB): {-18,-17,-15,-14,-13,-10,-8,-7,-1,1,3,9,11,13,14,15}
