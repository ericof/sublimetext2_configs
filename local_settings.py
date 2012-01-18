'''
First parameter is path to command, second - optional list of arguments.
If you want to disable line length checking in pep8, set second parameter
to ['--ignore=E501'].
'''
CHECKERS = [('/usr/bin/pep8', []),
            ('/usr/bin/pyflakes', [])]
