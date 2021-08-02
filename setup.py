import os
import pkg_resources
from setuptools import setup, find_packages

setup(
    name='ufo101TamingTransformers',
    version='0.0.1',
    description='Taming Transformers for High-Resolution Image Synthesis',
    packages=find_packages(include=['ufo101TamingTransformers', 'ufo101TamingTransformers.*']),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
)
