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


def make_wave_from_fourier_series(fourier_series, frequency, rate, duration):
    data = np.zeros((rate*duration))
    dim = fourier_series.shape[0]
    # 各倍音の重ね合わせ
    for i in range(dim):
        data += make_sinusoid(frequency*i, fourier_series[i], rate, duration)
    return data


def main():
    rate = 44100     # サンプリング周波数
    duration = 5     # 出力する音声の長さ（秒）
    frequency = 440  # 生成する音の基本周波数
    amplitude = 0.5  # 生成する音の振幅
    dim = 10         # 何倍音のフーリエ係数まで採用するか

    # ノコギリ波のフーリエ係数の作成
    fourier_series = np.array([0] + [((k % 2)*2-1)*amplitude*2/np.pi/k for k in range(1, dim + 1)])
    # フーリエ係数から波を作成
    data = make_wave_from_fourier_series(fourier_series, frequency, rate, duration)

    # 波形を拡大表示
    show_waveform(data, rate, xlim=[0, 0.01], title='sawtooth')

    # dataをWAVファイルに保存
    save('sawtooth_dim{}.wav'.format(dim), data, rate)

if __name__ == '__main__':
    main()
