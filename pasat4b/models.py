# -*- encoding: utf-8 -*-
############################################################################################
#
#    Django 4b Pasat Internet 4b Payments 
#    Copyright (C) 2011 Zikzakmedia S.L. (<http://www.zikzakmedia.com>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
############################################################################################

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

#import hashlib TODO

RESULT_ACTIVE = 0
RESULT_INACTIVE = 2

RESULT_CHOICES = (
    (RESULT_ACTIVE, _('Correct')),
    (RESULT_INACTIVE, _('Invalid')),
)

class pasat4bResponse(models.Model):
    
    creation_date = models.DateTimeField(auto_now_add=True)
    
    result = models.IntegerField(_('Result'), choices=RESULT_CHOICES, default=RESULT_CHOICES,) #0 -> transaccin autorizada / 2 -> Transaccion fallida
    pszPurchorderNum = models.CharField(_('Purchase Order'), max_length=12) # order number
    pszTxnDate = models.DateField(_('Txn Date'), ) #dd/mm/aa
    tipotrans = models.CharField(_('Tipo Trans'), max_length=3) #SSL/CES
    store = models.CharField(_('Store'), max_length=12) # PASSAT_4B_MERCHANT_CODE
    pszApprovalCode = models.CharField(_('Aproval Code'), max_length=12, null=True, blank=True) # successfully
    pszTxnID = models.CharField(_('Txn ID'), max_length=12, null=True, blank=True) # successfully
    coderror = models.CharField(_('Code Error'), max_length=12, null=True, blank=True) # Code Error
    deserror = models.CharField(_('Des Error'), max_length=256, null=True, blank=True) # Description Error
    MAC = models.CharField(_('Mac'),max_length=12, null=True, blank=True) # hash TODO
