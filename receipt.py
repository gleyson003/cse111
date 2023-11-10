import csv

def main():

    product_dict = read_dictionary("products.csv", 0)
    print('All Products')
    print(product_dict)

    print('\nRequested Items')
    with open("request.csv", "rt") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            PRODUCT_CODE = row[0]
            PRODUCT_DATA = product_dict[PRODUCT_CODE]

            PRODUCT_NAME = PRODUCT_DATA[1]
            PRODUCT_QUANTITY = 1
            PRODUCT_PRICE = PRODUCT_DATA[2]

            print(f'{PRODUCT_NAME}: {row[PRODUCT_QUANTITY]} @ {PRODUCT_PRICE}')

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    dictionary = {}

    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for product_list in reader:
            if product_list != 0:
                key = product_list[key_column_index]
                dictionary[key] = product_list

    return dictionary

if __name__ == "__main__":
    main()
