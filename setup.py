from setuptools import find_packages, setup

readme = open("./README.md", "r")


setup(
    name='calor_pared_compuesta_lineal',
    packages=['calor_pared_compuesta_lineal'],  # this must be the same as the name above
    version='0.0.1',
    description='Esta es la descripcion de mi paquete',
    long_description=readme.read(),
    long_description_content_type='text/markdown',
    author='Valentina Argüellez Angulo',
    author_email='valentina.arguellez@gmail.com',
    # use the URL to the github repo
    url='https://github.com/Valarg0502/calor_pared_compuesta_lineal',
    download_url='https://github.com/Valarg0502/calor_pared_compuesta_lineal/tarball/0.0.1',
    keywords=['transferencia de calor', 'pared compuesta', 'termodinamica'],
    classifiers=[ ],
    install_requires=[
        'numpy',
        'matplotlib'
    ],
    license='MIT',
    packages=find_packages(),
    include_package_data=True

)