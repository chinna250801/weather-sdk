from setuptools import setup, find_packages

setup(
    name="weather_sdk",
    version="0.1.0",
    author="Shin Chan",
    author_email="doraemon.email@example.com",
    description="A Python SDK for interacting with the OpenWeatherMap API",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/china250801/weather-sdk",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
)
