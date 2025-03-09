from setuptools import setup, find_packages

setup(
    name='network-traffic-analysis',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask==1.1.2',
        'Flask-SQLAlchemy==2.4.4',
        'Flask-Migrate==2.5.3',
        'Flask-OAuthlib==0.9.5',
        'psycopg2-binary==2.8.6',
        'scikit-learn==0.24.1',
        'pandas==1.2.3',
        'numpy==1.20.1',
        'pcapkit==0.15.5',
    ],
)