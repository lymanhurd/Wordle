import json
import math

# Opening JSON file
f = open('wordle-answers.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['words']:
    print(i)

# Closing file
f.close()


def score(guess, secret):
    already_used = []
    result = []
    for j in range(5):
        for k in range(5):
            if guess[j] not in already_used:
                if guess[j] == secret[k] and j == k:
                    result += 'g'
                    already_used += guess[j]
                elif guess[j] == secret[k]:
                    result += 'y'
                    already_used += guess[j]
        if j >= len(result):
            result += '-'
    print(result)


def tally_letters():
    result = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0,
              "f": 0, "g": 0, "h": 0, "i": 0, "j": 0,
              "k": 0, "l": 0, "m": 0, "n": 0, "o": 0,
              "p": 0, "q": 0, "r": 0, "s": 0, "t": 0,
              "u": 0, "v": 0, "w": 0, "x": 0, "y": 0,
              "z": 0}
    for j in data["words"]:
        for k in range(5):
            result[j[k]] += 1
    return result


def total_words():
    result = 0
    for j in data["words"]:
        result += 1
    return result


def find_probability():
    result = tally_letters()
    total = total_words()
    for j in result.keys():
        result[j] = result[j]/total
    return result


def find_information():
    result = find_probability()
    for j in result.keys():
        if result[j] is 0:
            result[j] = 0
        else:
            result[j] = -result[j] * math.log(result[j], 2)
    return result


def sort_information():
    x = find_information()
    return {k: v for k, v in sorted(x.items(), key=lambda item: item[1], reverse=True)}


def translate_guess(word):
    info = sort_information()
    result = 0
    for j in word:
        print(info[j])
        result += info[j]
        print(result)
    return result


if __name__ == '__main__':
    score('abdce', 'abcde')
    print(tally_letters())
    print(total_words())
    print(find_probability())
    print(find_information())
    print(sort_information())
    print(translate_guess("radio"))
