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

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test.client import Client
from django.utils.encoding import smart_unicode

from pasat4b.models import pasat4bResponse

class pasat4bTest(TestCase):
    # TODO
    def test_4b_ipn(self):
        data ={'DS_result': 1, 
                u'DS_pszPurchorderNum': u'1825926', 
                u'DS_pszTxnDate': u'05/10/2011'}
        c = Client()
        resp = c.post(reverse('pasat4b_ipn'), data)
        self.assertEqual(resp.status_code, 200)
        
        pasat4b_responses = pasat4bResponse.objects.all()
        self.assertEqual(pasat4b_responses.count(), 1)
        pasat4b_response = pasat4b_responses[0]
        self.assertTrue(pasat4b_response.check_signature())

