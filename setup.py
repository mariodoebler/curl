from setuptools import find_packages, setup

setup(
    name='curl',
    packages=find_packages(),
    version='0.1',
    # license='MIT',
    description='Curl',
    author='Michael Laskin',
    # author_email = 'lucidrains@gmail.com',
    url='https://github.com/MishaLaskin/curl',
    keywords=['self-supervised learning', 'artificial intelligence'],
    install_requires=[
        # 'torch>=1.6',
        # 'kornia>=0.4.0'
    ],
    classifiers=[
        # 'Development Status :: 4 - Beta',
        # 'Intended Audience :: Developers',
        # 'Topic :: Scientific/Engineering :: Artificial Intelligence',
        # 'License :: OSI Approved :: MIT License',
        # 'Programming Language :: Python :: 3.6',
    ],
)
