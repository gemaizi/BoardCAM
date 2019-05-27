#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-07
# Desc: BoardCAM主程序


from arc import gen_arc
from bezier import gen_curve
from gcode_export import export_gcode
from inserts import gen_inserts
from pdf_export import export_pdf
from svg_export import export_svg, gen_circle_path

if __name__ == "__main__":
    # 参数含义参考docs/Configuration.md
    origin = (0, 0)
    params = {
        # Nose Shape
        "nose_width": 300,
        "nose_length": 180,

        # Tail Shape
        "tail_width": 300,
        "tail_length": 180,

        "running_length": 1160,
        "sidecut_radius": 8000,

        # insert
        "stand_width": 550,
        "stand_setback": 0,
        "horizontal_spacing": 40,
        "vertical_spacing": 40,
        "inserts_number": 4,

        # curve
        "end_handle": 0.4,
        "transition_handle": 2,

        # profile
        "tip_radius": 300,
        "camber": 15,
        "thickness":  7,
        "camber_setback": 0,
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

    # export
    export_pdf(params, points, insert_coordinate_list)
    export_svg(params, points, insert_coordinate_list)
    export_gcode(points)
    gen_circle_path(params)
