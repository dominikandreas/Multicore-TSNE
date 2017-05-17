import sys
import os
from setuptools.command.install import install
from setuptools import setup

'''
    Just because I wanted .so file to be built same way for python and torch
    we exec cmake from cmd here.
'''

is_win = os.name=='nt'


class MyInstall(install):
    def run(self):
        if not is_win:
            if not os.path.exists('multicore_tsne/release'):
                os.makedirs('multicore_tsne/release')
            else:
                os.system('rm -rf multicore_tsne/release/')
                os.makedirs('multicore_tsne/release')

            os.chdir('multicore_tsne/release/')
            return_val = os.system('cmake -DCMAKE_BUILD_TYPE=RELEASE ..')

            if return_val != 0:
                print('cannot find cmake')
                exit(-1)

            os.system('make VERBOSE=1')
            os.chdir('../..')
            print(os.getcwd())
            os.system('cp multicore_tsne/release/tsne_multicore.dll python/libtsne_multicore.dll')
        install.run(self)


setup(
    name="MulticoreTSNE",
    version="0.1",
    description='Multicore version of t-SNE algorithm.',
    author="Dmitry Ulyanov (based on L. Van der Maaten's code)",
    author_email='dmitry.ulyanov.msu@gmail.com',
    url='https://github.com/DmitryUlyanov/Multicore-TSNE',
    install_requires=[
        'numpy',
        'psutil',
        'cffi'
    ],

    packages=['MulticoreTSNE'],
    package_dir={'MulticoreTSNE': 'python'},
    package_data={'MulticoreTSNE': ['libtsne_multicore.' + ('dll' if is_win else 'so')]},
    include_package_data=True,

    cmdclass={"install": MyInstall},
)
