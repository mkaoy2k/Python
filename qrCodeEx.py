"""
QR Code 生成器
這個程式可以根據指定的網址生成 QR Code，並儲存為 PNG 圖片檔案。

使用方法:
    python qrCodeEx.py --url <網址> --file <檔案路徑>
    或從環境變數讀取設定：
    QR_URL=網址
    QR_FILE=檔案路徑

參數說明:
    --url(optional): 要生成 QR Code 的網址
    --file(optional): 儲存 QR Code 圖片的檔案(可含路徑)
    default: 網址和儲存路徑由 .env 環境變數 QR_URL 和 QR_FILE 指定
"""

import qrcode
from absl import app
from absl import flags
from dotenv import load_dotenv
import os


def loadenv() -> None:
    """
    載入環境變數
    """
    try:
        load_dotenv()
        print("環境變數已載入")
    except Exception as e:
        print(f"載入環境變數時發生錯誤: {str(e)}")


def generate_qrcode(url: str, file_path: str) -> None:
    """
    生成 QR Code 圖片

    參數:
        url (str): 要生成 QR Code 的網址
        file_path (str): 儲存 QR Code 圖片的檔案路徑

    這個函數會根據指定的網址生成 QR Code，並儲存為 PNG 圖片檔案。
    """
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        img.save(file_path)
        print(f"QR Code 已成功生成並儲存於: {file_path}")
    except Exception as e:
        print(f"生成 QR Code 時發生錯誤: {str(e)}")




def main(argv) -> None:
    """
    主函數，處理 QR Code 生成流程

    參數:
        argv: 命令列參數列表
    """
    try:
        # 載入環境變數
        loadenv()
        
        # 定義命令列參數
        FLAGS = flags.FLAGS
        flags.DEFINE_string('url', os.getenv('QR_URL'), '要生成 QR Code 的網址')
        flags.DEFINE_string('file', os.getenv('QR_FILE'), '儲存 QR Code 圖片的檔案路徑')
        
        print(f"網址是: {FLAGS.url}")
        print(f"QR Code PNG 格式檔案將儲存於: {FLAGS.file}")
        
        generate_qrcode(FLAGS.url, FLAGS.file)
        print(f"===> 請打開 {FLAGS.file} 檢視 QR Code PNG 格式的檔案...")
    except Exception as e:
        print(f"執行過程中發生錯誤: {str(e)}")


if __name__ == '__main__':
    app.run(main)
