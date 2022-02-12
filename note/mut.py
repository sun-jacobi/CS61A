def oski(bear):
    def cal(berk):
        nonlocal bear
        if bear(berk) == 0 :
            return[berk+1,berk-1]
        bear = lambda ley: berk - ley
        return [berk,cal(berk)]
    return cal(2)

