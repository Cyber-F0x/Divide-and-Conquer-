import os
import argparse

# Cyber-F0x

def divide_and_conqure(size,data_list, iteration):
    print("Interation: {}".format(iteration))
    print("Halfing file down from {} bytes to {} bytes".format(size, size//2))
    os.chdir(make_dir("Iteration_{}".format(iteration)))
    middle_index = len(data_list)//2
    h1 = data_list[middle_index:]
    h2 = data_list[:middle_index]
    chunck_file( size, h1, iteration,1)
    chunck_file( size, h2, iteration,2)
    print("Scan files now")
    ans = get_answer()
    if ans == 1:
        data_list = h1
    else:
        data_list = h2

    # Doing this to clear up variable space on the system
    del h1
    del h2
    iteration += 1
    size = size/2
    os.chdir("..")
    divide_and_conqure(size,data_list, iteration)


def get_answer():
    while 1:
        choice = int(input("Which chunck was the scan in chunck 1 or 2. Enter 3 to kill excution"))
        if choice == 3:
            print("Exiting")
            exit()
        elif choice == 1 or choice == 2:
            return choice
        else:
            print("Error invalid choice")


def main(target):
    size = os.path.getsize(target)
    print("Size: {}".format(size))
    data_list = []
    with open(target, 'rb') as chuck:
        read_byte = chuck.read(1)
        data_list.append(read_byte)
        while read_byte != b"":
            read_byte =  chuck.read(1)
            data_list.append(read_byte)
    os.chdir(make_dir("output"))
    divide_and_conqure(size,data_list,0)


def chunck_file(size, data, interation,part):
    f_size = int(round(size))
    filename = "chunk_{}_{}_part_{}.bin".format(interation, f_size,part)
    with open(filename, "wb") as file:
        for each_byte in data:
            file.write(each_byte)


def make_dir(name):
    try:
        path = os.path.join(os.getcwd(),  name)
        if not os.path.exists(path):
            os.mkdir(path)
        return path
    except Exception as e:
        print(e)
        exit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", required=True)
    args = parser.parse_args()
    main(args.target)