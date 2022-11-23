from distutils.core import setup
setup(
  name = 'PyDaCo',         # How you named your package folder (MyLib)
  packages = ['PyDaCo'],   # Chose the same as "name"
  version = '0.1.1',      # Start with a small number and increase it with every change you make
  license = 'MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'PyDaCo is a Python package for easy use of dictionaries and lists.',   # Give a short description about your library
  author = 'Mücahit Yusuf Yasin Gündüz',                   # Type in your name
  author_email = 'myygunduz@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/myygunduz/PyDaCo',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/myygunduz/PyDaCo/archive/refs/tags/0.1.0.tar.gz',    # I explain this later on
  keywords = ['Python', 'dictionary', 'list'],   # Keywords that define your package best
  install_requires = ["typing"],
  classifiers = [
    "Programming Language :: Python :: 3.8",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Natural Language :: English",
    "Development Status :: 4 - Beta",
    "Topic :: Software Development :: Libraries :: Python Modules",
  ],
)