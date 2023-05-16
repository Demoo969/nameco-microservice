import sys
import requests
import getopt
import json

help_message = '''
    script to test microservice lab by Hose https://github.com/Hose968/practice/blob/main/main.py
    
    -h           print this help message and exit           | OPTIONAL
    -m/--method  [GET, POST] method for testing             | REQUIRED
    -t/--text    text of message to insert for POST method  | REQUIRED/OPTIONAL
    
'''
URL='http://127.0.0.1:8000/messages'

def get_messages():  
    response = requests.get(URL)
    ret=response.content.decode()
    return str(ret)


def post_messages(message: str = "base message"):
    body = json.dumps(message)
    response = requests.post(URL, data=body)
    ret=response.content.decode()
    return str(ret)


def main(argv):
    method = None
    message = 'test message'
    ret = ""

    try:
        opts, args = getopt.getopt(argv, "hm:t:", ['help', 'method=', 'text='])
    except getopt.GetoptError as e:
        print(f"Argument Error, reason: {e}")
        sys.exit(1)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print(help_message)
            sys.exit(0)
        elif opt in ('-m', '--method'):
            method = arg.upper()
        elif opt in ('-t', '--text'):
            message = arg
        else:
            print(f'unknown option {opt}')
            print(help_message)
            sys.exit(1)

    if method == "GET":
        ret = get_messages()
    elif method == "POST":
        if message is None:
            ret = post_messages()
        else:
            ret = post_messages(message)

    print(f"###: {ret}")


if __name__ == '__main__':
    main(sys.argv[1:])
