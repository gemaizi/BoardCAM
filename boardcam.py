#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-07
# Desc: BoardCAM主程序


from arc import gen_arc
from bezier import gen_curve
from gcode_export import gen_gcode
from inserts import gen_inserts
from pdf_export import draw_pdf
from svg_export import draw_svg

if __name__ == "__main__":
    # 参数含义参考docs/Configuration.md
    origin = (0, 0)

    # Nose Shape
    nose_width = 300
    half_nose_width = nose_width / 2
    nose_length = 180

    # Tail Shape
    tail_width = 300
    half_tail_width = tail_width / 2
    tail_length = 180

    running_length = 1160
    half_running_length = running_length / 2
    overall_length = nose_length + running_length + tail_length
    half_overall_length = overall_length / 2
    sidecut_radius = 8000

    # insert
    inserts_number = 4
    horizontal_spacing = 40
    vertical_spacing = 40
    stand_setback = 0
    stand_width = 550

    # profile
    nose_tip_radius = 300
    camber = 15
    camber_setback = 0
    tail_tip_radius = 300
    thickness = 7

    # curve
    end_handle = 0.4
    transition_handle = 2

    params = {
        "overall_length": overall_length,
        "half_overall_length": overall_length / 2,
        "running_length": running_length,
        "half_running_length": half_running_length,
        "nose_width": nose_width,
        "half_nose_width": half_nose_width,
        "half_tail_width": half_tail_width,
        "tail_width": tail_width,
        "nose_length": nose_length,
        "tail_length": tail_length,
        "sidecut_radius": sidecut_radius,
        "stand_width": stand_width,
        "stand_setback": stand_setback,
        "horizontal_spacing": horizontal_spacing,
        "vertical_spacing": vertical_spacing,
        "inserts_number": inserts_number,
        "end_handle": end_handle,
        "transition_handle": transition_handle,
    }

    # 板头&板尾曲线路径生成
    upper_left_list, lower_left_list, upper_right_list, lower_right_list = gen_curve(params)

    # 有效边刃路径生成
    points = []
    top_list, bottom_list = gen_arc(params)
    points.extend(lower_left_list)
    points.extend(top_list)
    points.extend(lower_right_list)
    points.extend(upper_right_list)
    points.extend(bottom_list)
    points.extend(upper_left_list)

    # 嵌件路径生成
    insert_coordinate_list = gen_inserts(params)
    draw_pdf(params, points, insert_coordinate_list)

    draw_svg(params, points, insert_coordinate_list)
    gen_gcode(points)
