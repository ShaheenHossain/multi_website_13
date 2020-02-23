===========================
 Multiwebsite in Sec.Rules
===========================

Allows to use ``website_id`` (current website) in ``domain_force`` field of Record Rules (``ir.rule``), e.g.:

* ``[('website_ids', 'in', [website_id])]``
* ``[('website_id', '=', website_id)]``


Example of usage:

* Show a blog on specific websites only (TODO: add link to the module)
* Show an event on specific websites only (TODO: add link to the module)
* Show a product on specific websites only (TODO: add link to the module)

Known issues
============

* This module redefines ``ir.rule`` ``_compute_domain`` base method and may be not compatible with others that redefine the method too.

Eagle 13.0+
==========

We hope this feature will be built-in since Eagle 13.0 at least: https://github.com/eagle/eagle/pull/22743

Credits
=======

Contributors
------------
* `Ivan Yelizariev <https://www.it-projects.info/team/yelizariev>`__
* `Ildar Nasyrov <https://www.it-projects.info/team/iledarn>`__

Sponsors
--------
* `IT-Projects LLC <https://it-projects.info>`__

Maintainers
-----------
* `IT-Projects LLC <https://it-projects.info>`__

      To get a guaranteed support you are kindly requested to purchase the module at `eagle apps store <https://apps.eagle.com/apps/modules/13.0/ir_rule_website/>`__.

      Thank you for understanding!

      `IT-Projects Team <https://www.it-projects.info/team>`__

Further information
===================

Demo: http://runbot.it-projects.info/demo/access-addons/13.0

HTML Description: https://apps.eagle.com/apps/modules/13.0/ir_rule_website

Usage instructions: `<doc/index.rst>`_

Changelog: `<doc/changelog.rst>`_

Tested on Eagle 12.0 0669eddc7e88303f3a97e9f4f834f64fd9a8158c
