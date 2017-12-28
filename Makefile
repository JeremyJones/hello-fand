clean:
	rm -rf build/*

package: clean
	mkdir build
	tar cvfz build/fanduel-homework.tar.gz --exclude=build --exclude='*.sqlite3' --exclude='*.pyc' --exclude=Makefile ./*

backup:
	tar zcpf backups/new-backup.tgz --exclude=backups --exclude='*~' --exclude='*.pyc' --exclude='.DS_Store' --exclude='.idea' --exclude=venv --exclude=build --exclude=Makefile ./*
	perl -e 'rename(qq[backups/new-backup.tgz], sprintf(qq[backups/backup-at-%s.tgz], time())) or warn $!'

