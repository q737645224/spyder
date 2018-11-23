import csv

with open("测试.csv","a",newline="",\
          encoding="gb18030") as f:
    # 初始化写入对象
    writer = csv.writer(f)
    # 写入数据 writer.writerow([])
    writer.writerow(["id","name","age"])
    writer.writerow(["1","Lucy","20"])
    writer.writerow(["2","Tom","25"])
    
10:45分



