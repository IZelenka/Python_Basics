# Code Organisation

**Currently meant only as a demo**, but you can try the commands and observe their results on your own.

## Wheel

```sh
# magic, don't worry, we will get to it next lecture
python -m venv venv
source venv/bin/activate


python -m pip install build
# install build package
python -m build -w

# install package via wheel
python -m pip install dist/demo_package-0.1-py3-none-any.whl

# try import the following
python -c "import demo_package.my_lib; print('import worked successfully')"

#  try failed import
python -c "import demo_package.my_lib2; print('import did not work and this message does not print')"

# try call function
python -c "from demo_package.my_lib import my_function; my_function()"

# run package's __main__.py
python -m demo_package

# run module
python -m demo_package.my_lib

# clean up
deactivate
rm -rf venv
```

## Source

Try the same commands with source distribution.

```sh
python -m venv venv
source venv/bin/activate

python -m pip install build

# build as a source
python -m build -s

# install package via wheel
python -m pip install dist/demo_package-0.1.tar.gz

# try import the following
python -c "import demo_package.my_lib; print('import worked successfully')"

#  try failed import
python -c "import demo_package.my_lib2; print('import did not work and this message does not print')"

# try call function
python -c "from demo_package.my_lib import my_function; my_function()"

# run package's __main__.py
python -m demo_package

# run module
python -m demo_package.my_lib

# clean up
deactivate
rm -rf venv
```