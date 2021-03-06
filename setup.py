from setuptools import setup, find_packages

setup(
    name='uptempo',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'jinja2',
    ],
    entry_points='''
        [console_scripts]
        uptempo=uptempo.cli:cli
    ''',
)
