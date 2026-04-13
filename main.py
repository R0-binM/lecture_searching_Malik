from searching import read_data


def main():

    sequential_data = read_data("sequential.json", "unordered_numbers")
    print (sequential_data)



if __name__ == "__main__":
    main()
