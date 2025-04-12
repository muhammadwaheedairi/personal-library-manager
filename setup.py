# setup.py

from setuptools import setup, find_packages

setup(
    name="personal-library-manager",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],  # List external dependencies if any
    entry_points={
        'console_scripts': [
            'library-manager = personal_library_manager.cli:main_menu',
        ],
    },
    author="Your Name",
    author_email="your_email@example.com",
    description="A CLI app to manage your personal book collection",
    long_description=open('README.md', encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/personal-library-manager",  # Change to your repo URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
