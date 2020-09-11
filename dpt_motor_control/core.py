import tkinter as tk

import RPi.GPIO as GPIO

from time import sleep


A = 5
B = 6
C = 13
D = 19


GPIO.setmode(GPIO.BCM)
DELAY = 0.005


class MotorControl:
    """

    """
    def __init__(self, a, b, c, d):
        """__init__

        """
        self.A = a
        self.B = b
        self.C = c
        self.D = d

        self.init()
        self.all_off()

    def init(self):
        """init

        :return:
        """
        GPIO.setup(self.A, GPIO.OUT)
        GPIO.setup(self.B, GPIO.OUT)
        GPIO.setup(self.C, GPIO.OUT)
        GPIO.setup(self.D, GPIO.OUT)

    def all_off(self):
        """all_off

        :return:
        """
        GPIO.output(self.A, False)
        GPIO.output(self.B, False)
        GPIO.output(self.C, False)
        GPIO.output(self.D, False)

    def __del__(self):
        """__del__

        :return:
        """
        print('Cleaning GPIO...')
        GPIO.cleanup()

    def steps_x4(self, steps):
        """steps_x4

        :return:
        """
        for step_index in range(steps):
            sleep(DELAY)
            self.all_off()
            GPIO.output(self.A, True)
            sleep(DELAY)
            self.all_off()
            GPIO.output(self.C, True)
            sleep(DELAY)
            self.all_off()
            GPIO.output(self.B, True)
            sleep(DELAY)
            self.all_off()
            GPIO.output(self.D, True)
            sleep(DELAY)


if __name__ == '__main__':
    mc = MotorControl(A, B, C, D)
    sleep(1)

    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

    button = tk.Button(frame,
                       text="QUIT",
                       fg="red",
                       command=quit)
    button.pack(side=tk.LEFT)
    slogan = tk.Button(frame,
                       text="Hello",
                       command=mc.steps_x4(85))
    slogan.pack(side=tk.LEFT)

    root.mainloop()

    # while True:
    #     try:
    #         user_steps = int(input())
    #     except ValueError:
    #         break
    #     mc.steps_x4(user_steps)
    #
    # sleep(1)
