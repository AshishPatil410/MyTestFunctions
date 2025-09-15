from setuptools import setup

install_requires = [
]

setup(
    name='MyLibs',
    version='1.0.0',
    author='ashish',
    author_email='ashishpatil2@icloud.com',
    description='This package contains test functions to learn pytest',
    python_requires='>=3.6',
    install_requires=install_requires,
    include_package_data=True,
    classifiers=[
        "Framework :: Pytest",
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)

