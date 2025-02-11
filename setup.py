# setup.py
from setuptools import setup, find_packages

setup(
    name='battery_monitor',
    version='0.1.0',  # Replace with your actual version number
    packages=find_packages(where='src'),  # Find packages in the 'src' directory
    package_dir={'': 'src'}, # Map the root package to the 'src' directory
    install_requires=[    # Dependencies from requirements.txt
        'PyQt6',
        'psutil',
        'PyQt6-Qt6'  # Include PyQt6-Qt6
    ],
    entry_points={
        'console_scripts': [
            #  'gui_scripts': [ # Use this instead of 'console_scripts' for a GUI app *without* a console window
            'battery_monitor = battery_monitor.main:main',  # Create a command-line entry point
        ],
    },

    # Optional: Add data files (like the icon)
    include_package_data=True,  # Important for including non-Python files

    # Metadata (optional, but good practice)
    author='Your Name',
    author_email='your.email@example.com',
    description='A PyQt6-based battery monitor application.',
    long_description=open('README.md').read(),  # Read from your README.md
    long_description_content_type='text/markdown', # Specify Markdown format
    url='https://github.com/yourusername/your-repo',  # Replace with your project's URL
    license='MIT',  # Replace with your chosen license
    classifiers=[  # Classifiers help users find your project on PyPI
        'Development Status :: 3 - Alpha',  # Or '4 - Beta', '5 - Production/Stable'
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',  # Use the correct license identifier
        'Operating System :: OS Independent', # Important for cross-platform
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: System :: Monitoring',
    ],
)