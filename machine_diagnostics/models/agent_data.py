from odoo import fields, models, api


class AgentData(models.Model):
    _name = "agent.data"
    _description = "Dados do Agente"

    name = fields.Char(
        string="Número de Série",
        required=True)
    age_deviceid = fields.Char(
        string="ID Componente",
        required=True)
    age_attribute = fields.Char(
        string="Atributo",
        required=True)
    age_attribute_value = fields.Char(
        string="Valor Atributo",
        required=True)
    age_register_date = fields.Datetime(
        string="Data Cadastro",
        required=True)
    age_last_check = fields.Datetime(
        string="Última Verificação",
        required=True)

    @api.model
    def get_agent_data(self, payload):
        for attr in payload:

            if attr["age_attribute"] == "Memória SLT1 Capacidade":
                age_attribute_value = str(int(attr["age_attribute_value"])/1073741824) + "Gb"

            elif attr["age_attribute"] == "Memoria SLT1 Frequência":
                age_attribute_value = str(attr["age_attribute_value"]) + "Mhz"

            elif attr["age_attribute"] == "Memória SLT2 Capacidade":
                age_attribute_value = str(int(attr["age_attribute_value"])/1073741824) + "Gb"

            elif attr["age_attribute"] == "Memoria SLT2 Frequência":
                age_attribute_value = str(attr["age_attribute_value"]) + "Mhz"

            elif attr["age_attribute"] == "Tela Marca":
                lista = attr["age_attribute_value"].split('\\')[1][:-4]
                age_attribute_value = lista[1][:-4]

            elif attr["age_attribute"] == "Tela Taxa de Atualização de Frame":
                age_attribute_value = str(attr["age_attribute_value"]) + "Hz"

            elif attr["age_attribute"] == "Placa de Vídeo Intel Memória Dedicada":
                age_attribute_value = str(int(attr["age_attribute_value"])/1073741824) + "Gb"

            #else if attr["age_attribute"] == "Placa de Vídeo Nvidia Memória Dedicada":
            #    age_attribute_value = str(int(attr["age_attribute_value"])/1073741824) + "G"
            #OBS: falta tratar o bug do uint32

            elif attr["age_attribute"] == "Armazenamento SSD Capacidade":
                age_attribute_value = str(int(attr["age_attribute_value"])/1073741824) + "Gb"

            elif attr["age_attribute"] == "Armazenamento HD Capacidade":
                age_attribute_value = str(int(attr["age_attribute_value"])/1073741824) + "Gb"

            elif attr["age_attribute"] == "Teclado Referência":
                if attr["age_attribute_value"] == "00010416":
                    age_attribute_value = "Portuguese (Brazilian ABNT2)"
                elif attr["age_attribute_value"] == "00000416":
                    age_attribute_value = "Portuguese (Brazilian ABNT)"
                elif attr["age_attribute_value"] == "00000409":
                    age_attribute_value = "United States - English"
                elif attr["age_attribute_value"] == "00020409":
                    age_attribute_value = "United States - International"

            elif attr["age_attribute"] == "Wireless Modelo":
                lista = attr["age_attribute_value"].split('] ')
                lista.pop(0)
                age_attribute_value = ''.join(lista)

            else:
                age_attribute_value = attr["age_attribute_value"]

            domain = [
                ("name", "=", attr["name"]),
                ("age_deviceid", "=", attr["age_deviceid"]),
                ("age_attribute", "=", attr["age_attribute"]),
                ("age_attribute_value", "=", age_attribute_value),
                ]
            register_line = self.search(domain, limit=1)

            # TODO: escrever no banco por CR
            if register_line:
                date = attr["age_last_check"]
                register_line.sudo().write({"age_last_check": date})
            else:
                vals = {
                    'name': attr["name"],
                    'age_deviceid': attr['age_deviceid'],
                    'age_attribute': attr['age_attribute'],
                    'age_attribute_value': age_attribute_value,
                    'age_register_date': attr['age_register_date'],
                    'age_last_check': attr['age_last_check']}
                self.sudo().create(vals)
        return True
