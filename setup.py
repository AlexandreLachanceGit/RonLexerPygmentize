from setuptools import setup

setup(
    name='ronlexer',
    version='0.1',
    packages=['ronlexer'],
    entry_points={
        'pygments.lexers': [
            'ron = ronlexer.ronlexer:RONLexer',
        ],
    },
    install_requires=[
        'pygments',
    ],
)

