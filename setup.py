from distutils.core import setup
setup(
    name = 'Esse3Api',
    packages = ['Esse3Api'],
    version = '1.0',
    license = 'MIT',
    description = 'A python library to query and interact with Cineca\'s ESSE3 REST API',
    author = 'Lorenzo Leonardini',
    author_email = 'lorenzo@leonardini.dev',
    url = 'https://github.com/LorenzoLeonardini/Esse3Api',
    download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
    keywords = ['CINECA', 'ESSE3', 'UNIVERSITY'],
    install_requires = [
        'requests',
        'json',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
