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

# Module constant - https://www.python.org/dev/peps/pep-0008/#constants
MY_MODULE_CONSTANT = "Module constant"

# Exceptions
class MyException(Exception):
    '''
    All exceptions are subclasses of BaseException.
    Exception is also subclass of BaseException and is the parent class
    for all non-exit exceptions.
    '''
    pass

def exceptions():
    try:
        raise MyException('Some description')
    except MyException as e:
        print('The error occurred: {}').format(e)

# Enum class
# usage: print Colours.Red
class Colours:
    Red, Green, Blue, White = range(4)

class MyClass:

    def __init__(self, attr):
        self.my_attr = attr

    def date_magic(self):
        import datetime

        one_day_maybe =  datetime.datetime.strptime("2018-09-21 21:49:55", "%Y-%m-%d %H:%M:%S")
        today = datetime.datetime.now()


def docstrings(param1, param2):
    """This is first line - doc string should start here.
    Docstrings should be enclosed by three double quotes.
    Docstrings are used also for introspection.

    Example usage of reST (=reStructuredText) documenting variables:

    :param timestamp: formatted date to display
    :type timestamp: str or unicode
    :returns: formatted string
    :rtype: str or unicode

    Last line of docstring should contain just three double quotes.
    """
    return "example string"

def datatypes():
    import numbers
    # is the variable a number?
    my_variable = 3.14
    isinstance(my_variable, numbers.Number)

    # determine iterables - str, dict, list...
    my_var = [1, 2, 3]
    import collections
    print "Is my_var iterable? - %s" % isinstance(my_var, collections.Iterable)

    # strings
    # interpolation can be made with both single or double quotes, but usually used with double
    single_quote_str = 'single quotes for short strings typically not intended for humans'
    double_quote_str = "double quotes for longer strings typically intended for humans"
    # raw string literal - the string is used directly without escaping and interpolations
    raw_str = r'this is raw string - all special characters has no meaning - {} abcd \n\n etc.'
    # unicode string
    unicode_str = u'my unicode string ěščřžáíé'

    # conversions
    int("5")


def lists():
    l = [1, 2, 'three'] # old-style: l = list(1, 2, 'three')
    # filter the list
    int_list = [1, 2, 3, 4]
    print "Even numbers: %s" % filter(lambda i: i % 2 == 0, int_list)
    print "Even numbers: %s" % [i for i in int_list if i % 2 == 0]


def dictionaries():
    # create
    number_one_players = {'man': 'Novak Djokovic', 'woman': 'Angelique Kerber'}

    # iterate
    for sex, name in number_one_players.items():
        print('World No.1 {}: {}'.format(sex, name))

    # merging dicts
    en = {1: 'one', 2: 'two'}
    cs = {2: 'dve', 3: 'tri'}   # overwrites the key 2
    en = {**en, **cs}

    # zip two lists into the dict
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    dictionary = dict(zip(keys, values))
    print dictionary    #{'a': 1, 'b': 2, 'c': 3}

    # ordered dicts
    from collections import OrderedDict
    orig = {
        'roger': {'gs_titles': 20},
        'rafa': {'gs_titles': 19},
        'nole': {'gs_titles': 17},
        'andy': {'gs_titles': 3}
        }

    # dictionary sorted by key
    orddict1 = OrderedDict(sorted(orig.items(), key=lambda t: t[0]))
    print orddict1  # {andy: ..., nole: ..., rafa: ..., roger: ...}
    # dictionary sorted by GS titles
    orddict2 = OrderedDict(sorted(orig.items(), key=lambda t: t[1]['gs_titles']))
    print orddict2  # {roger: ..., rafa: ..., nole: ..., andy: ...}

def lambdas():
    players = ['roger', 'rafa', 'nole']
    players_claims = map(lambda player: player+" is the best!", players)
    print()


def classes():
    # abstract methods
    class Base(object):
        def go(self):
            raise NotImplementedError("Method is not implemented.")


def iterate_object():
    """
    Examples: https://stackoverflow.com/questions/4019971/how-to-implement-iter-self-for-a-container-object-python
    """

    # Simplest case - use generator function (with yield)
    class IterClass1(object):
        def __iter__(self):
           yield 5
           for x in range(3):
              yield x
    iter_class_object = IterClass1()
    # will print the sequence: 5, 0, 1, 2
    for val in iter_class_object:
        print val

    # Inherit from appropriate collection
    from collections import Sequence
    class MyContainer(Sequence):
        def __init__(self, *data):
            self.data = list(data)
        def __getitem__(self, index):
            return self.data[index]
        def __len__(self):
            return len(self.data)
    cont = MyContainer(1, "two", 3, 4.0)
    print "\nContainer 2:"
    for val in cont:
        print val

    # If container is its own iterator, just implement next method
    from collections import Iterator
    class IterClass2(Iterator):
        def __init__(self, data):
           self.data = data
        def next(self):
            if not self.data:
               raise StopIteration
            return self.data.pop()
        # alternative when we do not want to use base Iterator class:
        #def __iter__(self):
        #    return self
    iterable_object = IterClass2(["a", 2, 3])
    print "\nContainer 3:"
    for val in iterable_object:
        print val


def printing():
    value1 = "val1"
    value2 = "val2"
    titles = {'roger': 20, 'rafa': 19}
    # python3 style
    print('Just print format args positionally: {}, {}'.format(1, 2))
    print("Printing args from defined position {1} and {0}".format(value1, value2))
    print("Roger has {roger} GS titles and Rafa {rafa}".format(roger=20, rafa=19))
    print("Roger has {roger} GS titles and Rafa {rafa}".format(**titles))
    print('Escaping the curly braces by doubling them - {{}} and normal arg: {}'.format('myarg'))

    # printint to stderr
    print("This is the testing error, don't panic!", file=sys.stderr)

    # round float to decimal
    print('Rounded to decimal: {:.0f}'.format(3.14))

    # print with leading zeros (padding)
    for i in range(5):
        # fill int
        print("{:03}".format(i))
        # fill string
        print(str(i).zfill(3))

    # thousands separator
    # comma separator works directly
    print("{:,}".format(1234))  # 1,234
    # other separators must use locale
    import locale
    locale.setlocale(locale.LC_ALL, '')  # Use '' for auto, or force e.g. to 'en_US.UTF-8'
    print("{:n}".format(1234))  # 1 234

    # print dict (named args)
    print "User %(username)s is from %(city)s. I love %(city)s city!" % {'username': "niwics", 'city': "Brno"}

    # Pretty-printing
    hierarchical_dict = {'a': 1, 'b': [{'ba': 2, 'bb': 3}]}
    import pprint
    pp = pprint.PrettyPrinter(indent=5)
    pp.pprint(hierarchical_dict)

    # dynamically rewriting the output line
    print("output A", end="\r")
    print("output B", end="\r")


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

    # basic example
    match = re.search(r"ne+dle", "searching neeedle in the haystack!")
    print match.group(0)    # neeedle

    # precompiling
    regexp = re.compile(r"(\d+):\d+")
    match = regexp.search("arrival in 12:00")
    print "arrival hour: %s" % match.group(1)

    # match / search / findall / finditer
    s_singleline = "one two two three"
    s_multiline = """one two two
    and two
    two three"""
    # match - from the begining, single line, first occurence
    re.match("two", s_singleline)   # None - matches from the begining
    re.match("\w+ two", s_singleline) # <re.Match object; span=(0, 7), match='one two'>
    re.match(".*three", s_multiline) # None - matches just first line
    # search - inside, multiline, first occurence
    re.search("two", s_singleline)  # <re.Match object; span=(4, 7), match='two'>
    re.search("two", s_multiline)   # <re.Match object; span=(4, 7), match='two'>
    re.search("three", s_multiline)   # <re.Match object; span=(24, 29), match='three'>
    # findall - inside, multiline, all occurences
    re.findall("two", s_singleline)  # ['two', 'two']
    re.findall("two", s_multiline)   # ['two', 'two', 'two', 'two']
    re.findall("three", s_multiline)   # ['three']
    re.findall("((tw)o?)", s_singleline)    # [('two', 'tw'), ('two', 'tw')]
    # finditer - inside, multiline, all occurences
    for match in re.finditer("two", s_multiline):
        print(match)
        # <re.Match object; span=(4, 7), match='two'>
        # <re.Match object; span=(8, 11), match='two'>
        # <re.Match object; span=(16, 19), match='two'>
        # <re.Match object; span=(20, 23), match='two'>

    # multiline strings - begining matching
    s = "one\ntwo"
    re.search("^two", s)    # None
    re.search("^two", s, re.MULTILINE)  # <re.Match object; span=(4, 7), match='two'>
    
    # named groups matching
    s = "one two three tw two"
    pattern = "(?P<first>tw)(?P<second>o)?"
    re.findall(pattern, s)  # [('tw', 'o'), ('tw', ''), ('tw', 'o')]
    match = re.search(pattern, s)   # <re.Match object; span=(4, 7), match='two'>
    match.groups()  # ('tw', 'o')
    match.groupdict()   # {'first': 'tw', 'second': 'o'}

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
    # load from the specific format (format ref: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)
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
    import yaml     # from package pyyaml
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
    #response attributes: r.headers, r.encoding, r.text, r.json()


def sftp_uploading():
    """
    ##### TODO
    """
    import paramiko
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
    ssh.connect(server, username='myuser', password='mypass')
    sftp = ssh.open_sftp()
    print "Copying %s to %s:%s" % (src, server, dst)
    sftp.put(src, dst, callback=None)
    sftp.close()
    ssh.close()


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
                                     ' will be displayed in help.',
                                     # ArgumentDefaultsHelpFormatter for displaying
                                     # default values in help
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
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
    # useful return codes: (more on https://docs.python.org/3/library/os.html#os._exit)
    # EX_OK
    # EX_USAGE - bad program usage
    # EX_DATAERR - incorrect input data
    # EX_NOINPUT - input file does nor exist or is not readable
    # EX_OSFILE - file does nor exist or is not readable
    # EX_IOERR - generic IO error
    # EX_UNAVAILABLE - required service is unavailable
    # EX_SOFTWARE - software runtime error
    # EX_CONFIG - configuration error
    # EX_NOTFOUND
    sys.exit(os.EX_OK)


if __name__ == '__main__':
    main()
