CFLAGS += -I.

.PHONY: run build clean


build: day2

run: build
	./day2

day2: main.o
	$(CC) $(LDFLAGS) $? $(LDLIBS) -o $@

clean:
	$(RM) main.o day2
