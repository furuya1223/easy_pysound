import numpy as np
import scipy.io.wavfile
import matplotlib.pyplot as plt


def main():
    # 音声ファイル読み込み
    wav_filename = 'sample.wav'
    rate, data = scipy.io.wavfile.read(wav_filename)
    data = data / 32768

    length = len(data) / rate                 # 音声の長さ(sec)
    time = np.arange(0, length, 1/rate)       # 各サンプルに対応する時刻の列
    plt.plot(time, data)                      # 音声波形の表示
    plt.title('waveform of ' + wav_filename)  # タイトル設定
    plt.xlabel('time[s]')                     # 横軸ラベル設定
    plt.ylabel('amplitude')                   # 縦軸ラベル設定
    plt.ylim([-1, 1])                         # 縦軸表示範囲設定
    plt.show()                                # グラフの表示


if __name__ == '__main__':
    main()
