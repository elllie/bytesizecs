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

### Accessing items in the kitchen
Matt doesn't have a pantry. His kitchen is organized using cabinets, shelves, and countertops exclusively.
```
HOWTO: findPot (returns: a pot)
    if shelf.equip.pots does not have a small pot: 
        stopAndPrint("Error: There's no clean pot")

    pot = shelf.equip.pots.saucepan
    return with pot
```

```
HOWTO: findRamen (returns: a ramen packet)
    turnToFace(shelf)
    if shelf.dryGoods does not have ramen:
        stopAndPrint("Error: We're out of ramen")

    return with shelf.dryGoods.ramenPacket
```

```
HOWTO: findScallion (returns: a scallion)
    turnToFace(window)
    if window.windowsill.scallionsJar does not have scallions:
        stopAndPrint("Error: We're out of scallions")

    scallion = window.windowsill.scallionsJar.longestScallion
    return with scallion
```

```
HOWTO: findEgg (returns: an egg)
    turnToFace(refrigerator)
    open(refrigerator)
    if refrigerator does not have eggs:
        stopAndPrint("Error: We're out of eggs")

    todays_egg = refrigerator.dairy.egg
    return with todays_egg
```

### Boiling water
Suppose we already know how to turn on the sink and fill objects with water. The following code chunks describe filling a pot with water and boiling the water in the pot.

Matt has an electric stove in a kitchen island across from the sink.

The stove has 4 burners, each with a corresponding circular dial on the front of the stove. Each dial has a picture that identifies which burner it goes to.

```
HOWTO: fillPotWithWater (NEED: an empty pot, "pot"; returns: the same pot filled with water)
    turnToFace(sink)
    sink.fillWithWater(pot)
    return with pot
```

```
HOWTO: boilWater (NEED: a pot with water, "BoilPot")
    If BoilPot does not have water: 
        abort
    otherwise:
        Find(an empty burner on the stove, "ActiveBurner")

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
```

### Chopping scallions
[Most folks call them green onions but they're really scallions.](https://youtu.be/O1vJ4sXetw4?t=56) You'll want to cut a single scallion into little rings until it starts producing little white coins at the root. The coins taste bad, but the rings are awesome.

```
HOWTO: chopScallion (NEED: a scallion, "theScallion"; returns: chopped scallion pieces)
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
    return with scallions_collection
```

### Cooking the ramen
The following code blocks describe how to open the ramen packet and cook the ramen noodles and flavor packet.
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
```

### Poaching an egg
This code block follows [Gordon Ramsay's instructions](https://www.youtube.com/watch?v=iHGO8ygUk0w) for poaching an egg, sans the dramatic music.
```
**HOWTO: PoachEgg (NEED: an egg, "egg"; a pot of boiling water, "boilingPot")
    turnToFace(drawer)
    if drawer does not have a whisk:
        if drawer has a large spoon:
            utensil = drawer.spoons.largest
        otherwise:
            stopAndPrint("Error: I don't have a whisk or spoon to spin the water with")
    otherwise:
        utensil = drawer.whisk
        
    if drawer does not have a bowl:
        if drawer has a measuring cup:
            bowl = drawer.measuring.1cup
        otherwise:
            stopAndPrint("Error: I don't have a bowl or cup to put the egg in")
    otherwise:
        bowl = drawer.bowls.smallest
    
    PlaceMany(items: [utensil, bowl], destination: countertop)

    whack(item: egg, with: utensil)
    Place(item: egg.innards, destination: bowl)
    
    Place(item: utensil.end, destination: boilingPot)
    until boilingPot.water is spinning quickly:
        whiskClockwise(utensil)
        
    Place(item: bowl.contents, destination: boilingPot.water.center)
    
    secondsToWait = 100
    wait(secondsToWait)
    
    scoop(item: boilingPot.egg, with: utensil)
    Place(item: utensil.egg, destination: bowl)
```

### Main Program (Computer starts here)
(Human readable instructions and an explanation for why this works)

```
**Main Instructions -- START HERE**

todays_packet = findRamen()
openPacket(todays_packet)

pot = findPot()
filledPot = fillPotWithWater(pot)
boilWater(filledPot)

pot2 = findPot()
filledEggPot = fillPotWithWater(pot2)

boilWater(filledEggPot)
todays_egg = findEgg()
PoachEgg(todays_egg, filledEggPot)

... put the flavor packet in the water (this is a function)
.... then the scallions (function)
..... then the noodles (function)
... wait 3 minutes
... remove and place in bowl (function)
... wait 3 more minutes to cool
```
