"""
實作一個使用字典的快取類別
這個快取類別提供了簡單的快取管理機制，包括：
1. 快取縮減時的百分比控制
2. 快取大小的上限控制
3. 保留最常使用的項目
"""

class Cache:
    """
    快取類別
    
    屬性:
    cache (dict): 儲存快取資料的字典
    """
    
    def __init__(self):
        """
        初始化快取實例
        
        每個快取項目的值是一個包含兩個元素的列表：
        1. value object (任何使用者定義的物件)
        2. reference count (整數): 用於追蹤該項目的存取次數
        """
        self.cache = dict()

    def __repr__(self):
        """
        顯示快取內容
        
        回傳:
        str: 快取內容的字串表示
        """
        str_dump = f'快取內容 ({len(self.cache)}) 項目...\n'
        count = 1
        for key, value in self.cache.items():
            str_dump += f'{count}: 鍵: {key}\n'
            val_str = str(value[0])
            str_dump += f'===>值: ...{val_str[0:50]}...\n'
            str_dump += f'===>存取次數: {value[1]}\n'
            count += 1
        return str_dump

    def has(self, key):
        """
        檢查快取中是否包含指定的鍵
        
        參數:
        key: 要檢查的鍵
        
        回傳:
        bool: 如果鍵存在則回傳 True，否則回傳 False
        """
        return key in self.cache

    def add(self, key, value):
        """
        將鍵值對加入快取
        
        參數:
        key: 要加入的鍵
        value: 要加入的值
        """
        self.cache[key] = [value, 1]  # 初始化存取次數為 1

    def inc(self, key):
        """
        增加指定鍵的存取次數
        
        參數:
        key: 要增加存取次數的鍵
        """
        val_list = self.cache.pop(key)
        val_list[1] += 1  # 增加存取次數
        self.cache[key] = val_list

    def get(self, key):
        """
        獲取指定鍵的值
        
        參數:
        key: 要獲取值的鍵
        
        回傳:
        any: 與鍵相關聯的值
        
        備註:
        如果鍵不存在，會引發 KeyError
        """
        return self.cache[key][0]

    def purge(self, size=100):
        """
        清除最不常用的項目，直到達到指定大小
        
        參數:
        size (int): 要保留的項目數量
        
        備註:
        這個方法會重設每個保留項目的存取次數
        """
        if len(self.cache) <= size:
            # 快取已經在限制範圍內
            return

        # 按存取次數排序（由高到低）
        sorted_list = sorted(self.cache.items(), key=lambda kv: (
            kv[1][1], kv[0]), reverse=True)

        # 清空快取
        self.cache.clear()
        
        # 保留前 size 個最常用的項目
        for i in range(size):
            sorted_list[i][1][1] = 0  # 重設存取次數
            self.cache[sorted_list[i][0]] = sorted_list[i][1]

    def shrink(self, percent=50):
        """
        縮減快取到指定的百分比
        
        參數:
        percent (int): 要保留的百分比
        
        備註:
        這個方法不會重設存取次數
        """
        # 按存取次數排序（由高到低）
        sorted_list = sorted(self.cache.items(), key=lambda kv: (
            kv[1][1], kv[0]), reverse=True)
        
        # 計算要保留的項目數量
        count_keep = len(self.cache) * percent // 100 + 1

        # 清空快取
        self.cache.clear()
        
        # 保留最常用的項目
        for i in range(count_keep):
            self.cache[sorted_list[i][0]] = sorted_list[i][1]

if __name__ == '__main__':
    print("=== Cache 類別測試 ===")
    
    # 建立快取實例
    cache = Cache()
    
    # 測試基本功能
    print("\n=== 測試基本功能 ===")
    cache.add("apple", "蘋果")
    cache.add("banana", "香蕉")
    cache.add("orange", "柳丁")
    
    print("快取內容:")
    print(cache)
    
    print("\n檢查鍵是否存在:")
    print(f"蘋果存在嗎? {'是' if cache.has('apple') else '否'}")
    print(f"芒果存在嗎? {'是' if cache.has('mango') else '否'}")
    
    print("\n獲取值:")
    print(f"蘋果的值: {cache.get('apple')}")
    
    # 測試存取次數
    print("\n=== 測試存取次數 ===")
    print("增加蘋果的存取次數")
    cache.inc("apple")
    print("快取內容:")
    print(cache)
    
    # 測試 purge 功能
    print("\n=== 測試 purge 功能 ===")
    # 添加更多項目
    cache.add("mango", "芒果")
    cache.add("pear", "梨子")
    cache.add("grape", "葡萄")
    
    print("原始快取內容:")
    print(cache)
    
    print("\n執行 purge(3) - 保留最常用的 3 個項目")
    cache.purge(3)
    print("快取內容:")
    print(cache)
    
    # 測試 shrink 功能
    print("\n=== 測試 shrink 功能 ===")
    # 添加更多項目
    cache.add("watermelon", "西瓜")
    cache.add("pineapple", "鳳梨")
    cache.add("strawberry", "草莓")
    
    print("原始快取內容:")
    print(cache)
    
    print("\n執行 shrink(50) - 縮減到 50%")
    cache.shrink(50)
    print("快取內容:")
    print(cache)
