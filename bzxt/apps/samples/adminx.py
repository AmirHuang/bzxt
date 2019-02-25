# _*_ coding: utf-8 _*_
# @Time     : 9:59
# @Author   : Amir
# @Site     : 
# @File     : adminx.py
# @Software : PyCharm

import xadmin
from .models import Image, exploSample, exploSampleFile, exploChSample, exploSamplePeak, devCompSample
from .models import devCompSampleFile, devCompChSample, devCompSamplePeak, devShapeSample


class ImageAdmin(object):
    list_display = ['user', 'url']


class exploSampleAdmin(object):
    list_display = ['sname', 'sampleID', 'user', "inputDate", "sampleState", 'sampleOrigin',
                    'sampleType', 'sampleMake', "sampleDraw", "sampleAnalyse", 'analyseCondition',
                    'picUrl', 'picDescrip', 'note']


class exploSampleFileAdmin(object):
    list_display = ['exploSample', 'user', 'detectDevice', "detectMrfs", "inputDate", 'detectType',
                    'docType', 'docUrl', "strength", "handledUrl"]


class exploChSampleAdmin(object):
    list_display = ['exploSampleFile', 'detectType', 'elementsList']


class exploSamplePeakAdmin(object):
    list_display = ['exploSampleFile', 'peakPos', 'peakHeight', 'peakArea']


class devCompSampleAdmin(object):
    list_display = ['sname', 'sampleID', 'user', "inputDate", "sampleState", 'sampleOrigin',
                    'sampleType', 'sampleMake', "sampleDraw", "sampleAnalyse", 'analyseCondition',
                    'picUrl', 'picDescrip', 'note']


class devCompSampleFileAdmin(object):
    list_display = ['devCompSample', 'user', 'detectDevice', "detectMrfs", "inputDate", 'detectType',
                    'docType', 'docUrl', "strength", "handledUrl"]


class devCompChSampleAdmin(object):
    list_display = ['devCompSampleFile', 'detectType', 'elementsList']


class devCompSamplePeakAdmin(object):
    list_display = ['devCompSampleFile', 'peakPos', 'peakHeight', 'peakArea']


class devShapeSampleAdmin(object):
    list_display = ['sname', 'sampleID', 'belongTo', "user", "inputDate", 'mrfs',
                    'sampleModel', 'trademark', "function", "isFirst", 'rectCoordi',
                    'proCoordi', 'backCoordi', 'boardCoordi', 'blackWhiteUrl', 'interColorUrl',
                    'middleResultUrl', 'compCheckCoordi', 'boardCheckCoordi', 'featureUrl',
                    'resultPicUrl', 'resultFileUrl', 'originalUrl', 'originalResolution',
                    'nomUrl', 'nomResolution', 'note']


xadmin.site.register(Image, ImageAdmin)
xadmin.site.register(exploSample, exploSampleAdmin)
xadmin.site.register(exploSampleFile, exploSampleFileAdmin)
xadmin.site.register(exploChSample, exploChSampleAdmin)
xadmin.site.register(exploSamplePeak, exploSamplePeakAdmin)
xadmin.site.register(devCompSample, devCompSampleAdmin)
xadmin.site.register(devCompSampleFile, devCompSampleFileAdmin)
xadmin.site.register(devCompChSample, devCompChSampleAdmin)
xadmin.site.register(devCompSamplePeak, devCompSamplePeakAdmin)
xadmin.site.register(devShapeSample, devShapeSampleAdmin)
