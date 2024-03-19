def main():
    import random
    import json

    print("\nHello Ableset Users, Welcome to AbleSort ver 1.2")
    print("Program will read in a '.json' file and create a new '.json' file sorted by song name")
    print("You can then read-in the new '.json' file into "
          "Ableset to see your sorted songs")
    print("Developed by Gary W. Steele 'aka Hoosier Farm Boy'\n")

    # Get valid command from user
    command = get_command()
    print('Command Entered = ', command)

    # Read and verify read file name and write file name
    json_readfile = get_read_file()
    print('Read File Name = ', json_readfile)
    if not file_exists(json_readfile):
        exit()
    else:
        # Continue to get output file name is input file exists, otherwise exit program
        json_write_file = get_write_file()
        print('json write file = ', json_write_file)

    with open(json_readfile, 'r') as f:
        data = json.load(f)
    print(data)

    # Process Command 1, Random List
    if command == "1":
        random_list = random.sample(data, len(data))
        print('\nSong List in Random Order')
        print_song_list(random_list)

        # Save random order list fo file
        with open(json_write_file, 'w') as f:
            json.dump(random_list, f, indent=2)

    # Process Command 2, Alphabetical Sort List
    elif command == "2":
        # Create List of original songs in alphabetical order
        print("\nSong List in alphabetical Order")
        # sorted_data = sorted(data, key=lambda i: i['lastKnownName'])
        sorted_data = sorted(data, key=lambda i: i['lastKnownName'])
        print_song_list(sorted_data)
        # Save alphabetical order list fo file
        with open(json_write_file, 'w') as f:
            json.dump(sorted_data, f, indent=2)

    # Create List of original songs in time sequence order
    elif command == "3":
        print("\nSong List in Time Sequential Order")
        sorted_data = sorted(data, key=lambda i: i['time'])
        print_song_list(sorted_data)
        # Save by time order to  file
        with open(json_write_file, 'w') as f:

            json.dump(sorted_data, f, indent=2)


def get_command():
    print("Available commands:")
    print("Enter 1 for Random Song Sort")
    print("Enter 2 for Alphabetical Sort")
    print("Enter 3 for Sequential Time Sort")
    print("Enter X to Exit Program")
    print("")
    print("Original .json file will NOT be changed.")
    print("")

    # Wait for correct command entry
    while True:
        command = input("Enter your command: ")
        # print(f"My command is: {command}")
        if command in ['1', '2', '3']:
            return command
        elif command[0].lower() == 'x':
            exit()


def get_read_file():
    # Get and verify .json file to open
    print("\nHit 'Enter' to read default file 'Sample Songs.json")
    print("Otherwise enter your .json filename without extension\n")
    file_name = input("Enter .json file name to sort: ")
    if len(file_name) < 1:
        file_name = 'Sample Songs'
    file_name += ".json"
    # print("input file name = " + file_name)
    return file_name


def file_exists(file_name):
    import os
    print("entering File_Exists function")
    # Verify that the input file exists and open
    if os.path.isfile(file_name):
        print("File Exists")
        return True
    else:
        print("File really Does Not Exist")
        return False


def get_write_file():
    # Get and verify .json file to write as output
    print("\nHit 'Enter' to write default output file 'Sorted Songs.json")
    print("Otherwise enter your .json filename without extension\n")
    file_name = input("Enter .json file name to create as output: ")
    # print(file_name)
    if len(file_name) < 1:
        print(file_name)
        file_name = 'Sorted Songs.json'
    else:
        file_name += ".json"
        print(file_name)
        # Check to see if the output file already exists
        if file_exists(file_name):
            overwrite = input("Output file already exists. Overwrite ? Y/N: ")
            if overwrite[0].lower() != "y":
                print("Exiting program")
                exit()
            else:
                print("OK to overwrite file")

    # print("output file name = ", file_name)
    return file_name


def print_song_list(file_name):
    for index, value in enumerate(file_name):
        print(f"New Order:  {index:3d}"
              f"\t Time:  {value["time"]:12}"
              f" \tSong Name:  {value['lastKnownName']}")


main()
