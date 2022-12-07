from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='linnworks_pandas',
    packages=['linnworks_pandas'],
    version='0.001',
    license='MIT',
    description='Linnworks Pandas is a Python package that queries the Linnworks Query Data API and returns data in a Pandas dataframe. ',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Matt Clarke',
    author_email='matt@practicaldatascience.co.uk',
    url='https://github.com/practicaldatascience/linnworks_pandas',
    download_url='https://github.com/practicaldatascience/linnworks_pandas/archive/master.zip',
    keywords=['python', 'pandas', 'linnworks', 'ecommerce'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=['pandas', 'requests']
)
