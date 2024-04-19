fileName = "sample/test.txt"

try:
    f = open(fileName, 'r')
except:
    print(f'事有蹊蹺')

# 檔案內容一次全部讀出返回成字串，並去掉最後'\n'
file_contents = f.read().strip()

f.close()

print(f'===> 檔案是否關閉? {f.closed}\n')
print(f'檔案內容一次讀出:\n{file_contents}\n')
print(f'f.read() 返回類型: {type(file_contents)}\n')

# 换成列表，一元素一行，印出行數
lines = file_contents.split('\n')
print(f'{fileName} 檔案共有:\n===> {len(lines)} 行\n')

# 印出行内容
print(f'{fileName} 檔案如下:\n{lines}\n')

# 算算字數 (word count)
wc = 0
for line in lines:
    words = line.split(' ')
    wc += len(words)
print(f'{fileName} 檔案共有:\n===> {wc} 字\n')
