# netsec


In order to compile program that uses external dynamic library (.so) use following command

gcc -L/home/stud/adilova/netsec/test_yourself -Wl,-rpath=/home/stud/adilova/netsec/test_yourself -Wall -o third third.c -lcodeninja

Keep in mind, that library is libcodeninja.so, but you write -lcodeninja
