# Python 程式庫

這個 README.md 文件總結了 Python 目錄中的主要程式類型和功能，包括：

1. 基礎程式設計範例
2. 檔案處理範例
3. 資料結構實作範例
4. 網路和通訊範例
5. 進階主題範例
6. 效能測試範例

每個部分都列出了相關的程式檔案，並簡要說明其功能。使用者可以根據需要選擇相應的範例來學習或參考。

## 目錄結構

```bash
Python/
├── .git/                    # Git 版本控制
├── .venv/                   # Python 虛擬環境
├── __pycache__/            # Python 編譯快取
├── sample/                  # 範例資料檔案
├── unit_test/               # 單元測試
├── img_processed/           # 圖片處理輸出
├── logger/                  # 日誌相關
├── photo/                   # 圖片檔案
├── video/                   # 影片檔案
├── video-orig/              # 原始影片檔案
├── git/                     # Git 相關檔案
├── 基礎範例
│   ├── dates.py            # 日期時間
│   ├── listEx.py           # 列表操作
│   ├── dictEx.py           # 字典操作
│   └── tupleEx1.py         # 元組操作
├── 數據結構
│   ├── biTree.py           # 二元樹
│   ├── bsTree.py           # 二元搜尋樹
│   └── bst.py              # 二元搜尋樹
├── 檔案處理
│   ├── filesEx1.py         # 檔案操作
│   ├── csvEx.py            # CSV 處理
│   ├── jsonEx.py           # JSON 處理
│   ├── xmlEx1.py           # XML 處理
│   └── xmlEx2.py           # XML 處理
├── 網路
│   ├── emailPublisher.py   # 電子郵件
│   └── smsOnQuake.py       # 簡訊通知
├── 遊戲
│   ├── gameSnake.py        # 蛇遊戲
│   └── gamePoker.py        # 扑克遊戲
├── GUI
│   ├── tkinterEx1.py       # Tkinter GUI
│   ├── guiEx.py            # GUI 範例
│   ├── graphEx6.py         # 軟體架構圖
│   └── graphUSA50.py       # 美國50州相鄰關係圖
├── 效能測試
│   ├── perf_LvsT.py        # 列表與元組
│   └── perfHeaps.py        # 堆積結構
│   ├── process_images_1P.py # 單進程影像處理效能測試
│   ├── process_images_CP.py # 多核心並行處理影像效能測試
│   └── process_images_CT.py # 多執行緒並行處理影像效能測試
└── 配置文件
    ├── .env                # 環境變數
    ├── requirements.txt    # Python 套件依賴
    ├── pyproject.toml      # Python 專案配置
    └── environment.yaml    # 環境配置
```

## 主要程式類型

### 基礎程式設計範例

- `dates.py`: 日期和時間處理範例
- `listEx.py`: 列表操作和處理範例
- `dictEx.py`: 字典操作範例
- `lambdaEx.py`: Lambda 函式範例

### 檔案處理範例

- `filesEx1.py` ~ `filesEx6.py`: 檔案讀取和寫入範例
- `csvEx.py` ~ `csvEx2.py`: CSV 檔案處理範例
- `jsonEx.py` ~ `jsonEx2.py`: JSON 資料處理範例
- `xmlEx1.py` ~ `xmlEx2.py`: XML 檔案讀取和寫入範例

### 資料結構範例

- `biTree.py` ~ `biTree_v2.py`: 二元樹實作
- `bsTree.py` ~ `bsTreeEx.py`: 二元搜尋樹實作
- `bst.py` ~ `bstEx2.py`: 二元搜尋樹範例

### 網路和通訊範例

- `emailPublisher.py`: 電子郵件發送功能
- `smsOnQuake.py`: 地震簡訊通知系統
- `emailSendAttach.py`: 帶附件的電子郵件發送
- `emailSendHTML.py`: HTML 格式電子郵件發送

### 進階主題範例

- `multiprocess10.py`: 多進程處理範例
- `scheduleEx.py`: 定時任務排程
- `tkinterEx1.py`: GUI 程式設計
- `reEx.py`: 正則表達式範例
- `piLib.py`: 圓周率計算庫
- `primeLib.py`: 質數計算庫

### 效能測試範例

- `perf_LvsT.py`: 列表與元組效能比較
- `perfHeaps.py`: 堆積結構效能測試
- `perfListvsGenerator.py`: 列表與生成器效能比較
- `process_images_1P.py`: 單進程影像處理效能測試
- `process_images_CP.py`: 多核心並行處理影像效能測試
- `process_images_CT.py`: 多執行緒並行處理影像效能測試

## 使用方式

每個程式都包含主函數 `main()`, 可以直接執行。例如：

```bash
python dates.py
python listEx.py
```

## 技術堆疊

主要使用的技術和套件：

- 核心 Python 標準庫
- Pygame（遊戲相關）
- requests（API 請求）
- logging（日誌記錄）
- json（資料處理）

## 注意事項

- 部分程式需要安裝額外的套件（如 Pygame）
- 建議在虛擬環境中運行這些程式

## 版本控制

建議使用 git 進行版本控制，以便追蹤程式碼變更歷史。
