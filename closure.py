#!/usr/bin/python2.4

import httplib, urllib, sys

fn = sys.argv[1]
fnm = fn[:-3] + ".min.js";

rf = open(fn, 'r');

params = urllib.urlencode([
    ('js_code', rf.read()),
    ('compilation_level', 'SIMPLE_OPTIMIZATIONS'),
    ('output_format', 'text'),
    ('output_info', 'compiled_code')
])

rf.close()

headers = { "Content-type": "application/x-www-form-urlencoded" }
conn = httplib.HTTPConnection('closure-compiler.appspot.com')
conn.request('POST', '/compile', params, headers)

wf = open(fnm, 'w')
wf.write(conn.getresponse().read())
wf.close()

conn.close()
