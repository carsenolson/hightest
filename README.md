#	Hightest 

Two local servers which provide web-interface for creating and complete tests. (In development) 

### Installing
 
You need just python3.6 (not tested in 3.5 etc) 

Installation debain/ubuntu users 
```
sudo apt-get install python3
```

## Run the program

Test_creator doesn't use foreign libraries, so you can: 

```
pyton3 test_creator.py
```
Everything hosting on `localhost:8080`

After creating some tests - terminate test_creator server and launch test_server.py with this code:

```
python3 test_server.py
```

After creating and compliting tests you may see results and tests in directories `./tests && ./results`
