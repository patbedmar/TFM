from setuptools import setup, find_packages

setup(
    name='traductor_sdh',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'scikit-learn',
        'sentence-transformers',
        'openpyxl'
    ],
    author='Tu Nombre',
    author_email='tuemail@example.com',
    description='Librería para traducir y detectar determinantes sociales de la salud (SDH)',
    long_description='Traduce y encuentra similitudes entre textos y un diccionario SDH personalizado.',
    long_description_content_type='text/markdown',
    url='https://github.com/patbedmar/traductor_sdh',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
