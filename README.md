hightest - is a complex program for creating tests for students.

there are tho types of servers:
	1. test_creator server -> this server starts http_server on localhost:3000
		with special web interface for creating tests (this server should be used by
		teachers or test_creators, not by students, because this server decrypt test's
		data)  
	2. test_server -> this server starts http_server on localhost:3000 with test 
		interface, this server is created for students.
