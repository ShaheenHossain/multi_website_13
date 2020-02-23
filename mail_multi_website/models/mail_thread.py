# Copyright 2018 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# License MIT (https://opensource.org/licenses/MIT).
from eagle import api, models, tools


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"

    @api.model
    def message_route_process(self, message, message_dict, routes):
        rcpt_tos = ",".join(
            [
                tools.decode_message_header(message, "Delivered-To"),
                tools.decode_message_header(message, "To"),
                tools.decode_message_header(message, "Cc"),
                tools.decode_message_header(message, "Resent-To"),
                tools.decode_message_header(message, "Resent-Cc"),
            ]
        )
        rcpt_tos_websiteparts = [
            e.split("@")[1].lower() for e in tools.email_split(rcpt_tos)
        ]
        website = (
            self.env["website"].sudo().search([("domain", "in", rcpt_tos_websiteparts)])
        )
        if website:
            self = self.with_context(website_id=website[0].id)

        return super(MailThread, self).message_route_process(
            message, message_dict, routes
        )
