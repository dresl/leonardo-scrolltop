
====================
Leonardo ScrollTop Widgets
====================

Leonardo ScrollTop allows to scroll up if you are at the bottom of page.

.. contents::
    :local:

Installation
------------

.. code-block:: bash

    pip install -e git+https://github.com/dresl/leonardo-scrolltop.git@#egg=leonardo_scrolltop


Add ``leonardo_scrolltop`` to APPS list, in the ``local_settings.py``::

    APPS = [
        ...
        'leonardo_scrolltop'
        ...
    ]

Load new template to db

.. code-block:: bash

    python manage.py sync_all -f

Read More
---------

* https://github.com/django-leonardo
