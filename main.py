import logging

from dancing_links.links import solve


word_dict = {}


def remove_duplicate_letters(lines):
    result = []
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip("\n")
    for j in range(len(lines)):
        if len(set(lines[j])) == 5:
            result.append(lines[j])
    return result


def sort_and_remove_duplicates(lines):
    result = []
    new_lines = remove_duplicate_letters(lines)
    for i in new_lines:
        organized = ''.join(sorted(i))
        if organized not in result:
            result.append(organized)
        if organized not in word_dict:
            word_dict[organized] = [i]
        else:
            word_dict[organized].append(i)
    return result


def break_word_into_vector(word):
    result = [0] * 27
    for i in word:
        result[ord(i.lower()) - 97] = 1
    return result


def convert_vector_into_word(vector):
    result = ""
    for i in range(26):
        if vector[i] == 1:
            result += chr(i + 97)
    return result


def alphabet_rows():
    mrow = ([0] * 26) + [1]
    matrix = []
    for i in range(26):
        matrix.append(mrow[:])
        matrix[i][i] = 1
    return matrix


def get_row_name(word):
    if len(word_dict[word]) == 1:
        return word_dict[word][0]
    else:
        return ", ".join(word_dict[word])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('wordle.txt') as f:
        lines = f.readlines()
    # word_dict = {}
    # print(len(lines))
    deduped = remove_duplicate_letters(lines)
    nodupelist = sort_and_remove_duplicates(lines)
    # print(convert_vector_into_word(break_word_into_vector("ABCYZ")))
    # print([w.strip() for w in lines if len(set(w)) == 5])
    # print(word_dict)
    row_names = [get_row_name(w) for w in word_dict.keys()]
    word_matrix = [break_word_into_vector(w) for w in word_dict.keys()]
    # print(word_matrix)
    #test_list = break_word_into_vector("ilrsw")
    #test_list = [1] + ([0] * 25) + [1]
    #print_solution([test_list])
    word_matrix += alphabet_rows()
    row_names += [chr(i) for i in range(97, 123)]
    solve(word_matrix, row_names=row_names)
