import sys
import json


def main():

    string = ""
    for line in sys.stdin:
        string = string + line

    data = json.loads(string)

    print(json.dumps(data, indent=4))

if __name__ == "__main__":
    main()

