print("\na)")


def write_to_file(data):
    f = open('myfile.txt', 'w')
    f.write(data)
    f.close()
    print(data, "was written to file.")

write_to_file('Lorem impsum, dette er en fil.')
write_to_file('I denne teksten skal jeg skrive om noe kult.')


print("\nb)")


def read_from_file(filename):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    print(data)


read_from_file('myfile.txt')


print("\nc)")


def main():
    choice = (input("Do you want to read or write?")).strip().lower()
    if choice == "done":
        print("You are done.")
        return
    else:
        if choice == "write" or choice == "w":
            data = input("What do you want to write to file?")
            write_to_file(data)
            main()
        elif choice == "read" or choice == "r":
            read_from_file('myfile.txt')
            main()
        else:
            print("Did not recognize the answer, try again.")
            main()


main()
