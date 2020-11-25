from tqdm import tqdm
import itertools
import copy

tag_seq_ls = []
word_seq_ls = []

tags_unique = []
words_unique = []

with open("SG(1)/train", "r") as f:
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


# emission_table = []
# for pair in tqdm(emission_pairs_possible):
#     b = calculate_b(pair[0], pair[1], emission_pairs, tag_seq_ls)
#     emission_table.append([pair, b])


def flatten(sequences):
    """
    Flatten a nested sequence
    """
    return itertools.chain.from_iterable(sequences)


emission_matrix = {}
for tag in tags_unique:
    emission_matrix_row = {}
    for word in words_unique:
        emission_matrix_row[word] = 0.0
    emission_matrix[tag] = emission_matrix_row

for tags, words in zip(tag_seq_ls, word_seq_ls):
    for tag, word in zip(tags, words):
        emission_matrix[tag][word] += 1

for emission_matrix_row_keys, emission_matrix_row in emission_matrix.items():
    row_sum = sum(emission_matrix_row.values())
    for word, cell in emission_matrix_row.items():
        emission_matrix[emission_matrix_row_keys][word] = cell / row_sum

#

print()