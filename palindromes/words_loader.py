import sys


def load(file):
    try:
        with open(file) as in_file:
            opened_file = in_file.read().strip().split('\n')
            return [x.lower() for x in opened_file]
    except IOError as e:
        print('{}\nError opening {}. Exiting...'.format(e, file), file=sys.stderr)
        sys.exit(1)