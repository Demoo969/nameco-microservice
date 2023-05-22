# nameco-microservice

  Its simply micro service code
  
 
**To run project use:** 
**First metod**
```shell
1 $ python3 -m venv env ```text recommended to  corect work```
2 $ pip install nameko 
3 $ nameko run [name of service]
```
**Second metod**
```shell
$ sudo docker-compose up
```
to rebuild it
```shell
$  sudo docker-compose up --no-deps --build 
```
**To use project:**
```shell
$ python3 runner.py -m/--method [-t/--text = 'text message'] [-n/--number = 1] 
```
**runner.py usage:**
```text
$ python3 runner.py -h

    script to test microservice lab
    
    -h           print this help message and exit           | OPTIONAL
    -m/--method  [GET, POST] method for testing             | REQUIRED
    -t/--text    text of message to insert for POST method  | REQUIRED/OPTIONAL
```
