from datetime import datetime
import datetime as dtime
import turtle as t

# Turtle setup
wn = t.Screen()
wn.title("Countdown till Xenoblade Chronicles 3 release!")
wn.bgcolor("black")
wn.setup(width = 600, height = 400)
wn.tracer(0)

# pens
pen1 = t.Turtle()
pen1.speed(0)
pen1.color("white")
pen1.penup()
pen1.hideturtle()
pen1.goto(0, 140)
pen1.write("Waiting finished in percent:", align="center", font=("Courier", 24, "normal"))
pen1.goto(0, 20)
pen1.color("lime")
pen1.write("Already waited:", align="center", font=("Courier", 24, "normal"))
pen1.goto(0, -120)
pen1.color("red")
pen1.write("Waiting left:", align="center", font=("Courier", 24, "normal"))

pen2 = t.Turtle()
pen2.speed(0)
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(0, 90)

pen3 = t.Turtle()
pen3.speed(0)
pen3.color("lime")
pen3.penup()
pen3.hideturtle()
pen3.goto(0, -30)

pen4 = t.Turtle()
pen4.speed(0)
pen4.color("red")
pen4.penup()
pen4.hideturtle()
pen4.goto(0, -170)


# setting dates
date_start = "2022/02/09 23:00:00.000000"
date_goal = "2022/7/29 12:00:00.000000"

# transforming dates
date_format_str = '%Y/%m/%d %H:%M:%S.%f'
start = datetime.strptime(date_start, date_format_str)
goal = datetime.strptime(date_goal, date_format_str)


while True:
    wn.update()

    temp_today_date = str(dtime.datetime.now())
    today_date = str(temp_today_date[0:4]) + "/" + str(temp_today_date[5:7]) + "/" + str(
        temp_today_date[8:10]) + " " + str(temp_today_date[11:])
    today = datetime.strptime(today_date, date_format_str)

    # calculation
    diff_tot = goal - start
    # diff_tot_sec = diff_tot.total_seconds()
    diff_done = today - start
    # diff_done_sec = diff_done.total_seconds()
    done = diff_done / diff_tot
    done_perc = done * 100

    # window
    pen2.clear()
    pen2.write(f"{str(done_perc)[:14]}", align="center", font=("Courier", 24, "normal"))
    pen3.clear()
    pen3.write(f"{str(diff_done)}", align="center", font=("Courier", 24, "normal"))
    pen4.clear()
    pen4.write(f"{str(diff_tot - diff_done)}", align="center", font=("Courier", 24, "normal"))
