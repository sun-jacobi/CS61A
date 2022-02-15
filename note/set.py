from linked_lst import * 

class set(Link):
    def empty(self):
        return self is Link.empty
    def set_contains(self,elem):
        if set.empty(self):
            return False
        elif self.first == elem :
            return True
        else :
            return set.set_contains(self.rest,elem)

    def adjoin_set(self, elem):
        if set.set_contains(self,elem):
            return self
        else:
            return Link(elem,self)
    
    def intersect_set(self,other):
        return Link.keep_if_link(lambda elem : not set.set_contains(other, elem))
    