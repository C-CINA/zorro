# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_DialogFileLoc.ui'
#
# Created: Thu Sep 29 11:15:15 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_DialogFileLocations(object):
    def setupUi(self, DialogFileLocations):
        DialogFileLocations.setObjectName("DialogFileLocations")
        DialogFileLocations.resize(542, 683)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../zorro_dev/automator/CINAlogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogFileLocations.setWindowIcon(icon)
        DialogFileLocations.setStyleSheet("background: rgb(0, 85, 127);\n"
"color: white;\n"
"font-weight: bold;\n"
"")
        self.frame = QtGui.QFrame(DialogFileLocations)
        self.frame.setGeometry(QtCore.QRect(0, 0, 541, 681))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 12, 0, 1, 1)
        self.leOutputPath = QtGui.QLineEdit(self.frame)
        self.leOutputPath.setStyleSheet("background: gray;\n"
"color: black;")
        self.leOutputPath.setText("")
        self.leOutputPath.setObjectName("leOutputPath")
        self.gridLayout.addWidget(self.leOutputPath, 13, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.frame)
        self.label_8.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 16, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 20, 0, 1, 1)
        self.leInputPath = QtGui.QLineEdit(self.frame)
        self.leInputPath.setMinimumSize(QtCore.QSize(0, 0))
        self.leInputPath.setStyleSheet("background: gray;\n"
"color: black;")
        self.leInputPath.setText("")
        self.leInputPath.setObjectName("leInputPath")
        self.gridLayout.addWidget(self.leInputPath, 3, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.frame)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 11, 0, 1, 1)
        self.leAlignPath = QtGui.QLineEdit(self.frame)
        self.leAlignPath.setStyleSheet("background: gray;\n"
"color: black;")
        self.leAlignPath.setText("")
        self.leAlignPath.setObjectName("leAlignPath")
        self.gridLayout.addWidget(self.leAlignPath, 21, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 22, 0, 1, 1)
        self.tbOpenGainRefPath = QtGui.QToolButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbOpenGainRefPath.sizePolicy().hasHeightForWidth())
        self.tbOpenGainRefPath.setSizePolicy(sizePolicy)
        self.tbOpenGainRefPath.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tbOpenGainRefPath.setStyleSheet("background: gray;\n"
"")
        self.tbOpenGainRefPath.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../zorro_dev/automator/icons/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbOpenGainRefPath.setIcon(icon1)
        self.tbOpenGainRefPath.setIconSize(QtCore.QSize(32, 32))
        self.tbOpenGainRefPath.setObjectName("tbOpenGainRefPath")
        self.gridLayout.addWidget(self.tbOpenGainRefPath, 26, 3, 1, 1)
        self.line = QtGui.QFrame(self.frame)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 7, 2, 1, 1)
        self.leRawPath = QtGui.QLineEdit(self.frame)
        self.leRawPath.setStyleSheet("background: gray;\n"
"color: black;")
        self.leRawPath.setText("")
        self.leRawPath.setObjectName("leRawPath")
        self.gridLayout.addWidget(self.leRawPath, 15, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.frame)
        self.label_9.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 25, 0, 1, 1)
        self.tbOpenRawPath = QtGui.QToolButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbOpenRawPath.sizePolicy().hasHeightForWidth())
        self.tbOpenRawPath.setSizePolicy(sizePolicy)
        self.tbOpenRawPath.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tbOpenRawPath.setStyleSheet("background: gray;\n"
"")
        self.tbOpenRawPath.setText("")
        self.tbOpenRawPath.setIcon(icon1)
        self.tbOpenRawPath.setIconSize(QtCore.QSize(32, 32))
        self.tbOpenRawPath.setObjectName("tbOpenRawPath")
        self.gridLayout.addWidget(self.tbOpenRawPath, 15, 3, 1, 1)
        self.leGainRefPath = QtGui.QLineEdit(self.frame)
        self.leGainRefPath.setEnabled(True)
        self.leGainRefPath.setStyleSheet("background: gray;\n"
"color: black;")
        self.leGainRefPath.setText("")
        self.leGainRefPath.setObjectName("leGainRefPath")
        self.gridLayout.addWidget(self.leGainRefPath, 26, 0, 1, 1)
        self.tbOpenFiguresPath = QtGui.QToolButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbOpenFiguresPath.sizePolicy().hasHeightForWidth())
        self.tbOpenFiguresPath.setSizePolicy(sizePolicy)
        self.tbOpenFiguresPath.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tbOpenFiguresPath.setStyleSheet("background: gray;\n"
"")
        self.tbOpenFiguresPath.setText("")
        self.tbOpenFiguresPath.setIcon(icon1)
        self.tbOpenFiguresPath.setIconSize(QtCore.QSize(32, 32))
        self.tbOpenFiguresPath.setObjectName("tbOpenFiguresPath")
        self.gridLayout.addWidget(self.tbOpenFiguresPath, 23, 3, 1, 1)
        self.tbOpenSumPath = QtGui.QToolButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbOpenSumPath.sizePolicy().hasHeightForWidth())
        self.tbOpenSumPath.setSizePolicy(sizePolicy)
        self.tbOpenSumPath.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tbOpenSumPath.setStyleSheet("background: gray;\n"
"")
        self.tbOpenSumPath.setText("")
        self.tbOpenSumPath.setIcon(icon1)
        self.tbOpenSumPath.setIconSize(QtCore.QSize(32, 32))
        self.tbOpenSumPath.setObjectName("tbOpenSumPath")
        self.gridLayout.addWidget(self.tbOpenSumPath, 18, 3, 1, 1)
        self.tbOpenAlignPath = QtGui.QToolButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbOpenAlignPath.sizePolicy().hasHeightForWidth())
        self.tbOpenAlignPath.setSizePolicy(sizePolicy)
        self.tbOpenAlignPath.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tbOpenAlignPath.setStyleSheet("background: gray;\n"
"")
        self.tbOpenAlignPath.setText("")
        self.tbOpenAlignPath.setIcon(icon1)
        self.tbOpenAlignPath.setIconSize(QtCore.QSize(32, 32))
        self.tbOpenAlignPath.setObjectName("tbOpenAlignPath")
        self.gridLayout.addWidget(self.tbOpenAlignPath, 21, 3, 1, 1)
        self.tbOpenOutputPath = QtGui.QToolButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbOpenOutputPath.sizePolicy().hasHeightForWidth())
        self.tbOpenOutputPath.setSizePolicy(sizePolicy)
        self.tbOpenOutputPath.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tbOpenOutputPath.setStyleSheet("background: gray;\n"
"")
        self.tbOpenOutputPath.setText("")
        self.tbOpenOutputPath.setIcon(icon1)
        self.tbOpenOutputPath.setIconSize(QtCore.QSize(32, 32))
        self.tbOpenOutputPath.setObjectName("tbOpenOutputPath")
        self.gridLayout.addWidget(self.tbOpenOutputPath, 13, 3, 1, 1)
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 14, 0, 1, 1)
        self.leFiguresPath = QtGui.QLineEdit(self.frame)
        self.leFiguresPath.setEnabled(True)
        self.leFiguresPath.setStyleSheet("background: gray;\n"
"color: black;")
        self.leFiguresPath.setText("")
        self.leFiguresPath.setObjectName("leFiguresPath")
        self.gridLayout.addWidget(self.leFiguresPath, 23, 0, 1, 1)
        self.tbOpenInputPath = QtGui.QToolButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbOpenInputPath.sizePolicy().hasHeightForWidth())
        self.tbOpenInputPath.setSizePolicy(sizePolicy)
        self.tbOpenInputPath.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tbOpenInputPath.setStyleSheet("background: gray;\n"
"")
        self.tbOpenInputPath.setText("")
        self.tbOpenInputPath.setIcon(icon1)
        self.tbOpenInputPath.setIconSize(QtCore.QSize(32, 32))
        self.tbOpenInputPath.setObjectName("tbOpenInputPath")
        self.gridLayout.addWidget(self.tbOpenInputPath, 3, 3, 1, 1)
        self.leSumPath = QtGui.QLineEdit(self.frame)
        self.leSumPath.setStyleSheet("background: gray;\n"
"color: black;")
        self.leSumPath.setText("")
        self.leSumPath.setObjectName("leSumPath")
        self.gridLayout.addWidget(self.leSumPath, 18, 0, 1, 1)
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_2.setLineWidth(1)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboCompressor = QtGui.QComboBox(self.frame_2)
        self.comboCompressor.setEnabled(True)
        self.comboCompressor.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.comboCompressor.setStyleSheet("background: white;\n"
"color:black;\n"
"\n"
"")
        self.comboCompressor.setObjectName("comboCompressor")
        self.comboCompressor.addItem("")
        self.comboCompressor.addItem("")
        self.comboCompressor.addItem("")
        self.comboCompressor.addItem("")
        self.horizontalLayout.addWidget(self.comboCompressor)
        self.label_10 = QtGui.QLabel(self.frame_2)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.sbCLevel = QtGui.QSpinBox(self.frame_2)
        self.sbCLevel.setEnabled(True)
        self.sbCLevel.setStyleSheet("background: white;\n"
"color:black;\n"
"")
        self.sbCLevel.setMinimum(1)
        self.sbCLevel.setMaximum(9)
        self.sbCLevel.setObjectName("sbCLevel")
        self.horizontalLayout.addWidget(self.sbCLevel)
        self.gridLayout.addWidget(self.frame_2, 27, 0, 1, 1)
        self.horizontalFrame = QtGui.QFrame(self.frame)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cbGainRot = QtGui.QCheckBox(self.horizontalFrame)
        self.cbGainRot.setObjectName("cbGainRot")
        self.horizontalLayout_2.addWidget(self.cbGainRot)
        self.cbGainHorzFlip = QtGui.QCheckBox(self.horizontalFrame)
        self.cbGainHorzFlip.setChecked(True)
        self.cbGainHorzFlip.setObjectName("cbGainHorzFlip")
        self.horizontalLayout_2.addWidget(self.cbGainHorzFlip)
        self.cbGainVertFlip = QtGui.QCheckBox(self.horizontalFrame)
        self.cbGainVertFlip.setChecked(True)
        self.cbGainVertFlip.setObjectName("cbGainVertFlip")
        self.horizontalLayout_2.addWidget(self.cbGainVertFlip)
        self.gridLayout.addWidget(self.horizontalFrame, 28, 0, 1, 1)
        self.line_3 = QtGui.QFrame(self.frame)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 24, 0, 1, 1)

        self.retranslateUi(DialogFileLocations)
        QtCore.QMetaObject.connectSlotsByName(DialogFileLocations)
        DialogFileLocations.setTabOrder(self.leInputPath, self.leOutputPath)
        DialogFileLocations.setTabOrder(self.leOutputPath, self.leRawPath)
        DialogFileLocations.setTabOrder(self.leRawPath, self.leSumPath)
        DialogFileLocations.setTabOrder(self.leSumPath, self.leAlignPath)
        DialogFileLocations.setTabOrder(self.leAlignPath, self.leFiguresPath)
        DialogFileLocations.setTabOrder(self.leFiguresPath, self.leGainRefPath)
        DialogFileLocations.setTabOrder(self.leGainRefPath, self.comboCompressor)
        DialogFileLocations.setTabOrder(self.comboCompressor, self.sbCLevel)

    def retranslateUi(self, DialogFileLocations):
        DialogFileLocations.setWindowTitle(QtGui.QApplication.translate("DialogFileLocations", "Automator Folder Locations", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setToolTip(QtGui.QApplication.translate("DialogFileLocations", "Subdirectory inside the working directory where Zorro logs and standard output will be saved.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DialogFileLocations", "Logs subdirectory path:", None, QtGui.QApplication.UnicodeUTF8))
        self.leOutputPath.setToolTip(QtGui.QApplication.translate("DialogFileLocations", "Subdirectory inside the working directory where Zorro logs and standard output will be saved.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setToolTip(QtGui.QApplication.translate("DialogFileLocations", "The directory to watch for new *.mrc, *.dm4, *.tif, and *.hdf5 files for processing.  Moves _all_ files in this directory.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("DialogFileLocations", "Input directory path:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setToolTip(QtGui.QApplication.translate("DialogFileLocations", "Where to save the *zorro.mrc aligned stack sums.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("DialogFileLocations", "Aligned sums subdirectory:                          ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setToolTip(QtGui.QApplication.translate("DialogFileLocations", "Where to save the zorro_movie.mrcs aligned movie files (can be the same as sums).", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("DialogFileLocations", "Aligned stacks subdirectory:", None, QtGui.QApplication.UnicodeUTF8))
        self.leInputPath.setToolTip(QtGui.QApplication.translate("DialogFileLocations", "The directory to watch for new *.mrc, *.dm4, *.tif, and *.hdf5 files for processing.  Moves _all_ files in this directory.", None, QtGui.QApplication.UnicodeUTF8))
        self.leAlignPath.setToolTip(QtGui.QApplication.translate("DialogFileLocations", "Where to save the zorro_movie.mrcs aligned movie files (can be the same as sums).", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setToolTip(QtGui.QApplication.translate("DialogFileLocations", "Where to save the diagnostic PNG plots.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("DialogFileLocations", "Figures subdirectory:", None, QtGui.QApplication.UnicodeUTF8))
        self.leRawPath.setToolTip(QtGui.QApplication.translate("DialogFileLocations", "Where to move all raw files (from input) to.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("DialogFileLocations", "Gain reference (for SerialEM):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setToolTip(QtGui.QApplication.translate("DialogFileLocations", "Where to move all raw files (from input) to.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("DialogFileLocations", "Raw stacks subdirectory:", None, QtGui.QApplication.UnicodeUTF8))
        self.leFiguresPath.setToolTip(QtGui.QApplication.translate("DialogFileLocations", "Where to save the diagnostic PNG plots.", None, QtGui.QApplication.UnicodeUTF8))
        self.leSumPath.setToolTip(QtGui.QApplication.translate("DialogFileLocations", "Where to save the *zorro.mrc aligned stack sums.", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DialogFileLocations", "Compression:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboCompressor.setItemText(0, QtGui.QApplication.translate("DialogFileLocations", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.comboCompressor.setItemText(1, QtGui.QApplication.translate("DialogFileLocations", "zstd", None, QtGui.QApplication.UnicodeUTF8))
        self.comboCompressor.setItemText(2, QtGui.QApplication.translate("DialogFileLocations", "lz4", None, QtGui.QApplication.UnicodeUTF8))
        self.comboCompressor.setItemText(3, QtGui.QApplication.translate("DialogFileLocations", "zlib", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("DialogFileLocations", "Level:", None, QtGui.QApplication.UnicodeUTF8))
        self.cbGainRot.setText(QtGui.QApplication.translate("DialogFileLocations", "Rotation", None, QtGui.QApplication.UnicodeUTF8))
        self.cbGainHorzFlip.setText(QtGui.QApplication.translate("DialogFileLocations", "Horizontal Flip", None, QtGui.QApplication.UnicodeUTF8))
        self.cbGainVertFlip.setText(QtGui.QApplication.translate("DialogFileLocations", "Vertical Flip", None, QtGui.QApplication.UnicodeUTF8))

