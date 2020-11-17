import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="RealtimeStock",
    version="1.0.2",
    author="Hurin Hu",
    author_email="hurin@live.ca",
    description="Realtime stock quote for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Iceloof/RealtimeStock",
    packages=setuptools.find_packages(),
    install_requires=['requests','pytz'],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
