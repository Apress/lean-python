
class calculator(object):

    def __init__(self,title):
        self.title=title
        return

    def runTest(self,a,op,b):
        self.result=self.calculate(a,op,b)
        return self.result
        
    def calculate(self,a,op,b):
        if len(a)==0 or len(b)==0 or len(op)==0:
            return 'Ending'

    def dispose(self):
        return
        
if __name__=='__main__':
    main()