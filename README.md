# pivot
a cli tool to create pivots from cli

# Arguments

## Input
```
--csv: The input file to be processed (required)
```

## At least one of the following export options must exist
```
--export_xlsx: Pivot export filename 
--export_html: HTML export filename.
--export_csv:  CSV export filename.
```

## Data manipulation options
```
-i,--index:    Column names used as pivot indexes. (required)
-v,--values:   Column names used as values. (required)
-c,--columns:  Column names used to breakdown the analysis.
-a,--aggfunc:  Pandas aggregate functions to be applied. (defaults to "mean")
```

## Other options
```
-f,--fillna:   Fill n/a values with specified value.
-m,--margins:  If present print a margins line.
```
