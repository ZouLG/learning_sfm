import os
from map import Map
from frame import Frame
from point import *
from camera import *
import glob


class Sfm(object):
    def __init__(self, dir):
        self.img_name_list = glob.glob(dir + '/*.jpg')
        self.map = Map()

    def reconstruct(self):
        plt.figure()
        ax = plt.gca(projection='3d')
        for k, img in enumerate(self.img_name_list):
            if k < 2:
                self.map.add_a_frame(Frame(), img, 4)
        self.map.plot_map(ax)
        plt.show()


if __name__ == "__main__":
    sfm = Sfm(r"F:\zoulugeng\program\python\01.SLAM\Data\data_qinghuamen\image data")
    sfm.reconstruct()