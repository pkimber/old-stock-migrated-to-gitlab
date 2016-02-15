Stock
*****

Django application for stock management (products etc).

Install
=======

Virtual Environment
-------------------

::

  virtualenv --python=python3.4 venv-stock
  source venv-stock/bin/activate
  pip install --upgrade pip

  pip install -r requirements/local.txt

Testing
=======

::

  find . -name '*.pyc' -delete
  py.test -x

Usage
=====

::

  ./init_dev.sh

Release
=======

https://www.kbsoftware.co.uk/docs/
