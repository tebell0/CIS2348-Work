import csv


def frequency(x):

    word_freq = {}
    with open(x, 'r', newline='') as file1:
        csv_reader = csv.reader(file1)
        for row in csv_reader:
            for word in row:
                word = word.strip()
                if word not in word_freq:
                    word_freq[word] = 1
                elif word in word_freq:
                    word_freq[word] += 1
    for word, freq in word_freq.items():
        print(f'{word} {freq}')


file = frequency(input())
