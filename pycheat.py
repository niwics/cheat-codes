#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
How to use:
1. Open python shell in the directory where this file resides
2. import pycheat
3. pycheat.test_function()
After modification of this file, you should reload the module:
reload(pycheat)

If you want to call this file directly, try to execute from shell: pycheat.py -h
"""

# Enum class
# usage: print Colours.Red
class Colours:
    Red, Green, Blue, White = range(4)

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

    # determine iterables - str, dict, list...
    my_var = [1, 2, 3]
    import collections
    print "Is my_var iterable? - %s" % isinstance(my_var, collections.Iterable)


def lists():
    l = [1, 2, 'three'] # old-style: l = list(1, 2, 'three')
    # filter the list
    int_list = [1, 2, 3, 4]
    print "Even numbers: %s" % filter(lambda i: i % 2 == 0, int_list)
    print "Even numbers: %s" % [i for i in int_list if i % 2 == 0]


def dictionaries():
    # create
    number_one_players = {'man': 'Andy Murray', 'woman': 'Angelique Kerber'}

    # merging dicts
    en = {1: 'one', 2: 'two'}
    cs = {2: 'dve', 3: 'tri'}   # overwrites the key 2
    en.update(cs)   # {1: 'one', 2: 'dve', 3: 'tri'}

    # ordered dicts
    orig = {
        'roger': {'gs_titles': 17},
        'rafa': {'gs_titles': 14},
        'nole': {'gs_titles': 12},
        'andy': {'gs_titles': 3}
        }

    # dictionary sorted by key
    OrderedDict(sorted(d.items(), key=lambda t: t[0]))
    # {andy: ..., nole: ..., rafa: ..., roger: ...}
    OrderedDict(sorted(d.items(), key=lambda t: t['gs_titles']))
    # {roger: ..., rafa: ..., nole: ..., andy: ...}


def classes():
    # abstract methods
    class Base(object):
        def go(self):
            raise NotImplementedError("Method is not implemented.")


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

    # rounding floats
    print "%.1f" % 3.141

    # print with leading zeros
    for i in range(5):
        print "%02d" % i

    # print dict (named args)
    print "User %(username)s is from %(city)s. I love %(city)s city!" % {'username': "niwics", 'city': "Brno"}

    # Pretty-printing
    hierarchical_dict = {'a': 1, 'b': [{'ba': 2, 'bb': 3}]}
    import pprint
    pp = pprint.PrettyPrinter(indent=5)
    pp.pprint(hierarchical_dict)


def logging():
    v1 = "variable for testing"
    v2 = 123
    import logging
    # logger names can be hierarchically set
    log = logging.getLogger("app_name." + __name__)
    log.setLevel("INFO")
    # create console handler
    ch = logging.StreamHandler()
    # create formatter and add it to the handlers
    # display just seconds: add second parameter to Formatter: "%Y-%m-%d %H:%M:%S"
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s {%(name)s: %(lineno)s}')
    ch.setFormatter(formatter)
    # add the handlers to the logger
    log.addHandler(ch)
    log.debug("Debug message with variables %s - %d", v1, v2)
    log.info("Info message with variables %s - %d", v1, v2)
    log.warning("Warning message with variables %s - %d", v1, v2)
    log.error("Error message with variables %s - %d", v1, v2)


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
    import datetime

    today_dt = datetime.datetime.now() # type datetime
    today_date = datetime.date.today()   # type date
    today_date2 = today_dt.date()   # datetime to date
    print "Current ISO date without time: %s" % today_date  # "2016-11-14"
    # print month with leading zeros
    print "This is month: %s" % today_dt.strftime("%-m")   # alternative in print: "%02d"

    # custom formatting
    # https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
    # Fotmats help: http://strftime.org/
    print today_dt.strftime("Today is the %d of %b in %y")  # Today is the 18 of Nov in 2016

    # ISO dates to datetime
    import dateutil.parser
    # more robust version
    dt = dateutil.parser.parse("2016-11-16 09:07:56")
    # load from the specific format
    dt2 = datetime.datetime.strptime("2016-11-16", "%Y-%m-%d" )
    print dt    # datetime.datetime(2016, 11, 16, 9, 7, 56)


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


def rpc_dates():
    # FRPC datetime: http://fastrpc.sourceforge.net/doc/python/classDateTime.html
    # loading datetime using xmlrpclib interface from frpc server returns
    # xmlrpclib.DateTime, which internally holds the value in invalid format
    # and cannot be used normally (ex. timetuple call)
    import xmlrpclib
    import fastrpc  # fastrpc.sourceforge.net
    d_x = xmlrcplib.DateTime("20161115T15:34:53+0100")
    print d_x # <DateTime '20161115T15:34:53+0100' at 7f4ab928d248>
    print type(d_x) # silly one: <type 'instance'>
    print d_x.timetuple() # Traceback: ValueError: unconverted data remains: +0100
    # convert to the proper frpc.DateTime
    d_f = fastrpc.DateTime(str(d_x))
    print d_f   # 20161115T15:34:53+0100
    print type(d_x) # <type 'DateTime'>
    # direct print using fastrpc.Datetime attributes
    print "In %d at %02d:%02d" % (df.year, df.hour, df.min) # In 2016 at 15:34
    # convert to the datetime
    d_dt = datetime.datetime.fromtimestamp(d_f.unixTime)


def paths():
    import os
    relative_path_to_script = \
        os.path.join(os.path.dirname(__file__), '../another-dir/other-file')


def working_with_yaml():
    import yaml
    # load the config file
    try:
        with open('/path/to/yaml-file.yml', 'r') as stream:
            config = yaml.safe_load(stream)
    except IOError as e:
        print >> sys.stderr, "Could not open the file: %s" % e


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


def write_file():
    # create the testing template
    with open('/tmp/pycheat-test-file', 'w') as f:
        f.write("test line no.1\ntest line no.2\nline 3\nanother line!")


def read_file():
    write_file()
    with open('/tmp/pycheat-test-file') as f:
        # read all at once to the list of lines
        lines_list = f.readlines()
        print lines_list
        # seek to the file beginging
        f.seek(0)
        # iterate over lines - do not load the whole file to the memory
        print "Iterate over lines:\n--------------"
        for line in f:
            print line


def file_info():
    import os
    statinfo = os.stat('somefile.txt')
    statinfo.st_size # 926L (size in bytes)


def requests_parsing():
    import requests
    request_url = "http://testing-page.com/slug/?querystring"
    timeout = 2 # seconds
    r = requests.get(request_url, timeout=timeout)
    if r.status_code != 200:
        print "Error in the request: %s" % r


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


def jinja():
    """
    Jinja2 templating engine usage.
    """
    template_path = '/tmp/pycheat-jinja-template.html'
    output_path = '/tmp/pycheat-jinja-output.html'

    # create the testing template
    with open(template_path, 'w') as f:
        f.write("""Testing template with {{athlet_type}}:
{% for a in athlets %}
{{a.name}} is from {{a['country']}}
{% endfor %}""")

    # testing dict with variables
    context = {
        'athlet_type': 'tennis players',
        'athlets': [
            {'name': 'Roger Federer', 'country': 'SUI'},
            {'name': 'Rafael Nadal', 'country': 'ESP'},
            {'name': 'Novak Djokovic', 'country': 'SRB'}
        ]
    }

    import jinja2
    import os
    # render the template
    template_dir, template_filename = os.path.split(template_path)
    loader = jinja2.FileSystemLoader(template_dir)

    # whitespace control:
    # http://jinja.pocoo.org/docs/2.9/templates/#whitespace-control
    jinja_env = jinja2.Environment(loader=loader, trim_blocks=True,
                                  lstrip_blocks=True)
    template = jinja_env.get_template(template_filename)
    rendered_output = template.render(context)
    # print and write the result to the file
    print rendered_output
    with open(output_path, 'w') as f:
        f.write(rendered_output.encode('utf-8'))


def main():
    print "Main function called"

    # argparse example
    import argparse
    parser = argparse.ArgumentParser(description='Program description which'
                                     ' will be displayed in help.')
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
    opts = vars(args)   # accessing: opts['myparam']
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
