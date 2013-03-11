Introduction
============

This addon register webshims_ to Plone resource registry.

version: 1.9.7

About webshims
==============

Webshims Lib is a modular capability-based polyfill-loading
library, which focuses on accurate implementations of stable
HTML5 features, so that developers can write modern,
interoperable and robust code in all browsers.

It is built on top of jQuery and Modernizr.

List of features:

* json-storage
* es5
* geolocation
* canvas
* forms
* forms-ext
* mediaelement
* track
* details

How to install
==============

This addon can be installed has any other addons. please follow official
documentation_

Dependencies
------------

* collective.js.jqueryui
* plone.app.jquery
* plone.app.modernizr

Custom Modernizr build
----------------------

Webshims lib does not need every Modernizr test and supports creating a
`custom Modernizr build`_.

Webshims lib uses requireJS as a script loader, if this is included, if not
it uses Modernizr.load/yepnope.

This addon override plone.app.modernizr.custom.js resource using this one.
If you have conflict with an other addon which does the same, you can use
@@plone.app.modernizr.download view to build a new one with all requested
features.

How to upgrade
==============

Download last tag zip from https://github.com/aFarkas/webshim

unzip and copy all resources of 'demos/js-webshim/minified' in
'collective.js.webshims/collective/js/webshims/resources/js'

Credits
=======

Companies
---------

* `Planet Makina Corpus <http://www.makina-corpus.org>`_
* `Contact Makina Corpus <mailto:python@makina-corpus.org>`_

People
------

- JeanMichel FRANCOIS aka toutpt <toutpt@gmail.com>

.. _documentation: http://plone.org/documentation/kb/installing-add-ons-quick-how-to
.. _webshims: http://afarkas.github.com/webshim
.. _`custom Modernizr build`: http://modernizr.com/download/#-canvas-audio-video-input-inputtypes-localstorage-sessionstorage-geolocation-shiv-cssclasses-addtest-prefixed-testprop-testallprops-prefixes-domprefixes-elem_track-load
