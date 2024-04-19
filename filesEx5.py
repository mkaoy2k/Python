"""更多 f.readline(bytes) 一次讀出50個位元的例子"""

fileName = 'sample/test.txt'
with open(fileName, 'r') as f:
    print(f'讀寫頭現在位置 = {f.tell()}\n')

    # 一次讀出幾個位元
    size_to_read = 50
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f'一次讀出 {size_to_read} 個位元...\n===>{f_contents}<===\n')
        f_contents = f.read(size_to_read)
    print(f'===> {f.name} 讀取完畢！\n')

    print(f'讀寫頭現在位置 = {f.tell()}\n')
