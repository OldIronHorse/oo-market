from setuptools import setup

def readme():
  with open('README.rst') as f:
    return f.read()

setup(name='oo-market',
      version='0.1',
      description='Supermarket code test',
      long_description=readme(),
      keywords='codetest',
      url='http://github.com/OldIronHorse/oo-market',
      download_url='https://github.com/oldironhorse/oo-market/archive/0.1.tar.gz',
      author='Simon Redding',
      author_email='s1m0n.r3dd1ng@gmail.com',
      license='GPL3',
      packages=['supermarket'],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)
