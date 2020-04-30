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
    age_status = fields.Char( # adicionado, removido.
        string="Status",
        required=True)

    @api.model
    def get_agent_data(self, payload):
        lista = []
        for attr in payload:
            # [word.lower() for word in s.split()]
            
            if attr["age_attribute"] == "Memória SLT1 Capacidade":
                age_attribute_value = str(int(int(attr["age_attribute_value"])/1073741824)) + "GB"

            elif attr["age_attribute"] == "Memória SLT1 Frequência":
                age_attribute_value = str(attr["age_attribute_value"]) + "MHz"

            elif attr["age_attribute"] == "Memória SLT2 Capacidade":
                age_attribute_value = str(int(int(attr["age_attribute_value"])/1073741824)) + "GB"

            elif attr["age_attribute"] == "Memória SLT2 Frequência":
                age_attribute_value = str(attr["age_attribute_value"]) + "MHz"

            elif attr["age_attribute"] == "Tela Marca":
                age_attribute_value = attr["age_attribute_value"].split('\\')[1][:-4]

            elif attr["age_attribute"] == "Tela Taxa de Atualização de Frame":
                age_attribute_value = str(attr["age_attribute_value"]) + "Hz"

            elif attr["age_attribute"] == "Placa de Vídeo Nvidia Memória Dedicada":
                # age_attribute_value = str(int(int(attr["age_attribute_value"])/1073741824)) + "GB"

                modelo = attr["age_attribute_value"]
                words = [word.lower() for word in modelo.split()]

                if ("geforce" and "gtx" and "1650") in words:
                    age_attribute_value = "4GB"

                elif ("geforce" and "gtx" and "1050") in words:
                    age_attribute_value = "3GB"

                elif ("geforce" and "gtx" and "1050") in words:
                    age_attribute_value = "3GB"

                elif ("geforce" and "gtx" and "1660TI") in words:
                    age_attribute_value = "6GB"

                elif ("geforce" and "rtx" and "2070" and "MAX-Q") in words:
                    age_attribute_value = "8GB"

                elif ("geforce" and "rtx" and "2060") in words:
                    age_attribute_value = "6GB"

                elif ("geforce" and "rtx" and "2070") in words:
                    age_attribute_value = "8GB"

                elif ("geforce" and "rtx" and "2080" and "MAX-Q") in words:
                    age_attribute_value = "8GB"

                else:
                    age_attribute_value = "NULL"
                #OBS: falta tratar o bug do uint32

            elif attr["age_attribute"] == "Placa de Vídeo Intel Memória Dedicada":
                age_attribute_value = str(int(int(attr["age_attribute_value"])/1073741824)) + "GB"

            elif attr["age_attribute"] == "Armazenamento SSD Capacidade":
                #age_attribute_value = str(int(int(attr["age_attribute_value"])/1073741824)) + "GB"
                capacidade = int(attr["age_attribute_value"])/1073741824
                if capacidade <= 500 and capacidade >= 400:
                    age_attribute_value = "500GB"
                elif capacidade <= 250 and capacidade >= 100:
                    age_attribute_value = "250GB"
                elif capacidade <= 1000 and capacidade > 750:
                    age_attribute_value = "1TB"
                elif capacidade <= 2000 and capacidade > 1750:
                    age_attribute_value = "2TB"
                else:
                    age_attribute_value = "NULL"

            elif attr["age_attribute"] == "Armazenamento HD Capacidade":
                capacidade = int(attr["age_attribute_value"])/1073741824
                if capacidade <= 500 and capacidade > 400:
                    age_attribute_value = "500GB"
                elif capacidade <= 250 and capacidade > 100:
                    age_attribute_value = "250GB"
                elif capacidade <= 1000 and capacidade > 750:
                    age_attribute_value = "1TB"
                elif capacidade <= 2000 and capacidade > 1750:
                    age_attribute_value = "2TB"
                else:
                    age_attribute_value = "NULL"

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

            elif attr["age_attribute"] == "Bios Data":
                #20190819000000.000000+000
                #\'%Y-%m-%d %H:%M:%S\'
                aux = attr["age_attribute_value"]
                ano = aux[0:4]
                mes = aux[4:6]
                dia = aux[6:8]
                age_attribute_value = ano + "-" + mes + "-" + dia

            else:
                age_attribute_value = attr["age_attribute_value"]

            domain = [
                ("name", "=", attr["name"]),
                ("age_deviceid", "=", attr["age_deviceid"]),
                ("age_attribute", "=", attr["age_attribute"]),
                ("age_attribute_value", "=", age_attribute_value),
                ]
            register_line = self.search(domain, limit=1)
            lista.append(register_line)
            # TODO: escrever no banco por CR
            # if register_line:
            #     date = attr["age_last_check"]
                # register_line.sudo().write({"age_last_check": date})
                # componente já existente
            if not(register_line):
                if age_attribute_value == False:
                    age_attribute_value = "NULL"
                vals = {
                    'name': attr["name"],
                    'age_deviceid': attr['age_deviceid'],
                    'age_attribute': attr['age_attribute'],
                    'age_attribute_value': age_attribute_value,
                    'age_register_date': attr['age_register_date'],
                    # 'age_last_check': attr['age_last_check'],
                    'age_status': 'Adicionado'}
                # componente adicionado
                register_line = self.search([("name", "=", attr["name"]), ("age_attribute", "=", attr['age_attribute'])], limit=1)
                if register_line:
                    register_line.sudo().write({"age_status": "Trocado"})
                self.sudo().create(vals)

            register_agent = self.search([("name", "=", attr["name"])])
            for register in register_agent:
                if register["age_deviceid"] == attr["age_deviceid"]:
                    register.sudo().write({"age_status": "Existe"})
            # componente removido/inativo

        #começa aqui
        return lista
