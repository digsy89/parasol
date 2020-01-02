import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="parasol-nlp",
  description="Korean tokenizer with charactor decomposition",
  long_description=long_description,
  long_description_content_type="text/markdown",
  keywords="hangul korean nlp tokenizer",

  version="0.0.1",

  author="Keeho Ahn",
  author_email="digsy89@gmail.com",

  project_urls={
    "Source": "https://github.com/digsy89/parasol",
  },

  python_requires=">=3.6",
  install_requires= ["hgtk", "transitions", "sentencepiece", "importlib-resources"],

  packages=setuptools.find_packages(),
  package_data={
    "": ["*.model", "*.vocab"],
  },
  classifiers=[
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: OS Independent",
    "Topic :: Text Processing"
  ],
)
