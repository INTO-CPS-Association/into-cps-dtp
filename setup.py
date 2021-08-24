"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README_PYINDEX.md').read_text(encoding='utf-8')


setup(
    name='into-cps-dtp',  # Required
    version='0.0.3',  # Required
    long_description_content_type='text/markdown',  # Optional (see note above)
    long_description=long_description,  # Optional
    description='A utility to show basic ISO 1178-10 XML data',  # Optional
    license='INTO-CPS',
    url='https://github.com/INTO-CPS-Association/into-cps-dtp',
    package_dir={'': 'src'},  # Optional
    author='INTO-CPS',
    packages=find_packages(where='src'),  # Required
    python_requires='>=3.7, <4',
    keywords='digitaltwin, co-simulation',  # Optional
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/INTO-CPS-Association/into-cps-dtp/issues',
        'Funding': 'https://into-cps.org/',
        'Source': 'https://github.com/INTO-CPS-Association/into-cps-dtp',
    },
    # https://packaging.python.org/en/latest/requirements.html
    # install_requires=['gpiozero', 'pika', 'pyhocon','argparse'],  # Optional

    extras_require={  # Optional
        'dev': ['check-manifest'],
        'tests': ['coverage'],
    },

    # entry_points={  # Optional
    #     'console_scripts': [
    #         'cli=isoxmlviz:main',
    #     ],
    # },
# For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],

)
