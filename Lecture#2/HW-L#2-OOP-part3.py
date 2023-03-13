from abc import ABC


class Laptop:

    def screen(self):
        return None

    def keyboard(self):
        return None

    def touchpad(self):
        return None

    def webcam(self):
        return None

    def ports(self):
        return None

    def dynamics(self):
        return None


class HPLaptop(Laptop):
    def screen(self):
        return "15.6 in, Touchscreen Multi-Touch, LCD IPS, 1366 x 768 Pixels, 16:9 Aspect Ratio, 220 Nits, 60 Hz"

    def keyboard(self):
        return "6 Rows, No Backlight, QWERTY, US English, Extended Sized ( with Number Pad with function keys )"

    def touchpad(self):
        return "Multi-Touch"

    def webcam(self):
        return "HP TrueVision HD Camera"

    def ports(self):
        return "2 USB 3.1 Gen 1 (Data transfer only); 1 USB 2.0; 1 HDMI; 1 RJ-45"

    def dynamics(self):
        return "High Definition (HD) Audio"


laptop = HPLaptop()
print(laptop.screen())
print(laptop.keyboard())
print(laptop.touchpad())
print(laptop.webcam())
print(laptop.ports())
print(laptop.dynamics())
