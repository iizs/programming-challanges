%.out: %.c %.in
	gcc -Wall -o $@ $<  
	./$@ < $(patsubst %.c,,$^)
	if [ -e $(patsubst %.out,%.answer,$@) ]; then \
		./$@ < $(patsubst %.c,,$^) > $(patsubst %.out,%.stdout,$@) ; \
	    diff $(patsubst %.out,%.answer,$@) $(patsubst %.out,%.stdout,$@) ; \
	    rm $(patsubst %.out,%.stdout,$@) ; \
	fi;
