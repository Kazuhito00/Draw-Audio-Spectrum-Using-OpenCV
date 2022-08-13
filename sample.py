#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

import cv2
import wave
import pyaudio
import numpy as np

from draw_audio_function import (
    draw_audio_spectrum01,
    draw_audio_spectrum02,
    draw_audio_spectrum03,
    draw_audio_waveform01,
    draw_audio_waveform02,
)

draw_function_list = [
    draw_audio_spectrum01,
    draw_audio_spectrum02,
    draw_audio_spectrum03,
    draw_audio_waveform01,
    draw_audio_waveform02,
]


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--wave", type=str, default=None)
    parser.add_argument("--device", type=int, default=1)

    parser.add_argument("--frames", type=int, default=2048)
    parser.add_argument("--fft_n", type=int, default=1024)

    parser.add_argument("--draw_type", type=int, default=0)

    args = parser.parse_args()

    return args


def main():
    args = get_args()

    filename = args.wave
    device_index = args.device
    frame_n = args.frames
    fft_sample_size = args.fft_n

    draw_type = args.draw_type

    # オーディオストリームを開く
    audio = pyaudio.PyAudio()
    if filename is not None:
        # Waveファイル
        wave_file = wave.open(filename, "r")

        format = audio.get_format_from_width(wave_file.getsampwidth())
        nchannels = wave_file.getnchannels()
        framerate = wave_file.getframerate()
        input_mode = False
        input_device_index = device_index
        frames_per_buffer = frame_n
    else:
        # マイクなどのデバイス
        format = pyaudio.paInt16
        nchannels = 1
        framerate = 44100
        input_mode = True
        input_device_index = device_index
        frames_per_buffer = frame_n

    audio_stream = audio.open(
        format=format,
        channels=nchannels,
        rate=framerate,
        input=input_mode,
        input_device_index=input_device_index,
        output=True,
        frames_per_buffer=frames_per_buffer,
    )

    # ハミング窓生成
    hamming_window = np.hamming(fft_sample_size)

    while True:
        if filename is not None:
            # Waveファイル フレーム読み込み
            frame = wave_file.readframes(frame_n)
            if frame == b'':
                break
        else:
            # デバイスからの読み込み
            frame = audio_stream.read(frame_n)

        # フレーム再生
        audio_stream.write(frame)

        # オーディオスペクトラム用データを生成
        # 正規化バッファ取得
        buffer = np.frombuffer(frame, dtype="int16") / 32767
        # 一部分のみ切り出し
        # （正確なスペクトログラムが欲しいわけではないので処理時間短縮のためにシフト省略）
        if buffer.shape[0] > fft_sample_size:
            sampling_data = buffer[buffer.shape[0] - fft_sample_size:]
        # 窓適応
        sampling_data = hamming_window * sampling_data
        # 周波数解析
        frequency = np.fft.fft(sampling_data)
        amplitude = np.abs(frequency)
        amplitude_spectrum = 20 * np.log(amplitude)

        # 描画
        image = draw_function_list[draw_type](
            amplitude_spectrum,
            sampling_data,
        )

        cv2.imshow('Draw-Audio-Spectrum-Using-OpenCV Sample', image)

        key = cv2.waitKey(1)
        if key == 27:  # ESC
            break

    audio_stream.close()
    audio.terminate()


# --------------------------------------------------------------------
if __name__ == "__main__":
    main()
