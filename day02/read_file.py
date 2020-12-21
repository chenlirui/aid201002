#打开文件
# file = open("file.txt","rb")
# #读取文件内容
# data = file.read(5)
# print(data)
# #接着上次内容继续读
# data = file.read()
# print(data)
#
# # file.close()
# file = open("file.txt", "r")
# while True:
#     data = file.read(5)
#     print(data)
#     if data == " ":
#         break
#     print(data, end=" ")
# file = open("file.txt","r")
# data = file.readlines(5)
# print(data)

# for line in file:
#      print(line)
def find_word(word:str)->str:
     file = open("dict.txt","r")
     for line in file:
          tmp = line.split(" ",1)
         if word == tmp[0]:
              return tmp[1].strip()
print(find_word(aa))


