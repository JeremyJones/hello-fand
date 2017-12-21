clean:
	rm -rf build/*

package: clean
	mkdir build
	tar cvfz build/fanduel-homework.tar.gz --exclude=build --exclude='*.sqlite3' --exclude='*.pyc' --exclude=Makefile ./*
