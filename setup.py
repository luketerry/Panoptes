from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["easygui>=0.98", "Keras>=2.3", "numpy>=1.17.5", "opencv-python>=4.1.2",
                "openslide-python>=1.1.1", "pandas>=0.25", "Pillow>=7", "scikit-learn>=0.22", "scipy>=1.3",
                "spams>=2.6", "staintools>=2.1.2", "tensorflow>=1.11", "matplotlib>=3.1"]

setup(
    name="panoptes",
    version="0.0.5",
    author="Runyu Hong",
    author_email="Runyu.Hong@nyu.edu",
    description="A multi-resolution CNN to predict endometrial cancer features",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/rhong3/Panoptes/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
    ],
)
