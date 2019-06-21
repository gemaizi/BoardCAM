#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-06-13
# Desc: 

from math_tools import INCH


class CNCRouter:
    def __init__(self, name, unit):
        self.name = name
        self.unit = unit
        # 加工面积 (工件要小于)
        # Spindle Speed
        # Feed rate
        # 安全加工距离
        # Drilling speed
        # 单层步距


class RouterBits:
    def __init__(self, diameter, desc):
        if diameter[-2:] == "in":
            self.diameter = self.inch_to_mm(float(eval(diameter[:-2])))
        elif diameter[-4:] == "inch":
            self.diameter = self.inch_to_mm(float(eval(diameter[:-4])))
            print(self.diameter)
        elif diameter[-2:] == "mm":
            self.diameter = float(eval(diameter[:-2]))
        elif diameter[-2:] == "cm":
            self.diameter = float(eval(diameter[:-2])) * 10
        else:
            raise ValueError("diameter variable must specify the unit. (support inch、in、cm、mm)")
        self.radius = self.cal_radius()
        self.description = desc
        self.blade_length = None
        self.blade_number = 1

    def cal_radius(self):
        return self.diameter / 2

    @staticmethod
    def inch_to_mm(inch_value):
        """

        :param inch_value:
        :return: mm
        """
        return inch_value * INCH


if __name__ == '__main__':
    # cnc = CNCRouter("TigerCNC", "metric")
    bit = RouterBits("1/4inch", "1/4英寸螺旋向上双刃")
    print(bit.radius)