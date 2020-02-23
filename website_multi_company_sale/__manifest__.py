# Copyright 2017-2018 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# Copyright 2018 Ilmir Karamov <https://it-projects.info/team/ilmir-k>
# Copyright 2018 Ildar Nasyrov <https://it-projects.info/team/iledarn>
# Copyright 2019 Kolushov Alexandr <https://it-projects.info/team/KolushovAlexandr>
# License MIT (https://opensource.org/licenses/MIT).
{
    "name": """Multi Ecommerce""",
    "summary": """Multi Website support in eCommerce""",
    "category": "eCommerce",
    # "live_test_url": "http://apps.it-projects.info/shop/product/website-multi-company?version=12.0",
    "images": ["images/website_multi_company_sale_main.png"],
    "version": "13.0.1.5.2",
    "application": False,
    "author": "IT-Projects LLC, Ivan Yelizariev",
    "support": "apps@itpp.dev",
    "website": "https://it-projects.info/team/yelizariev",
    "license": "Other OSI approved licence",  # MIT
    "price": 9.00,
    "currency": "EUR",
    "depends": ["website_multi_company", "website_sale", "ir_rule_website"],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/product_public_category_views.xml",
        "views/res_config_views.xml",
        "views/product_template_views.xml",
        "views/payment_views.xml",
        "views/sale_views.xml",
        "security/website_multi_company_sale_security.xml",
    ],
    "qweb": [],
    "demo": [],
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,
    "auto_install": False,
    "installable": False,
}
