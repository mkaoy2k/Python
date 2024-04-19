# Reading Files via 'with' context manager
# not only file, but also other resources, like threads
fileName = 'sample/test.txt'
with open(fileName, 'r') as f:
    print(f'Context Manager 執行 with-block 前，開啓檔案...')
    file_contents = f.read()
    print(f'檔案物件名稱: {f.name}')
    print(f'檔案存取模式: {f.mode}\n')

# Context Manager 執行 with-block 結束時，自動關閉檔案
print(f'Context Manager 執行 with-block 結束，自動關閉檔案')
print(f'===> 檔案是否關閉? {f.closed}\n')
print(f'檔案內容一次讀出:\n{file_contents}\n')
