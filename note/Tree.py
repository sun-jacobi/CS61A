def tree(label,branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + branches

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1 : 
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def count_leaves(t):
    if is_leaf(t):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(t)]
        return sum(branch_counts)

def partition_tree(n,m):
    if n == 0:
        return tree(True)
    elif n < 0  or m == 0: 
        return tree(False)
    else:
        left = partition_tree(n-m,m)
        right = partition_tree(n,m-1)
        return tree(m,[left,right])
    
def print_parts(tree,partition=[]):
    if is_leaf(tree):
        if label(tree):
            print('+'.join(partition))
    else:
        left, right = branches(tree)
        m = str(label(tree))
        print_parts(left,partition + [m])
        print_parts(left,partition)

def right_binarize(tree):
    if is_leaf(tree):
        return tree
    if len(tree) > 2 : 
        tree = [tree[0],tree[1:]]
    return [right_binarize(b) for b in tree]
        
            