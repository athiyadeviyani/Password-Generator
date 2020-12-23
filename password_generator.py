from nltk.corpus import brown 
import random
import pyperclip

# Retrieve English words from brown corpus
print('Starting password generator...')

words = brown.tagged_words(tagset='universal')
adjectives = [x.lower() for x,y in words if y == 'ADJ' if x.isalpha()]
verbs = [x.lower() for x,y in words if y == 'VERB' if x.isalpha() and 'ing' in x]
nouns = [x.lower() for x,y in words if y == 'NOUN' if x.isalpha()]
det = [x.lower() for x,y in words if y == 'DET' if x.isalpha()]

vowels = 'aeiou'

def generate(no_words, caps, nums, punc):
    """
    Generates password from input parameters.

    Input
    - no_words: number of words in final password
    - caps: final password includes capital letters
    - nums: final password includes numbers
    - punc: final password includes punctuations
    """

    words_list = []
    password = ''

    if no_words == 4:
        i, j, k, l = random.randint(0, len(det)-1), random.randint(0, len(adjectives)-1), random.randint(0, len(verbs)-1), random.randint(0, len(nouns)-1)
        cdet = det[i]
        cadj = adjectives[j]
        while cadj[0] in vowels and cdet == 'a':
            i = random.randint(0, len(det)-1)
            cdet = det[i]
        words_list.append(cdet)
        words_list.append(cadj)
        words_list.append(verbs[k])
        words_list.append(nouns[l])

    elif no_words == 3:
        i, j, k = random.randint(0, len(det)-1), random.randint(0, len(adjectives)-1), random.randint(0, len(nouns)-1)
        cdet = det[i]
        cadj = adjectives[j]
        while cadj[0] in vowels and cdet == 'a':
            i = random.randint(0, len(det)-1)
            cdet = det[i]
        words_list.append(cdet)
        words_list.append(cadj)
        words_list.append(nouns[k]) 

    elif no_words == 2:
        i, j = random.randint(0, len(adjectives)-1), random.randint(0, len(nouns)-1)
        words_list.append(adjectives[i])
        words_list.append(nouns[j]) 

    elif no_words == 1:
        word = ''
        while len(word) < 8:
            word = words[random.randint(0, len(words)-1)][0]
        if nums == 'y':
            numstr = ''
            while len(numstr) < 2:
                numstr += str(random.randint(0, 9))
            word += numstr 
            
        if caps == 'y' and punc == 'y':
            password = word.capitalize()
            password += '!'
            return password
        elif caps == 'y' and punc == 'n':
            return word.capitalize()
        elif caps == 'n' and punc == 'y':
            return (word + '!')
        else:
            return word

    # Add two digits to final password
    if nums == 'y':
        numstr = ''
        while len(numstr) < 2:
            numstr += str(random.randint(0, 9))
        words_list.append(numstr)

    # Add capital letters and puncuations to final password
    if caps == 'y' and punc == 'n':
        words_list = [x.capitalize() for x in words_list]
        password = ''.join(words_list)
        return password
    elif caps == 'n' and punc == 'y':
        password = '-'.join(words_list)
        return password
    elif caps == 'y' and punc == 'y':
        words_list = [x.capitalize() for x in words_list]
        password = '-'.join(words_list)
        return password
    else:
        password = ''.join(words_list)
        return password


def main():
    """
    Program entry-point.
    """

    no_words = int(input('How many words? (1-4) '))
    while no_words not in [1,2,3,4]:
        print('Please input only the numbers 1, 2, 3, or 4!')
        no_words = int(input('How many words? (1-4) '))
    caps = input('Include capitals? (y/n) ')
    while caps not in ['y', 'n']:
        print('Please input only y or n.')
        caps = input('Include capitals? (y/n) ')
    nums = input('Include numbers? (y/n) ')
    while nums not in ['y', 'n']:
        print('Please input only y or n.')
        nums = input('Include numbers? (y/n) ')
    punc = input('Include punctuations? (y/n) ')
    while punc not in ['y', 'n']:
        print('Please input only y or n.')
        punc = input('Include punctuations? (y/n) ')

    retry = 'y'
    
    while retry == 'y':
        password = generate(no_words, caps, nums, punc)
        pyperclip.copy(password)
        print('Here is your password: ' + password)
        retry = input('Try again? (y/n) ')
        while retry not in ['y', 'n']:
            print('Please input only y or n.')
            retry = input('Try again? (y/n) ')

    print('Your password has been copied to clipboard. Thank you for using Password Generator and stay safe online!')

main()
