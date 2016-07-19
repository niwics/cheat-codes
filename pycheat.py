#!/usr/bin/python

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


def generate_date_ranges(start_date_str, end_date_str):
    """
    In:
    Inspired by: http://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
    """
    import datetime
    from dateutil.rrule import rrule, DAILY

    # working with datet
    #https://docs.python.org/2/library/datetime.html




    start = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
    end = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")

    for dt in rrule(DAILY, dtstart=start, until=end):
        print dt.strftime("%Y-%m-%d")

def random():
    import random
    random.random()        # Random float x, 0.0 <= x < 1.0
    random.uniform(1, 10)  # Random float x, 1.0 <= x < 10.0
    random.randint(1, 10)  # Integer from 1 to 10, endpoints included
    random.randrange(0, 101, 2)  # Even integer from 0 to 100
    random.choice('abcdefghij')  # Choose a random element
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
    parser.add_argument('--host', help='Hostname help text', required=True)
    parser.add_argument('--port', help='some help text', default=8080)
    parser.add_argument('--workers', help='Number of parallel workers', type=int, default=1)
    args = parser.parse_args()
    # in case of invalid input, it prints the help and exits
    if len(USER_IDS) == len(args.entities):
        print "WARNING: Number of users should not be the multiple of number of entities (because of caching)!"

    import sys
    import os
    sys.exit(os.EX_CONFIG)
    sys.exit(os.EX_OK)


if __name__ == "__main__":
    main()
