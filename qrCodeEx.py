"""This is an example to generate a QR code and writing it to a PNG file
#### 例子：我們用一個網址產生二維碼，並生成 PNG 圖檔
Syntax
    Python <this file name> -url <url> -file <fn>

    where:
    <url>: Your target location to generate QR code
    <fn>: Your file location (path can be included) to store QR code PNG image
"""

import qrcode


def generate_qrcode(url, fn):
    """Generate QR Code image file (PNG) format, named 'fn',
    given the 'url' web address.
    由網址產生二維碼"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants. ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    with open(fn, "w") as f:
        img.save(fn)


from absl import app
from absl import flags
from sample.credentials import qr_url, qr_file

FLAGS = flags.FLAGS

flags.DEFINE_string('url', qr_url,
                    'Your Target to generate QR code.')
flags.DEFINE_string('file', qr_file,
                    'Your file location (path can be included) to store QR code PNG image.')


def main(argv):

    print(f'網址是: {FLAGS.url}')
    print(f'QR Code PNG 格式檔案在: {FLAGS.file}')

    generate_qrcode(FLAGS.url, FLAGS.file)
    print(f'===>請打開 {FLAGS.file} 檢視 QR Code PNG 格式的檔案...\n')


if __name__ == '__main__':

    app.run(main)
