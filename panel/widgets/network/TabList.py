# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import Qt


class TabList(QWidget):
    items = []

    def __init__(self):
        super(QWidget, self).__init__()
        self.initUI()

    def initUI(self):
        self.itemLayout = QVBoxLayout()
        self.itemLayout.setAlignment(Qt.AlignTop)
        self.itemLayout.setSpacing(20)
        self.setLayout(self.itemLayout)

    def addItem(self, linkLabel):
        self.itemLayout.addWidget(linkLabel)
        self.items.append(linkLabel)

    def removeItem(self):
        for item in self.items:
            try:
                self.itemLayout.removeWidget(item)
                item.deleteLater()
            except Exception as ex:
                print(ex)
        self.items = []
        pass
