from setuptools import setup

setup(
    name='okane-server',
    packages=['okane'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
