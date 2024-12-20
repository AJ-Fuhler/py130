# # Write a program that prints the longest sentence in a string based on the 
# number of words. You should also print the number of words in the longest 
# sentence.

# Sentences may end with periods (.), exclamation points (!), or question marks
# (?). You should treat any sequence of characters that are not spaces or
# sentence-ending characters as a word. Thus, -- should count as a word. Log
# the longest sentence and its word count. Pay attention to the expected
# output, and be sure you preserve the punctuation from the end of the
# sentence.

# Note that this problem is about manipulating and processing strings. As such,
# every detail about the string matters (e.g., case, punctuation, tabs, spaces,
# etc.).



SENTENCE_ENDINGS = '.?!'

def split_on_sentence_endings(text):
    sentences = []
    previous_sent_ending = 0
    
    for idx in range(len(text)):
        if text[idx] in SENTENCE_ENDINGS:
            curr_sent_ending = idx + 1
            sentences.append(text[previous_sent_ending:curr_sent_ending].strip())
            previous_sent_ending = curr_sent_ending
    
    return sentences


def word_count(string):
    words = string.split()
    return len(words)


def longest_sentence(text):
    sentences = split_on_sentence_endings(text)
    
    longest_sent = max(sentences, key=word_count)
    longest_sent_word_count = word_count(longest_sent)

    print(longest_sent + '\n')
    print(f"The longest sentence has {longest_sent_word_count} words.\n")

long_text = (
    'Four score and seven years ago our fathers brought forth on this '
    'continent a new nation, conceived in liberty, and dedicated to the '
    'proposition that all men are created equal. Now we are engaged in a '
    'great civil war, testing whether that nation, or any nation so '
    'conceived and so dedicated, can long endure. We are met on a great '
    'battlefield of that war. We have come to dedicate a portion of that '
    'field, as a final resting place for those who here gave their lives '
    'that that nation might live. It is altogether fitting and proper that '
    'we should do this.'
)

longer_text = long_text + (
    'But, in a larger sense, we can not dedicate, we can not consecrate, '
    'we can not hallow this ground. The brave men, living and dead, who '
    'struggled here, have consecrated it, far above our poor power to add '
    'or detract. The world will little note, nor long remember what we say '
    'here but it can never forget what they did here. It is for us the '
    'living, rather, to be dedicated here to the unfinished work which '
    'they who fought here have thus far so nobly advanced. It is rather '
    'for us to be here dedicated to the great task remaining before us -- '
    'that from these honored dead we take increased devotion to that '
    'cause for which they gave the last full measure of devotion -- that '
    'we here highly resolve that these dead shall not have died in vain '
    '-- that this nation, under God, shall have a new birth of freedom -- '
    'and that government of the people, by the people, for the people, '
    'shall not perish from the earth.'
)

longest_sentence(long_text)
# Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal.
#
# The longest sentence has 30 words.

longest_sentence(longer_text)
# It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth.
#
# The longest sentence has 86 words.

longest_sentence("Where do you think you're going? What's up, Doc?")
# Where do you think you're going?
#
# The longest sentence has 6 words.

longest_sentence("To be or not to be! Is that the question?")
# To be or not to be!
#
# The longest sentence has 6 words.