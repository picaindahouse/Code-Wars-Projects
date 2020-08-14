import random
class Machine:
    def __init__(self):
        self.n, self.boo, self.act = [], [], ACTIONS
    def command(self, cmd, num):
        haiz, self.cmd, self.num = 0, cmd, num
        if self.cmd in [i for i,x in self.n]: return [self.act[h](self.num) for w,h in self.n if w == self.cmd][0]
        while haiz == 0:
            self.action = random.choice([0,1,2,3,4])
            if [self.cmd,self.action] in self.boo: pass
            else: haiz = 1
        return self.act[self.action](self.num)
    def response(self,res):
        if res == True:
            if self.cmd in [i for i,x in self.n]: pass
            else: self.n.append([self.cmd,self.action])
        else:
            if [self.cmd,self.action] in self.n: 
                print([self.cmd,self.action])
                self.n.remove([self.cmd,self.action])
                self.boo.append([self.cmd,self.action])
            else: self.boo.append([self.cmd,self.action])