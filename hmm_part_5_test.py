from tqdm import tqdm
import itertools

languages = ["EN"]


def load_dataset(language):
    tag_seq_ls = []
    tag_seq_ls_with_start_stop = []
    word_seq_ls = []
    test_word_seq_ls = []

    path_train = f'{language}/train'
    path_test = f'{language}/test.in'

    with open(path_train, "r") as f:
        document = f.read().rstrip()
        sentences = document.split("\n\n")

        for sentence in tqdm(sentences):
            word_seq = []
            tag_seq = []
            tag_seq_with_start_stop = []
            for word_tag in sentence.split("\n"):
                word, tag = word_tag.split(" ")
                tag_seq.append(tag)
                word_seq.append(word)

            tag_seq_with_start_stop = ["START"] + tag_seq + ["STOP"]

            tag_seq_ls.append(tag_seq)
            tag_seq_ls_with_start_stop.append(tag_seq_with_start_stop)
            word_seq_ls.append(word_seq)

    with open(path_test, "r") as f:
        document = f.read().rstrip()
        sentences = document.split("\n\n")

        for sentence in tqdm(sentences):
            word_seq = []
            for word in sentence.split("\n"):
                word_seq.append(word)
            test_word_seq_ls.append(word_seq)

    return tag_seq_ls, tag_seq_ls_with_start_stop, word_seq_ls, test_word_seq_ls


def get_unique_elements(nested_list):
    return list(set(list(itertools.chain.from_iterable(nested_list))))


def get_unique_tags(tag_seq_ls):
    tags_unique = get_unique_elements(tag_seq_ls)
    tags_unique.sort()
    tags_unique_with_start_stop = ["START"] + tags_unique + ["STOP"]

    return tags_unique, tags_unique_with_start_stop


def get_unique_words(word_seq_ls):
    words_unique = get_unique_elements(word_seq_ls)
    words_unique.sort()

    return words_unique


def generate_emission_pairs(tag_seq_ls, word_seq_ls):
    emission_pairs = []

    for tag_seq, word_seq in zip(tag_seq_ls, word_seq_ls):
        for tag, word in zip(tag_seq, word_seq):
            emission_pairs.append([tag, word])

    return emission_pairs


def get_transition_pairs(tag_seq_ls):
    transition_pairs = []

    for tag_seq in tag_seq_ls:
        for tag1, tag2 in zip(tag_seq[:-1], tag_seq[1:]):
            transition_pairs.append([tag1, tag2])

    return transition_pairs


def generate_possible_transition_pairs(tags_unique):

    return list(itertools.product(tags_unique[:-1], tags_unique[1:]))


def get_transition_triplets(tag_seq_ls):
    transition_triplets = []

    for tag_seq in tag_seq_ls:
        for tag1, tag2, tag3 in zip(tag_seq[:-2], tag_seq[1:-1], tag_seq[2:]):
            transition_triplets.append([tag1, tag2, tag3])

    return transition_triplets


def generate_possible_emission_pairs(tags_unique, words_unique):

    return list(itertools.product(tags_unique, words_unique))


def generate_possible_transition_triplets(tags_unique):

    return list(
        itertools.product(tags_unique[:-1], tags_unique[1:-1],
                          tags_unique[1:]))


def count_y(tag, tag_seq_ls):
    tag_seq_ls_flattened = list(itertools.chain.from_iterable(tag_seq_ls))
    return tag_seq_ls_flattened.count(tag)


def get_emission_matrix(tags_unique, words_unique, tag_seq_ls, word_seq_ls, k):

    # create and initialise emission matrix
    emission_matrix = {}
    for tag in tags_unique:
        emission_matrix_row = {}
        for word in words_unique:
            emission_matrix_row[word] = 0.0
        emission_matrix_row["#UNK#"] = 0.0
        emission_matrix[tag] = emission_matrix_row

    # population emission matrix with counts
    for tags, words in zip(tag_seq_ls, word_seq_ls):
        for tag, word in zip(tags, words):
            emission_matrix[tag][word] += 1

    # divide cells by sum, to get probability
    for tag, emission_matrix_row in emission_matrix.items():
        row_sum = count_y(tag, tag_seq_ls) + k

        # words in training set
        popped = emission_matrix_row.popitem()
        for word, cell in emission_matrix_row.items():
            emission_matrix[tag][word] = cell / row_sum

        # word == #UNK#
        emission_matrix[tag]["#UNK#"] = k / (row_sum)

    return emission_matrix


def get_transition_matrix_pairs(tags_unique_with_start_stop, transition_pairs,
                                tag_seq_ls_with_start_stop):

    # create and initialise transition matrix
    transition_matrix = {}
    for tag1 in tags_unique_with_start_stop[:-1]:
        transition_matrix_row = {}
        for tag2 in tags_unique_with_start_stop[1:]:
            transition_matrix_row[tag2] = 0.0
        transition_matrix[tag1] = transition_matrix_row

    # population transition matrix with counts
    for tag1, tag2 in transition_pairs:
        transition_matrix[tag1][tag2] += 1

    # divide cells by sum, to get probability
    for tag1, transition_matrix_row in transition_matrix.items():
        row_sum = count_y(tag1, tag_seq_ls_with_start_stop)

        # words in training set
        for tag2, cell in transition_matrix_row.items():
            transition_matrix[tag1][tag2] = cell / row_sum

    return transition_matrix


def get_transition_matrix_triplets(tags_unique_with_start_stop,
                                   transition_triplets,
                                   tag_seq_ls_with_start_stop):

    # create and initialise transition matrix
    transition_matrix = {}
    for tag1 in tags_unique_with_start_stop[:-1]:
        transition_matrix_table = {}
        for tag2 in tags_unique_with_start_stop[1:-1]:
            transition_matrix_row = {}
            for tag3 in tags_unique_with_start_stop[1:]:
                transition_matrix_row[tag3] = 0.0
            transition_matrix_table[tag2] = transition_matrix_row
        transition_matrix[tag1] = transition_matrix_table

    # population transition matrix with counts
    for tag1, tag2, tag3 in transition_triplets:
        transition_matrix[tag1][tag2][tag3] += 1

    # divide cells by sum, to get probability
    for tag1, transition_matrix_table in transition_matrix.items():
        for tag2, transition_matrix_row in transition_matrix_table.items():
            row_sum = count_y(tag1, tag_seq_ls_with_start_stop)

            # words in training set
            for tag3, cell in transition_matrix_row.items():
                transition_matrix[tag1][tag2][tag3] = cell / row_sum

    return transition_matrix


def get_best_tag(word, emission_matrix):
    y = ""
    score_max = -1

    for tag, emission_matrix_row in emission_matrix.items():
        score_current = emission_matrix_row[word]

        if score_current > score_max:
            score_max = score_current
            y = tag

    return y


def get_prediction(test_word_seq_ls, emission_matrix):
    output = ""
    for test_word_seq in test_word_seq_ls:
        for word in test_word_seq:
            best_tag = ""
            if word in unseen_words:
                best_tag = get_best_tag("#UNK#", emission_matrix)
            else:
                best_tag = get_best_tag(word, emission_matrix)

            output += f"{word} {best_tag}"
            output += "\n"
        output += "\n"

    return output


def get_prediction_viterbi(test_word_seq_ls, emission_matrix,
                           transition_matrix_pairs, transition_matrix_triplets,
                           tags_unique_with_start_stop):
    output = ""
    for test_word_seq in tqdm(test_word_seq_ls):
        viterbi = Viterbi(test_word_seq, emission_matrix,
                          transition_matrix_pairs, transition_matrix_triplets,
                          tags_unique_with_start_stop)

        viterbi.initialise()
        viterbi.step_two()
        viterbi.final_step()
        best_y = viterbi.recover_y_seq()

        for word, y in zip(test_word_seq, best_y):
            output += f"{word} {y}"
            output += "\n"

        output += "\n"

    return output


def save_prediction(exp, language, prediction):
    with open(f"{language}/test.{exp}.out", "w") as f:
        f.write(prediction)


class Viterbi:
    def __init__(self, test_word_seq, emission_matrix, transition_matrix_pairs,
                 transition_matrix_triplets,
                 tags_unique_with_start_stop) -> None:
        self.pi = {}
        self.n = len(test_word_seq)  # number of words in word_seq
        self.test_word_seq = test_word_seq  # x
        self.emission_matrix = emission_matrix
        self.transition_matrix_pairs = transition_matrix_pairs
        self.transition_matrix_triplets = transition_matrix_triplets
        self.tags_unique_with_start_stop = tags_unique_with_start_stop

    def initialise(self):
        self.test_word_seq = ["START"] + self.test_word_seq + ["STOP"]

        for j in range(self.n + 2):
            pi_row = {}
            for tag in self.tags_unique_with_start_stop:
                pi_row[tag] = -1.0

            self.pi[j] = pi_row

        # initialise pi(0, u) 1 for START, 0 otherwise
        for u in self.tags_unique_with_start_stop:
            if u == "START":
                self.pi[0][u] = 1
            else:
                self.pi[0][u] = 0

    def step_two(self):
        for j in range(0, self.n):
            for u in self.tags_unique_with_start_stop:
                score_max = -1

                for v in self.tags_unique_with_start_stop:

                    for w in self.tags_unique_with_start_stop:

                        test_word = self.test_word_seq[j + 1]

                        if test_word not in self.emission_matrix["START"].keys(
                        ):
                            test_word = "#UNK#"

                        if j == 0 and v == "START":

                            try:
                                score = self.pi[j][v] * self.emission_matrix[u][
                                    test_word] * self.transition_matrix_pairs[
                                        v][u]
                            except KeyError:
                                score = 0
                        else:
                            try:
                                score = self.pi[j][v] * self.emission_matrix[u][
                                    test_word] * self.transition_matrix_triplets[
                                        w][v][u]
                            except KeyError:
                                score = 0

                        if score > score_max:
                            score_max = score

                self.pi[j + 1][u] = score_max

    def final_step(self):
        score_max = -1

        for v in self.tags_unique_with_start_stop[1:-1]:
            for w in self.tags_unique_with_start_stop[:-1]:
                score = self.pi[
                    self.n][v] * self.transition_matrix_triplets[w][v]["STOP"]

                if score > score_max:
                    score_max = score

        self.pi[self.n + 1]["STOP"] = score_max

    def recover_y_seq(self):

        y_seq = []

        y_n_star = ""

        y_n_score_max = -1
        for u in self.tags_unique_with_start_stop[1:-1]:
            for w in self.tags_unique_with_start_stop[1:-1]:
                score = self.pi[
                    self.n][u] * self.transition_matrix_triplets[w][u]["STOP"]
                if score > y_n_score_max:
                    y_n_score_max = score
                    y_n_star = u

        y_seq.insert(0, y_n_star)

        for j in range(self.n - 1, 0, -1):
            y_j_star = ""
            y_j_score_max = -1
            for u in self.tags_unique_with_start_stop[1:-1]:
                for w in self.tags_unique_with_start_stop[1:-1]:
                    score = self.pi[j][u] * self.transition_matrix_triplets[w][
                        u][y_seq[0]]
                    if score > y_j_score_max:
                        y_j_score_max = score
                        y_j_star = u

            y_seq.insert(0, y_j_star)

        return y_seq


"""
# part 1, without UNK
emission_matrix = {}
for tag in tags_unique:
    emission_matrix_row = {}
    for word in words_unique:
        emission_matrix_row[word] = 0.0
    emission_matrix[tag] = emission_matrix_row

for tags, words in zip(tag_seq_ls, word_seq_ls):
    for tag, word in zip(tags, words):
        emission_matrix[tag][word] += 1

for tag, emission_matrix_row in emission_matrix.items():
    row_sum = sum(emission_matrix_row.values())
    count_y(tag, tag_seq_ls)
    for word, cell in emission_matrix_row.items():
        emission_matrix[tag][word] = cell / row_sum
"""

for language in languages:

    tag_seq_ls, tag_seq_ls_with_start_stop, word_seq_ls, test_word_seq_ls = load_dataset(
        language)

    tags_unique_with_start_stop, tags_unique_with_start_stop = get_unique_tags(
        tag_seq_ls)
    words_unique = get_unique_words(word_seq_ls)

    emission_pairs = generate_emission_pairs(tag_seq_ls, word_seq_ls)

    emission_pairs_possible = generate_possible_emission_pairs(
        tags_unique_with_start_stop, words_unique)

    transition_pairs = get_transition_pairs(tag_seq_ls_with_start_stop)

    transition_pairs_possible = generate_possible_transition_pairs(
        tags_unique_with_start_stop)

    transition_triplets = get_transition_triplets(tag_seq_ls_with_start_stop)

    transition_triplets_possible = generate_possible_transition_triplets(
        tags_unique_with_start_stop)

    k = .5
    emission_matrix = get_emission_matrix(tags_unique_with_start_stop,
                                          words_unique, tag_seq_ls,
                                          word_seq_ls, k)

    transition_matrix_pairs = get_transition_matrix_pairs(
        tags_unique_with_start_stop, transition_pairs,
        tag_seq_ls_with_start_stop)

    transition_matrix_triplets = get_transition_matrix_triplets(
        tags_unique_with_start_stop, transition_triplets,
        tag_seq_ls_with_start_stop)

    test_word_unique = get_unique_elements(test_word_seq_ls)

    unseen_words = set(test_word_unique).difference(set(words_unique))

    # prediction = get_prediction(test_word_seq_ls, emission_matrix)
    prediction = get_prediction_viterbi(test_word_seq_ls, emission_matrix,
                                        transition_matrix_pairs,
                                        transition_matrix_triplets,
                                        tags_unique_with_start_stop)

    save_prediction("p5", language, prediction)

    print()