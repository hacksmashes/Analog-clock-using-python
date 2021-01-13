from turtle import *
from datetime import datetime

bgcolor("black")
def jump(distance, winkel=0):
    penup()
    right(winkel)
    forward(distance)
    left(winkel)
    pendown()

def hand(height, angle):
    fd(height*1.15)
    rt(90)
    fd(angle/2.0)
    lt(120)
    fd(angle)
    lt(120)
    fd(angle)
    lt(120)
    fd(angle/2.0)

def make_hand_shape(name, height, angle):
    reset()
    jump(-height*0.15)
    begin_poly()
    hand(height, angle)
    end_poly()
    hand_form = get_poly()
    register_shape(name, hand_form)

def clockface(radius):
    reset()
    pensize(5)
    color("white")
    for i in range(60):
        jump(radius)
        if i % 5 == 0:
            fd(25)
            jump(-radius-25)
        else:
            dot(3)
            jump(-radius)
        rt(6)

def setup():
    global second_hand, minute_hand, hour_hand, writer
    mode("logo")
    make_hand_shape("second_hand", 125, 20)
    make_hand_shape("minute_hand",  130, 20)
    make_hand_shape("hour_hand", 90, 20)
    clockface(160)
    second_hand = Turtle()
    second_hand.shape("second_hand")
    second_hand.color("white", "white")
    minute_hand = Turtle()
    minute_hand.shape("minute_hand")
    minute_hand.color("white", "white")
    hour_hand = Turtle()
    hour_hand.shape("hour_hand")
    hour_hand.color("white", "white")
    for hand in second_hand, minute_hand, hour_hand:
        hand.resizemode("user")
        hand.shapesize(1, 1, 3)
        hand.speed(0)
    ht()
    writer = Turtle()
    writer.ht()
    writer.pu()
    writer.bk(85)
    writer.color("white")
    
def days_name(t):
    days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
    return days[t.weekday()]

def month_name(z):
    months = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June",
             "July", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
    j = z.year
    m = months[z.month - 1]
    t = z.day
    return "%s %d %d" % (m, t, j)

def tick():
    t = datetime.today()
    seconds = t.second + t.microsecond*0.000001
    minute = t.minute + seconds/60.0
    hours = t.hour + minute/60.0
    try:
        tracer(False)  
        writer.clear()
        writer.home()
        writer.forward(65)
        writer.write(days_name(t),
                     align="center", font=("times", 14, "italic"))
        writer.back(150)
        writer.write(month_name(t),
                     align="center", font=("times", 14, "italic"))
        writer.forward(85)
        tracer(True)
        second_hand.setheading(6*seconds)  
        minute_hand.setheading(6*minute)
        hour_hand.setheading(30*hours)
        tracer(True)
        ontimer(tick, 100)
    except Terminator:
        pass  

def main():
    tracer(False)
    setup()
    tracer(True)
    tick()
    return "CLOCK"

if __name__ == "__main__":
    mode("logo")
    msg = main()
    print(msg)
    mainloop()
