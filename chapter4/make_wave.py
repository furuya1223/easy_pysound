import numpy as np
import scipy.io.wavfile
import scipy.signal
import matplotlib.pyplot as plt


def show_waveform(data, rate, xlim=None, ylim=None,
                  title=None, xlabel='time [s]', ylabel='amplitude'):
    duration = len(data) / rate            # 音声全体の長さ（秒）
    time = np.arange(0, duration, 1/rate)  # 各サンプルに対応する時刻の列
    plt.plot(time, data)   # データのプロット
    if title is not None:  # タイトルの設定
        plt.title(title)
    plt.xlabel(xlabel)     # 横軸ラベルの設定
    plt.ylabel(ylabel)     # 縦軸ラベルの設定
    if xlim is not None:   # 横軸表示範囲の設定
        plt.xlim(xlim)
    if ylim is not None:   # 縦軸表示範囲の設定
        plt.ylim(ylim)
    else:
        plt.ylim([-1, 1])
    plt.show()             # 画像の表示


def save(path, data, rate):
    data = np.clip(data * 32768, -32768, 32767).astype(np.int16)
    scipy.io.wavfile.write(path, rate, data)


def make_sinusoid(frequency, amplitude, rate, duration):
    return np.array([amplitude * np.sin(2*np.pi*frequency*i/rate)
                     for i in range(0, rate * duration)])


def make_square(frequency, amplitude, rate, duration):
    return amplitude * scipy.signal.square([2*np.pi*frequency*i/rate
                                            for i in range(0, rate * duration)])


def make_sawtooth(frequency, amplitude, rate, duration):
    return amplitude * scipy.signal.sawtooth([2*np.pi*frequency*i/rate
                                              for i in range(0, rate * duration)])


def make_triangle(frequency, amplitude, rate, duration):
    return amplitude * scipy.signal.sawtooth([2*np.pi*frequency*i/rate
                                              for i in range(0, rate * duration)], 0.5)


def main():
    rate = 44100
    duration = 5

    frequency = 16000
    amplitude = 0.5

    data = make_sinusoid(frequency, amplitude, rate, duration)

    # 波形を拡大表示
    show_waveform(data, rate, xlim=[0, 0.01], title='mosquito')

    # dataをWAVファイルに保存
    save('mosquito.wav', data, rate)

if __name__ == '__main__':
    main()
