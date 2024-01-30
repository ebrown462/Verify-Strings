from string_validation import validation
# testing data
sentence1 = 'The quick brown fox said "hello Mr lazy dog".'
sentence2 = 'The quick brown fox said hello Mr lazy dog.'
sentence3 = 'One lazy dog is too few, 13 is too many.'
sentence4 = 'One lazy dog is too few, thirteen is too many.'
sentence5 = 'The quick brown fox said "hello Mr lazy dog".'
sentence6 = 'How many "lazy dogs" are there?'
sentence7 = 'The quick brown fox said "hello Mr. lazy dog".'
sentence8 = 'the quick brown fox said "hello Mr lazy dog".'
sentence9 = '"The quick brown fox said "hello Mr lazy dog."'
sentence10 = 'One lazy dog is too few, 12 is too many.'
sentence11 = 'Are there 11, 12, or 13 lazy dogs?'
sentence12 = 'There is no punctuation in this sentence'

# testing (Should return either tru or false)
print(validation(sentence1))
print(validation(sentence2))
print(validation(sentence3))
print(validation(sentence4))
print(validation(sentence5))
print(validation(sentence6))
print(validation(sentence7))
print(validation(sentence8))
print(validation(sentence9))
print(validation(sentence10))
print(validation(sentence11))
print(validation(sentence12))