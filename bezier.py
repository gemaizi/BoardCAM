#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-07
# Desc: 贝塞尔曲线点

from math import fsum


def gen_bezier(points):
    """
    P0和P3是endpoints, P1和P2是control points
    参考通用贝塞尔通用计算公式
    :param points:
    :return:
    """
    upper_left_list = []
    lower_left_list = []
    upper_right_list = []
    lower_right_list = []
    # 计算步骤
    step = 0.01
    end = 1
    step_count = int(end / step)

    # 所有点的个数P0 P1... Pn
    points_no = len(points) - 1
    for i, t in enumerate(range(step_count + 1), start=1):
        t *= step
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

    return upper_left_list, lower_left_list, upper_right_list, lower_right_list
