from setuptools import setup, find_packages

setup(
    name='passreset', 
    version='0.1',
    author='Ben Davis',
    author_email='bendavis78@gmail.com',
    url='http://github.com/bendavis78',
    description='A simple app which adds password reset functionality to the Django admin site.',
    keywords='django admin',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    packages = find_packages(),
    include_package_data = True
)