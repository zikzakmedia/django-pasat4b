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

from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from pasat4b.pasat4b.signals import *
from pasat4b.pasat4b.forms import pasat4bResponseForm

@csrf_exempt
def pasat4b_ipn(request):

    form = pasat4bResponseForm(request.GET)
    if form.is_valid():
        pasat4b_resp = form.save()
        payment_was_successful.send(sender=pasat4b_resp)

        if request.GET['result'] == 0:
            payment_was_successful.send(sender=pasat4b_resp)
        else:
            payment_was_error.send(sender=pasat4b_resp)

    return HttpResponse()
