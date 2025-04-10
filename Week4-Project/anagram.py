from anagram_checker import AnagramChecker
checker = AnagramChecker('Week4-Project/sowpods.txt')

#Show a menu, offering the user to input a word or exit. Keep showing the menu until the user chooses to exit.
while True:
    choice = input("type in a word or type in 'exit'")
    if choice.lower() == 'exit':
        break
    elif len(choice.split())> 1:
        print('you type in too many words, start over')
    elif not choice.isalpha():
        print('letters only! try again')
    else:
        word = choice.lower()
        print(f'Your Word: {word.upper()}')
        print('Is valid:',checker.is_valid_word(word))

        anagrams = checker.get_anagrams(word)
        print(f'Anagrams found: {', '.join(anagrams) if anagrams else 'None'}')
