# https://www.codewars.com/kata/51fda2d95d6efda45e00004e/train/python
# Codewars style ranking system

class User():
    def __init__(self):
        self.rank = -8
        self.rlkt = [-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8]
        self.rrank = 0
        self.progress = 0
    
    def update_rank(self):
        while self.progress >= 100 and self.rrank < 15:
            self.progress -= 100
            self.rrank += 1
            self.rank = self.rlkt[self.rrank]

        if self.rrank == 15:
            self.progress = 0
        return    
    
    def rank_diff(self, rank):
        return self.rlkt.index(rank) - self.rrank         
        
    def inc_progress(self, rank):
        if rank < -8 or rank > 8:
            raise(ValueError)
        rdiff = self.rank_diff(rank)
        if rdiff == -1:
            self.progress += 1
        if rdiff == 0:
            self.progress += 3
        if rdiff > 0:
            self.progress += 10 * rdiff**2        
        self.update_rank()
        return
        
        



            
user = User()
for i in [1,1,1,1,1,2,2,-1,3,8,8,8,8,8,8,8,8,8,8]:
    print("==========")
    print(user.rrank, user.rank, user.progress,i)           
    user.inc_progress(i)
    print(user.rrank, user.rank, user.progress)           
