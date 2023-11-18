import csv
from datetime import datetime

def main():

    current_date_and_time = datetime.now()
    product_dict = read_dictionary("products.csv", 0)

    print('\nInkom Emporium\n')

    try:
        with open("request.csv", "rt") as file:
            reader = csv.reader(file)
            next(reader)

            number_of_items = 0
            subtotal = 0
            tax = 0.06

            for row in reader:
                PRODUCT_CODE = row[0]

                try:
                    PRODUCT_DATA = product_dict[PRODUCT_CODE]
                    PRODUCT_NAME = PRODUCT_DATA[1]
                    PRODUCT_QUANTITY = 1
                    PRODUCT_PRICE = PRODUCT_DATA[2]

                    number_of_items += int(row[PRODUCT_QUANTITY])
                    subtotal += float(PRODUCT_PRICE) * int(row[PRODUCT_QUANTITY])

                    print(f'{PRODUCT_NAME}: {row[PRODUCT_QUANTITY]} @ {PRODUCT_PRICE}')

                except KeyError as err_key:
                    error_message = f"Error: unknown product ID in the request.csv file\n{err_key}"
                    print(error_message)

            sales_tax = subtotal * tax
            discount_amount = 0

            if current_date_and_time.weekday() in [1, 2]:
                discount = 0.10
                discount_amount = subtotal * discount
                total = subtotal + sales_tax - discount_amount
                print(f'\nDiscount applied (10%) for Tuesday or Wednesday')
            else:
                total = subtotal + sales_tax

            print(
                f'\nNumber of items: {number_of_items}\n'
                f'Subtotal: {subtotal:.2f}\n'
                f'Sales Tax: {sales_tax:.2f}\n'
                f'Discount: {discount_amount:.2f}\n'
                f'Total: {total:.2f}\n'
            )

            print(
                f"Thank you for shopping at the Inkom Emporium.\n"
                f"{current_date_and_time:%a %b %d %H:%M:%S %Y}"
            )

    except FileNotFoundError as not_found_err:
        print('Error: missing file')
        print(not_found_err)

def read_dictionary(filename, key_column_index):
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
