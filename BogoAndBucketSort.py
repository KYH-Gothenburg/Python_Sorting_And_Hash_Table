import random


def is_sorted(data):
    for i in range(len(data)-1):
        if data[i] > data[i+1]:
            return False
    return True


def bogo_sort(data):
    tries =0
    while not is_sorted(data):
        tries += 1
        print(f"Try {tries}")
        random.shuffle(data)


def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        value = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > value:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = value



def bucket_sort(values):
    buckets = []
    number_of_buckets = 10

    # Create 10 empty buckets
    for _ in range(number_of_buckets):
        buckets.append([])

    for value in values:
        index = int(number_of_buckets * value)
        buckets[index].append(value)

    for i in range(number_of_buckets):
        insertion_sort(buckets[i])

    k = 0
    for i in range(number_of_buckets):
        for j in range(len(buckets[i])):
            values[k] = buckets[i][j]
            k += 1



def main():
    data = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    bucket_sort(data)
    #data = [2, 3, 1]
    #bogo_sort(data)
    print(data)
    #O(n!)

    # 6n^4 + 3n^3 + 6
    #O(n^4)


if __name__ == '__main__':
    main()
