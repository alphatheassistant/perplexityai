from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="perplexityai",
    version="0.1",
    author="Author Name",  # Add the author name here
    author_email="author@example.com",  # Add the author's email here
    description="A python API to use perplexity.ai",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alphatheassistant/perplexityai",
    packages=find_packages(),
    install_requires=[
        "requests",
        "websocket-client"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Ensure the license is correct
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Adjust as necessary
)
