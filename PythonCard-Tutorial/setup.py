#Must install distutils for this to work!

from distutils.core import setup, Extension

setup(name='GUI Application',
	version='0.1',
	description='Generic installable GUI application template',
	author='Michael',
	author_email='michael@ipv6secure.co.uk',
	py_modules=['example'])

#Extension modules to be appended here later
