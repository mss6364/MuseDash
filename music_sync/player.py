"""
音乐播放接口占位。
主要接口：listen_and_play(chart_path_or_audio_path)
调用后监听键盘，按下空格立即播放对应音乐（无音乐时可自行决定是否播放节拍）。
具体逻辑留待实现。
"""


def listen_and_play(chart_name):
    """
    TODO: 监听键盘，空格触发播放。
    - 输入：曲目名或谱面/音频路径
    - 根据曲目名查找 charts/<曲目名>/<曲目名>.mp3，若不存在则回退播放节拍
    """
    raise NotImplementedError("音乐播放逻辑尚未实现。")


def main():
    """
    调试入口：可手动调用 listen_and_play 进行本地测试。
    """
    raise NotImplementedError("调试入口未实现。")


if __name__ == "__main__":
    main()
