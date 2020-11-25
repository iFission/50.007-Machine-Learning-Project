from tqdm import tqdm
import itertools


def load_dataset(language):
    tag_seq_ls = []
    word_seq_ls = []
    test_word_seq = []

    path_train = f'{language}/train'
    path_test = f'{language}/dev.in'

    with open(path_train, "r") as f:
        document = f.read().rstrip()
        sentences = document.split("\n\n")

        for sentence in tqdm(sentences):
            word_seq = []
            tag_seq = []
            for word_tag in sentence.split("\n"):
                word, tag = word_tag.split(" ")
                tag_seq.append(tag)
                word_seq.append(word)

            tag_seq_ls.append(tag_seq)
            word_seq_ls.append(word_seq)

    with open(path_test, "r") as f:
        document = f.read().rstrip()
        sentences = document.split("\n\n")

        for sentence in tqdm(sentences):
            word_seq = []
            for word in sentence.split("\n"):
                word_seq.append(word)
            test_word_seq.append(word_seq)

    return tag_seq_ls, word_seq_ls, test_word_seq


tag_seq_ls, word_seq_ls, test_word_seq = load_dataset("SG")

tags_unique = []
words_unique = []


def get_unique_elements(nested_list):
    return list(set(list(itertools.chain.from_iterable(nested_list))))


tags_unique = get_unique_elements(tag_seq_ls)
tags_unique.sort()
words_unique = get_unique_elements(word_seq_ls)
tags_unique_with_start_stop = ["START"] + tags_unique + ["STOP"]


def generate_emission_pairs(tag_seq_ls, word_seq_ls):
    emission_pairs = []

    for state_seq, obser_seq in zip(tag_seq_ls, word_seq_ls):
        for state, obser in zip(state_seq[1:-1], obser_seq):
            emission_pairs.append([state, obser])

    return emission_pairs


emission_pairs = generate_emission_pairs(tag_seq_ls, word_seq_ls)


def generate_possible_emission_pairs(tags_unique, words_unique):

    return list(itertools.product(tags_unique, words_unique))


emission_pairs_possible = generate_possible_emission_pairs(
    tags_unique, words_unique)


def calculate_b(u, o, emission_pairs, tag_seq_ls):
    numerator = emission_pairs.count([u, o])
    denominator = sum([pair.count(u) for pair in tag_seq_ls])

    return numerator / denominator


def count_y(tag, tag_seq_ls):
    tag_seq_ls_flattened = list(itertools.chain.from_iterable(tag_seq_ls))
    return tag_seq_ls_flattened.count(tag)


"""
# part 1
emission_matrix = {}
for tag in tags_unique:
    emission_matrix_row = {}
    for word in words_unique:
        emission_matrix_row[word] = 0.0
    emission_matrix[tag] = emission_matrix_row

for tags, words in zip(tag_seq_ls, word_seq_ls):
    for tag, word in zip(tags, words):
        emission_matrix[tag][word] += 1

for emission_matrix_row_key, emission_matrix_row in emission_matrix.items():
    row_sum = sum(emission_matrix_row.values())
    count_y(emission_matrix_row_key, tag_seq_ls)
    for word, cell in emission_matrix_row.items():
        emission_matrix[emission_matrix_row_key][word] = cell / row_sum
"""

k = .5
emission_matrix_2 = {}
for tag in tags_unique:
    emission_matrix_2_row = {}
    for word in words_unique:
        emission_matrix_2_row[word] = 0.0
    emission_matrix_2_row["#UNK#"] = 0.0
    emission_matrix_2[tag] = emission_matrix_2_row

for tags, words in zip(tag_seq_ls, word_seq_ls):
    for tag, word in zip(tags, words):
        emission_matrix_2[tag][word] += 1

for emission_matrix_2_row_key, emission_matrix_2_row in emission_matrix_2.items(
):
    row_sum = count_y(emission_matrix_2_row_key, tag_seq_ls) + k

    # words in training set
    emission_matrix_2_row.popitem()
    for word, cell in emission_matrix_2_row.items():
        emission_matrix_2[emission_matrix_2_row_key][word] = cell / row_sum

    # word == #UNK#
    emission_matrix_2[emission_matrix_2_row_key]["#UNK#"] = k / (row_sum + k)

test_word_unique = get_unique_elements(test_word_seq)

unseen_words = set(test_word_unique).difference(set(words_unique))


def get_best_tag(word, emission_matrix):
    y = ""
    score_max = -1

    for tag, emission_matrix_row in emission_matrix.items():
        score_current = emission_matrix_row[word]

        if score_current > score_max:
            score_max = score_current
            y = tag

    return y


def get_prediction(test_word_seq, emission_matrix):
    output = ""
    for test_word in test_word_seq:
        for word in test_word:
            best_tag = ""
            if word in unseen_words:
                best_tag = get_best_tag("#UNK#", emission_matrix)
            else:
                best_tag = get_best_tag(word, emission_matrix)

            output += f"{word} {best_tag}"
            output += "\n"
        output += "\n"

    return output


prediction = get_prediction(test_word_seq, emission_matrix_2)

with open("SG/dev.p2.out", "w") as f:
    f.write(prediction)

print()