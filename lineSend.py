"""
This example sneds a message, an image or both to a Line group
via 'LINE Notify' HTTP gateway
Syntax:
    python <this file> -msg <text> -img <file>

    where:
    <text> (optional): Your message to send.
        Default text loaded from the '/line_msg.txt' file.
    <file> (optional): Your image location (path can be included) to send.
        Default no image to send.
"""

import requests
from sample.credentials import line_gw_url, line_my_token, line_my_name, line_fileMsg

# ! pip install 'absl-py' Module if needed.
from absl import app
from absl import flags

FLAGS = flags.FLAGS


flags.DEFINE_string('msg', None, 'Your message to send.')
flags.DEFINE_string('img', None,
                    'Your image location (path can be included) to send.')


def main(argv):

    headers = {
        'Authorization': 'Bearer ' + line_my_token    # 設定 LINE Notify 權杖
    }

    # Text message is required.
    if FLAGS.msg is None:
        fileMsg = line_fileMsg
        with open(fileMsg, 'r') as f:
            textMsg = f.read().strip()
    else:
        textMsg = FLAGS.msg

    data = {
        'message': textMsg
    }

    # Send a Line-Notify
    print(f'LINE to {line_my_name}...')
    if FLAGS.img is None:
        # 沒有圖片資訊
        data = requests.post(line_gw_url, headers=headers, data=data)
    else:
        with open(FLAGS.img, 'rb') as image:    # 以二進位方式開啟圖片
            imageFile = {'imageFile': image}    # 設定圖片資訊
            data = requests.post(line_gw_url,
                headers=headers, data=data,
                files=imageFile)                # 發送 LINE Notify


if __name__ == '__main__':

    app.run(main)
