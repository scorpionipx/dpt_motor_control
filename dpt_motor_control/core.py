import tkinter as tk

import RPi.GPIO as GPIO

from time import sleep

from os import system


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

    def steps_x4(self, steps=85):
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

    def steps_minus_x4(self, steps=85):
        """steps_minus_x4

        :return:
        """
        for step_index in range(steps):
            sleep(DELAY)
            self.all_off()
            GPIO.output(self.D, True)
            sleep(DELAY)
            self.all_off()
            GPIO.output(self.B, True)
            sleep(DELAY)
            self.all_off()
            GPIO.output(self.C, True)
            sleep(DELAY)
            self.all_off()
            GPIO.output(self.A, True)
            sleep(DELAY)

    def rotate_180(self):
        """rotate_180

        """
        self.steps_x4(85)

    def rotate_20_steps(self):
        """rotate_20_steps

        """
        self.steps_x4(5)

    def rotate_minus_20_steps(self):
        """rotate_minus_20_steps

        """
        self.steps_minus_x4(5)

    @staticmethod
    def shutdown():
        """shutdown

        """
        system('shutdown -h now')


if __name__ == '__main__':
    mc = MotorControl(A, B, C, D)
    sleep(1)

    root = tk.Tk()
    frame = tk.Frame(root, width=600, height=400)
    frame.pack(fill=None, expand=False)

    button = tk.Button(frame,
                       text="QUIT",
                       fg="red",
                       command=mc.shutdown,
                       height=15,
                       width=15,
                       )
    button.pack(side=tk.LEFT)

    button_dummy = tk.Button(frame,
                             text="",
                             fg="red",
                             height=15,
                             width=5,
                            )
    button_dummy.pack(side=tk.LEFT)

    minus_5 = tk.Button(frame,
                       text="LEFT",
                       command=mc.rotate_minus_20_steps,
                       height=15,
                       width=15,)
    minus_5.pack(side=tk.LEFT)

    button_dummy = tk.Button(frame,
                             text="",
                             fg="red",
                             height=15,
                             width=1,
                            )
    button_dummy.pack(side=tk.LEFT)
    slogan = tk.Button(frame,
                       text="+180",
                       command=mc.rotate_180,
                       height=15,
                       width=15,)
    slogan.pack(side=tk.LEFT)

    button_dummy = tk.Button(frame,
                             text="",
                             fg="red",
                             height=15,
                             width=1,
                            )
    button_dummy.pack(side=tk.LEFT)
    plus_5 = tk.Button(frame,
                       text="RIGHT",
                       command=mc.rotate_20_steps,
                       height=15,
                       width=15,)
    plus_5.pack(side=tk.LEFT)

    root.mainloop()

    # while True:
    #     try:
    #         user_steps = int(input())
    #     except ValueError:
    #         break
    #     mc.steps_x4(user_steps)
    #
    # sleep(1)
