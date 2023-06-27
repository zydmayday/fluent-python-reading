fp = open('cafe.txt', 'w', encoding='utf-8')
fp.write('你好')
fp.close()

fp2 = open('cafe.txt')
print(fp2.read())
fp2.close()
