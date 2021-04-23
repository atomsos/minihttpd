all: mhttpd

mhttpd: httpd.c mimes.c
	make clean
	gcc -W -Wall -o mhttpd httpd.c mimes.c -lpthread

clean:
	rm -f mhttpd
