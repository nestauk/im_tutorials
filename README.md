Innovation Mapping Tutorials 
============================

Welcome to Nesta's Innovation Mapping tutorial repository! :books:

## Introduction

Here you will find materials and information for Innovation Mapping tutorials, as well as data dictionaries and participation information for live events and workshops that we run.

The tutorials in this repository cover practical implementations of data science techniques including data collection, machine learning, natural language processing, network science and data visualisation that we use in our work here in the [Innovation Mapping](https://www.nesta.org.uk/project/innovation-mapping/) team at [Nesta](https://www.nesta.org.uk/). There are also tutorials on applications of these methods to answer innovation mapping questions.

## Tutorials

The tutorials are in notebook form and can be found in `im_tutorials/notebooks/`. They are designed to run locally or on cloud hosted notebook platforms. Each notebook begins with a preamble that installs the `im_tutorials` package from this repository:

```
!pip install git+https://github.com/nestauk/im_tutorials.git
```

This package mainly contains useful utility functions for accessing data.

## Data

For Innovation Mapping events, open datasets are made available to download or pull in to notebooks directly. This can be done easily using functions available in the `im_tutorials` package, which load data straight into Pandas DataFrames. For example, if we want to load projects from Gateway to Research, we can simply do:

```python
from im_tutorials.data.gtr import gtr_table
gtr_projects_df = gtr_table('projects')
```

More information on the datasets available and how to access them can be found in the [data dictionaries](https://github.com/nestauk/im_tutorials/tree/master/data).

## Partners

Most of the notebooks here have been created by people from Nesta, but we are fortunate enough to have partnered with other organisations who have also contributed tutorials. They are:

- [Alan Turing Institute](https://www.turing.ac.uk/)
- [Office for National Statistics](https://www.ons.gov.uk/)
