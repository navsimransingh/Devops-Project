#!/usr/bin/env python

from __future__ import print_function

# Install virustotal-api from pip before using API:
from virus_total_apis import PublicApi as VirusTotalPublicApi

import argparse
import json
import sys
import time
import HTML  # Install module before using HTML

import html_gen
import webserver

# ===== PARSING COMMAND LINE ARGUMENTS TO SCRIPT =====
desc = '''
Specify the text file containing a list of hashes
to be checked against the virustotal.com database
'''
p = argparse.ArgumentParser(description=desc)

# Positional arguments:
p.add_argument('file', type=str, help='list of hashes')

# Optional arguments:
p.add_argument('-p', '--port', type=int, default=8000, help='webserver port')

args = p.parse_args()
# ====================================================

# ============ ACCESS Virustotal.com API =============
API_KEY = '2a11b9bed44b9580bde1033624b38d32fad0c470a8611dc5928ee8d85060745a'
virustotal = VirusTotalPublicApi(API_KEY)
# ====================================================

# ============== BUILDING HTML TABLE =================
msg = '''
This may take a while...

API quota is 4 queries per minute.
it will some time to complete
'''
print(msg)

HEADER_ROW = [
    'hash_value (MD5)',
    'FORTINET detection names',
    'Number of engines detected',
    'Scan Date'
]
table_data = []

# open the file as first command line argument for hash list analysis
f = open(sys.argv[1])
lines = f.readlines()
for line in lines:
    response = virustotal.get_file_report(line)

    # Convert json to dictionary:
    json_data = json.loads(json.dumps(response))

    if json_data['results']['response_code'] == 1 and \
       'Fortinet' in json_data['results']['scans']:
            table_data.append([
                json_data['results']['md5'],
                json_data['results']['scans']['Fortinet']['result'],
                json_data['results']['positives'],
                json_data['results']['scan_date']
                ])
    elif json_data['results']['response_code'] == 1 and \
            'Fortinet' not in json_data['results']['scans']:

            table_data.append([
                json_data['results']['md5'],
                '--',
                json_data['results']['positives'],
                json_data['results']['scan_date']
                ])
    else:
            table_data.append([
                line,
                'Hash is not in database',
                '--',
                '--'
                ])
    time.sleep(15)

f.close()

htmltable = HTML.table(table_data, header_row=HEADER_ROW)
# ====================================================

# =============== BUILDING HTML PAGE =================

cont_start = """
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta content="text/html; charset=ISO-8859-1" http-equiv="content-type">
<title>Virustotal Results Page</title>
<link rel="icon"
      type="image/png"
      href="http://localhost:%s/favicon.png">
</head>
<body style="background-color:powderblue;">
<center>
<h4>Hash analysis results from Virustotal.com</h4>
""" % args.port

cont_end = """
</center>
</body>
</html>
 """
contents = "%s %s %s" % (cont_start, htmltable, cont_end)
html_gen.str_to_file(contents, filename='index.html')
# ====================================================

# ================= RUN WEB SERVER ===================
msg1 = """
To see the results please open browser and navigate to
    http://localhost:%s\n\r""" % args.port
print(msg1)

# second command line argument is web server port# (integer):
webserver.start(port=args.port)
# ====================================================
