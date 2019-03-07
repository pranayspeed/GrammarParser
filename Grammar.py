from TextIterator import TextIterator
from Parser import EBNFParser
from Parser import BNFParser

class Grammar:
    def __init__(self, grammar):
        self.ebnfParser = BNFParser(grammar)
        self.root = None
        self.token = None
    
    def compile(self): 
        current_nt = None 
        prev_token = None  
        appendNew=True  # should append new production in same NONTERMINAL  
        for t in self.ebnfParser.tokenize():
            if self.root == None and t.type != 'NONTERMINAL':
                raise RuntimeError(f'Grammar should start with a non terminal value, {t.type} found')
            
            elif self.root == None:
                self.root = t
                current_nt = t
            else:
                if self.token == None:
                    #started the tree
                    self.token = dict()
                if t.type == 'EQUAL':
                    if prev_token.type != 'NONTERMINAL':
                        raise RuntimeError(f'Expected NONTERMINAL symbol, {prev_token.type} found')                        
                    current_nt = prev_token
                    appendNew = True

                elif t.type == 'TERMINAL' or t.type == 'NONTERMINAL':
                    if appendNew == True:
                        if current_nt in self.token:
                            self.token[current_nt].append(t)
                        else:
                            self.token[current_nt] = [t]
                        appendNew = False
                    else:
                        #need to fix as reference is not changing
                        curNode = self.token[current_nt][-1]
                        while curNode.next !=None:
                            curNode = curNode.next
                        curNode = curNode._replace(next=t)
                elif t.type== 'OR':
                    appendNew = True
            prev_token = t

    