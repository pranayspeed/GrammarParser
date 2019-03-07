
class EBNFParser:
    def __init__(self, enbf_grammer):
        self.ebnf_grammer = enbf_grammer
        self.t = {}
        ruleIter = iter(self.ebnf_grammer)
        t_started=False
        nt_started=False
        current_nt = ""
        current_token=""
        chr = ruleIter.next()
        while ruleIter != None:            
            if(chr !=" "):
                if(t_started == False and nt_started == False):
                    #parsing not started
                    print('Parsing Start Valid Charater "{}"', chr)
                    if(chr == "'"):
                        print("Non terminal Cannot be on LHS")
                        break
                    if(current_nt != ""):
                        if(chr != ':'):
                            print(": expected")
                        else:
                            chr = ruleIter.next()
                            if(chr != "="):
                                print("= expected {}", chr)
                            else:
                                chr = ruleIter.next()
                                while chr == " ":
                                     chr = ruleIter.next()
                                if(chr.isalpha()):
                                    nt_started = True
                                    current_token+=chr
                                elif(chr == "'"):
                                    t_started = True
                                    current_token+=chr
                                else:
                                    print("Terminal or non terminal expected {}", chr)


                    if(chr.isalpha()):
                        nt_started=True
                        current_token+=chr
                    else:
                        print("Non Terminal symbol can only start with Alphabets")
                        break
                else:
                    if(chr == "|"):
                        NotImplemented
                        # process next token
                    elif(chr == "'"):
                        current_token+=chr
                        if(t_started== False):
                            # new Terminal symbol started
                            t_started=True
                        else:
                            t_started=False
                            # terminal collected completely
                            self.t[current_nt].append(current_token)
                            current_token=""

                    else:    
                        current_token+=chr
                        if(nt_started == True):
                            #non terminal processing
                            None                          

                        elif(t_started==True):
                            #terminal processing                            
                            pass
            else:
                if(nt_started == True):
                    # current Non terminal completed
                    current_nt = current_token
                    current_token=""
                    nt_started = False
                #elif(t_started== True):
                    # current terminal is completed
            chr = ruleIter.next() 


        
import collections
import re

Token = collections.namedtuple('Token', ['type', 'value', 'line', 'column','next'])

class BNFParser:
    def __init__(self, grammar):
        self.token_specification = [
                ('EQUAL',   r':='),           # Assignment operator
                ('NONTERMINAL',       r'[A-Za-z]+'),    # Identifiers
                ('OR',       r'\|'),      # Arithmetic operators
                ('NEWLINE',  r'\n'),           # Line endings
                ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
                ('T_START',  r'\''),       # Skip over spaces and tabs
                #('TERMINAL', r'[^;]+'),    # Identifiers
                ('MISMATCH', r'.'),            # Any other character
        ]
        self.tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in self.token_specification)
        self.grammar = grammar


    def tokenize(self):
        line_num = 1
        line_start = 0
        termst=False
        tmpValue =""
        for mo in re.finditer(self.tok_regex, self.grammar):
            kind = mo.lastgroup
            value = mo.group()
            column = mo.start() - line_start
            if termst == True and kind != 'T_START':
                tmpValue+=value
                
            if kind == 'T_START':
                if termst== False:
                    termst=True
                    tmpValue =value
                else:
                    termst=False
                    value = tmpValue + value
                    kind = 'TERMINAL'
            elif kind == 'NEWLINE':
                line_start = mo.end()
                line_num += 1
                continue
            elif kind == 'SKIP':
                continue
            elif kind == 'MISMATCH' and termst==False:
                raise RuntimeError(f'{value!r} unexpected on line {line_num}')
            
            if termst==False:
                yield Token(kind, value, line_num, column, None)
        if termst==True:
            raise RuntimeError(f'Missing single quote, {value!r} unexpected on line {line_num},column {column}') 




        
    



    
