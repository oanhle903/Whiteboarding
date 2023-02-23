def snake_to_camel(string):
    camel_words = []
    for i, word in enumerate(string.split('_')):
        if i == 0:
            camel_words.append(word)
        else:
            camel_words.append(word.title())
    return "".join(camel_words)


def lookup(phrase):
    """
    Write a function that takes in a phrase and returns a dictionary that can be used to lookup words by word lengths.

    For example, the phrase "cute cats chase funny rats" should return a dictionary like so:

    {
        4: {"cute", "cats", "rats"},
        5: {"chase", "funny"}
    }
    Notice that the keys of the dictionary above are integers and its values are sets that contain strings.
    """
    word_lengths = {}

    for word in phrase.split():
        #checks if the length of the current word is already a key in the word_lengths 
        word_lengths[len(word)] = word_lengths.get(len(word), set())

        word_lengths[len(word)].add(word)

    return word_lengths

def reverse_list_in_place(list):
    """Write a function that takes in a list and reverses it in-place (without creating a new list)."""

    for i in range(len(list)//2):
        list[i], list[-i-1] = list[-i-1], list[i]

        #alternative method
        # temp = list[i]
        # list[i] = list[-i-1]
        # list[-i-1] = temp

    return list

def is_anagram(str1, str2):
    """Write a function that takes in two strings and returns True if the strings are anagrams of one another. For example,

    "moon", "noom" => True
    "bat", "snack" => False
    "", "" => True
    """

    if len(str1) != len(str2):
        return False

    dict1 = {}
    for char in str1:
        dict1[char] = dict1.get(char, 0) + 1

    dict2 = {}
    for char in str2:
        dict2[char] = dict2.get(char, 0) + 1
                
    return dict1 == dict2


def print_message(phrase):
    """
    Write a function that prints an encrypted message.
    HOT SAUCE

    HTAC
    OSUE
    """
    new_string = "".join(phrase.split())
    string1 = ""
    string2 = ""
    for i, char in enumerate(new_string):
        if i % 2 == 0:
            string1 += char
        else:
            string2 += char

    print(string1)
    print(string2)

