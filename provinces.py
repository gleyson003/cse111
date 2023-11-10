
def main():
    provinces = load_provinces('provinces.txt')
    no_first_and_last_item = remove_first_and_last(provinces)
    item_times = times_item_apear(no_first_and_last_item)
    
    print(f'{no_first_and_last_item} \n'
          f' \nAlberta occurs {item_times} times in the modified list.')

def load_provinces(filename):
    provinces_list = []

    with open(filename, "rt") as provinces:

        for province in provinces:
            province = province.strip()
            if province == 'AB':
                province =  'Alberta'
                provinces_list.append(province)
            else:
                provinces_list.append(province)

    return provinces_list

def remove_first_and_last(list):
    last_item = len(list) - 1
    del list[last_item]
    del list[0]
    
    return list

def times_item_apear(list):
    times = 0

    for item in list:
        if item == 'Alberta':
            times += 1
    
    return times

if __name__ == '__main__':
    main()
