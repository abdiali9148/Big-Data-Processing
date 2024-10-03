# CS 1440 Project 3: Big Data Processing - Performance Benchmark Tool

This tool will tell you how slow `big_data.py` can be and still meet the customer's requirements.

Its command line interface is identical to the Big Data program:

```
Usage: demo/benchmark.py DATA_DIR
```

After downloading and unzipping the `data/USA_full/2023.annual.singlefile.csv` data set, run this command from the root of the repository:

```bash
$ python demo/benchmark.py data/USA_full
Done!                     
It took 4.34s to process 3,636,534 lines of data (490 MB)
On this computer big_data.py should finish in under 21.69s
```

This program will crash if it does not find `2023.annual.singlefile.csv` in its `DATA_DIR` argument.
