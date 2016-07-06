# Amazon Used Price Scraper
Scrape any product used price off of Amazon.com. Tool is meant for bulk-searches, but can also be used for individual products. Can pull info from either the command line, or from an input file.

Examples bellow utilize only ISBN numbers, but you may use any search queries.

## Arguments

####-d: Pull directly from command line.
```python main.py -d```
or
```python main.py -d [First search query]```

####-f: Pull from file.
```python main.py -f input.txt```

## Examples

####-d
```
~$ python main.py -d 9780385495646
Type 'exit' to exit.

0.01	Ghost Soldiers: The Forgotten Epic Story of World War II's Most Dramatic Mission

Input: exit

~$ 
```

####-f
```
~$ python main.py -f input.txt
Processing |######                          | 1/5	Processing: 9780385495646
Processing |############                    | 2/5	Processing: 9780786300013
Processing |###################             | 3/5	Processing: 9780446572
Processing |#########################       | 4/5	Processing: 9780446578141
Processing |################################| 5/5	Processing: 978044657
Finished with 2 error(s). Saved to output.txt.

~$
```

#####input.txt
```
9780385495646
9780786300013
9780446572
9780446578141
978044657
```

#####output.txt
```
0.01	Ghost Soldiers: The Forgotten Epic Story of World War II's Most Dramatic Mission
0.83	The Handbook of Fixed Income Securities
Error. Could not find 9780446572
0.01	The Real Deal: My Life in Business and Philanthropy
Error. Could not find 978044657

```






