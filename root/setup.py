from setuptools import setup, find_packages

setup(
    name="your_package_name",  # Replace with your package name
    version="0.0.1",  # Initial version
    author="Mladen Blizanac, Petar Popov",
    author_email="mladenblizanac@gmail.com",
    description="Projekat iz predmeta Teorija igraca",
    long_description=open("README.md").read(),  # Make sure README.md exists in your project root
    long_description_content_type="text/markdown",
    url="https://github.com/blizanac76/gametheory-faks",  # URL to the project (e.g., GitHub link)
    packages=find_packages(),  # Automatically find sub-packages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Replace with appropriate license
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Specify the minimum Python version required
    install_requires=[
        # List your project's dependencies here, e.g.:
        # 'requests>=2.20.0',
        # 'numpy>=1.18.0'
    ],
    entry_points={
        "console_scripts": [
            # Uncomment and edit the line below to create a command-line tool from a Python file
            # "your-command-name=your_package_name.your_module:main_function",
        ],
    },
    include_package_data=True,  # Include data files from MANIFEST.in
)
