import os

def text_to_mp3(text, mp3_filename):
    cmd = 'edge-tts --voice zh-CN-XiaoxiaoNeural --text "{}" --write-media {}'.format(text, mp3_filename)
    os.system(cmd)


if __name__ == '__main__':

    f = open('audio.txt', 'r', encoding='utf-8')
    for each in f:
        items = each.strip().split()
        print(text_to_mp3(items[1], f"./audio/{items[0]}.mp3"))
    f.close()

