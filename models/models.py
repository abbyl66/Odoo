# -*- coding: utf-8 -*-

from odoo import models, fields, api


class modelo51y(models.Model):
     _name = 'odoo51y.modelo51y'
     _description = 'model modelo51y'

     name = fields.Char('ID', required=True)
     titulo = fields.Char(String = 'titulo', required = True)
     autor = fields.Char(String = 'autor', required=True)

#2do Trimestre (Odoo)
#Segundo modelo.

class autores51y(models.Model):
     _name = 'odoo51y.autores51y'
     _description = 'model autores51y'

     #Campos
     name = fields.Char('ID', required = True)
     nombre = fields.Char(String = 'nombre', required = True)
     pais_Nacimiento = fields.Char(String = 'pais nacimiento')
     libro_Destacado = fields.Char(String = 'libro destacado')

#Tercer modelo
class editoriales51y(models.Model):
     _name = 'odoo51y.editoriales51y'
     _description = 'model editoriales51y'

     #Campos
     name = fields.Char('ID', required=True)
     nombre = fields.Char(String='nombre', required=True)
     fundador = fields.Char(String='fundador', required = True)
     pais = fields.Char(String='pais')

#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
