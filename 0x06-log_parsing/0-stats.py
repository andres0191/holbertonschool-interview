#!/usr/bin/python3
"""script that reads stdin line by
    line and computes metrics:
    Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size> (if the format is not this one, the
    line must be skipped)
    After every 10 lines and/or a keyboard interruption (CTRL + C),
    print these statistics from the beginning:
    Total file size: File size: <total size>
    where <total size> is the sum of all previous <file size>
    (see input format above)
    Number of lines by status code:
    possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
    if a status code doesn’t appear or is not an integer, don’t print anything for this status code
    format: <status code>: <number>
    status codes should be printed in ascending order
"""

import sys

if __name__ == "__main__":

    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}
    file_size = [0]
    count = 1

    def print_stats():
        '''
        Prints file size and stats for every 10 loops
        '''
        print('File size: {}'.format(file_size[0]))

        for code in sorted(status_codes.keys()):
            if status_codes[code] != 0:
                print('{}: {}'.format(code, status_codes[code]))

    def parse_stdin(line):
        '''
        Checks the stdin for matches
        '''
        try:
            line = line[:-1]
            word = line.split(' ')
            # File size is last parameter on stdout
            file_size[0] += int(word[-1])
            # Status code comes before file size
            status_code = int(word[-2])
            # Move through dictionary of status codes
            if status_code in status_codes:
                status_codes[status_code] += 1
        except BaseException:
            pass

    try:
        for line in sys.stdin:
            parse_stdin(line)
            # print the stats after every 10 outputs
            if count % 10 == 0:
                print_stats()
            count += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
