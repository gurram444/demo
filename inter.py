list=['2','6','0','4','1']
list=[int(i)for i in list]
list.sort()
print(list)


class x:
    def __init__(self):
        print('in constructor x')
class y(x):
    def __init__(self):
        super().__init__()
        print('in y')

y1=y()
