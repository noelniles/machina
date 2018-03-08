# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/template_plugin/plugin.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PluginGui(object):
    def setupUi(self, PluginGui):
        PluginGui.setObjectName("PluginGui")
        PluginGui.resize(319, 530)
        self.gridLayout = QtWidgets.QGridLayout(PluginGui)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(PluginGui)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(PluginGui)
        QtCore.QMetaObject.connectSlotsByName(PluginGui)

    def retranslateUi(self, PluginGui):
        _translate = QtCore.QCoreApplication.translate
        PluginGui.setWindowTitle(_translate("PluginGui", "Form"))
        self.label.setText(_translate("PluginGui", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">This is a template plugin.</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">It can be cloned and used to create new plugins.</span></p></body></html>"))

