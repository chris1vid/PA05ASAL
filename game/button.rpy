init python:

    # Create a variable to keep track of whether we're in a conversation
    global jump_lock
    jump_lock = 0

    # Only jump to the label if the lock is 0 (false), indicating we're
    # not already in a conversattion.
    def locked_jump(jump_label):
        global jump_lock
        if jump_lock == 0:
            jump_lock = 1
            renpy.jump(jump_label)
            # After the conversation at jump_label is finished, we'll come
            # back to this point and set jump_lock to 0, allowing jumps again.
            jump_lock = 0

    # Helper function for clearing the lock, if u need it
    def clear_lock():
        global jump_lock
        jump_lock = 0

    # No need for this junk no more
    # def jump(jump_label):
    #     renpy.jump(jump_label)

#############################################################
#              LAYERED EXIT BUTTON EXAMPLE
#############################################################
define exit_button_pos = (120,350)

# The exit_buttons screen contains the exit button over to the left
screen exit_buttons():
    button:
        add "layered_exit_button" # match the name!
        xysize (203, 120) # Match the size of the image
        pos exit_button_pos
        action [Return(), Function(locked_jump, jump_label="introforestmenu")]

# Describe the different states of the button
image layered_exit_button:
    on idle:
        "buttons/button01.png"
    on hover:
        "layered_exit_hover" # Match the name of your fancy image

# Define the image displayed when you hover over the button.
image layered_exit_hover = Composite(
    (0, 0),
    (0, 0), "buttons/button01Glow.png",
    (0, 0), "buttons/button01.png" )
