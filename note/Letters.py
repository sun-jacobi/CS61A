class Letters:
    def __init__(self,start ='a', end = 'e'):
        self.start = start
        self.end = end
    def __iter__(self):
        return LetterIter(self.start,self.end)
    
def LetterIter(start,end):
        current = start
        while current <= end :
            yield current
            current = chr(ord(current)+1)