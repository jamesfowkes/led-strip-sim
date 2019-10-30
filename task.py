class Task:
    
    def __init__(self, period, cb=None, cbargs=[], cbkwargs={}):
         self.period = period
         self.last = 0
         self.cb = cb
         if type(cbargs) is not list:
             cbargs = [cbargs]
             
         self.cbargs = cbargs
         self.cbkwargs = cbkwargs
         
    def setPeriod(self, period):
        self.period = period
        
    def run(self):
        run = (millis() - self.last) > self.period
        if run:
            self.last = millis()
            if self.cb is not None:
                self.cb(*self.cbargs, **self.cbkwargs)
        return run
