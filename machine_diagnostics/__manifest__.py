{   # pylint: disable=C8101,C8103
    'name': "Prontuário de Notebooks",

    'summary': "Gerenciamento de Prontuários de Notebooks",

    'description': "",
    'author': "Redmaxx",
    'website': "http://www.redmaxx.com.br",
    'category': '',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'contributors': [
        'Andrea Monicque dos Santos Silva <andrea.silva@redmaxx.com.br>'
        'Petronilo Neto <petronilo.neto@redmaxx.com.br>'
        'Mackilem Van der Laan <mack.vdl@gmail.com>',
    ],
    'depends': ['sale'],
    'data': [
        'views/agent_data.xml',
        'views/diagnostic_records.xml',
        'data/res_group.xml',
        'security/ir.model.access.csv'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
