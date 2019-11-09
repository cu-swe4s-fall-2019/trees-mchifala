import time  # noqa: E402
import argparse  # noqa: E402
import sys  # noqa: E402
sys.path.insert(1, "hash-tables-mchifala")  # noqa: E402
from hash_tables import LinearProbe  # noqa: E402
from hash_functions import h_rolling  # noqa: E402
from a import avl  # noqa: E402
from binary_tree import insert  # noqa: E402
from binary_tree import insert_helper  # noqa: E402
from binary_tree import Node  # noqa: E402
from binary_tree import search  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
from tqdm import tqdm  # noqa: E402


def get_data(data_set, num_points):
    """
    This function parses data from a .txt file with two
    columns into key, value tuples.

    Parameters:
    - data_set(str): A .txt file of data
    - num_points(int): The number of data points from the
    data set that we wish to include in analysis

    Returns:
    - key_values(list): A list of key-value tuples

    """
    key_values = []
    file = open(data_set, "r+")
    for i in range(num_points):
        line = next(file).strip().split(" ")
        key_values.append((line[0], line[1]))
    file.close()
    return key_values


def make_plot(t_add, t_search, t_missing, title, outfile):
    """
    This function makes a figure with 3 subplots, each containing
    a line graph for inserting or searching for key-value pairs
    in the relevant data structure.

    Parameters:
    - t_add(list): A list of insertion times
    - t_search(list): A list of search times for key in data structure
    - t_missing(list): A list of search times for keys not
    in data structure
    - title(str): The title of the figure
    - outfile(str): The file name to save the figure

    Returns:
    - None, but a .png file is saved

    """
    fig = plt.figure()
    ax = plt.subplot(3, 1, 1)
    plt.plot(range(len(t_add)), t_add, c='b', label="Insert")
    plt.legend()

    plt.subplot(3, 1, 2, sharey=ax)
    plt.plot(range(len(t_search)), t_search, c='r',
             label="Search existing keys")
    plt.legend()

    plt.subplot(3, 1, 3, sharey=ax)
    plt.plot(range(len(t_missing)), t_missing, c='g',
             label="Search missing keys")
    plt.legend()

    fig.add_subplot(111, frameon=False)
    plt.xlabel("Number of keys, $n$", labelpad=20)
    plt.ylabel("Time to complete, $s$", labelpad=50)
    plt.title(title)
    plt.xticks([]), plt.yticks([])
    plt.tight_layout()
    plt.savefig(outfile)


def main(data_struct, data_set, num_points):
    """
    This function performs our experiment for an AVL tree, BST,
    or hash table depending on user input. A figure of search
    and insertion times is produced.

    Parameters:
    - data_struct(str): The type of data structure
    - data_set(str): The type of data set. Random or sorted
    - num_points(int): The number of data points from the
    data set that we wish to include in analysis

    Returns:
    - None, but a .png file is saved

    """
    key_values = get_data(data_set, num_points)
    n = list(range(num_points))
    t_add = []
    t_search = []
    t_missing = []

    if data_struct == "avl":
        for num in n:
            t0 = time.perf_counter()
            avl_tree = avl.AVL()
            for k, _ in key_values:
                avl_tree.insert(k)
            t1 = time.perf_counter()
            t_add.append(t1-t0)

            t0 = time.perf_counter()
            for k, _ in key_values[0:int(.1*num_points)]:
                avl_tree.find(str(k))
            t1 = time.perf_counter()
            t_search.append(t1-t0)

            t0 = time.perf_counter()
            for k in range(num_points, int(num_points*1.1)):
                avl_tree.find(str(k))
            t1 = time.perf_counter()
            t_missing.append(t1-t0)

        make_plot(t_add, t_search, t_missing,
                  "AVL performance", "avl_test.png")

    elif data_struct == "hash":
        for num in n:
            t0 = time.perf_counter()
            ht = LinearProbe(5*num_points, h_rolling)
            for k, v in key_values:
                ht.add(str(k), v)
            t1 = time.perf_counter()
            t_add.append(t1-t0)

            t0 = time.perf_counter()
            for k, _ in key_values[0:int(.1*num_points)]:
                ht.search(str(k))
            t1 = time.perf_counter()
            t_search.append(t1-t0)

            t0 = time.perf_counter()
            for k in range(num_points, int(num_points*1.1)):
                ht.search(str(k))
            t1 = time.perf_counter()
            t_missing.append(t1-t0)

        make_plot(t_add, t_search, t_missing,
                  "Hashing performance", "hash_test.png")

    elif data_struct == "tree":
        for num in n:
            t0 = time.perf_counter()
            root_key = key_values[0][0]
            root_val = key_values[0][1]
            root = Node(root_key, root_val)
            for k, v in key_values[1:]:
                insert(root, k, v)
            t1 = time.perf_counter()
            t_add.append(t1-t0)

            t0 = time.perf_counter()
            for k, _ in key_values[0:int(.1*num_points)]:
                search(root, k)
            t1 = time.perf_counter()
            t_search.append(t1-t0)

            t0 = time.perf_counter()
            for k in range(num_points, int(num_points*1.1)):
                search(root, str(k))
            t1 = time.perf_counter()
            t_missing.append(t1-t0)

        make_plot(t_add, t_search, t_missing,
                  "BST performance", "bst_test.png")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Key-value input")

    parser.add_argument('data_struct',
                        type=str,
                        help='The type of data structure')

    parser.add_argument('data_set',
                        type=str,
                        help='Type of data set')

    parser.add_argument('num_points',
                        type=int,
                        help='Number of data points')

    args = parser.parse_args()

    main(args.data_struct, args.data_set, args.num_points)
