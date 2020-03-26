#
# mathScores=[60,70,10,20,81,63,55,64,84,88]
# print(mathScores[2])
# print(mathScores[1:6])
# print(mathScores[-1])
# print(mathScores[5:])
# print(sum(mathScores))
# print(min(mathScores))
# print(max(mathScores))
# k=[]
# print(k)
#
# k.append(6)
# k.append(50)
# k.append(55)
# k.append(566)
# print(k)
# # k.insert[1,5]
# k.remove(50)
# print(k)
# k.pop()
# print(k)
# print(55 in k)

# gr=[[5,14,7],[23,36,28],[88,80,92]]
# print(gr[2])
# print(sum(gr[0])/len(gr[0]))
# print(sum(gr[1])/len(gr[1]))
# print(sum(gr[2])/len(gr[2]))
# gr.append([94,90,96])
# gr[0].insert(1,20)
# gr[0].remove(14)
# print(gr[0])

# tuple=(1,2,3,4,5)
# tuple2=1,2,3,4,5
# tuple3=()
# print(tuple)
# print(tuple2)
# print(tuple3)
# print(tuple[3])
# print(tuple.index(4))
# print(tuple.count(4))
#
# print(sorted(tuple+tuple2,reverse=True))
# tuple1=(88,12)
# x, y=tuple1
# print(x)
# print(y)
#
# gr=((5,14,17),(23,36,28),(88,80,29))
# print(gr[2])
# print(sum(gr[0])/len(gr[0]))
# print(sum(gr[1])/len(gr[1]))
# print(sum(gr[2])/len(gr[2]))

# gr={'ch':[5,14,7],'en':[23,36,38],'ma':[88,80,92]}
# print(gr['ma'])
# print(gr.get('ma'))
# print(sum(gr['ch'])/len(gr['ch']))
# print(sum(gr['en'])/len(gr['en']))
# print(sum(gr['ma'])/len(gr['ma']))
# gr['sc']=[94,90,96]
# gr.update({'sc':[94,90,96]})
# print(gr.values())
# for ite in gr.items():
#     print(ite)
# print(gr.pop("sc"))
# for ite in gr.items():
#     print(ite)

all = {'jo', 'ev', 'ji', 'er', 'an', 'al', 'po', 'kr', 'ang'}
gi = {'jo', 'ev', 'ji', 'er', 'an'}
pi = {'an', 'er', 'al', 'po', 'kr'}
print(gi & pi)
print(gi - pi)
print(all - gi - pi)
all.add('kk')
print(all)
all.remove('kk')
print(all)
all.discard('kr')
print(all)
all.clear()
print(all)
