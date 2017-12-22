Usage
=====

.. code-block::

   >>> from eo_lookup import Lookup
   >>> from eo_lookup_revo import get_content
   >>> LOOKUP = Lookup(get_content())
   >>> LOOKUP.lookup_html('grandpersonoj')
   '<strong>granda</strong>: large, <strong>persono</strong>: person, character'

License
-------

Dictionary content provided by [Reta Vortaro](http://www.reta-vortaro.de/) is not bundled, but
should be installed separately via the eo_lookup_revo package. This content is licenced under the
GPL which prohibits us from including it here.
