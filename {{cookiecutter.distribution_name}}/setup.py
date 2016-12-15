from setuptools import setup, find_packages
import re
import ast

# version parsing from __init__ pulled from Flask's setup.py
# https://github.com/mitsuhiko/flask/blob/master/setup.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('{{cookiecutter.package_name}}/__init__.py', 'rb') as f:
    hit = _version_re.search(f.read().decode('utf-8')).group(1)
    version = str(ast.literal_eval(hit))


# NOTE: If you are testing your plugin with `q2cli` (i.e. the `qiime` command)
# while you are developing it, you'll need to run `qiime dev refresh-cache` to
# see the latest changes to your plugin reflected in the CLI. You'll need to
# run this command anytime you modify your plugin's interface (e.g.
# add/rename/remove a command or its inputs/parameters/outputs).
#
# Another option is to set the environment variable `Q2CLIDEV=1` so that the
# cache is refreshed every time a command is run. This will slow down the CLI
# while developing because refreshing the cache is slow. However, the CLI is
# much faster when a user installs release versions of QIIME 2 and plugins, so
# this slowdown should only be apparent when *developing* a plugin.
#
# This manual refreshing of the `q2cli` cache is necessary because it can't
# detect when changes are made to a plugin's code while under development (the
# plugin's version remains the same across code edits). This manual refreshing
# of the cache should only be necessary while developing a plugin; when users
# install QIIME 2 and your released plugin (i.e. no longer in development), the
# cache will automatically be updated when necessary.
setup(
    name="{{cookiecutter.distribution_name}}",
    version=version,
    packages=find_packages(),
    # pandas, q2templates and q2-dummy-types are only required for the dummy
    # methods and visualizers provided as examples. Remove these dependencies
    # when you're ready to develop your plugin, and add your own dependencies
    # (if there are any).
    install_requires=['qiime >= 2.0.6', 'pandas', 'q2-dummy-types >= 0.0.6',
                      'q2templates >= 0.0.6'],
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.email}}",
    description="{{cookiecutter.description}}",
    entry_points={
        "qiime.plugins":
        ["{{cookiecutter.distribution_name}}={{cookiecutter.package_name}}.plugin_setup:plugin"]
    },
    # If you are creating a visualizer, all template assets must be included in
    # the package source, if you are not using q2templates this can be removed
    package_data={
        "{{cookiecutter.package_name}}": ["assets/index.html"]
    }
)
