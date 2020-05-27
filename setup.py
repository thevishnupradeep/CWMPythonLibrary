import setuptools

with open("../README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cwm_codewatchman",
    version="0.0.1",
    author="Code Watchman",
    author_email="codewatchmanapp@gmail.com",
    description="Code Watchman Python API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thevishnupradeep/CWMPythonLibrary",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers'
    ],
    install_requires=[
    ],
    python_requires='>=3.4'
)