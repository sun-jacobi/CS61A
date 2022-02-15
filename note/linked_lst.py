from queue import Empty


class Link:
    empty = ()
    def __init__(self, first, rest = empty):
        assert rest is Link.empty or isinstance(rest,Link)
        self.first = first
        self.rest = rest
    
    def __getitem__(self,i):
        if i == 0 :
            return self.first
        else:
            return self.rest[i-1]
    def __len__(self):
        return 1 + len(self.rest)
    
    def __repr__(self):
        if self.rest is Link.empty:
            rest = ''
        else:
            rest = ',' + repr(self.rest)
        return 'Link({0}{1})'.format(self.first,rest)
    
    def keep_if_link(self,f):
        if self == Link.empty:
            return self
        else:
            kept = Link.keep_if_link(self.rest,f)
            if f(self.first):
                return Link(self.first,kept)
            else:
                return kept
            
            

        
        