class BagofWord:
    def __init__(self):
        self.array = {}
        
    def add(self, word):
        self.array[word.lower()] =  self.array.get(word.lower(), 0) + 1
    def print(self):
        print(self.array)
    def __getitem__(self, word):
        return self.array.get(word.lower(), 0)
    def __setitem__(self, word, value):
        self.array[word.lower()] = value
    


d = BagofWord()
d.add("amin")
d.add("Amin")

d.print()
d["nima"]= 90
x = d["nima"]
print(x)