import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="convert2vars",
    version="0.0.1",
    install_requires=[
        "click",
        "python-dotenv",
        "iniconfig",
        "Jinja2",
        "PyYAML",
    ],
    entry_points={
        'console_scripts': [
            'convert2vars=convert2vars:main',
        ],
    },
    author="t-m0riyama",
    author_email="mt52405@gmail.com",
    description="A small tool for mutual conversion of json, yaml, including parameters.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/t-m0riyama/convert2vars",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
