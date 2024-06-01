import setuptools

setuptools.setup(
    name="weather-sdk",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    author="Shin Chan",
    author_email="your.email@example.com",
    description="A Python SDK for accessing weather data from OpenWeatherMap API",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/china250801/weather-sdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
