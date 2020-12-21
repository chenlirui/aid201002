# 练习1：
# 一次读取5个字符，将file.txt
# 文件从头到尾读取打印出来，打印
# 内容与原文件保持一直
# file = open("file.txt","r")
# while True:
#     data = file.read(1028)
#     if not data:
#         break
#     print(data)


# 练习2：
# 单词本： 每行一个单词
#         单词和解释之间有空格
#         后面的单词比前面的大
# 编写一个函数，传入一个单词
# 返回单词的对应解释
# def find_word(word):
#     file = open("dict.txt","r")
#     for line in file:
#         tmp = line.split(" ",1)
#         if tmp[0] > word:
#             break
#         elif word == tmp[0] :
#             return tmp[1].strip()
# print(find_word("a"))





#
# 练习3：
# 请在屏幕上使用input函数输入一首古诗
# 《悯农》
# 将其写入到文件file.txt中
# 要求每次input只输入一句
#
# 锄禾日当午，
# 汗滴禾下土。
# 谁知盘中餐，
# 粒粒皆辛苦。
# file = open("file.txt","w")
# while True:
#     data = input(">>")
#     if not data:
#         break
#     file.write(data + "\n")
# file.close()
#
# 练习4： 假设在当前文件夹下有一个图片timg.jfif
# 请编写一个函数，将该文件名传入，通过执行函数将其
# 复制一份到 主目录下
# 注意： 考虑可能文件比较大，不允许一次性读取
def copy(filename):
    fr = open("../filename", "rw")
    fw = open("/home/tarena/" + filename, "wb")
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
copy(timg.jfif)

#
# 逻辑提示： 边从原来的文件读取内容，再将内容写入新文件
#
# 作业：1. 熟练 open  write  read 函数
#      2. 重点练习自己能完成 练习4
#      3. 编写一个程序，每隔2秒向文件 my.log中写入一行
#      内容（如果这个文件不存在则自动创建）
#      程序死循环不会停止. 当强行结束程序，重新启动之后
#      能够继续写入内容，并序号衔接，每次写入一行都要显
#      示出来
#
#         1. 2020-11-30 18:18:18
#         2. 2020-11-30 18:18:20
#         3. 2020-11-30 18:18:22
#         4. 2020-11-30 18:18:24
#         5. 2020-11-30 18:20:08
#         6. 2020-11-30 18:20:10
#         7. 2020-11-30 18:20:12
#
#       提示： sleep(2)   localtime()