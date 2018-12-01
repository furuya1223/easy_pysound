import numpy as np
import scipy.io.wavfile


def main():
    # 音声ファイルパスを指定
    wav_filename = 'sample.wav'

    # 音声ファイル読み込み（面倒なので正規化しない）
    rate, data = scipy.io.wavfile.read(wav_filename)

    print(rate)

    # サンプリングレートを半分にして保存
    scipy.io.wavfile.write('sampling_rate_changed.wav', int(rate / 2), data)


if __name__ == '__main__':
    main()
