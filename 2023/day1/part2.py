# open the text file inputs/1.txt
def read_input():
    with open(f'input.txt', 'r') as f:
        data = f.read().splitlines()
    return data

word_to_number = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
}

def replace_number_with_word(string):
    '''Replace all numbers in a string with their corresponding word
    Example: "two1nine" -> "twoonenine" ''' 
    for word, number in word_to_number.items():
        string = string.replace(str(number), word)
    return string

def find_substrings_with_digits(string):
    ''' Find all substrings in a string that contain digits
    Example: "eightwothree" -> ["eight", "two", "three"] 
    The function returns the substrings in the order they appear in the string 
    and translates them to their corresponding number'''
    substrings_with_indices = []

    for word in word_to_number.keys():
        index = string.find(word)
        while index != -1:
            substrings_with_indices.append((word, index))
            index = string.find(word, index + 1)

    # sort the substrings based on their indices
    substrings_with_indices.sort(key=lambda x: x[1])

    # extract the translated numbers from the sorted substrings
    substrings_translated = [word_to_number[word] for word, _ in substrings_with_indices]
    return substrings_translated

def get_calibration_value(): 
    second_sum_of_digits = 0
    for i in read_input():
        # replace numbers with words
        string = replace_number_with_word(i)
        # find all substrings with digits
        substrings = find_substrings_with_digits(string)

        first_digit = substrings[0]
        last_digit = substrings[-1]
        final_digit = first_digit*10 + last_digit

        second_sum_of_digits += final_digit

    return second_sum_of_digits

value = get_calibration_value()
print(value)