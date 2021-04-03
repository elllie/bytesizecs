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

### Boiling water
(Human instructions here)

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
```

### Chopping scallions
(Human instructions here)

```
**HOWTO: chopScallion** (NEED: a scallion, "theScallion")
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

    scallions_collection = take(CutBoard.center.scallion_pieces)
    Place(item: scallions_collection, destination: counter.bowl)

    # Done cutting scallions
```

### Opening a ramen packet
(Human instructions here)

```
**HOWTO: openPacket** (NEED: a ramen package, "thePacket")
    turnToFace(stove)
    turnToFace(counter.knifeBlock)
    if counter.knifeBlock does not have knives:
        stopAndPrint("Error: There are no clean knives in the knife block")
    
    RamenScissors = counter.knifeBlock.knives.scissors
    take(RamenScissors)
    
    Hold(thePacket)
    Hold(RamenScissors)
    
    RamenScissors.cut(thePacket.edge)
    
    if thePacket.edge has a hole:
        continue
    otherwise:
        stopAndPrint("Error: The ramen packet is still sealed")
        
    Place(item: finger, destination: thePacket.edge.hole)
    tearOpen(at_placement)
    
    Noodles = thePacket.inside.noodles
    FlavorPacket = thePacket.inside.miniPacket
    
    PlaceMany(items: [Noodles, FlavorPacket], destination: countertop)
    
    # Done opening ramen package
```

### Poaching an egg
(Human instructions here)
```
**HOWTO: PoachEgg (NEED: an egg, "egg")
    # Instructions here
```

### Main Program (Computer starts here)
(Human readable instructions and an explanation for why this works)

```
**Main Instructions -- START HERE**

# find ramen
turnToFace(shelf)
if shelf.dryGoods does not have ramen:
    stopAndPrint("Error: We're out of ramen")

todays_packet = shelf.dryGoods.ramenPacket

take(todays_packet)
openPacket(todays_packet)

# find pot
if shelf.equip.pots does not have a small pot: 
    stopAndPrint("Error: There's no clean pot")

pot = shelf.equip.pots.saucepan
turnToFace(sink)
sink.fillWithWater(pot)

boilWater(pot)

# scallions
turnToFace(window)
if window.windowsill.scallionsJar does not have scallions:
    stopAndPrint("Error: We're out of scallions")

scallion = window.windowsill.scallionsJar.longestScallion

take(scallion)
chopScallion(scallion)
```
