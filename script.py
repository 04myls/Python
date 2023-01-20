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

# スライス　省略
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

