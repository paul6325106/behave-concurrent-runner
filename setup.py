from setuptools import setup


def get_readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='paul6325106.behave-concurrent-runner',
    version='1.0.dev0',
    description="Example of a concurrent runner for Behave",
    long_description=get_readme(),
    long_description_content_type='text/markdown',
    packages=[
        'paul6325106.behaveconcurrent'
    ],
    package_dir={'': 'src'},
    python_requires='>=3.10',
    install_requires=[
        'behave'
    ],
    extras_require={
        'test': [
            'pytest',
            'pytest-runner'
        ],
        'lint': [
            'mypy',
            'pycodestyle'
        ]
    },
    zip_safe=False
)

