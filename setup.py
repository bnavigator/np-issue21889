try:
    from skbuild import setup
    from skbuild.command.sdist import sdist
except ImportError:
    raise ImportError('scikit-build must be installed before running setup.py')


CLASSIFIERS = """\
Development Status :: 4 - Beta
Intended Audience :: Science/Research
Intended Audience :: Developers
License :: OSI Approved
License :: OSI Approved :: GNU General Public License v2 (GPLv2)
Programming Language :: C
Programming Language :: Fortran
Programming Language :: Python
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9
Programming Language :: Python :: 3.10
Topic :: Software Development
Topic :: Scientific/Engineering
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: Unix
Operating System :: MacOS
"""


setup(
    name='issue21889',
    packages=['issue21889'],
    cmake_languages=('C', 'Fortran'),
    version='0.0.1',
    maintainer="bnavigator",
    maintainer_email="code@bnavigator.de",
    description="a reproducer for numpy#21889",
    long_description="",
    url='https://github.com/bnavigator/np-issue21889',
    author='bnavigator',
    license='BSD-3-Clause',
    classifiers=[_f for _f in CLASSIFIERS.split('\n') if _f],
    platforms=["Windows", "Linux", "Solaris", "Mac OS-X", "Unix"],
    zip_safe=False,
    install_requires=['numpy>=1.23.0'],
    python_requires=">=3.7"
)