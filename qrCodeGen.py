"""
QR Code 生成器

這個模組提供了一個簡單的介面來生成 QR Code 圖片。
可以從命令列參數或環境變數讀取設定，並將生成的 QR Code 儲存為 PNG 圖片。

範例:
    1. 使用命令列參數:
       python qrCodeGen.py --url "https://github.com/mkaoy2k/Kids-Lets-Play-Python" --file sample/qrCode.png
    
    2. 使用環境變數:
       在 .env 檔案中設定:
       QR_URL=https://github.com/mkaoy2k/Kids-Lets-Play-Python
       QR_FILE=qrcode.png
       然後執行:
       python qrCodeGen.py

命令列參數:
    --url: 要編碼成 QR Code 的網址
    --file: 儲存 QR Code 圖片的檔案路徑

依賴套件:
    - qrcode: 用於生成 QR Code
    - absl: 用於命令列參數解析
    - python-dotenv: 用於讀取 .env 檔案中的環境變數
"""

import qrcode
from absl import app, flags

FLAGS = flags.FLAGS
flags.DEFINE_string('url', None, '要生成 QR Code 的網址')
flags.DEFINE_string('file', None, '儲存 QR Code 圖片的檔案路徑')

def generate_qrcode(url: str, file_path: str) -> None:
    """
    生成並儲存 QR Code 圖片
    
    根據提供的網址生成 QR Code，並將其儲存為 PNG 圖片。
    預設使用以下 QR Code 設定：
    - 版本: 1 (21x21 模組)
    - 錯誤修正: L (約 7% 或更少的錯誤可以被修正)
    - 方塊大小: 10 像素
    - 邊框: 4 個模組寬
    - 顏色: 黑色 QR Code 在白色背景上

    參數:
        url (str): 要編碼成 QR Code 的網址
        file_path (str): 儲存 QR Code 圖片的完整路徑
        
    異常:
        Exception: 當生成或儲存 QR Code 時發生錯誤
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
    
    這個函數會：
    1. 載入環境變數
    2. 解析命令列參數
    3. 生成 QR Code
    4. 將 QR Code 儲存為圖片檔案
    
    參數:
        argv: 命令列參數列表 (由 absl 自動處理)
        
    異常:
        SystemExit: 當參數解析失敗或發生錯誤時
    """
    try:
        # 解析命令列參數
        FLAGS(argv)
        
        # 檢查必要參數
        if not FLAGS.url:
            raise ValueError("請提供要生成 QR Code 的網址 (--url 參數或 QR_URL 環境變數)")
        if not FLAGS.file:
            raise ValueError("請提供儲存 QR Code 的檔案路徑 (--file 參數或 QR_FILE 環境變數)")
        
        print(f"網址是: {FLAGS.url}")
        print(f"QR Code PNG 格式檔案將儲存於: {FLAGS.file}")
        
        generate_qrcode(FLAGS.url, FLAGS.file)
        print(f"===> 請打開 {FLAGS.file} 檢視 QR Code PNG 格式的檔案...")
    except Exception as e:
        print(f"執行過程中發生錯誤: {str(e)}")
        raise  # 重新拋出異常，讓 absl 可以處理


if __name__ == '__main__':
    app.run(main)
