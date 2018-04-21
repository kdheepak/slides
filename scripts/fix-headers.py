"""
Fix headers
"""

import sys
import panflute as pf

ignore_elements = []


def fix_header_level(elem, doc):
    sys.stderr.write(str(elem))
    pass


def finalize(doc):
    pass

def main(doc=None):
    return pf.run_filter(fix_header_level, doc=doc, finalize=finalize)


if __name__ == "__main__":
    main()
