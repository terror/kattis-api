import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    author="Liam Scalzulli",
    author_email="liam@scalzulli.com",
    description="A python wrapper for the Kattis API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="kattis",
    packages=setuptools.find_packages(),
    url="https://github.com/terror/kattis-api",
    version="1.0.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
