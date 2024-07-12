from setuptools import setup, find_packages

setup(
    name='docx_merger',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'python-docx',
        'ebooklib',
    ],
    entry_points={
        'console_scripts': [
            'merge-docx=docx_merger.merger:main',
        ],
    },
    author='Luis Miguel Martinez',
    author_email='lmiguel.martinezg@gmail.com',
    description='A package to merge DOCX files into one EPUB file',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/lmmartinez97/merger',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
