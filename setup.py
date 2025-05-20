from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setup(
    name="meta-ads-analytics",
    version="1.0.0",
    author="Seu Nome",
    author_email="seu.email@exemplo.com",
    description="Análise de anúncios da Meta (Facebook) através da API oficial",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seu-usuario/meta-ads-analytics",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "meta-ads-analytics=main:main",
        ],
    },
) 