import sys
import operator
import collections

def percentage(part, whole):
  return 100 * float(part)/float(whole)

filename = sys.argv[0]
word_dict = dict()
char_count = 0
line_count = 0
word_count = 0
letter_count = 0

# The list is defined by the programmer
list_exclude = ["i","of","this","the","and","or","to","a","that","is",""]

file = open(filename,"r")
data = file.read()

# Count the number of characters(including blankspace)
char_count = len(data)
text = data.strip()

# Count the number of occurences of each letter
letter_dict = dict()
for x in 'abcdefghijklmnopqrstuvwxyz':
    letter_dict[x] = text.count(x)
    letter_count += letter_dict[x]

file.close()

# Count the number of lines in the file
file = open(filename,"r")
for line in file:
    line_count += 1
file.close()


# Count frequencies of each word
# Merge hyphenated words
file = open(filename, 'r')
filedata = file.read()
filedata = filedata.replace('-\n', '')
file.close()
file = open(filename,'w')
file.write(filedata)
file.close()

# Count the number of words
file = open(filename,"r")
for line in file:

  # Get rid of punctuations
  for char in line:
      if char in ",.!?:;()[]\"*~_<>":
          line = line.replace(char,'')
  # Remove leading and trailing characters
  line = line.strip()
  line = line.lower()

  words = line.split(" ")
  word_count += len(words)

  #make word dictionary
  for word in words:
      if word not in list_exclude:
          if word in word_dict:
              word_dict[word] += 1
          else:
              word_dict[word] = 1
file.close()

#print the number of chars, lines and words
print("%%%%%%%%%%%%%%%%Number of Characters, Lines and Words%%%%%%%%%%%%%%%%")
print("The number of characters in the txt file is {}".format(char_count))
print("The number of lines in the txt file is {}".format(line_count))
print("The number of words in the txt file is {}".format(word_count))

#print letters' number of occurences
print("%%%%%%%%%%Number of Occurrences (Percentage) of Each Letter%%%%%%%%%%")
for key in list(letter_dict.keys()):
    percent = percentage(letter_dict[key],letter_count)
    print("{}:{}%".format(key,percent))

#print most frequent 10 Words
print("%%%%%%%%%%%%%%%%Top 10 Number of Occurrences of Words%%%%%%%%%%%%%%%%")
word_counter = collections.Counter(word_dict)
for word, count in word_counter.most_common(10):
    print("{}:{}".format(word, count))
