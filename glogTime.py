"""函式執行時間測量模組

此模組提供功能裝飾器和上下文管理器，用於測量函式執行的時間。
主要功能包括：
- `inAndOutLog`: 上下文管理器，用於記錄函式開始和結束時間
- `func_timer_decorator`: 裝飾器，用於測量函式執行時間

使用範例：
@func_timer_decorator
def my_function():
    ...

當 my_function() 執行時，會自動記錄開始和結束時間，並計算執行時間。
"""

import glog as log
import datetime
import random
from typing import Callable, Any

class inAndOutLog:
    """上下文管理器，用於記錄函式執行時間

    Args:
        funcName (str): 被測量的函式名稱
    """
    def __init__(self, funcName: str):
        self.funcName = funcName

    def __enter__(self):
        """進入上下文時，記錄開始時間"""
        log.info(f'開始: {self.funcName}')
        self.init_time = datetime.datetime.now()
        return self

    def __exit__(self, type, value, tb):
        """離開上下文時，記錄結束時間並計算執行時間"""
        end_time = datetime.datetime.now()
        duration = end_time - self.init_time
        log.info(f'結束: {self.funcName} 共花 {duration.total_seconds():.6f} 秒.\n')

def func_timer_decorator(func: Callable) -> Callable:
    """函式裝飾器，用於測量函式執行時間

    Args:
        func (Callable): 被裝飾的函式

    Returns:
        Callable: 包裝後的函式
    """
    def func_wrapper(*args, **kwargs) -> Any:
        """函式包裝器，負責執行時間測量"""
        with inAndOutLog(func.__name__):
            return func(*args, **kwargs)
    return func_wrapper

@func_timer_decorator
def lookupList(cnt: int) -> None:
    """測試列表讀取性能

    Args:
        cnt (int): 測試次數
    """
    L = list(range(cnt))
    for _ in range(cnt):
        i = random.randint(0, L[cnt-1])
        j = random.randint(0, L[cnt-1])
        _ = abs(L[i] - L[j])

@func_timer_decorator
def lookupTuple(cnt: int) -> None:
    """測試元組讀取性能

    Args:
        cnt (int): 測試次數
    """
    T = tuple(range(cnt))
    for _ in range(cnt):
        i = random.randint(0, T[cnt-1])
        j = random.randint(0, T[cnt-1])
        _ = abs(T[i] - T[j])

def main() -> None:
    """主程式入口點

    測試列表和元組的讀取性能，並比較它們的執行時間。
    """
    # 設定測試次數
    max_loop = 2_000_000

    print(f'進行 {max_loop:,} 次列表與元組讀取性能測試：')
    lookupList(max_loop)
    lookupTuple(max_loop)

if __name__ == '__main__':
    main()