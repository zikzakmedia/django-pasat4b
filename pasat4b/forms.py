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

from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe

from models import pasat4bResponse

class pasat4bPaymentForm(forms.Form):

    Ds_Merchant_Order = forms.CharField(widget=forms.HiddenInput())
    Ds_Merchant_MerchantCode = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(pasat4bPaymentForm, self).__init__(*args, **kwargs)

    def render(self):
        return mark_safe(u"""<form action="https://tpv.4b.es/tpvv/teargral.exe" method="post" id="pasat4b_standard_checkout">
            %s
            <input type="image" src="%s" border="0" name="submit" alt="%s" />
        </form>""" % (self.as_p(), settings.PASAT4B_BUTTON_IMG, settings.PASAT4B_BUTTON_TEXT))
        
    def sandbox(self):
        return mark_safe(u"""<form action="https://tpv2.4b.es/simulador/teargral.exe" method="post" id="pasat4b_standard_checkout">
            %s
            <input type="image" src="%s" border="0" name="submit" alt="%s" />
        </form>""" % (self.as_p(), settings.PASAT4B_BUTTON_IMG, settings.PASAT4B_BUTTON_TEXT))
        
class pasat4bResponseForm(forms.ModelForm):
    Ds_Date = forms.DateField(required=False, input_formats=('%d/%m/%Y',))
    Ds_Hour = forms.TimeField(required=False, input_formats=('%H:%M',))

    class Meta:
        model = pasat4bResponse
    
