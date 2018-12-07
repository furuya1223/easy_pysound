import numpy as np
import scipy.io.wavfile
import scipy.signal
import matplotlib.pyplot as plt


def make_sinusoid(frequency, amplitude, rate, duration):
    return np.array([amplitude * np.sin(2*np.pi*frequency*i/rate)
                     for i in range(0, rate * duration)])


def make_sawtooth(frequency, amplitude, rate, duration):
    return amplitude * scipy.signal.sawtooth([2*np.pi*frequency*i/rate
                                              for i in range(0, rate * duration)])


def make_triangle(frequency, amplitude, rate, duration):
    return amplitude * scipy.signal.sawtooth([2*np.pi*frequency*i/rate
                                              for i in range(0, rate * duration)], 0.5)


def make_square(frequency, amplitude, rate, duration):
    return amplitude * scipy.signal.square([2*np.pi*frequency*i/rate
                                            for i in range(0, rate * duration)])


def show_waveform(data, rate, duration, xlim=None, ylim=None,
                  title=None, xlabel='time [s]', ylabel='amplitude'):
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


def save(path, rate, data):
    data = np.clip(data * 32768, -32768, 32767).astype(np.int16)
    scipy.io.wavfile.write(path, rate, data)


def main():
    rate = 44100
    duration = 5

    frequency = 440
    amplitude = 0.5

    data = make_sinusoid(frequency, amplitude, rate, duration)

    # 波形を拡大表示
    show_waveform(data, rate, duration, xlim=[1, 1.01], title='sinusoid')

    # dataをWAVファイルに保存
    save('sinusoid.wav', rate, data)

if __name__ == '__main__':
    main()
