from setuptools import setup, find_packages

str_version = '1.0.0'

setup(name='yifeitechsupport',
	  version=str_version,
	  description='bofangliang tools for yifei',
	  author='yifei_tech_support',
	  author_email='zufang.st@gmail.com',
	  license='feimi',
	  url = 'https://github.com/yifei-techsupport/yifei-tech-support.git'
	  packages=find_packages(),
	  zip_safe=False,
	  python_requires='>3')