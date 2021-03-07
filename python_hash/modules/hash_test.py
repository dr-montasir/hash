#!/usr/bin/env python3
import sys
import time
import hashlib

def hash_function():
    counter = 1

    if len(sys.argv) != 3:
        print("hash_function() takes 3 arguments")
        print("Arguments: (main.py file_names_path files_directory)")
        print("Example for Linux: python3 main.py ~/Desktop/hash/python_hash/examples/filenames.txt ~/Desktop/hash/python_hash/examples/files")
        print("Example for Windows: python main.py C:/Users/username/Desktop/hash/python_hash/examples/filenames.txt C:/Users/username/Desktop/hash/python_hash/examples/files")
        sys.exit()
    else:
        file_names_path = sys.argv[1]
        files_directory = sys.argv[2]
        if files_directory[-1] != '/':
            files_directory += '/'

        try:
            file_names = open(file_names_path, 'r')
            with file_names as file:
                for list_item in file:
                    start = time.time()
                    counter += 1
                    end = time.time()
                    test_time = end - start

                    if len(list_item.split()) == 3:
                        file_name = list_item.strip().split()[0]
                        hash_algorithm = list_item.strip().split()[1]
                        hashing_value = list_item.strip().split()[2]

                        KILOBYTE = 1024 # Kilobyte = 1024 bytes
                        file_size = 128 # file_size is a number (file_size >= 0). 128 -> 128 kb 
                        buf_size = file_size * KILOBYTE
                        md5 = hashlib.md5()
                        sha1 = hashlib.sha1()
                        sha256 = hashlib.sha256()
                        hash_sum = ""

                        try:
                            with open(files_directory + file_name, 'rb') as file:
                                while True:
                                    file_data = file.read(buf_size)
                                    if not file_data:
                                        break
                                    md5.update(file_data)
                                    sha1.update(file_data)
                                    sha256.update(file_data)

                            if hash_algorithm == 'md5':
                                hash_sum = md5.hexdigest()
                            elif hash_algorithm == 'sha1':
                                hash_sum = sha1.hexdigest()
                            elif hash_algorithm == 'sha256':
                                hash_sum = sha256.hexdigest()
                            else:
                                print(file_name, "INCORRECT HASHING ALGORITHM")

                            if hashing_value == hash_sum:
                                print(file_name, "OK")
                            else:
                                print(file_name, "FAIL")

                        except FileNotFoundError as err:
                            print(file_name, "NOT FOUND")
                    else:
                        print(file_name, "INCORRECT INPUT FORMAT")
                print("\nTotal Testing Time: ", test_time, "seconds")
        except FileNotFoundError as err:
            print(err)
            sys.exit()

# hash_function()