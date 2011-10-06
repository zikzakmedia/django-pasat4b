#!/usr/bin/env python
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

from setuptools import setup, find_packages

import pasat4b

setup(
    name='django-pasat4b',
    version=".".join(map(str, pasat4b.__version__)),
    author='Raimon Esteve',
    author_email='zikzak@zikzakmedia.com',
    maintainer="Raimon Esteve",
    maintainer_email="resteve@zikzakmedia.com",
    url='https://github.com/zikzakmedia/django-pasat4b',
    install_requires=[
        'Django>=1.0'
    ],
    description = 'A pluggable Django application for integrating 4b Payments (Pasat Internet 4b)',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
