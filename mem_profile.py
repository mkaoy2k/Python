"""
記憶體使用量監控工具

這個模組提供了多種方法來監控和測量 Python 程式在運行時的記憶體使用量。
主要包含以下功能：
1. 使用 psutil 監控進程記憶體使用量
2. 使用 resource 模組監控系統資源使用量
3. 提供不同的記憶體測量方法以適應不同平台

使用方法：
1. 呼叫 memory_usage_psutil() 來獲取記憶體使用量（MB）
2. 呼叫 memory_usage_resource() 來獲取系統資源使用量
"""
import psutil   # pip install psutil
import resource
import os
import sys

def memory_usage_psutil():
    # return the memory usage in MB
    process = psutil.Process(os.getpid())
    mem = process.memory_info()[0] / float(2 ** 20)
    return mem


def memory_usage_resource():
    rusage_denom = 1024.
    if sys.platform == 'darwin':
        # ... it seems that in OSX the output is different units ...
        rusage_denom = rusage_denom * rusage_denom
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / rusage_denom
    return mem

def main():
    """
    主函數，示範如何使用記憶體監控功能
    """
    print("使用 psutil 測量記憶體使用量:", memory_usage_psutil(), "MB")
    print("使用 resource 測量記憶體使用量:", memory_usage_resource(), "MB")

if __name__ == "__main__":
    main()
