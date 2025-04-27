# Python 程式碼庫

這個目錄包含了多種 Python 程式碼，涵蓋了從基本程式設計概念到實用應用的範例。以下是主要的程式碼類別和功能說明：

## 1. 教學示範程式

### 基本程式設計概念

- `loopEx.py`: 教學示範各種循環結構
- `dictEx.py`: 字典操作示範
- `condFlowEx.py`: 條件判斷示範
- `funcEx.py`: 函數使用示範

### 數據結構

- `biTree.py` 系列: 二元樹相關實作
- `bst.py` 系列: 二元搜尋樹實作
- `heap*.py`: 堆積資料結構實作

### 算法

- `primeLib.py`: 質數相關算法
- `gRatio.py`: 黃金比例計算
- `fibo.py`: 斐波那契數列計算

## 2. 遊戲程式

### 蛇蛇遊戲

- 多個版本的蛇蛇遊戲實現（`gameSnake.py` 系列）
- 使用 Pygame 框架
- 支援分數系統和遊戲結束檢測

### 其他遊戲

- `gameSRP.py`: 剪刀石頭布遊戲
- `gameRollDice.py`: 擲骰子遊戲
- `gameGuessNbr.py`: 猜數字遊戲
- `gamePoker.py`: 扑克牌遊戲

## 3. 實用工具

### 地震監測系統

- `quake.py`: 地震資料爬取
- `smsOnQuake.py`: 地震簡訊通知系統

### 其他工具

- `qrCodeEx.py`: QR Code 生成器
- `jsonAPI.py`: JSON API 處理示範
- `emailSender.py`: 電子郵件發送工具

## 4. 數學計算

- `piLib.py`: π值計算方法比較
- `piEstimate.py`: π值估算
- 數學相關的算法和計算工具

## 使用方式

大多數程式都可以直接運行，例如：

```bash
python gameSnake.py
python primeLib.py
```

## 注意事項

- 部分程式需要安裝額外的套件（如 Pygame）
- 部分程式需要設定環境變數（如電子郵件相關設定）
- 建議在虛擬環境中運行這些程式

## 技術堆疊

主要使用的技術和套件：

- 核心 Python 標準庫
- Pygame（遊戲相關）
- requests（API 請求）
- logging（日誌記錄）
- json（資料處理）

## 版本控制

建議使用 git 進行版本控制，以便追蹤程式碼變更歷史。
