from setuptools import setup,find_packages
from sistr.version import __version__
from setuptools.command.install import install
#init database before package setup
from pre_setup import db_init
import os

classifiers = """
Development Status :: 4 - Beta
Environment :: Console
License :: OSI Approved :: Apache Software License
Intended Audience :: Science/Research
Topic :: Scientific/Engineering
Topic :: Scientific/Engineering :: Bio-Informatics
Programming Language :: Python
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Programming Language :: Python :: Implementation :: CPython
Operating System :: POSIX :: Linux
""".strip().split('\n')


class GetDBFirst(install):
    def run(self):
        """Install special binary dependencies before the others."""
        db_init()
        install.run(self)
        self.do_egg_install()


setup(
    name='sistr_cmd',
    version=__version__,
    packages=find_packages(exclude=['tests']),
    url='https://github.com/phac-nml/sistr_cmd',
    license='Apache 2.0',
    author='Peter Kruczkiewicz',
    author_email='peter.kruczkiewicz@gmail.com',
    description=('Serovar predictions from Salmonella whole-genome sequence assemblies by determination of antigen gene'
                 'and cgMLST gene alleles using BLAST. Mash MinHash can also be used for serovar prediction.'),
    keywords='Salmonella serotyping genotyping cgMLST BLAST Mash MinHash',
    classifiers=classifiers,
    package_dir={'sistr':'sistr'},
    include_package_data=True,
    setup_requires=['pycurl>=7.43.0', 'pandas>=0.18.1'],
    install_requires=[
        'numpy>=1.11.1',
        'pandas>=0.18.1',
        'tables>=3.3.0',
        'pycurl>=7.43.0',
        'scipy>=1.1.0'
    ],
    cmdclass={"install": GetDBFirst},
    extras_require={
        'test': ['pytest>=2.9.2',],
    },
    entry_points={
        'console_scripts': [
            'sistr=sistr.sistr_cmd:main'
        ],
    },
)

