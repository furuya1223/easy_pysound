import numpy as np
import scipy.io.wavfile


def main():
    # 音声ファイルパスを指定
    wav_filename = 'sample.wav'

    # 音声ファイル読み込み, -1～1の範囲に正規化
    rate, data = scipy.io.wavfile.read(wav_filename)
    data = data / 32768

    print(rate) # サンプリングレート
    print(type(data)) # dataの型（numpy.ndarrayのはず）
    print(data.shape) # データの長さ
    print(data) # データ内容表示（-1～1の範囲の実数のはず）

    # クリッピング処理を用いて音割れさせてみる
    data = np.clip(data, -0.03, 0.03)
    data = data * 3 # 音量調節

    # dataを-32768～32767の範囲にしてから符号付き16bit整数に変換
    data = np.clip(data * 32768, -32768, 32767).astype(np.int16)

    # dataを'output.wav'の名前で保存
    scipy.io.wavfile.write('output.wav', rate, data)


if __name__ == '__main__':
    main()
