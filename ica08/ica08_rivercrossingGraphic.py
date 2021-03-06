import time #Importing time module

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
# TODO: Maybe can rewrite this with any() and all() and listcomps
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
    #return left==set()
    
# Let the farmer ferry across the river, taking an item with him.
# 'item' can be None is the farmer is to take nothing with him.
# Return the new configuration, or None is the crossing can't be performed
# because the item is not on the same shore as the farmer.
def ferry(cfg,item):
    left,right=[set(x) for x in cfg[0]] # make copies, because 'left' and 'right' will be mutated
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
    return ((left,right),desc) # return the resulting configuration

# pretty-print a configuration
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
        if mayhem(child): # skip configurations which are not allowed
            continue
        if child[0] in previouscfgs: # skip shore configurations which have been seen before
            continue
        previouscfgs.append(child[0])
        generate(child,level+1)

# starting configuration
cfg=((set((farmer,goat,cabbage,wolf)), set()),"")

# this records any previously encountered configurations
previouscfgs=[cfg[0]]

# keep a solution stack for later printing
solutionstack=[]

# go!
print "Trace of the recursive solution-finding process:"
generate(cfg)

print "\nThe solution to the problem:"

#imports the PIL module which helps loading images. Idea is that for each step a new image will be shown for two seconds
import psutil # Not in use, idea was to kill pop-up window, did not work
import os
from PIL import Image  


for step in solutionstack:
    time.sleep(2)       #Time delay between printing each step.
    
    if step == "The farmer goes --> with the goat":
        img = Image.open("state1.png")
        img.show()
        img.close
    elif step == "The farmer goes <-- alone":     
        os.system("taskkill /im dllhost.exe")
        img = Image.open("state2.png")
        img.show()
        img.close()
    elif step == "The farmer goes --> with the cabbage":
        os.system("taskkill /im dllhost.exe")
        img = Image.open("state3.png")
        img.show()
        img.close()
    elif step == "The farmer goes <-- with the goat":
        os.system("taskkill /im dllhost.exe")
        img = Image.open("state4.png")
        img.show()
        img.close() 
    elif step == "The farmer goes --> with the wolf":
        os.system("taskkill /im dllhost.exe")
        img = Image.open("state5.png")
        img.show()
        img.close()
    elif step == "The farmer goes <-- alone":
        os.system("taskkill /im dllhost.exe")
        img = Image.open("state6.png")
        img.show()
        img.close()
    elif step == "The farmer goes --> with the goat":
        os.system("taskkill /im dllhost.exe")
        img = Image.open("state7.png")
        img.show()
        img.close()
        
    if step:
        print "  ",step

#print ths endstate, and loads up correct picture
print cfg
os.system("taskkill /im dllhost.exe")
img = Image.open("end.png")
img.show()
img.close()
time.sleep(2)
os.system("taskkill /im dllhost.exe")
