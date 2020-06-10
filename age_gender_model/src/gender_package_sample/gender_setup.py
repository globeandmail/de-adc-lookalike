from setuptools import setup, find_packages

setup(
    name="gender-pkg",
    version="0.0.1",
    author="Sean Xiong",
    author_email="sean.xiong@mail.utoronto.ca",
    description="An email-based gender prediction package, requires joblib package, "
                "from sklearn.externals import joblib ",
    long_description="For Globe and Mail Internal Use Only ",
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=['scikit-learn','sklearn', 'pandas'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Internal Server",
        "Intended Audience :: ADC Data Engineering Team"
    ],
    python_requires='>=3.6'
)
