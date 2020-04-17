import cv2
from point import *
import numpy as np


class KeyPoint(cv2.KeyPoint):
    def __init__(self, kp, des, pw=Point3D((0, 0, 0))):
        self.angle = kp.angle
        self.response = kp.response
        self.class_id = kp.class_id
        self.size = kp.size
        self.octave = kp.octave
        self.pt = kp.pt

        self.des = des
        self.pw = pw
        self.frm_list = []

    def __repr__(self):
        return "pi = " + str(self.pt) + "    pw = " + str(self.pw)


if __name__ == "__main__":
    pass
