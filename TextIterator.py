
class TextIterator:
    def __init__(self, text):
        self.itr = iter(text)

    def __iter__(self):
        # since your string is already iterable
        return self.itr
        
    def next(self):
        return next(self.itr)



    
