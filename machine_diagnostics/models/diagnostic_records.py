
from odoo import api, fields, models


class DiagnosticRecords(models.Model):
    _name = "diagnostic.records"
    _description = "Registros de Prontuário"

    name = fields.Char(
        string="Número de Série", )
    diagrec_deviceid = fields.Char(
        string="ID Modelo", )
    diagrec_component = fields.Char(
        string="Componente", )
    diagrec_property = fields.Char(
        string="Propriedade", )
    diagrec_property_value = fields.Char(
        string="Descrição", )
    diagrec_register_date = fields.Datetime(
        string="Data Cadastro")
    diagrec_status = fields.Char( # adicionado, removido.
        string="Status")

    #agent_data_id = fields.Many2one(
    #    string="Agent Data",
    #    comodel_name="agent.data", )


    # diagrec_product = fields.Many2one(
    #     string="Produto",
    #     comodel_name="product.product",
    #     # domain="[('name', 'like', notebook)]",
    #     ondelete="set null")
