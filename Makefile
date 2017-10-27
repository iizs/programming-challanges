%.out: %.c %.in
	gcc -Wall -o $@ $<  
	./$@ < $(patsubst *.c,,$?)
