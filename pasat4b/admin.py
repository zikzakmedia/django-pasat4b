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

from django.contrib import admin

from models import pasat4bResponse

class pasat4bResponseAdmin(admin.ModelAdmin):
    search_fields = ['pszPurchorderNum',]
    list_display = ('store', 'pszTxnDate', 'result', 'pszPurchorderNum', 'pszApprovalCode','creation_date', )
    list_filter = ('creation_date','store','result')

admin.site.register(pasat4bResponse,pasat4bResponseAdmin)

