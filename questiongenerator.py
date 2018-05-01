import nltk

qdic = {
       'HUMAN':'siapa',
       'ENTITY':'apa',
       'LOCATION':'mana',
       'TIME':'kapan',
       'COUNT':'berapa'       
       }

inp = 'budi/b/human main/b/verb bola/b/entity'
asdf = 'Novel/b/entity dibaca/b/verb Andi/b/human di/b/verb kamar/b/location'
res = qGen.process(asdf)

class qGen():
    
    def __init__(self):
        a = 1
        
    def process(inp):
        tupl = [nltk.tag.str2tuple(t) for t in inp.split()]
        
        tuplez = []
        
        for x in tupl:
            tup = nltk.tag.str2tuple(x[0])
            tuplez.append([tup[0],tup[1],x[1]])
        
        tuples = []
        
        for x in range(0,len(tuplez)):
            if x+1 < len(tuplez):
                
                if tuplez[x][1] == 'B' and tuplez[x+1][1] == 'B':
                    tuples.append([tuplez[x][0], tuplez[x][2]])
                elif tuplez[x][1] == 'B'and tuplez[x+1][1] == 'I':
                    word = tuplez[x][0]
                    a = 1
                    while True:
                        if x+a < len(tuplez):
                            if tuplez[x+a][1] == 'I':
                                word += ' ' + tuplez[x+a][0]
                                a += 1
                            elif tuplez[x+a][1] == 'B':
                                break
                        else:
                            break
                    tuples.append([word, tuplez[x][2]])
            else:
                if tuplez[x][1] == 'B':
                    tuples.append([tuplez[x][0], tuplez[x][2]])
        
        questions = []
        for x in tuples:
            if x[1] in qdic:
                word = ''
                qword = qdic[x[1]]
                for y in tuples:
                    if x[0] is not y[0]:
                        word += y[0] + ' '
                    elif x[0] == y[0]:
                        word += qword + ' '
                questions.append(word)
                
        return questions

