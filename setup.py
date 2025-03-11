from setuptools import setup, find_packages

setup(
    name='network-traffic-analyzer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'scapy',
        'numpy',
        'scikit-learn',
    ],
    entry_points={
        'console_scripts': [
            'network-traffic-analyzer=network_traffic_analyzer:main',
        ],
    },
)