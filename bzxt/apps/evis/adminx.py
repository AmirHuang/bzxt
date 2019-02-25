# _*_ coding: utf-8 _*_
# @Time     : 19:36
# @Author   : Amir
# @Site     : 
# @File     : adminx.py
# @Software : PyCharm

import xadmin
from .models import exploEvi, exploEviFile, exploChEvi, exploEviPeak
from .models import devCompEvi, devCompEviFile, devCompChEvi, devCompEviPeak, devShapeEvi


class exploEviAdmin(object):
    list_display = ['case_ID', 'evidenceID', 'inputDate', "eviState", "eviMake", 'eviDraw',
                    'eviAnalyse', 'analyseCondition', "picUrl", "picDescrip", 'note']


class exploEviFileAdmin(object):
    list_display = ['exploEvi', 'user', 'detectDevice', "detectMrfs", "inputDate", 'detectType',
                    'docType', 'docUrl', "handledUrl"]


class exploChEviAdmin(object):
    list_display = ['exploEviFile', 'detectType', 'elementsList']


class exploEviPeakAdmin(object):
    list_display = ['exploEviFile', 'peakPos', 'peakHeight', 'peakArea']


class devCompEviAdmin(object):
    list_display = ['caseID', 'evidenceID', 'user', "inputDate", "eviState", 'eviMake',
                    'eviDraw', 'eviAnalyse', "analyseCondition", "picUrl", 'picDescrip', 'note']


class devCompEviFileAdmin(object):
    list_display = ['devCompEvi', 'user', 'detectDevice', "detectMrfs", "inputDate", 'detectType',
                    'docType', 'docUrl', "handledUrl"]


class devCompChEviAdmin(object):
    list_display = ['devCompEviFile', 'detectType', 'elementsList']


class devCompEviPeakAdmin(object):
    list_display = ['devCompEviFile', 'peakPos', 'peakHeight', 'peakArea']


class devShapeEviAdmin(object):
    list_display = ['isCircuit', 'isFirst', 'eviID', "user", "inputDate", 'rectCoordi',
                    'proCoordi', 'backCoordi', "boardCoordi", "blackWhiteUrl", 'interColorUrl',
                    'middleResultUrl', 'compCheckCoordi', 'boardCheckCoordi', 'featureUrl',
                    'resultPicUrl', 'resultFileUrl', 'originalUrl', 'originalResolution',
                    'nomUrl', 'nomResolution', 'note']


xadmin.site.register(exploEvi, exploEviAdmin)
xadmin.site.register(exploEviFile, exploEviFileAdmin)
xadmin.site.register(exploChEvi, exploChEviAdmin)
xadmin.site.register(exploEviPeak, exploEviPeakAdmin)
xadmin.site.register(devCompEvi, devCompEviAdmin)
xadmin.site.register(devCompEviFile, devCompEviFileAdmin)
xadmin.site.register(devCompChEvi, devCompChEviAdmin)
xadmin.site.register(devCompEviPeak, devCompEviPeakAdmin)
xadmin.site.register(devShapeEvi, devShapeEviAdmin)
