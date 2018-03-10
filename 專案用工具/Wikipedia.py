'''
 此程式當初是要從維基百科上抽取資料所用
'''
import wikipedia

target=input("請輸入要搜尋的條目")

storage=wikipedia.page(target)
target=target+".txt"
obj=open(target,"w")
obj.write(storage.content.encode("utf8").decode("cp950","ignore"))
