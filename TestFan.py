from Fan import Fan
def main():
    fan1 = Fan()
    fan1.setFanOn()
    fan1.setSpeedFast()
    fan1.setRadius(10)
    fan1.setColor('yellow')

    fan2 = Fan()
    fan2.setFanOff()
    fan2.setSpeedMedium()
    fan2.setRadius(5)
    fan2.setColor('blue')

    print("Fan1: Speed-{}, Radius-{}, Color-{}, On-{}".format(fan1.getSpeed(), fan1.getRadius(), fan1.getColor(), fan1.getOn()))
    print("Fan2: Speed-{}, Radius-{}, Color-{}, On-{}".format(fan2.getSpeed(), fan2.getRadius(), fan2.getColor(),
                                                              fan2.getOn()))
main()