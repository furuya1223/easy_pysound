import numpy as np
import scipy.io.wavfile


def main():
    # 音声ファイルパスを指定
    wav_filename = 'sample.wav'

    # 音声ファイル読み込み, -1～1の範囲に正規化
    rate, data = scipy.io.wavfile.read(wav_filename)
    data = data / 32768

    # dataを0～255の範囲にしてから符号無し8bit整数に変換
    data = np.clip((data + 1) * 128, 0, 255).astype(np.uint8)
    # ↓のコメントアウトを外すと，さらに解像度を下げる（256段階から64段階に変える）
    # data = (data // 4) * 4

    # dataを'output.wav'の名前で保存
    scipy.io.wavfile.write('bitrate_changed.wav', rate, data)


if __name__ == '__main__':
    main()
