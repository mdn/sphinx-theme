Mozilla Developer Network Sphinx Theme
======================================

This is a version of the Mozilla Developer Network theme, for
the `Sphinx documentation engine`_. It is used for the
`Kuma development documentation`_.

Here is how I use it
--------------------

To use it, you need to clone it somewhere in your Sphinx's architecture::

    $ pip install mdn-sphinx-theme

and to configure Sphinx to use it. In your `conf.py` file::

    import mdn_theme

    html_theme_path = [mdn_theme.get_theme_dir()]
    html_theme = 'mdn'

Take care and remove the `pygments_style` configuration, as it may not be of
the better taste with the mozilla's theme.

Any contributions are of course welcome!

Readthedocs
-----------

Add a pip requirements file to your project and have the following
packages listed there::

    Sphinx
    mdn-sphinx-theme

Then configure your Readthedocs project to use that requirement file
before rendering your project's documentation.

.. _`Sphinx documentation engine`: http://www.sphinx-doc.org/en/stable/
.. _`Kuma development documentation`: https://kuma.readthedocs.io/en/latest/
