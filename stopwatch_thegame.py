# template for "Stopwatch: The Game"

import simplegui
# define global variables
global counter
global successcount
global attemptcount
global time




counter = 0
successcount = 0
attemptcount = 0
time = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    a = t//600
    b = ((t //10) %60) //10
    c= (t //10) %10
    d= t%10
    
    return str(a) + ":" + str(b) + str(c) +"." + str(d)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global time
    timer.start()
    time = True
    
def stop():
    global counter,time,successcount,attemptcount
    
    timer.stop()
    time = False
    attemptcount+=1
    if (counter % 10 == 0):
        successcount += 1
    
         
def reset():
    global counter,successcount,attemptcount,time
    counter = 0
    time = True
    successcount = 0
    attemptcount = 0
    
# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    counter +=1
    

# define draw handler
def draw(canvas):
        canvas.draw_text(format(counter),(100,100),24,'White')
        canvas.draw_text(str(successcount) + "/" + str(attemptcount),(100,60),24,"Red")
       
        
# create frame
frame = simplegui.create_frame("Time to par-tay", 200,200)
timer = simplegui.create_timer(100,tick) 
frame.set_draw_handler(draw)

# register event handlers
button1 = frame.add_button("Start",start,100)
button2 = frame.add_button("Stop",stop,100)
button3 = frame.add_button("Reset",reset,100)

# start frame
frame.start()
