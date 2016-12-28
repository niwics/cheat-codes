#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
How to use:
1. Open python shell in the directory where this file resides
2. import(pycheat)
3. pycheat.test_function()
"""

# Enum class
# usage: print Materials.Matte
class Materials:
    Shaded, Shiny, Transparent, Matte = range(4)

class MyClass:

    def __init__(self, attr):
        self.my_attr = attr

    def date_magic(self):
        import datetime

        one_day_maybe =  datetime.datetime.strptime("2016-06-13", "%Y-%m-%d")
        today = datetime.datetime.now()

def datatypes():
    import numbers
    # is the variable a number?
    my_variable = 3.14
    isinstance(my_variable, numbers.Number)


def printing():
    value1 = "val1"
    value2 = "val2"
    # python3 style
    print("This is {0} and {1}".format(value1, value2))

    # printint to stderr
    # python 2
    import sys
    print >> sys.stderr, "This is the testing error, don't panic!"
    # for python 3:
    #from __future__ import print_funtion
    #print("This is the testing error, don't panic!, file=sys.stderr)

    # print with leading zeros
    for i in range(5):
        print "%02d" % i

    # print dict (named args)
    print "User %(username)s is from %(city)s. I love %(city)s city!" % {'username': "niwics", 'city': "Brno"}

def regexps():
    # Regexps
    # https://docs.python.org/2/library/re.html

    # important thig when working with regexp patterns: do not forget to use
    # raw strings = r"xyz"
    import re

    # basic searching
    match = re.search(r"ne+dle", "searching neeedle in the haystack!")
    print match.group(0)    # neeedle

    # precompiling + group matching
    regexp = re.compile(r"(\d+):\d+")
    match = regexp.search("arrival in 12:00")
    print "arrival hour: %s" % match.group(1)

    # simple replacing
    print re.sub(r"@", r"(at)", "me@email.com")   # me(at)email.com

def dates():
    # print month with leading zeros
    import datetime
    today_dt = datetime.datetime.now() # type datetime
    today_date = date.today()   # type date
    today_date2 = today_dt.date()
    print "This is month: %s" % today_dt.strftime("%-m")   # alternative in print: "%02d"


def generate_date_ranges(start_date_str, end_date_str):
    """
    In:
    Inspired by: http://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
    """
    import datetime
    from dateutil.rrule import rrule, DAILY

    # working with datetime
    #https://docs.python.org/2/library/datetime.html


    start = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
    end = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")

    for dt in rrule(DAILY, dtstart=start, until=end):
        print dt.strftime("%Y-%m-%d")

def multiprocessing_worker(worker_id, sleep_seconds):
    """
    Worker function for multiprocesing
    """
    print "Worker #%s started" % worker_id
    import time
    time.sleep(sleep_seconds)
    msg = "Worker #%s finished" % worker_id
    print msg
    return msg

def multiprocessing_pool_of_workers():
    """
    Multiprocessing Pool.
    """
    from multiprocessing import Pool
    num_workers = 4
    pool = Pool(num_workers)
    workers_params = [[worker_id, num_workers-worker_id] for worker_id in range(num_workers)]
    results = pool.map(multiprocessing_worker, workers_params)
    print results

def multiprocessing_process():
    """
    Multiprocessing Pool: https://pymotw.com/2/multiprocessing/basics.html
    """
    from multiprocessing import Process
    num_workers = 4
    jobs = []
    for worker_id in range(num_workers):
        p = Process(target=multiprocessing_worker, args=(worker_id, num_workers))
        jobs.append(p)
        p.start()

def random():
    import random
    random.random()        # Random float x, 0.0 <= x < 1.0
    random.uniform(1, 10)  # Random float x, 1.0 <= x < 10.0
    random.randint(1, 10)  # Integer from 1 to 10, endpoints included
    random.randrange(0, 101, 2)  # Even integer from 0 to 100
    random.choice('abcdefghij')  # Choose a random element
    random.choice(['one', 'two', 'three'])  # Choose a random element
    random.choice(string.ascii_lowercase)   # random ASCII lowercase character
    random.shuffle([1, 2, 3, 4])    # shuffle the array
    random.shuffle([1, 2, 3, 4], 2)    # pick two random numbers


def rpc():

    # XML-RPC = python module for XML-RPC
    import xmlrpclib
    # Connects. Ignores path after port: http://myserver.dev:1234/IGNORED
    server = xmlrpclib.ServerProxy("http://myserver.dev:1234", allow_none=True)
    # direct method call
    print server.help()
    # method name from the variable
    method_handler = getattr(server, "myMethod")
    params = {
        "flag": True,
        "mystring": "test",
        "date": xmlrpclib.DateTime("2015-04-20")
    }
    res = method_handler(params)
    if res["status"] / 100 != 2:
        raise Exception("Invalid RPC call: %s", res)

    # FRPC - Seznam.cz module (http://opensource.seznam.cz/frpc/)
    # supports numbers > int32
    import fastrpc
    # Connects. Alternative params: readTimeout (ms), writeTimeout,
    #  connectTimeout, useBinary=fastrpc.ON_SUPPORT_ON_KEEP_ALIVE
    server = fastrpc.ServerProxy("http://myserver.dev:1234/notignored-path")
    # the rest is similar to XML-RPC
    try:
        res = server.myMethod(params)
        print "status: %s" % res["status"]
        print res
    except fastrpc.Fault, e:
        print e
    except fastrpc.ProtocolError, e:
        print e
    except fastrpc.StreamError, e:
        print e


def main():
    print "Main function called"

    # argparse example
    import argparse
    parser = argparse.ArgumentParser()
    # group of exclusive options
    sp = parser.add_subparsers(dest='subparser_value')
    sp.add_parser('start', help='Starts %(prog)s daemon')
    sp.add_parser('stop', help='Stops %(prog)s daemon')
    sp.add_parser('restart', help='Restarts %(prog)s daemon')
    # required
    parser.add_argument('--host', help='Hostname help text', required=True)
    # default
    parser.add_argument('--port', help='some help text', default=8080)
    # options (possibilities)
    parser.add_argument('--protocol', help='some help text', choices=['http', 'https'])
    # type setting
    parser.add_argument('--workers', help='Number of parallel workers', type=int, default=1)
    # bool value (store_true sets True when flag is present and it omits the value;
    #  similar is store_false and store_const)
    parser.add_argument('--dry-run', help='This is bool flag', action='store_true')
    # parse arguments (in case of invalid input, it prints the help and exits)
    args = parser.parse_args()  # accessing: args.myparam
    # you cannot use reserved keywords like "from" (ex. args.from) - in that case you need a dict:
    # source: https://parezcoydigo.wordpress.com/2012/08/04/from-argparse-to-dictionary-in-python-2-7/
    opts = vars(args)           # accessing: opts['myparam']
    print "Current mode: %s" % opts['subparser_value']
    if opts['subparser_value'] == 'start':
        print "Yes, we launched!"

    # return codes
    import sys
    import os
    # useful return codes: (more on https://docs.python.org/2/library/os.html)
    # EX_OK
    # EX_USAGE - bad program usage
    # EX_DATAERR - incorrect input data
    # EX_UNAVAILABLE - required service is unavailable
    # EX_SOFTWARE - software runtime error
    # EX_CONFIG - configuration error
    # EX_NOTFOUND
    sys.exit(os.EX_OK)


if __name__ == "__main__":
    main()