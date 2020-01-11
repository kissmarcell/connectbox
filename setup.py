from setuptools import setup
setup(
    name="connectbox",
    version="0.1",
    author="Marcell Kiss",
    author_email="info@kmarcell.com",
    description=("Compal Router CH7465LG Python Interface"),
    keywords="compal CH7465LG interface",
    license="GPL",

    packages=["connectbox"],
    install_requires=['requests'],

    zip_safe=False
)