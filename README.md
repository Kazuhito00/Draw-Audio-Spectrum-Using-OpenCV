# Draw-Audio-Spectrogram-Using-OpenCV
オーディオスペクトラムや波形をOpenCVで描画するサンプルです。<br>

# Requirement
```
opencv-python 4.5.5.62 or later
PyAudio 0.2.11         or later
```

WindowsでPyAudioをインストールしたい方は、自力でビルドするか、<br>
[非公式のWindowsビルドPyAudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)を用いてください。


# Contents
<table>
    <tr>
        <td width="50">
            No.0
        </td>
        <td width="640">
            <img src="https://user-images.githubusercontent.com/37477845/184486210-a7b4f36e-ebc6-4a3b-99e4-2a94ecc9bb8d.gif" loading="lazy" width="620px">
        </td>
    </tr>
    <tr>
        <td width="50">
            No.1
        </td>
        <td width="640">
            <img src="https://user-images.githubusercontent.com/37477845/184486230-f57a14bd-4616-4c84-93b2-51b66b5d4030.gif" loading="lazy" width="620px">
        </td>
    </tr>
    <tr>
        <td width="50">
            No.2
        </td>
        <td width="640">
            <img src="https://user-images.githubusercontent.com/37477845/184486234-50d0caad-6deb-4c81-9871-f0d3235a95b3.gif" loading="lazy" width="240px">
        </td>
    </tr>
    <tr>
        <td width="50">
            No.3
        </td>
        <td width="640">
            <img src="https://user-images.githubusercontent.com/37477845/184486246-6225aab4-71a6-4d16-9ffe-36f8950cf340.gif" loading="lazy" width="620px">
        </td>
    </tr>
    <tr>
        <td width="50">
            No.4
        </td>
        <td width="640">
            <img src="https://user-images.githubusercontent.com/37477845/184486280-d920223c-678b-4581-ae4e-a47200e46e4e.gif" loading="lazy" width="620px">
        </td>
    </tr>
</table>

# Usage
デモの実行方法は以下です。
```bash
python sample.py
```
* --device<br>
マイクなどの入力デバイス番号の指定<br>
デフォルト：1
* --wave<br>
Waveファイルの指定 ※指定時はマイクデバイスより優先<br>
デフォルト：指定なし
* --frames<br>
フレーム読み出し数<br>
デフォルト：2048
* --fft_n<br>
FFTポイント数<br>
デフォルト：1024
* --draw_type<br>
Contentsの描画種別<br>
デフォルト：0

# Author
高橋かずひと(https://twitter.com/KzhtTkhs)
 
# License 
Draw-Audio-Spectrogram-Using-OpenCV is under [Apache-2.0 license](LICENSE).<br><br>
