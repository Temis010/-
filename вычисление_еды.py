import random

for n in range(10):
    bylo1=open('Уже_было1.txt','a+',encoding='utf-8')
    bylo2=open('Уже_было2.txt','a+',encoding='utf-8')

    byloNedavno1=bylo1.read().split('\n')
    byloNedavno2=bylo2.read().split('\n')
    print(byloNedavno2)
    
    eda1=open('Список_первых_блюд.txt','r',encoding='utf-8').read().split('\n')
    data1=list(map(str,eda1))

    eda2=open('Список_вторых_блюд.txt','r',encoding='utf-8').read().split('\n')
    data2=list(map(str,eda2))

    if len(byloNedavno1)>=len(data1):
        byloNedavno1=byloNedavno1[-8:]
    if len(byloNedavno2)>=len(data2):
        byloNedavno2=byloNedavno1[-21:]
        
    print('было 1:',byloNedavno1)
    print('было 2:',byloNedavno2)
    
    pervoeChoice=[i for i in data1 if not(i in byloNedavno1)]
    vtoroeChoice=[i for i in data2 if not(i in byloNedavno2)]

    vtoroe=random.choice(vtoroeChoice)
    pervoe=random.choice(pervoeChoice)

    print(pervoe,vtoroe)

    bylo1.write(pervoe)
    bylo2.write(vtoroe)
    bylo1.write('\n')
    bylo2.write('\n')

    bylo1.close()
    bylo2.close()


