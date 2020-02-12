from setuptools import setup

setup(
    name='controllers',
    packages=['controllers'],
    include_package_data=True,
    install_requires=[
        'flask',
        'sqlalchemy'
    ],
)

