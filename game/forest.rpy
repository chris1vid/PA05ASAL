# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Patches", color = "#aa98c7", what_prefix='"', what_suffix='"')
define c = Character("Coco", color = "#dbd04b", what_prefix='"', what_suffix='"')
define a = Character("Angel", color = "#a1e7fd", what_prefix='"', what_suffix='"')
define u = Character("???", color = "#fff", what_prefix='"', what_suffix='"')
define g = Character("Ghosts", color = "#fff", what_prefix='"', what_suffix='"')


# The game starts here.

label start:

    transform left_c:
        xalign .1 yalign 1.0
    transform right_c:
        xalign 0.9 yalign 1.0
    transform icon_c:
        xalign 0.02 yalign 0.04
    transform icon_c2:
        xalign 0.11 yalign 0.04
    transform love_c:
        xalign 0.0043 yalign 0.15
    transform love_c2:
        xalign 0.097 yalign 0.15

    init python:
        renpy.music.register_channel ("sound2", "sfx", False)


    $ angelgoodpoints = 0
    $ angelbadpoints = 0
    $ cocogoodpoints = 0
    $ cocobadpoints = 0

    $ inventory = ["invcamera"]
    $ introplayed = False
    $ talkedtoangelday1 = False
    $ examinedcamera = False
    jump introforest



## *** *** *** *** *** FOREST START
    label introforest:
    image black = "black.jpg"
    image forest = "forest.jpg"
    scene black with dissolve
    define fadehold = Fade(0.0, 1.0, 1.0)
    stop music
    
    play sound "sfx-foliagerustle.mp3"
    u "{cps=3}...{/cps}"
    u "Almost there..."
    play sound "sfx-foliagerustle.mp3"
    u "{cps=3}...{/cps}"
    play sound "sfx-breakbranch.mp3"
    u "{cps=3}..!{/cps}" with vpunch
    u "{cps=2}...{/cps}{cps=10}There you are{/cps}{cps=3}...{/cps}"
    scene forest with fadehold
    show p01 with moveinleft
    p "..."
    label introforestmenu:
    menu: 
        "Examine Forest":
            p "Everything's all shriveled up, hardly appropriate to hide behind."
            p "Though I don't much enjoy hiding anyhow; feels like letting that thing {i}win{/i}."
            jump introforestmenu
        "Examine Oak Tree": 
            p "I'd bet you anything it knows I like sitting there."
            p "It probably wants to keep me away from cat territory by scaring me off."
            p "..."
            p "Let's see how well that works out!"
            jump introforestmenu
        "Examine Camera":
            if examinedcamera == False:
                p "An old clunky polarioid camera."
                p "Shame about the stickers ruining it's asthetic."
                p "I tried peeling some off, but that just made it worse."
                p "I can only hope it still has film in it."
                $ examinedcamera = True
                jump introforestmenu
            elif examinedcamera == True:
                p "On second thought, I should've just kept the stickers on, this thing is ruined."
                jump introforestmenu
        "Examine Cat":
            p "Damn flea-bitten stray."
            p "Once I'm done with you, the only thing you'll have to do with reading is your name being in the obituaries."
            menu:
                "Take His Picture":
                    "fart"
                "Not Yet":
                    p "Hmm..."
                    jump introforestmenu
            
            
    return
