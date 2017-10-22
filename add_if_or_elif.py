import random

def write_formula():
    temp1=random.choice(['~','x','y','X','Y','p','f','F','P','S','c','C','A','t','h','H','q','Q','g','G','w','W'])
    if temp1=='~':
        temp1=str(random.randint(0,9999))

    temp2=random.choice(['+','-','*','/','%'])

    temp3=random.choice([str(random.randint(0,9999)),'x','y','X','Y','p','f','F','P','S','c','C','A','t','h','H','q','Q','g','G','w','W'])

    return str(temp1+temp2+temp3)


def add_if(dna,place):
    temp=place
    indent=0
    return_code=''
    temp2=''
    for i in dna:
        if i==':':
            indent+=1
        if i==';':
            inndent-=1

        if indent>0:
            returnCode=random.choice(['i','i','i','l'])
        else:
            return_code='i'
        return_code+=write_formula()+random.choice('=','!','<',',','>','.')+write_formula()
    for j in range(1,3):
        return_code+=random.choice('&','|')+write_formula()+random.choice('=','!','<',',','>','.')+write_formula()
    return_code+=':'
    for j in range(1,3):
        temp2=random.choice('U','L','R','D','b','a','s')
        return_code+=temp2
        if temp2 in ('U','L','R','D','s'):
            return_code+=write_formula()
    if random.randint(0,1)==0:
        return_code+=';'

    return return_code

    # print(dna[place])
    # print(dna[place-1:place)

print (add_if_or_elif("abcdefghijklmnop",3))
