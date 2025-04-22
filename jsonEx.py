'''
JSON (JavaScript Object Notation) 是一種輕量級的資料交換格式。
本範例示範如何從 JSON 檔案讀取資料到 Python 字典，
以及如何將 Python 字典寫入 JSON 檔案。

程式功能說明：
1. 讀取 JSON 檔案：
   - 從指定的 JSON 檔案中讀取資料，包含：
      - 美國各州名稱
      - 縮寫
      - 郵遞區號   
- 將 JSON 格式的資料轉換為 Python 字典

2. 資料處理：
   - 從字典中刪除指定的欄位（郵遞區號）
   - 修改字典中的資料

3. 寫入 JSON 檔案：
   - 將修改後的字典資料寫入新的 JSON 檔案
   - 使用縮排格式化輸出，提高可讀性

4. JSON 字串處理範例：
   - 將 JSON 格式的字串轉換為 Python 字典
   - 遍歷字典中的資料
   - 將 Python 字典轉換回 JSON 格式的字串

使用方法：
1. 確保在相同目錄下有一個名為 'sample' 的資料夾
2. 在 'sample' 資料夾中放置名為 'json_states.json' 的 JSON 檔案
3. 執行程式後，會在 'sample' 資料夾中生成 'json_states_new.json'

注意事項：
- 程式會自動創建所需的目錄結構
- JSON 檔案需要符合正確的格式
- 確保有足夠的寫入權限
'''
import json
from pathlib import Path

def main():
    # 使用 pathlib 初始化當前目錄和資料夾路徑
    current_dir = Path(__file__).parent
    data_path = current_dir / 'sample'

    # 設定範例中使用的資料檔案名稱
    file_read = data_path / 'json_states.json'
    file_write = data_path / 'json_states_new.json'

    # 從 JSON 檔案讀取資料到 Python 字典
    print(f'從 {file_read} JSON 檔案讀入 ...')
    with open(file_read) as f:
        data = json.load(f)
    print(f'轉成字典 data 類型：{type(data)}\n')
    print(f'===>{data}\n')

    # 從字典中刪除郵遞區號
    print(f'字典中刪除郵遞區號 ...')
    for state in data['states']:
        del state['area_codes']

    # 將美國各州名稱及其縮寫以 JSON 格式寫入檔案
    print(f'字典物件轉成JSON格式的字串並寫入檔案 ...')
    with open(file_write, 'w') as f:
        json.dump(data, f, indent=2)
    print(f'===>請打開 {file_write} 檢視 JSON 格式的檔案...\n')

    # JSON 字串讀取/寫入範例

    # JSON 格式的字串，包含一個州名稱及其相關縮寫的列表
    string_json = '''{
      "states": [
        {
          "name": "Alabama",
          "abbreviation": "AL"
        },
        {
          "name": "Alaska",
          "abbreviation": "AK"
        }
      ]
    }
    '''

    print(f'JSON 格式字串：\n===>{string_json}\n')

    # 將 JSON 格式字串轉換為 Python 字典
    dict_pi = json.loads(string_json)
    print(f'載入 JSON 字串轉成字典 dict_pi 類型：{type(dict_pi)}:')
    print(f'===>{dict_pi}\n')

    # 遍歷 'states' 鍵的值（列表），逐一印出每個元素
    print(f'取出鍵="states"的值（列表）逐一印出每一元素 ...')
    for state in dict_pi['states']:
        print(f'===>{state}')
    print()

    # 將 Python 字典轉換為 JSON 格式的字串
    # 選擇性地，使用縮排來提高可讀性
    new_str_json = json.dumps(dict_pi, indent=2)

    print(f'字典轉成字串 new_str_json 類型：{type(new_str_json)}')
    print(f'===>{new_str_json}\n')

if __name__ == '__main__':
    main()
