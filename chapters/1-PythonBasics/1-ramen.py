---
title: "1. Ramen Noodles"
parent: "1. Python Basics"
has_children: false
has_toc: true
nav_order: 1
---

# Byte 1-1: Ramen Noodles

When Charles Babbage designed the first ever mechanical computer in the early 19th century, instant ramen wouldn’t be invented for another 150 years. So what gives? It turns out that writing instructions for computers is exactly like making a quick meal. We’ll explain how and why this matters.

(iplayer here)

## How to cook ramen

We start by writing some detailed instructions for smaller tasks.

Then at the bottom, we put it all together and describe how to make ramen (using the smaller tasks).

NOTE: These instructions are written specifically for Matt's kitchen and may not work in other kitchens.
They are written to look like code, but don't match the syntax of any actual programming language. (Programmers call this style of writing "pseudocode.")

```
**HOWTO: boilWater** (NEED: a pot with water, "BoilPot")
    If BoilPot does not have water: 
        abort
    otherwise:
        Find(an empty burner on the stove, "ActiveBurner")

    # ActiveBurner will have a corresponding circular dial on the front of the stove.
    # Note that each dial has a picture that identifies the corresponding burner.

    until ActiveBurner.Dial is at setting.HI:
        turnDialClockwise

    if ActiveBurner turns red:
        continue
    otherwise:
        stopAndPrint("Error: The burner didn't turn red like it was supposed to when you turned the heat on")

    Place(item: BoilPot, destination: ActiveBurner)

    Boiling = you see many bubbles covering the entire surface of the water

    until Boiling:
        Watch(water)

    until ActiveBurner.Dial is at setting.5:
        turnDialCounterClockwise

    # Done boiling water

**HOWTO: chopScallion (NEED: a scallion, "theScallion")
    turnToFace(stove)
    turnToFace(counter.knifeBlock)
    if counter.knifeBlock does not have knives:
        stopAndPrint("Error: There are no clean knives in the knife block")
    
    ChopKnife = counter.knifeBlock.knives.topRightKnife
    take(ChopKnife)
    
    CutBoard = counter.cuttingBoards.smallestBoard
    
    Place(item: CutBoard, destination: countertop)
    Place(item: theScallion, destination: CutBoard)
    
    Hold(theScallion.stem)
    Hold(ChopKnife)
    
    while theScallion has green:
        Hover(ChopKnife, location: theScallion.top, position: theScallion.perpendicular)
        
        if ChopKnife.location is above hand:
            stop
        otherwise: 
            cut(theScallion, with: ChopKnife)


Collect the thin cicles of scallion in the center of <span style="color:blue">Cut Board</span> and save these for later use

* Done cutting scallions

<ins>**How to open a Ramen Package** (if you are given a ramen package):</ins>

* Call the Ramen Package that you are given <span style="color:blue">The Package</span>

* Face the stove and turn right

* You will see a wooden block with a set of knives in wooden block, if there are no knives this is an error

* Take the scissors out of the bottom hole in the wooden block, call this <span style="color:blue">Ramen Scissors</span>

* Place your thumb and index finger into the holes in the handle <span style="color:blue">Ramen Scissors</span>

* Use your thumb and index finger to open up  <span style="color:blue">Ramen Scissors</span>

* With your other hand, hold <span style="color:blue">The Package</span> so that a corner of <span style="color:blue">The Package</span> is between the blades of <span style="color:blue">Ramen Scissors</span>

* Use your thumb and index finger to close <span style="color:blue">Ramen Scissors</span>

* A corner of Ramen Package should now be missing and you see a hole in the package, if not this is an error

* Return <span style="color:blue">Ramen Scissors</span> to the wooden block where you found it

* Put your fingers into the hole where the corner was removed and use your fingers to tear open <span style="color:blue">The Package</span>

* Inside the package you should obtain ramen noodles and a flavor package, save these for later use

* Done opening ramen package

---------------

<ins>**Main Instructions -- START HERE**</ins>

* Obtain package of Ramen

* Open the package of Ramen

* Obtain a pot

* Put water in the pot
