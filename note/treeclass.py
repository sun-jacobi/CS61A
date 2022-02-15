from multiprocessing.context import assert_spawning


class tree:
    def __init__(self,label,branches = []):
        self.label = label
        for branch in branches:
            assert isinstance(branch,tree)
        self.branches = branches
    
        
def fib_tree(n):
        if n==0 and n==1:
            return tree(n)
        else:
            left = fib_tree(n-2)
            right = fib_tree(n-1)
            fib_n  =left.label + right.label
            return tree(fib_n,[left, right])    