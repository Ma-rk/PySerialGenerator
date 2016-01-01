import sys
import time
import string
import random
import hashlib


now = time.localtime()


def gen_time_stamp():
    time_stamp = \
        u"{0:04d}/{1:02d}/{2:02d} {3:02d}:{4:02d}:{5:03d}".format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour,
                                                                  now.tm_min, now.tm_sec)
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


def main():
    if len(sys.argv) is not 2:
        print("usage: GenerateSerial.py (number of serial)")
        sys.exit()

    f_serial = open("serial_codes.txt", 'w')
    f_output = open("output_codes.txt", 'w')

    num_of_serial = int(sys.argv[1])

    print('generating ' + str(num_of_serial) + ' serials and outputs')

    for i in range(0, num_of_serial):
        time_stamp = gen_time_stamp()
        rand_str = gen_rand_str()
        serial_str = gen_serial(time_stamp, rand_str)

        f_serial.write(time_stamp + '\t' + serial_str + '\n')
        f_output.write(hashlib.sha224(serial_str).hexdigest() + '\n')

    f_serial.close()
    f_output.close()

    print('done.')

if __name__ == '__main__':
    main()
