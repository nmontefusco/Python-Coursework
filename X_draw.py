# Display an X

###################################################
# Student should add code where relevant to the following.

import simplegui 

# Draw handler
def draw_handler(canvas):
    canvas.draw_text("X",(-20,20),48,"Red")

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("X-time",96,96)
frame.set_draw_handler(draw_handler)



# Start the frame animation
frame.start()