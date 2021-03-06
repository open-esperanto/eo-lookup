Esperanto dictionary lookup tool
================================

This tool enables instant dictionary lookup for Esperanto words, simple, complex and
conjugated.

License
-------

Dictionary content provided by `Reta Vortaro <http://www.reta-vortaro.de/>`_ is not bundled, but
should be installed separately via the ``eo_lookup_revo`` package. This content is licenced under
the GPL which prohibits us from including it here.

Installation
------------

.. code-block:: bash

   pip install eo_lookup
   pip install eo_lookup_revo

Usage
-----

.. code-block:: python

   >>> from eo_lookup import Lookup
   >>> from eo_lookup_revo import get_content
   >>> LOOKUP = Lookup(get_content())
   >>> LOOKUP.lookup_html('grandpersonoj')
   '<strong>granda</strong>: large, <strong>persono</strong>: person, character'

Development
-----------

Requirements: Nix package manager. See ``default.nix`` for building instruction.

To publish:

.. code-block:: bash

    ./publish.sh eoLookupDist
    ./publish.sh eoLookupRevoDist


