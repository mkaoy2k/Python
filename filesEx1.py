fileName = "sample/test.txt"
for mode in ["r", "w", "a", "r+", "w+", "a+"]:
    try:
        f = open(fileName, mode)
        print(f'檔案物件名稱: {f.name}')
        print(f'檔案存取模式: {f.mode}\n')
        f.close()
    except:
        print(f'事有蹊蹺')
