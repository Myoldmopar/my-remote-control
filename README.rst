My Remote Control
=================

This repo is the Django-backed, Angular-fronted website for my beast's remote control.
Honestly, this is mostly just an exercise in refining my web skills, but will make a nice site/app anyway.

Testing |tstimage|_
-------------------

The source is tested using Django's test framework (based on unittest). To find and execute all
the unit tests, just execute ``python manage.py test``. The tests are automatically executed by `Travis
CI <https://travis-ci.org/myoldmopar/my-remote-control>`__. There is a problem though.  The Linux kernel used
by Travis does not include full ALSA mixer support.  So even though I can pip install and import the alsa audio
Python bindings, it fails to instantiate a volume mixer, and surely won't be able to do any media key support.
So until I think of a good solution, the tests must be run locally only.  Right now the tests that will fail
are going to configured with a skip-if so they won't run on Travis.

Code Coverage |covimage|_
-------------------------

After testing is complete, the code coverage status for those tests are tracked on
`Coveralls <https://coveralls.io/github/myoldmopar/my-remote-control?branch=master>`__.

.. |tstimage| image:: https://travis-ci.org/Myoldmopar/my-remote-control.svg?branch=master
.. _tstimage: https://travis-ci.org/Myoldmopar/my-remote-control

.. |covimage| image:: https://coveralls.io/repos/github/Myoldmopar/my-remote-control/badge.svg?branch=master
.. _covimage: https://coveralls.io/github/Myoldmopar/my-remote-control?branch=master
