#BRIANNE KELLY R. OLLOS
#STRUCTURES

letters = ['s','l','l','o','s','s','o','l',
                's','o','o','l','o','l','s','s',
                'o','s','s','o','l','l','l',
                's','l','s','l','l','o','o','s',
                'l','l','s','o','s','s','o']


from collections import Counter
letters_counts = Counter(letters)
repeat = letters_counts.most_common(3)
print ("letters repeated")
print(repeat)
