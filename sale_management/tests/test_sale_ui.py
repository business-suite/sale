import odoo.tests



@odoo.tests.tagged('post_install', '-at_install')
class TestUi(odoo.tests.HttpCase):

    def test_01_sale_tour(self):
        self.start_tour("/web", 'sale_tour', login="admin", step_delay=100)
