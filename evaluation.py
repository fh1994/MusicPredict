# the predict and answer are all in same dimensions (numpy)
# noted that day is bias number such as 1,2,3
# wish you enjoy my bad code.
#                                by Roger
###############################################################################

from numpy import *
import math
# per singer alpha
def delta( predict, answer):
    temp = (predict - answer) / answer
    temp = pow(temp, 2)
    ans = temp.sum() / temp.shape[0]
    return math.sqrt(ans)

# per singer phi
def phi( answer):
    temp = answer.sum()
    return math.sqrt(temp)

# per singer Fi
def Fij( predict, answer):
    return phi( answer) * (1 - delta( predict, answer))

if __name__ == '__main__':
    a = array([35,20,12,14,40,18])
    b = array([15,10,6,7,20,9])
    print(Fij(a,b))