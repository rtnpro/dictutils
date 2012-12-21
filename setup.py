from setuptools import setup


setup(
    name='dictutils',
    version='0.1.1',
    url='https://github.com/rconradharris/dictutils',
    license='MIT',
    author='Rick Harris',
    author_email='rconradharris@gmail.com',
    description='Utilities for working with Python dictionaries',
    long_description=__doc__,
    py_modules=['dictutils'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[''],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
