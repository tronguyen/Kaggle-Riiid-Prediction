from setuptools import setup, find_packages

setup_info = dict(
    name='bert_src',
    version='1.0',
    url='https://github.com/tronguyen/bert_src',
    author='Trong Nguyen',
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=[
        "numpy",
        "tqdm >= 4.27",
        "torch==1.6.0",
        "torchvision==0.7.0"
    ],
    description='Modules for graph embedding model',
    long_description=open('README.md').read(),
)

setup(**setup_info)
