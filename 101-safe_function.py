#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        fct(args)
    except Exception:
        raise Exception(sys.stderr)
        # print(fct, Exception=sys.stderr)
        return None