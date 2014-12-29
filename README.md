# Test toolkit

A toolkit for CSS used across multiple projects.

## Generating the documentation pages

The documentation pages, kept on github as github pages, can be generated using a few commands.

### Requirements

- Python
- [PIP](https://pip.pypa.io/en/latest/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/)

### Set up a virtualenv

To set up an isolated environment for the project, run this command.

```
virtualenv ~/Envs/test_toolkit
```

Note: you can set the virtualenv to any location on your system.

### Install the dependancies

```
pip install -r requirements.txt
```

### Generate the pages

```
python publish-gh-page.py
```
