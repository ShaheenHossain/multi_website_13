.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://opensource.org/licenses/MIT
   :alt: License: MIT

=============================
 Website Switcher in Backend
=============================

Technical module to switch Websites in Backend similarly to Company Switcher. On changing it update field **backend_website_id** in ``res.users``.

website_dependent
=================

The module adds new field attribute ``website_dependent``, which is analog of ``company_dependent``, but for websites.

See `<models/test_website.py>`_ and `<tests/test_website_dependent.py>`_ to understand how it works.

If you need to convert existing field to a website-dependent field it's not
enough just to add the attributes. You need additional stuff to make your module
safely installable and uninstallable. See module
``ir_config_parameter_multi_company`` as an example. Things to do:

* extend ``ir.property``'s ``write`` to call ``_update_db_value_website_dependent``
* Add to the field both ``company_dependent=True`` and ``website_dependent=True``
* In the field's module extend following methods:

  * ``create`` -- call ``_force_default``
  * ``write`` -- call ``_update_properties_label``
  * ``_auto_init`` -- call ``_auto_init_website_dependent``

* In the field's module add ``uninstall_hook``:

  * remove field's properties

Roadmap
=======

* TODO: Use context on switching between websites to allow work with different
  websites at the same time by using different browser tabs. It also fixes
  problem of using superuser's configuration when ``sudo()`` is used.

* TODO: Since eagle 12, there is another switcher at ``[[ Website ]] >> Dashboard`` menu. It has to be syncronized with the switcher of this module, i.e. hide default one and use value of this module switcher.

Credits
=======

Contributors
------------
* `Ivan Yelizariev <https://it-projects.info/team/yelizariev>`__

Sponsors
--------
* `IT-Projects LLC <https://it-projects.info>`__

Maintainers
-----------
* `IT-Projects LLC <https://it-projects.info>`__

      To get a guaranteed support
      you are kindly requested to purchase the module 
      at `eagle apps store <https://apps.eagle.com/apps/modules/13.0/web_website/>`__.

      Thank you for understanding!

      `IT-Projects Team <https://www.it-projects.info/team>`__

Further information
===================

Demo: http://runbot.it-projects.info/demo/misc-addons/13.0

HTML Description: https://apps.eagle.com/apps/modules/13.0/web_website/

Usage instructions: `<doc/index.rst>`_

Changelog: `<doc/changelog.rst>`_

Notifications on updates: `via Atom <https://github.com/it-projects-llc/misc-addons/commits/13.0/web_website.atom>`_, `by Email <https://blogtrottr.com/?subscribe=https://github.com/it-projects-llc/misc-addons/commits/13.0/web_website.atom>`_

Tested on Eagle 13.0 8ebb5bdb4b63927a302f0d057b2f4db535d93829
