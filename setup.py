from setuptools import setup, find_packages

setup(
    name="shadowbyte",
    version="2.8.5",
    author="ShadowByte Developers",
    description="AI-Driven Autonomous Exploit & Network Reconnaissance Framework",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.31.0",
        "cryptography>=41.0.0",
        "colorama>=0.4.6",
    ],
    entry_points={
        "console_scripts": [
            "shadowbyte=shadowbyte:main",
        ],
    },
)
