print('Hello, world!')

# raw文字列
print(R"年齢は22歳です")

# 文字列と数値の連結
num = 22
print("My age is " + str(num))

# 文字列の連結
str1 = "04,"
str2 = "myls"
print(str1 + str2)

# 文字数の取得
print("04mylsの文字数は" +str(len("04myls")))

# スライス
str = "04myls"

print(str[1:4])

print(str[2:6])

# スライス 省略
print("04myls"[:3])

# 書式化演算子
name = "04myls"
old = 22
print("名前は%-8sです。年齢は%03d歳です。"% (name,old))

# リストの文字列の連結
print("".join(["04","my","ls"]))

# formatメソッド
name = "04myls"
old = 22
print("名前は{:<8s}です。年齢は{:>3d}歳です。".format(name,old))

# if文 基本形
value = int(input('1～5の数を入力してください'))
if value == 1:
    print('1です')

# if else
value = int(input('1～5の数を入力してください'))
if value == 1:
    print('1です')
else:
    print('1ではありません')

# if elif else
value = int(input('1～5の数を入力してください'))
if value == 1:
    print('1です')
elif value == 2:
    print('2です')
else:
    print('1でも2でもありません')

# 小文字に変換
print("04MYLS".lower())

#　大文字に変換
print("04myls".upper())

# 先頭を大文字にして、それ以降を小文字
print("hello world".capitalize())

# 単語毎に最初の文字を大文字
print("hello world".title())

# 大文字を小文字に、小文字を大文字に変換
print("04Myls".swapcase())

# 全ての文字が小文字かどうか
print("myls".islower())

print("Myls".islower())

# 全ての文字が大文字かどうか
print("MYLS".isupper())

print("Myls".isupper())
