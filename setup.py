import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("__init__.py", "r") as file:
    regex_version = r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]'
    version = re.search(regex_version, file.read(), re.MULTILINE).group(1)

with open("README.rst", "rb") as file:
    readme = file.read().decode("utf-8")

setup(
    name="install_package_pip",
    version=version,
    packages=["install_package_pip"],
    package_data={"install_package_pip": ["__init__.pyi", "py.typed"]},
    description="Installer package for pip it tread",
    long_description=readme,
    long_description_content_type="text/x-rst",
    author="Kolokoltsev Maxim",
    author_email="Kolokolcev20@mail.ru",
    url="https://github.com/MaximTourist/install_package_pip",
    download_url="https://github.com/MaximTourist/install_package_pip_v{version}.tar.gz".format(version),
    project_urls={
        "Changelog": "https://github.com/MaximTourist/install_package_pip/README.md",
        "Documentation": "https://github.com/MaximTourist/install_package_pip/README.md",
    },
    keywords=["install_package_pip", "installer", "pip"],
    license="MIT license",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
#        "Topic :: System :: Logging",
        "Intended Audience :: Developers",
        "Natural Language :: Russia",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
"""
    install_requires=[
        "colorama>=0.3.4 ; sys_platform=='win32'",
        "loguru>=0.5.3"
    ],
    extras_require={
        "dev": [
            "loguru>=0.5.3",
            "colorama>=0.3.4",
        ]
    }, """
    python_requires=">=3.7",
)