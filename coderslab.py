words = ["hello", "darkness", "my", "old", "friend"]


def coderslab_welcome():
    return "Welcome to CodersLab!"


def random_word():
    from random import randint
    return words[randint(0, len(words) - 1)]

# def r():
#     from random import sample
#     return sample(words, 1)

