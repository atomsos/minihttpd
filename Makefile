all: httpd

httpd: httpd.c mimes.c
	gcc -W -Wall -o httpd httpd.c mimes.c -lpthread

clean:
	rm httpd
