from general import replace_letter_by_positions, replace_char_by_index, replace_multiple_letters_by_positions
from general import ReplacementArgs 


def test_letter_replacement_by_positions():
    """ Tests that letter is replaced correctly in a given text. """
    modified_text = replace_letter_by_positions(
        text="Watching whales in Wales, wow!",
        letter_to_replace="w",
        replacement_letter="z",
        positions=[2,3,4]
    )
    assert modified_text == "Watching zhales in Zales, zow!"

def test_replace_char_by_index():
    """ Tests that char is replaced by the index in a given text correctly. """
    text = "example"
    assert replace_char_by_index(text, 1, "D") == "eDample"
    assert replace_char_by_index(text, 3, "T") == "exaTple"

def test_multiple_letter_replacement_by_positions():
    """ Tests that multiple letters are replaced in respective positions in a given text. """
    replacement_args_1 = ReplacementArgs(
        letter_to_replace="w",
        replacement_letter="z",
        positions=[2,3,4]
    )
    replacement_args_2 = ReplacementArgs(
        letter_to_replace="a",
        replacement_letter="b",
        positions=[1,2]
    )

    modified_text = replace_multiple_letters_by_positions(
        text="Watching whales in Wales, wow!",
        replacement_args_list=[replacement_args_1, replacement_args_2]
    )
    assert modified_text == "Wbtching zhbles in Zales, zow!"

def test_multiple_letter_replacement_by_positions_without_helper_class():
    """ Tests that multiple letters are replaced in respective positions in a given text without using the ReplacementArgs class. """
    original_text = "Watching whales in Wales, wow!"

    modified_text = replace_letter_by_positions(original_text,"w","z",[2,3,4])
    modified_text = replace_letter_by_positions(modified_text,"a","b",[1,2])

    assert modified_text == "Wbtching zhbles in Zales, zow!"