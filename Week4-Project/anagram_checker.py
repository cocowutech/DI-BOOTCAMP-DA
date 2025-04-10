class AnagramChecker:
    def __init__(self,word_list_file):
        with open(word_list_file, 'r') as file:
            self.word_list = [line.strip().lower() for line in file if line.strip().isalpha()]

    def is_valid_word(self,word):
        word = word.lower()
        return word in self.word_list
    
    def is_anagrams(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower()) and word1.lower()!= word2.lower()
        
    def get_anagrams(self,word):
        word = word.lower()
        anagrams = []
        
        for w in self.word_list:
            if self.is_anagrams(word,w):
                anagrams.append(w)
        return anagrams
    


