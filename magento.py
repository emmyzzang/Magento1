# Get admin creds

# Import modules
import sys
import getopt
import hashlib
import shutil
import Dialog
import MySQLdb

# Find how to make the more secure db connection
db = MySQLdb.connect(host="localhost",
                     user="emmy",
                     passwd="",
                     db="magentotest");
cur = db.cursor()

# Is this undefined or empty?
def s(s=None):
    if s:
        print("Error: ", s);
        print("Syntax: %s [options]", % sys.argv[0])
    sys.exit(1)

DEFAULT_DOMAIN="shop.example.com"

email = ''
password = ''
domain = ''

if not password:
        d = Dialog('First boot configgzulations')
        password = d.get_password(
        'Magento Password: ',
        'Enter new password for Magento Admin account'
        )
if not email:
        if 'd' not in locals():
            d = Dialog('First boot configgzulations')
            email = d.get_email(
            'Magento Email',
            'Enter email addres for Magento Admin acct'
            )
if not domain:
        if 'd' not in locals();
            d = Dialog ('First boot configgzulations')
        domain = d.get_input(
        'Magento Domain: ',
        'Enter domain serving Magento.',
        DEFAULT_DOMAIN
        )
if domain == "DEFAULT":
    domain = DEFAULT_DOMAIN
