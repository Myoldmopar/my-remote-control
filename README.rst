My Remote Control
=================

This repo is the Django-backed, Angular-fronted website for my beast's remote control.
Honestly, this is mostly just an exercise in refining my web skills, but will make a nice site/app anyway.

Documentation |docimage|_
-------------------------

Documentation is hosted on `ReadTheDocs <http://solar-calculations.readthedocs.org/en/latest>`__.
To build the documentation, enter the docs/ subdirectory and execute `make html`; then open `/docs/_build/html/index.html` to see the documentation.
The API also has built in Swagger documentation, at the `/swagger/` endpoint.

Testing |tstimage|_ |covimage|_
-------------------------------

For the testing that is performed, tests are based on Django's test framework (unittest). To find and execute all
the unit tests, just execute ``python manage.py test``. The tests are automatically executed by `Travis
CI <https://travis-ci.org/myoldmopar/my-remote-control>`__.

After testing is complete, the code coverage status for those tests are tracked on
`Coveralls <https://coveralls.io/github/myoldmopar/my-remote-control?branch=master>`__.
If you look very closely at the code coverage, you'll see it's not great.  There are a lot of pieces ignored.
This has to do with how this application is based on media/volume controls, which don't exist on CI images.
The Linux kernel used by Travis does not include full ALSA mixer support, and xdotool won't properly simulate without a display.
I can test the successful code paths locally; I can test the unsuccessful code paths on CI; but not both in any one spot.
So I test as best I can and then I don't worry about it anymore.  Occasionally I will try to loosen the ignored coverage
and see if I can gain more real coverage.

.. |tstimage| image:: https://travis-ci.org/Myoldmopar/my-remote-control.svg?branch=master
.. _tstimage: https://travis-ci.org/Myoldmopar/my-remote-control

.. |covimage| image:: https://coveralls.io/repos/github/Myoldmopar/my-remote-control/badge.svg?branch=master
.. _covimage: https://coveralls.io/github/Myoldmopar/my-remote-control?branch=master

.. |docimage| image:: https://readthedocs.org/projects/solar-calculations/badge/?version=latest
.. _docimage: http://solar-calculations.readthedocs.org/en/latest/
