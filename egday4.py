words = ['this', 'is', 'just', 'a', 'test']
capitalized_words = [x.capitalize() for x in words]

print 'Words:',words
print 'capitalized_words:', capitalized_words

words = ['hello', 'world','foo','bar','test','python',]
short_words = [x for x in words if len(x) <= 3]
others_words = [x for x in words if x not in short_words]
words_with_e = [x for x in words if x.count('e') >= 1]

print 'Words:', words
print 'short words:', short_words
print 'others words:', others_words
print 'words with "e":', words_with_e