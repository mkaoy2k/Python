"""
本程式會自動產生一張以「大俠米粉炒」為主題的紅底招牌圖片，主標題與副標語分別置中顯示。
程式會自動尋找系統可用的中文字體，根據內容與字體大小計算合適的排版位置，
並將圖片儲存為 JPG 格式於 sample 資料夾。

功能摘要：
- 設定圖片尺寸、背景色、主副標題顏色
- 自動尋找合適中文字體（macOS 常見字體）
- 主標題、副標語內容與字體大小可調整
- 文字自動置中排版
- 產生並儲存招牌圖片
"""

from PIL import Image, ImageDraw, ImageFont
import os

# 設定圖片尺寸和顏色

def get_font(font_candidates, size):
    """嘗試依序載入字型，若皆失敗則回傳預設字型"""
    for font_name in font_candidates:
        try:
            return ImageFont.truetype(font_name, size)
        except OSError:
            continue
    return ImageFont.load_default()

def get_text_size(text, font):
    """取得文字尺寸，兼容 Pillow 新舊版本"""
    if hasattr(font, 'getbbox'):
        bbox = font.getbbox(text)
        return bbox[2] - bbox[0], bbox[3] - bbox[1]
    elif hasattr(font, 'getsize'):
        return font.getsize(text)
    else:
        mask = font.getmask(text)
        return mask.size

def main():
    width, height = 800, 480
    bg_color = (221, 160, 221)  # 淡紫色背景
    text_color_main = (0, 0, 0)  # 黑色主標題
    text_color_sub = (255, 215, 0)     # 金色副標語

    # 建立圖片
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    # 主標題字體（較粗、正楷/黑體/蘋方）
    main_font_candidates = [
        '/System/Library/Fonts/STHeiti Medium.ttc',
        '/System/Library/Fonts/PingFang.ttc',
        '/System/Library/Fonts/Hiragino Sans GB W6.ttc',
        '/System/Library/Fonts/Hiragino Sans GB.ttc',
        '/System/Library/Fonts/Heiti TC.ttc',
        '/Library/Fonts/Arial Unicode.ttf',
        '/System/Library/Fonts/Supplemental/Arial Unicode.ttf',
    ]
    main_font = get_font(main_font_candidates, 80)

    # 副標語字體（較細、仿草書/行書/標楷體）
    sub_font_candidates = [
        '/System/Library/Fonts/STKaiti.ttc',
        '/System/Library/Fonts/PingFang.ttc',
        '/System/Library/Fonts/Hiragino Sans GB.ttc',
        '/System/Library/Fonts/Songti.ttc',
        '/System/Library/Fonts/Heiti TC.ttc',
        '/Library/Fonts/Arial Unicode.ttf',
        '/System/Library/Fonts/Supplemental/Arial Unicode.ttf',
    ]
    sub_font = get_font(sub_font_candidates, 48)

    # 內容
    main_text = '大俠米粉炒'
    sub_text1 = '金光搶搶滾'
    sub_text2 = '大俠炒米粉'

    # 主標題位置
    w_main, h_main = get_text_size(main_text, main_font)
    main_x = (width - w_main) // 2
    main_y = 60
    draw.text((main_x, main_y), main_text, font=main_font, fill=text_color_main)

    # 副標語位置
    w_sub1, h_sub1 = get_text_size(sub_text1, sub_font)
    w_sub2, h_sub2 = get_text_size(sub_text2, sub_font)
    sub_x1 = (width - w_sub1) // 2
    sub_x2 = (width - w_sub2) // 2
    sub_y1 = main_y + h_main + 60
    sub_y2 = sub_y1 + h_sub1 + 10
    draw.text((sub_x1, sub_y1), sub_text1, font=sub_font, fill=text_color_sub)
    draw.text((sub_x2, sub_y2), sub_text2, font=sub_font, fill=text_color_sub)

    # 儲存為 JPG 至 sample 資料夾
    sample_dir = os.path.join(os.path.dirname(__file__), 'sample')
    os.makedirs(sample_dir, exist_ok=True)
    output_path = os.path.join(sample_dir, 'daxia_rice_noodle_sign.jpg')
    img.save(output_path, 'JPEG')
    print(f'已產生招牌圖片：{output_path}')

if __name__ == "__main__":
    main()
