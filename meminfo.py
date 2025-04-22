# meminfo.py

# Copyright (c) 2009, Giampaolo Rodola'. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
系統記憶體資訊顯示工具

這個程式會顯示系統的記憶體使用狀況，包括：
- 物理記憶體（RAM）：總量、可用量、使用率、已用量、空閒量等
- 換頁記憶體（Swap）：總量、已用量、空閒量、使用率等

使用方式：
直接執行此程式即可顯示系統的記憶體資訊

依賴：
- psutil：用於獲取系統記憶體資訊
"""

"""
Print system memory information.
Example:
MEMORY
------
Total      :    9.7G
Available  :    4.9G
Percent    :    49.0
Used       :    8.2G
Free       :    1.4G
Active     :    5.6G
Inactive   :    2.1G
Buffers    :  341.2M
Cached     :    3.2G

SWAP
----
Total      :      0B
Used       :      0B
Free       :      0B
Percent    :     0.0
Sin        :      0B
Sout       :      0B
"""

import psutil
from psutil._common import bytes2human


def pprint_ntuple(nt):
    for name in nt._fields:
        value = getattr(nt, name)
        if name != 'percent':
            value = bytes2human(value)
        print('%-10s : %7s' % (name.capitalize(), value))


def mem_info():
    print('MEMORY\n------')
    pprint_ntuple(psutil.virtual_memory())
    print('\nSWAP\n----')
    pprint_ntuple(psutil.swap_memory())

def main():
    """主程式函數，用於顯示系統記憶體資訊"""
    mem_info()

if __name__ == '__main__':
    main()
