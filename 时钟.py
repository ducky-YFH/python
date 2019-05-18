import turtle
import datetime


def skip(distance):
    """
    移动一段距离，不留下痕迹
    :param distance:像素
    :return:
    """
    turtle.penup()
    turtle.forward(distance)
    turtle.pendown()


def draw_clock():
    """画表盘"""
    # 让乌龟的朝向默认向上
    turtle.reset()
    turtle.mode('logo')
    for i in range(60):
        skip(160)
        # 根据5格一个时钟
        if i % 5 == 0:
            # 画时钟
            turtle.pensize(7)
            turtle.forward(20)
            if i == 0:
                turtle.write(12, align='center', font=('Courier',14, 'bold'))
            elif i == 25 or i == 30 or i == 35:
                skip(25)
                turtle.write(int(i / 5), align='center', font=('Courier', 14, 'bold'))
                skip(-25)
            else:
                turtle.write(int(i / 5), align='center', font=('Courier',14, 'bold'))

            skip(-20)
        else:
            turtle.pensize(1)
            turtle.dot()
        skip(-160)
        turtle.right(6)


def get_week(t):
    week = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    return week[t.weekday()]


def create_hand(length, name):
    skip(-length * 0.1)
    turtle.penup()
    turtle.begin_poly()
    turtle.forward(length * 1.1)
    turtle.end_poly()
    turtle.home()
    # 注册
    turtle.register_shape(name, turtle.get_poly())
    hand = turtle.Turtle()
    hand.shape(name)
    hand.shapesize(1, 1, 3)
    return hand


def run():
    t = datetime.datetime.today()
    bob.penup()
    bob._tracer(False)
    bob.forward(65)
    bob.write(get_week(t), align='center', font=('Courier',
                                                 14, 'bold'))
    bob.back(130)
    bob.write(t.strftime('%Y-%m-%d'), align='center', font=('Courier', 14, 'bold'))
    bob.home()
    bob._tracer(True)
    # 指针移动
    second = t.second + t.microsecond * 0.000001
    minute = t.minute + second / 60
    hour = t.hour + minute / 60
    # 设置转向
    second_hand.setheading(6 * second)
    minute_hand.setheading(6 * minute)
    hour_hand.setheading(30 * hour)
    turtle.ontimer(run, 1000)


if __name__ == '__main__':
    # 画时针
    turtle.mode('logo')
    turtle.tracer(False)
    draw_clock()
    turtle.tracer(True)
    global second_hand, minute_hand, hour_hand, bob
    second_hand = create_hand(135, "second_hand")
    minute_hand = create_hand(125, "minute_hand")
    hour_hand = create_hand(90, "hour_hand")
    bob = turtle.Turtle()
    bob.hideturtle()
    # 隐藏小乌龟
    run()
    turtle.mainloop()
