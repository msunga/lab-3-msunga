# Linked List Functions

# an AnyList is one with
# "None"
# or any value 

class Pair:
   def __init__(self, first, rest):
      self.first = first
      self.rest = rest
   def __eq__(self, other):
      return type(other) == Pair and self.first == other.first and self.rest == other.rest
   def __repr__(self):
      return "Pair({}, {})".format(self.first, self.rest)


