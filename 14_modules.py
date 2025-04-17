from math import pi
import sys
import random as rdm
from rps import rock_paper_scissors


print(pi)
# prints out everything you can do with a module  
for item in dir(rdm):
    print(item)
    
rock_paper_scissors()