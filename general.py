text = "Watching whales in Wales, wow!"

# Expected output: 

# Next: Replace multiple characters
# w with c [2,3,4] and a with b in fist and second position [1,2]


def replace_letter_by_positions(text, letter_to_replace, replacement_letter, positions):
    """ 
    Replaces a character in a given set of word positions keeping current case. 

    :param text: Original string.
    :param letter_to_replace: Letter that is going to be replaced.
    :param replacement_letter: Letter that will be inserted. 
    :param positions: Iterable containing positions as "nth() instance of letter to replace".
    :return: String with letters replaced.
    """
    modified_text = text
    working_position = 0

    for i, char in enumerate(text):
        if char == letter_to_replace.upper() or char == letter_to_replace.lower():
            working_position += 1 
            if working_position in positions: 
                is_upper_case = char.isupper()    
                if is_upper_case:
                    modified_text = replace_char_by_index(modified_text, i, replacement_letter.upper())
                else:
                    modified_text = replace_char_by_index(modified_text, i, replacement_letter.lower())
    return modified_text

def replace_char_by_index(text, index, replacement_letter):
    """ Replaces a character in a string by its index. """
    return text[:index] + replacement_letter + text[index+1:]


class ReplacementArgs:
    """ Helper class for the replacement of a letter by a given list of positions. """ 
    
    def __init__(self, letter_to_replace, replacement_letter, positions):
        self.letter_to_replace = letter_to_replace
        self.replacement_letter = replacement_letter
        self.positions = positions


def replace_multiple_letters_by_positions(text, replacement_args_list):
    """ 
    Helper function to replace multiple characters in a given string by respective replacement letters in respective 
    positions as specified in each instance of ReplacementArgs.

    :param text: Original string.
    :replacement_parms_list: Iterable of ReplacementArgs instances.
    :return: String with letters replaced.
    """
    modified_text = text

    for replacement_args in replacement_args_list:
        modified_text = replace_letter_by_positions(
            modified_text,
            letter_to_replace=replacement_args.letter_to_replace,
            replacement_letter=replacement_args.replacement_letter,
            positions=replacement_args.positions
        )
    return modified_text