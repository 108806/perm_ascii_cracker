import hashlib

# INIT THE FILES, SOLVE POTENTIAL DUPS PROBLEM, AND CONCAT ALL:
file = open('matches.txt', 'r', encoding='UTF-8')
file_content = file.readlines()
words = ''.join(list(dict([x.split(":") for x in file_content]).keys())).lower()
print('\nThe concatenated string is :', words)

# SAVE A WORDS TO HASH TO THE EXTERNAL FILE,
# IE IF YOU WANT TO CHECK ANOTHER HASHING ALGORITH :
with open('wordsToHash.txt', 'w+', encoding='UTF8') as f:
    f.write(words)
    f.close()

# OPTIONAL - OUTPUT THE WORDS AND A HASH TO THE STDOUT:
print(len(words), 'Chars')
print(hashlib.sha256(words.encode('UTF-8')).hexdigest())
