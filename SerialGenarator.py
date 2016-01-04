import sys
import time
import string
import random
import hashlib
import os


NOW = time.localtime()
MAX_SERIAL_IN_FILE = 10


def gen_time_stamp():
    time_stamp = \
        u"{0:04d}/{1:02d}/{2:02d} {3:02d}:{4:02d}:{5:03d}".format(NOW.tm_year, NOW.tm_mon, NOW.tm_mday, NOW.tm_hour,
                                                                  NOW.tm_min, NOW.tm_sec)
    return time_stamp


def gen_rand_str():
    rand_str = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(21)])
    return rand_str


def gen_serial(time_stamp, rand_str):
    serial_str = rand_str[:3]
    serial_str += time_stamp[19:20]
    serial_str += rand_str[3:5]
    serial_str += time_stamp[18:19]
    serial_str += rand_str[5:7]
    serial_str += time_stamp[17:18]
    serial_str += rand_str[7:9]
    serial_str += time_stamp[15:16]
    serial_str += rand_str[9:11]
    serial_str += time_stamp[14:15]
    serial_str += rand_str[11:13]
    serial_str += time_stamp[9:10]
    serial_str += rand_str[13:15]
    serial_str += time_stamp[8:9]
    serial_str += rand_str[15:17]
    serial_str += time_stamp[6:7]
    serial_str += rand_str[17:19]
    serial_str += time_stamp[5:6]
    serial_str += rand_str[19:21]
    return serial_str


def create_output_file_name():
    file_name_list = os.listdir('.')

    last_serial_file = 'serial_codes_001.txt'
    last_output_file = 'output_codes_001.txt'

    for file_name in file_name_list:
        if file_name[:13] == 'serial_codes_' and last_serial_file < file_name:
            last_serial_file = file_name
            last_output_file = last_output_file[:13] + file_name[13:20]

    return last_serial_file, last_output_file


def get_some_numbers(last_serial_file):
    temp_open = open(last_serial_file, 'r')
    num_of_lines_of_last_file = len(temp_open.readlines())
    temp_open.close()
    num_of_serial_to_generate = int(sys.argv[1])
    return num_of_lines_of_last_file, num_of_serial_to_generate


########################################################################################################################
########################################################################################################################


def main():

    if len(sys.argv) is not 2:
        print("usage: GenerateSerial.py (number of serial)")
        sys.exit()

    last_serial_file, last_output_file = create_output_file_name()
    print('======file names=======')
    print(last_serial_file)
    print(last_output_file)

    num_of_lines_of_last_file, num_of_serial_to_generate = get_some_numbers(last_serial_file)
    total_write_line = 0

    f_serial = open(last_serial_file, 'a')
    f_output = open(last_output_file, 'a')

    print('generating ' + str(num_of_serial_to_generate) + ' serials and outputs')

    while total_write_line < num_of_serial_to_generate:

        if num_of_lines_of_last_file is MAX_SERIAL_IN_FILE:
            print('=======create next file=========')
            num_of_lines_of_last_file = 0
            f_serial.close()
            f_output.close()

            new_file_number = str(int(last_serial_file[13:16]) + 1).zfill(3)

            last_serial_file = last_serial_file[:13] + new_file_number + '.txt'
            last_output_file = last_output_file[:13] + new_file_number + '.txt'

            f_serial = open(last_serial_file, 'a')
            f_output = open(last_output_file, 'a')

        time_stamp = gen_time_stamp()
        rand_str = gen_rand_str()
        serial_str = gen_serial(time_stamp, rand_str)

        f_serial.write(time_stamp + '\t' + serial_str + '\n')
        f_output.write(time_stamp + '\t' + hashlib.sha224(serial_str.encode('utf-8')).hexdigest() + '\n')

        num_of_lines_of_last_file += 1
        total_write_line += 1

    f_serial.close()
    f_output.close()

    print('done.')

if __name__ == '__main__':
    main()
