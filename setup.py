from setuptools import setup, find_packages

setup(
    name='data-viz-toolkit',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'matplotlib',
        'pandas',
        'dash',
        'plotly',
        'fpdf'
    ],
    entry_points={
        'console_scripts': [
            'data-viz-toolkit=data_viz_toolkit.cli:main',
        ],
    },
)
