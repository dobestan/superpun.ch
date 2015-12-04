# target: help - Display callable targets
help:
	@egrep "^# target:" [Mm]akefile


# target: clean - Clean all ".pyc" files
clean:
	find . -name "*.pyc" -exec rm -rf {} \;


# target: migrate - Migrate all django applications considering app dependencies
migrate:
	python superpunch/manage.py makemigrations multisites items
	python superpunch/manage.py migrate


# target: clean_migration - folders in all django apps
clean_migrations:
	ls superpunch/ | grep -v -e 'manage.py' | xargs -I{} rm -rf superpunch/{}/migrations/


# target: test - execute project related tests including coding convention and unittest
test:
	flake8 superpunch/
	superpunch/manage.py test superpunch/ -v 2
