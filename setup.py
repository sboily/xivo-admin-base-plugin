#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup


setup(
    name='xivo_base',
    version='0.1',

    description='XiVO base',

    author='Sylvain Boily',
    author_email='sboily@avencall.com',

    url='https://github.com/sboily/xivo-admin-base',

    packages=find_packages(),
    include_package_data = True,
    zip_safe = False,

    entry_points={
        'xivo_admin.plugins': [
            'xivobase = xivo_base.plugins.xivobase:XiVOBase',
        ],
    }
)

