#!/usr/bin/env python3
import pandas as pd
import numpy  as np
import argparse
import sys

def stringify_one_element_list(l):
    """
    if the list has only one element convert it to a string.
    """
    if len(l) == 1:
        return str(l)
    else:
        return l

def stderr_print(*args, **kwargs):
    """
    print to stderr
    """
    print(*args, file=sys.stderr, **kwargs)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Create pivots from csv files.")
    parser.add_argument('--csv',
                        type     = str,
                        required = True,
                        help     = "csv input.")

    parser.add_argument('--export_xlsx',
                        type     = str,
                        required = False,
                        default  = None,
                        help     = "Excel export filename.")

    parser.add_argument('--export_html',
                        type     = str,
                        required = False,
                        default  = None,
                        help     = "HTML export filename.")

    parser.add_argument('--export_csv',
                        type     = str,
                        default  = None,
                        required = False,
                        help     = "CSV export filename.")

    parser.add_argument('-f','--fillna',
                        type     = str,
                        required = False,
                        default  = 0,
                        help     = "fill n/a values.")

    parser.add_argument('-i','--index',
                        type     = str,
                        nargs    = "+",
                        required = True,
                        help     = "column names used as pivot indexes.")

    parser.add_argument('-v','--values',
                        type     = str,
                        nargs    = "+",
                        required = True,
                        default  = [],
                        help     = "column names used as values.")

    parser.add_argument('-c','--columns',
                        type     = str,
                        nargs    = "+",
                        required = False,
                        default  = [],
                        help     = "column names used to breakdown the analysis.")

    parser.add_argument('-m','--margins',
                        default  = True,
                        required = False,
                        action   = 'store_false')

    parser.add_argument('-a','--aggfunc',
                        type     = str,
                        nargs    = "+",
                        required = False,
                        default  = 'sum',
                        help     = "pandas aggregate functions to be applied.")

    args = parser.parse_args()

    if args.export_csv == None and args.export_xlsx == None and args.export_html == None:
        stderr_print("Export filename is required.")
        sys.exit(1)

    # Create dataframe from csv
    try:
        df = pd.read_csv(args.csv)
    except Exception as ex:
        stderr_print(str(ex))
        sys.exit()

    if len(args.columns) == 0:
        pivot = df.pivot_table(index      = args.index,
                               fill_value = args.fillna,
                               margins    = args.margins,
                               values     = args.values,
                               aggfunc    = args.aggfunc)
    elif len(args.columns) > 0:
        pivot = df.pivot_table(index      = args.index,
                               columns    = args.columns,
                               values     = args.values,
                               fill_value = args.fillna,
                               margins    = args.margins,
                               aggfunc    = args.aggfunc)

    if args.export_xlsx != None:
        pivot.to_excel(args.export_xlsx, index = True)

    if args.export_csv != None:
        pivot.to_csv(args.export_csv, index = True)

    if args.export_html != None:
        pivot.to_html(args.export_html, index = True)
