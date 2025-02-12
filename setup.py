from setuptools import setup, find_packages

setup(
    name='eye_tracking_analysis',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scipy',
        'matplotlib',
        'seaborn'
    ],
    entry_points={
        'console_scripts': [
            'eye_tracking_analysis=eye_tracking_analysis.cli:main',
        ],
    },
)
