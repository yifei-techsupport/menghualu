import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="yifeitechsupport",
    version="0.0.1",
    author="yifei_tech_support",
    author_email="zufang.st@gmail.com",
    description="tools for yifei",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yifei-techsupport/menghualu",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
