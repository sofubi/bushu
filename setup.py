import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bushu-sofubi",
    version="0.0.1",
    author="Thomas Lawton",
    author_email="thomaslawton91@gmail.com",
    description="A small reader for manga from Mangadex",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sofubi/bushu",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
