#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-07
# Desc: 贝塞尔曲线点

from math import fsum

import numpy as np


def gen_bezier(points):
    """
    P0和P3是endpoints, P1和P2是control points
    参考通用贝塞尔通用计算公式
    :param points:
    :return:
    """
    content = ""
    upper_left = ""
    upper_left_list = []
    lower_left = ""
    lower_left_list = []
    upper_right = ""
    upper_right_list = []
    lower_right = ""
    lower_right_list = []
    # 计算步骤
    step = 0.01

    # 所有点的个数P0 P1... Pn
    points_no = len(points) - 1
    for i, t in enumerate(np.arange(0, 1.00 + step, step), start=1):
        x_list, y_list, y_sym = [], [], []
        for index, point in enumerate(points):
            x_value = point[0] * pow(1 - t, points_no - index) * pow(t, index)
            x_list.append(x_value)
            y_value = point[1] * pow(1 - t, points_no - index) * pow(t, index)
            y_list.append(y_value)

        x = fsum(x_list)
        y = fsum(y_list)
        print("Step{}: {} {}".format(i, x, y))
        upper_left_list.append([x, y])
        lower_left_list.append([x, 300 - y])

        upper_right_list.append([180 - x + 1340, y])
        lower_right_list.append([180 - x + 1340, 300 - y])
        if i == 1:
            # moveto
            upper_left += "M{} {} ".format(x, y)
            lower_left += "M{} {} ".format(x, 300 - y)
            upper_right += "M{} {} ".format(180 - x + 1340, y)
            lower_right += "M{} {} ".format(180 - x + 1340, 300 - y)
        else:
            # lineto
            upper_left += "L{} {} ".format(x, y)
            lower_left += "L{} {} ".format(x, 300 - y)
            upper_right += "L{} {} ".format(180 - x + 1340, y)
            lower_right += "L{} {} ".format(180 - x + 1340, 300 - y)

    content += ("""<path stroke="#000000" id="svg_3" d="{}" stroke-width="1" fill="none"/>\
                  <path stroke="#000000" id="svg_3" d="{}" stroke-width="1" fill="none"/>""".format(upper_left,
                                                                                                    lower_left))
    content += ("""<path stroke="#000000" id="svg_3" d="{}" stroke-width="1" fill="none"/>""".format(upper_right))
    content += ("""<path stroke="#000000" id="svg_3" d="{}" stroke-width="1" fill="none"/>""".format(lower_right))
    return content, upper_left_list, lower_left_list, upper_right_list, lower_right_list
