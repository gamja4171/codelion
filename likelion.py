total_list=[]

while True:
    question=input("질문을 입력하셈 : ")
    if question == 'q':
        break
    else:
        total_list.append({"질문" : question})
for i in total_list:
    print(i["질문"])
    answer=input("답변을 입력하셈 : ")
    i["답변"]=answer
print(total_list)