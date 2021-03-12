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

if __name__ == '__main__':

    def printer(size, d):
        """Print function"""
        sort = sorted(d.keys())
        print("File size: {:d}".format(size))
        for i in sort:
            if d[i] != 0:
                print("{}: {}".format(i, d[i]))

    size = 0
    d = {"200": 0, "301": 0, "400": 0, "401": 0,
         "403": 0, "404": 0, "405": 0, "500": 0}

    counter = 0
    try:
        with open(0) as f:
            for line in f:
                counter += 1
                arr = line.split()
                try:
                    size += int(arr[-1])
                except:
                    pass
                try:
                    st = arr[-2]
                    if st in d:
                        d[st] += 1
                except:
                    pass
                if counter % 10 == 0:
                    printer(size, d)
            printer(size, d)
    except KeyboardInterrupt:
        printer(size, d)
        raise