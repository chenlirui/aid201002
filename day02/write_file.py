#文件写法 示例
# #打开一个文件
# file = open("file.txt","w")
# # #写入内容
# file.write("hello,你好\n",)
# n=file.write("晚上好\n")
# file.seek(0)
# print("写入%d 字符"%file.tell())
# file = open("file.txt","w")
#写入内容

# file.write("hello,你好\n".encode())
# n=file.write("晚上好\n".encode())
# print("写入%d 字节"%n)
# file.write("hello,你好\n")
# n=file.write("晚上好\n")
# print("写入%d 字节"%n)
# data = ["但去莫相问\n","白云空悠悠\n"]
# file.writelines(data)
# file = open("file.txt","w")
# data = input("锄禾日当午，汗滴禾下土。谁知盘中餐，粒粒皆辛苦。")
#
# file.write(data)
# file.close()
# for line in m:
#     data = (file,end ==" ")
#     print(line)
# with open("file.txt") as file:
#     data = file.read()
#     print(data)
# with open("home/tarena/桌面/2010/张若昀.jpg") as picute:
# fr = open(张若昀.jpg,rb)
# fw = open("home/tarena/桌面/2010/张若昀.jpg")
# while True:
# file = open("file.txt","r")
# while True:
#     data = file.read(1028)
#     if not data:
#         break
#     print(data,end=" ")
def find_word(word):
    """
    :param word: 要查找的单词
    :return: 得到的解释
    """
    file = open("/home/tarena/mouth02/day03/dict.txt") # 打开
    # 每次回去一个单词
    for line in file:
        tmp = line.split(" ",1) # 按照空格分割
        # 如果迭代得到的单词已经比word大了就不用找了
        if tmp[0] > word:
            break
        elif word == tmp[0]:
            
            return tmp[1].strip()
    file.close()

print(find_word("at"))