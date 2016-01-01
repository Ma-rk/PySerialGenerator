import sys
import hashlib


def main():
    f_output = open("output_codes.txt", 'r')

    print('Begin verifying...')

    while True:
        line = f_output.readline()
        line = (line[:-1])

        hash_value = hashlib.sha224(sys.argv[1]).hexdigest()

        if not line:
            print('The key ' + sys.argv[1] + ' is not valid.')
            break

        if line == hash_value:
            print('The key ' + sys.argv[1] + ' is valid.')
            break

    print('')

if __name__ == '__main__':
    main()
