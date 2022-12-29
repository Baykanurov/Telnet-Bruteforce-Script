import argparse

parser = argparse.ArgumentParser(description='Bruteforce Telnet Script')

parser.add_argument('--target_host', help='Target Host', required=True)
parser.add_argument('--target_port', help='Target Port', required=True)
parser.add_argument('--file_logins', help='File logins', required=True)
parser.add_argument('--file_passwords', help='File passwords', required=True)
parser.add_argument('--failed_text', help='Text Failure', default='Invalid.')
