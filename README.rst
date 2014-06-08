Stock
*****

Django application for an stock management (products etc).

Install
=======

Virtual Environment
-------------------

::

  pyvenv-3.4 --without-pip venv-stock
  source venv-stock/bin/activate
  wget https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py
  python get-pip.py

  pip install -r requirements/local.txt

Testing
=======

::

  find . -name '*.pyc' -delete
  py.test -x

Usage
=====

::

  py.test -x && \
      touch temp.db && rm temp.db && \
      django-admin.py syncdb --noinput && \
      django-admin.py migrate --all --noinput && \
      django-admin.py demo_data_login && \
      django-admin.py init_app_stock && \
      django-admin.py demo_data_stock && \
      django-admin.py runserver

Release
=======

https://django-dev-and-deploy-using-salt.readthedocs.org/
