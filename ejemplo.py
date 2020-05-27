import time
import sys


def main():
    time.sleep(15)
    if sys.platform in ['win32', 'cygwin']:
        print('Soy Windows!!')
    else:
        print('Soy Unix!!')


if __name__ == '__main__':
    main()
