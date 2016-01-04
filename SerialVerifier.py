import sys
import hashlib
import os


def main():
    input_serial = sys.argv[1]
    encoded_input_serial = str(input_serial).encode('utf-8')

    file_name_list = os.listdir('.')

    existing_file_name_list = []

    for file_name in file_name_list:
        if file_name[:13] == 'output_codes_':
            existing_file_name_list.append(file_name)

    for file_name in existing_file_name_list:
        print('Verifying file [' + file_name + ']...')

        f_output = open(file_name, 'r')

        while True:
            line = f_output.readline()
            line = (line[21:-1])

            hash_value = hashlib.sha224(encoded_input_serial).hexdigest()

            if line == hash_value:
                print('The key ' + sys.argv[1] + ' is valid.')
                f_output.close()
                sys.exit()

            if not line:
                if file_name == existing_file_name_list[-1]:
                    print('The key ' + sys.argv[1] + ' is not valid.')
                    f_output.close()
                    sys.exit()
                else:
                    break

        f_output.close()
        print('')

if __name__ == '__main__':
    main()
