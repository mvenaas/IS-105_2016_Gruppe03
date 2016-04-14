import os
import time
from PIL import Image  
from socket import *
import sys
import select

# Code based on following code: http://codepad.org/cywKyxXO . Edited to support our needs aswell adapted to ICA08
print """
A farmer is to ferry across a river a goat, a cabbage, and a wolf.
Besides the farmer himself, the boat allows him to carry only
one of them at a time. Without supervision, the goat will gobble
the cabbage whereas the wolf will not hesitate to feast on the goat.
"""

# Solution snatched from the web:
#
# The farmer brings the goat to the right side then comes back alone.
# He then takes the cabbage to the right side and brings the goat back to the left.
# He now takes the wolf to the right side and comes back alone and then
# finally takes the goat back.

# A configuration is a nested tuple: ((left,right),desc)
# left and right are sets representing the entities on each shore
# and 'desc' is a description how this configuration was reached

farmer,goat,cabbage,wolf=("farmer","goat","cabbage","wolf") # Four variables are being assigned a string in a tuple
carryables=(goat,cabbage,wolf,None)

# these combinations may not happen unsupervised
forbiddens=(set((goat,cabbage)), set((wolf,goat))) # Set is a method used to make unordered lists. Here meaning that any combinaiton of goat and cabbage is illegal

# return wether a undesirable situation occurs
# If mayhem is met, verdict w
def mayhem(cfg):
    for shore in cfg[0]:
        if farmer not in shore:
            for forbidden in forbiddens:
                if shore.issuperset(forbidden):
                    return True
    return False

# return True when the end condition is reached (when all entities are on the right shore)
def done(cfg):
    left,right=cfg[0]
    return left==set()
    
# Let the farmer ferry across the river, taking an item with him.
# 'item' can be None is the farmer is to take nothing with him.
# Return the new configuration, or None is the crossing can't be performed
# because the item is not on the same shore as the farmer.
def ferry(cfg,item):
    left,right=[set(x) for x in cfg[0]]                                 # Make copies, because 'left' and 'right' will be mutated
    
    # determine on which shore the farmer is, and to which shore he will ferry
    if farmer in left:
        src,dst=left,right
        
    else:
        src,dst=right,left
        
    # make sure that if there's an item to carry, it is on the same shore as the farmer
    if item and not item in src:
        return None
    
    # cross the farmer and possibly the item
    desc="The farmer goes -->" if farmer in left else "The farmer goes <--"
    src.remove(farmer)
    dst.add(farmer)
    if item:
        src.remove(item)
        dst.add(item)
        desc+=" with the "+item
    else:
        desc+=" alone"
    return ((left,right),desc)                                          # Return the resulting configuration

# Print a configuration
def printcfg(cfg,level=0):
    left,right=cfg[0]
    verdict="(Not allowed)" if mayhem(cfg) else "(Ok)"
    print "    "*level,", ".join(left),"  ~~~  ",", ".join(right),cfg[1],verdict

# given a certain configuration, generate the configurations that could result from it
def onegeneration(cfg):
    followups=[]
    for item in carryables:
        followup=ferry(cfg,item)
        if not followup: continue
        followups.append(followup)
    return followups

# recursively generate from a given configuration
def generate(cfg,level=0):
    solutionstack.extend([None]*(level-len(solutionstack)+1))
    solutionstack[level]=cfg[1]
    printcfg(cfg,level)
    childs=onegeneration(cfg)
    for child in childs:
        if mayhem(child):                                               # Skip configurations which are not allowed
            continue
        if child[0] in previouscfgs:                                    # Skip shore configurations which have been seen before
            continue
        previouscfgs.append(child[0])
        generate(child,level+1)

cfg=((set((farmer,goat,cabbage,wolf)), set()),"")                       # Starting configuration


previouscfgs=[cfg[0]]                                                   # This records any previously encountered configurations

solutionstack=[]                                                        # Keep a solution stack, we'll use it later for printing

print "The sollution for RiverCrossing:"            
generate(cfg)                                                           # Shows the sollution in text form before continue with the visulization
print ""                                                                # Allways nice with spaces, reduce screen cluttering
print ""

print "Please start the client to visualize the sollution"
from server import *                                                    # Imports the server settings and awaits an connection before continue on with the visulization
    
if connected == True:                                                   # Checks if the connection is made, if true, continue on
    print "Starting state:"
    time.sleep(1.5)                                                     # Gives the user 1.5 seconds to read the message before opening the picture
    img = Image.open("start.png")                                       # Loads the immage into memory
    img.show()                                                          # Displays the picture
    img.close()
    time.sleep(2)                                                       # System sleeps for additional two seconds
    os.system("taskkill /im dllhost.exe")                               # Terminates the image veiwer to preent cluttering of the screen 

for step in solutionstack:                                              # Goes through the sollution and displays the corresponding image related to the different states
    
    if step == "The farmer goes --> with the goat":
        img = Image.open("state1.png")
        img.show()
        img.close
        time.sleep(2)
        os.system("taskkill /im dllhost.exe")
        
    elif step == "The farmer goes <-- alone":     
        img = Image.open("state2.png")
        img.show()
        img.close()
        time.sleep(2)
        os.system("taskkill /im dllhost.exe")
        
    elif step == "The farmer goes --> with the cabbage":
        img = Image.open("state3.png")
        img.show()
        img.close()
        time.sleep(2)
        os.system("taskkill /im dllhost.exe")
        
    elif step == "The farmer goes <-- with the goat":
        img = Image.open("state4.png")
        img.show()
        img.close() 
        time.sleep(2)
        os.system("taskkill /im dllhost.exe")
        
    elif step == "The farmer goes --> with the wolf":
        img = Image.open("state5.png")
        img.show()
        img.close()
        time.sleep(2)
        os.system("taskkill /im dllhost.exe")
        
    elif step == "The farmer goes <-- alone":
        img = Image.open("state6.png")
        img.show()
        img.close()
        time.sleep(2)
        os.system("taskkill /im dllhost.exe")
        
    elif step == "The farmer goes --> with the goat":
        img = Image.open("state7.png")
        img.show()
        img.close()
        time.sleep(2)
        os.system("taskkill /im dllhost.exe")
        
    if step:
        print "  ",step

# Displays the end state, and closes the picture after two seconds
img = Image.open("end.png")
img.show()
img.close()
time.sleep(2)
os.system("taskkill /im dllhost.exe")
