def hashing_func(key, n):
    #value = sum([ord(ch) for ch in key])
    #numeric = ord(key[0])
    return hash(key) % n


def insert(table, value):
    hash_key = hashing_func(value, len(table))
    if table[hash_key] is None:
        table[hash_key] = []
    table[hash_key].append(value)


def is_in_table(value, table):
    hash_value = hashing_func(value, len(table))
    if table[hash_value] is None:
        return False
    if value in table[hash_value]:
        return True
    return False


def main():

    country = ["Russia", "Germany", "United Kingdom", "France", "Italy", "Spain", "Ukraine", "Poland", "Romania", "Netherlands", "Belgium", "Czech Republic (Czechia)", "Greece", "Portugal", "Sweden", "Hungary", "Belarus", "Austria", "Serbia", "Switzerland", "Bulgaria", "Denmark	", "Finland	", "Slovakia", "Norway", "Ireland", "Croatia", "Moldova", "Bosnia and Herzegovina", "Albania", "Lithuania", "North Macedonia", "Slovenia", "Latvia", "Estonia", "Montenegro	", "Luxembourg", "Malta	", "Iceland	", "Andorra", "Monaco", "Liechtenstein", "San Marino", "Holy See"]

    table = [None] * 10
    for c in country:
        insert(table, c.strip())
        print(hash(c.strip()))

    print(is_in_table("Sweden", table))
    print(is_in_table("Finland", table))
    print(is_in_table("USA", table))

    # O(n)
    #for cc in country_code:
    #    if cc[0] == 10:
    #        print(cc)
    #        break


if __name__ == '__main__':
    main()
