import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kattis",  # Replace with your own username
    version="0.0.1",
    author="Liam Scalzulli",
    author_email="liamscalzulli@gmail.com",
    description="A python wrapper for the Kattis API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/terror/kattis-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
