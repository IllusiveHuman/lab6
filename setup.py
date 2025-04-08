from setuptools import setup, find_packages

setup(
    name="calculator",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "tkinter"  
    ],
    entry_points={
        "gui_scripts": [
            "calculator=main:main"
        ]
    },
    author="Ілля_Новіков",
    description="Простой графический калькулятор на Tkinter",
)
