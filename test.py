

ebnfGrammer = """
S := 'Hello' | 'Hi' P | P
| 'bye'
P:= 'World' | 'Everyone' | '[A-Za-z0-9]+      ' | 'a'
"""



#from Parser import BNFParser


#ebnG = BNFParser(ebnfGrammer)

#for t in ebnG.tokenize():
#    print(t)

from Grammar import Grammar
gm = Grammar(ebnfGrammer)
gm.compile()

print(gm.root)

for tk in gm.token:
    print(tk.value)
    for v in gm.token[tk]:
        print('  ', end =" ")
        while v.next != None:
            print(v.value, end =" ")
            v=v.next
        print(v.value)
    