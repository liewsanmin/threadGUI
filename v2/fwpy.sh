WXPYTHON_APP="main_1.py"
PYVER=2.7

if [ -z "$VIRTUAL_ENV" ] ; then
    echo "You must activate your virtualenv: set '$VIRTUAL_ENV'"
    exit 1
fi

SYSTEM_FRAMEWORK_PYTHON_ROOT="/Library/Frameworks/Python.framework/Versions/$PYVER"
# OS X 10.10
SYSTEM_FRAMEWORK_PYTHON_ROOT="/System$SYSTEM_FRAMEWORK_PYTHON_ROOT"

#PYSUBVER="$(python --version 2>&1 | cut -d ' ' -f2)"  # e.g., 2.7.10
PYSUBVER="2.7.11"  # e.g., 2.7.10
BREW_PYTHON_ROOT="$(brew --prefix)/Cellar/python/$PYSUBVER/Frameworks/Python.framework/Versions/$PYVER"

PYTHON_BINARY="bin/python$PYVER"
#FRAMEWORK_PYTHON="$SYSTEM_FRAMEWORK_PYTHON_ROOT/$PYTHON_BINARY"

FRAMEWORK_PYTHON="$BREW_PYTHON_ROOT/$PYTHON_BINARY"

VENV_SITE_PACKAGES="$VIRTUAL_ENV/lib/python$PYVER/site-packages"

# Ensure wx.pth is set up in the virtualenv
cp "/Users/sanmin/Desktop/Jobs/Companies/advancedBionic/$WXPYTHON_APP" "$VENV_SITE_PACKAGES/"

# Use the Framework Python to run the app
export PYTHONHOME=$VIRTUAL_ENV
exec "$FRAMEWORK_PYTHON" "$VENV_SITE_PACKAGES/$WXPYTHON_APP" $*