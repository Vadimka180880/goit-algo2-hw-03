import csv
import timeit
from BTrees.OOBTree import OOBTree

def add_item_to_tree(tree, item):
    tree[item["ID"]] = item

def add_item_to_dict(dictionary, item):
    dictionary[item["ID"]] = item

def range_query_tree(tree, min_price, max_price):
    return [item for _, item in tree.items() if min_price <= float(item["Price"]) <= max_price]

def range_query_dict(dictionary, min_price, max_price):
    return [item for item in dictionary.values() if min_price <= float(item["Price"]) <= max_price]

def load_data(filename):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def main():
    data = load_data("generated_items_data.csv")

    tree = OOBTree()
    dictionary = {}

    for item in data:
        add_item_to_tree(tree, item)
        add_item_to_dict(dictionary, item)

    min_price = 20
    max_price = 100

    tree_time = timeit.timeit(
        stmt=lambda: range_query_tree(tree, min_price, max_price),
        number=100
    )

    dict_time = timeit.timeit(
        stmt=lambda: range_query_dict(dictionary, min_price, max_price),
        number=100
    )

    print(f"\nTotal range_query time for OOBTree: {tree_time:.6f} seconds")
    print(f"Total range_query time for Dict: {dict_time:.6f} seconds")


if __name__ == "__main__":
    main()
