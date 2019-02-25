# _*_ coding: utf-8 _*_
# @Time     : 10:35
# @Author   : Amir
# @Site     : 
# @File     : adminx.py
# @Software : PyCharm

import xadmin
from .models import exploMatch, devCompMatch, devShapeMatch


class exploMatchAdmin(object):
    list_display = ['exploSample', 'exploEvi', 'matchType', 'matchModel', 'strength', 'matchDegree', 'isSure']


class devCompMatchAdmin(object):
    list_display = ['devCompSample', 'devCompEvi', 'matchType', 'matchModel', 'matchDegree', 'strength', 'isSure']


class devShapeMatchAdmin(object):
    list_display = ['devShapeSample', 'devShapeEvi', 'isCircuit', 'matchDegree', 'matchSampleCoordi', 'matchEviCoordi',
                    'isSure']


xadmin.site.register(exploMatch, exploMatchAdmin)
xadmin.site.register(devCompMatch, devCompMatchAdmin)
xadmin.site.register(devShapeMatch, devShapeMatchAdmin)
