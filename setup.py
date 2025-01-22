from setuptools import setup, find_packages

setup(
    name="holospooky",
    version="0.1.0",
    description="Unofficial fixed module + pre-built programs + self-made features for Cozmo SDK",
    #long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Julia Al-Otoom, @D3M0NG1RL17 on GitHub",
    author_email="julia.alotoom@icloud.com",
    url="https://github.com/D3M0NG1RL17/holospooky",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.13",
)
print(setup)