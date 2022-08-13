#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np


def draw_audio_spectrum01(
        amplitude_spectrum,
        sampling_data,
        width=854,
        height=240,
        bar_num=60,
        bar_gap=1,
        bg_color=(0, 0, 0),
        plot_color=(0, 255, 0),
):
    image = np.zeros((height, width, 3))
    cv2.rectangle(
        image,
        (0, 0),
        (width, height),
        bg_color,
        thickness=-1,
    )

    bar_width = width / bar_num

    for index in range(bar_num):
        value = amplitude_spectrum[index * 2 + 0]
        value *= int(height / 20)
        if np.isinf(value):
            value = 0

        bar_x1 = int(bar_width * (index + 0) + bar_gap)
        bar_y1 = int(height)
        bar_x2 = int(bar_width * (index + 1) - bar_gap)
        bar_y2 = int(max(height - value / 4, 0))

        cv2.rectangle(
            image,
            (bar_x1, bar_y1),
            (bar_x2, bar_y2),
            plot_color,
            thickness=-1,
        )

    return image


def draw_audio_spectrum02(
        amplitude_spectrum,
        sampling_data,
        width=854,
        height=240,
        bar_num=60,
        bar_gap=6,
        bg_color=(0, 0, 0),
        plot_color=(255, 255, 255),
):
    image = np.zeros((height, width, 3))
    cv2.rectangle(
        image,
        (0, 0),
        (width, height),
        bg_color,
        thickness=-1,
    )

    bar_width = width / bar_num
    center_y = int(height / 2)

    for index in range(bar_num):
        value = amplitude_spectrum[index * 2 + 0]
        value *= int(height / 40)
        if value < 0:
            value = 0

        bar_x1 = int(bar_width * (index + 0) + bar_gap)
        bar_y1 = int(height) - center_y
        bar_x2 = int(bar_width * (index + 1) - bar_gap)
        bar_y2 = int(max(height - value / 4, 0)) - center_y

        cv2.rectangle(
            image,
            (bar_x1, bar_y1),
            (bar_x2, bar_y2),
            plot_color,
            thickness=-1,
        )

        bar_y2 = int(max(value / 4, 0)) + center_y

        cv2.rectangle(
            image,
            (bar_x1, bar_y1),
            (bar_x2, bar_y2),
            plot_color,
            thickness=-1,
        )

    return image


def draw_audio_spectrum03(
        amplitude_spectrum,
        sampling_data,
        width=480,
        height=480,
        radius=100,
        bar_num=64,
        thickness=3,
        bg_color=(0, 0, 0),
        plot_color=(0, 128, 255),
):
    image = np.zeros((height, width, 3))
    cv2.rectangle(
        image,
        (0, 0),
        (width, height),
        bg_color,
        thickness=-1,
    )

    for index in range(bar_num):
        value = amplitude_spectrum[index + 0]
        value *= int(height / (radius))
        if value < 0:
            value = 0

        rad = (2 * np.pi) * (index / bar_num)
        x1 = int(width / 2 + np.sin(rad) * radius)
        y1 = int(height / 2 - np.cos(rad) * radius)
        rad = (2 * np.pi) * (index / bar_num)
        x2 = int(width / 2 + np.sin(rad) * (radius + value / 4))
        y2 = int(height / 2 - np.cos(rad) * (radius + value / 4))

        cv2.line(image, (x1, y1), (x2, y2), plot_color, thickness=thickness)

    return image


def draw_audio_waveform01(
        amplitude_spectrum,
        sampling_data,
        width=854,
        height=240,
        thickness=2,
        bg_color=(255, 255, 255),
        plot_color=(255, 0, 0),
):
    original_width = len(sampling_data)
    center_y = int(height / 2)

    image = np.zeros((height, original_width, 3))
    cv2.rectangle(
        image,
        (0, 0),
        (original_width, height),
        bg_color,
        thickness=-1,
    )

    prev_value = None
    for index, point in enumerate(sampling_data):
        value = center_y + int(point * height)
        if prev_value is not None:
            cv2.line(
                image,
                (index - 1, prev_value),
                (index, value),
                plot_color,
                thickness=thickness,
                lineType=cv2.LINE_8,
            )
        prev_value = value

    image = cv2.resize(image, (width, height))

    return image


def draw_audio_waveform02(
        amplitude_spectrum,
        sampling_data,
        width=854,
        height=240,
        thickness=2,
        n_conv=32,
        bg_color=(255, 255, 255),
        plot_color=(0, 0, 0),
):
    original_width = len(sampling_data)
    center_y = int(height / 2)

    image = np.zeros((height, original_width, 3))
    cv2.rectangle(
        image,
        (0, 0),
        (original_width, height),
        bg_color,
        thickness=-1,
    )

    sampling_data_valid = np.convolve(
        np.array(sampling_data),
        (np.ones(n_conv) / n_conv),
        mode='valid',
    )

    prev_value = None
    for index, point in enumerate(sampling_data_valid):
        value = center_y + int(point * height)
        if prev_value is not None:
            cv2.line(
                image,
                (index - 1, prev_value),
                (index, value),
                plot_color,
                thickness=thickness,
                lineType=cv2.LINE_8,
            )
        prev_value = value

    image = cv2.resize(image, (width, height))

    return image
