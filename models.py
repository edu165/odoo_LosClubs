# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Club(models.Model):
    _name = 'losclubs.club'
    name = fields.Char(string="Nombre Club", required=True)
    
    equipo_id = fields.One2many('losclubs.equipo','equipo_id', string="Equipo")
    #uno a muchos poblaciones una provimcia teine mucha poblaciones
  # En Uno  muchos tienes que el campo con el que se relaciona
class Equipo(models.Model):
    _name = 'losclubs.equipo'
    name = fields.Char(string="Nombre Equipo", required=True)
    club_id = fields.Many2one('losclubs.club', string="Club")

 

   

