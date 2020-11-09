# PyArrow Flight

* Create an environment: `conda env create -f environment.yml`
* Activate environment: `conda activate pyarrow-flight`
* Run server: `python ./server.py`
 
Client can now receive Arrow table from Server via gRPC with Pandas integration. 
```
$ python ./client.py 
       city  population
0    Moscow    12000000
1  New-York     8300000
2    Mexico     8800000
```
