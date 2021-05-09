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
    transform farleft:
        xanchor 0.5 xalign -0.06 yalign 1.0
    transform left:
        xanchor 0.5 xalign 0.22 yalign 1.0
    transform center:
        xanchor 0.5 xalign 0.5 yalign 1.0
    transform right:
        xanchor 0.5 xalign 0.78 yalign 1.0 xzoom -1
    transform farright:
        xanchor 0.5 xalign 1.06 yalign 1.0 xzoom -1

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
    define fadeabrupt = Fade(0.5, 1.0, 0.0)
    define fadehold = Fade(0.0, 1.0, 1.0)
    define flash = Fade(0.0, 0.10, .25, color="#fff")
    stop music
    
    play sound "sfx-foliagerustle.mp3"
    u "{cps=3}...{/cps}"
    u "Almost there..."
    play sound "sfx-foliagerustle.mp3"
    u "{cps=3}...{/cps}"
    play sound "sfx-breakbranch.mp3"
    u "{cps=3}..!{/cps}" with vpunch
    u "{cps=2}...{/cps}{cps=10}There you are{/cps}{cps=3}...{/cps}"
    play music "song-closing.ogg"
    scene forest with fadehold
    show p01 at left with moveinleft
    p "..."
    #
    python:
        # Let's show a couple screens that may have buttons on them.
        # we could use different layers, but this time let's
        # use the master layer so that they're on the same level.
        renpy.show_screen("exit_buttons", _layer="master")
    python:
        # Makes the program hang out here until the user clicks something.
        # Doing things in this way lets us show multiple screens with buttons.
        ui.interact()
    #
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
            show a01 at right_c with moveinright
            p "Damn flea-bitten stray."
            p "Once I'm done with you, the only thing you'll have to do with reading is your name being in the obituaries."
            menu:
                "Take His Picture":
                    p "Alright, let's get this over with."
                    p "Once the school paper has his picture, I'm sure this'll be over."
                    show black with fadeabrupt
                    "Patches aims the camera at the cat..."
                    hide black with flash
                    jump introforestafterpicture
                "Not Yet":
                    p "Hmm..."
                    hide a01 with moveoutright
                    jump introforestmenu
            
            label introforestafterpicture: #seems labels have to follow indent heiarchy as well, shame.
                p "Shit! Why is the flash on?!"
            
    return
