# nameco-microservice

  Its simply micro service code
  
 
**To run project use:** 
```shell
1 $ python3 -m venv env
2 $ pip install nameko in 
3 $ service folder/nameko run [name of service]
```
**To use project:**
```shell
$ python3 runner.py -m/--method [-t/--text = 'text message'] [-n/--number = 1] 
```
**runner.py usage:**
```text
$ python3 main.py -h

    script to test microservice lab
    
    -h           print this help message and exit           | OPTIONAL
    -m/--method  [GET, POST] method for testing             | REQUIRED
    -t/--text    text of message to insert for POST method  | REQUIRED/OPTIONAL
```
