f = open('파일명.txt', 'w') # create, open
f.write("데이터 입니다.")
f.close()


f = open('파일명.txt', 'r') # create, open
data = f.read()
f.close()

print(data)

with open('파일명.txt', 'r') as f:
    print(f.read())
