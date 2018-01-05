#!/usr/bin/python3
# -- encoding utf-8--

import os


def parser_unicode(src_string):
    """ parser unicode string to utf-8 string
    Arguments:
        src_string {str} -- [unicode string]
    Returns:
        [str] -- [utf-8 string]
    """

    # src_string = "\\u4e0b\\u6587\\u6709\\u4eba{}\"'<>《》～¥#@%……&&@@##"
    letters = src_string.split(r'\u')

    temp_letters = []
    results = []
    for letter in letters:
        if len(letter) > 4:
            temp_letters.append(letter[:4])
            results.append(
                repr('\\u'.join(temp_letters).encode('utf-8').decode(
                    'unicode_escape')))
            results.append(letter[4:])
            temp_letters = ['']
        else:
            temp_letters.append(letter)

    final_string = ''.join(results)
    print(final_string)
    return final_string


if __name__ == '__main__':
    print('hello World')
    with open(os.path.join("", "test.json"), 'w+', encoding="utf-8") as fwrite:
        with open(os.path.join("", "test.txt"), "r", encoding="utf-8") as file_conent:
            line_list = file_conent.readlines()
            for line in line_list:
                line = parser_unicode(line)
                fwrite.write(line)
