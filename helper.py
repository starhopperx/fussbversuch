
class Test(object):

    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def so(self):
        print(self.var2 ,self.var1)


test = Test('lala', "lulu")
test.so()