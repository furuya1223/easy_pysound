import numpy as np
import scipy.io.wavfile
import matplotlib.pyplot as plt
import librosa
import librosa.display


def get_log_power(data, fft_size, hop_length):
    # 短時間フーリエ変換の結果の絶対値を取って振幅を取得
    # amplitude[f, t] = t フレーム目における f 番目の周波数成分の振幅
    amplitude = np.abs(librosa.core.stft(data,
                                         n_fft=fft_size,
                                         hop_length=hop_length))
    # 振幅をパワー（振幅の二乗）の対数に変換（単位は[dB]）
    log_power = librosa.core.amplitude_to_db(amplitude)
    return log_power


def show_spectrogram(data, rate, fft_size, hop_length):
    # 対数パワーを取得
    log_power = get_log_power(data, fft_size, hop_length)
    # 対数パワーを、横軸時間・縦軸周波数で表示
    librosa.display.specshow(log_power,
                             sr=rate,
                             hop_length=hop_length,
                             x_axis='time',
                             y_axis='hz',
                             cmap='magma')
    plt.title('Power spectrogram')    # 図のタイトル設定
    plt.colorbar(format='%+2.0f dB')  # 色とデシベル値の対応図を表示
    plt.tight_layout()                # 余白を小さくする
    plt.show()                        # 図を表示する


def main():
    # 音声ファイル読み込み
    wav_filename = 'sawtooth_dim10.wav'
    rate, data = scipy.io.wavfile.read(wav_filename)
    data = data / 32768

    fft_size = 1024                  # フレーム長
    hop_length = int(fft_size / 4)  # フレームシフト長

    show_spectrogram(data, rate, fft_size, hop_length)


if __name__ == '__main__':
    main()
