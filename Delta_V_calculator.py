import math
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(340, 620)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(330, 580))
        MainWindow.setMaximumSize(QtCore.QSize(330, 580))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        MainWindow.setWindowIcon(QtGui.QIcon('rocket.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.group_box_mode = QtWidgets.QGroupBox(self.centralwidget)
        self.group_box_mode.setEnabled(True)
        self.group_box_mode.setGeometry(QtCore.QRect(10, 10, 311, 51))
        self.group_box_mode.setAutoFillBackground(False)
        self.group_box_mode.setStyleSheet("")
        self.group_box_mode.setObjectName("group_box_mode")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.group_box_mode)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 281, 21))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radio_orbital_v = QtWidgets.QRadioButton(self.horizontalLayoutWidget, clicked = lambda: self.disable_options())
        self.radio_orbital_v.setChecked(True)
        self.radio_orbital_v.setObjectName("radio_orbital_v")
        self.horizontalLayout.addWidget(self.radio_orbital_v)
        self.radio_delta_v = QtWidgets.QRadioButton(self.horizontalLayoutWidget, clicked = lambda: self.disable_options())
        self.radio_delta_v.setObjectName("radio_delta_v")
        self.horizontalLayout.addWidget(self.radio_delta_v)
        self.group_box_primary = QtWidgets.QGroupBox(self.centralwidget)
        self.group_box_primary.setGeometry(QtCore.QRect(10, 70, 311, 111))
        self.group_box_primary.setStyleSheet("")
        self.group_box_primary.setObjectName("group_box_primary")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.group_box_primary)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 281, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radio_earth = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radio_earth.setChecked(True)
        self.radio_earth.setObjectName("radio_earth")
        self.verticalLayout.addWidget(self.radio_earth)
        self.radio_moon = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radio_moon.setObjectName("radio_moon")
        self.verticalLayout.addWidget(self.radio_moon)
        self.radio_sun = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radio_sun.setObjectName("radio_sun")
        self.verticalLayout.addWidget(self.radio_sun)
        self.group_box_injection = QtWidgets.QGroupBox(self.centralwidget)
        self.group_box_injection.setGeometry(QtCore.QRect(10, 360, 311, 81))
        self.group_box_injection.setStyleSheet("")
        self.group_box_injection.setObjectName("group_box_injection")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.group_box_injection)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 161, 51))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.radio_peryapse = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.radio_peryapse.setChecked(True)
        self.radio_peryapse.setObjectName("radio_peryapse")
        self.verticalLayout_4.addWidget(self.radio_peryapse)
        self.radio_apoapse = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.radio_apoapse.setObjectName("radio_apoapse")
        self.verticalLayout_4.addWidget(self.radio_apoapse)
        self.group_box_variables = QtWidgets.QGroupBox(self.centralwidget)
        self.group_box_variables.setGeometry(QtCore.QRect(10, 190, 311, 161))
        self.group_box_variables.setStyleSheet("")
        self.group_box_variables.setObjectName("group_box_variables")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.group_box_variables)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 160, 131))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_peryapse = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_peryapse.setObjectName("label_peryapse")
        self.verticalLayout_2.addWidget(self.label_peryapse)
        self.line_peryapse_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.line_peryapse_input.setInputMask("")
        self.line_peryapse_input.setText("")
        self.line_peryapse_input.setMaxLength(32767)
        self.line_peryapse_input.setFrame(True)
        self.line_peryapse_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.line_peryapse_input.setCursorPosition(0)
        self.line_peryapse_input.setObjectName("line_peryapse_input")
        self.verticalLayout_2.addWidget(self.line_peryapse_input)
        self.label_apoapse = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_apoapse.setObjectName("label_apoapse")
        self.verticalLayout_2.addWidget(self.label_apoapse)
        self.line_apoapse_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.line_apoapse_input.setInputMask("")
        self.line_apoapse_input.setObjectName("line_apoapse_input")
        self.verticalLayout_2.addWidget(self.line_apoapse_input)
        self.label_orbit_height = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_orbit_height.setObjectName("label_orbit_height")
        self.verticalLayout_2.addWidget(self.label_orbit_height)
        self.line_orbit_height_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.line_orbit_height_input.setInputMask("")
        self.line_orbit_height_input.setObjectName("line_orbit_height_input")
        self.verticalLayout_2.addWidget(self.line_orbit_height_input)
        self.group_box_result = QtWidgets.QGroupBox(self.centralwidget)
        self.group_box_result.setGeometry(QtCore.QRect(10, 450, 311, 111))
        self.group_box_result.setStyleSheet("")
        self.group_box_result.setTitle("")
        self.group_box_result.setObjectName("group_box_result")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.group_box_result)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 291, 91))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.push_button_calculate = QtWidgets.QPushButton(self.verticalLayoutWidget_3, clicked = lambda: self.calculate())
        palette = QtGui.QPalette()
        self.push_button_calculate.setPalette(palette)
        self.push_button_calculate.setStyleSheet("")
        self.push_button_calculate.setAutoDefault(False)
        self.push_button_calculate.setDefault(False)
        self.push_button_calculate.setFlat(False)
        self.push_button_calculate.setObjectName("push_button_calculate")
        self.verticalLayout_3.addWidget(self.push_button_calculate)
        self.label_result = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_result.setObjectName("label_result")
        self.verticalLayout_3.addWidget(self.label_result)
        self.label_circ_orbit_inj_result = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_circ_orbit_inj_result.setObjectName("label_circ_orbit_inj_result")
        self.verticalLayout_3.addWidget(self.label_circ_orbit_inj_result)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 340, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def disable_options(self):
        if self.radio_orbital_v.isChecked():
            self.label_orbit_height.setText(f"Calculation orbit (km):")
            self.group_box_injection.setDisabled(True)

        elif self.radio_delta_v.isChecked():
            self.label_orbit_height.setText(f"Final orbit (km):")
            self.group_box_injection.setEnabled(True)

    def calculate(self):
        self.check_numerical()
        print("check_numerical function ended")
        self.get_data()
        print("get_data function ended")
        if self.radio_orbital_v.isChecked():
            print("get_equation_orbital function started")
            self.get_equation_orbital()
            print(self.get_equation_orbital())
            print("get_equation_orbital function ended")
        else:
            print("get_equation_delta function started")
            self.get_equation_delta()
            print(self.get_equation_delta())
            print("get_equation_delta function ended")

        if is_numeric:
            print("passed")
        else:
            print("failed")

    def check_numerical(self):
        global is_numeric
        is_numeric = False
        self.radius_peryapse = self.line_peryapse_input.text()
        self.radius_apoapse = self.line_apoapse_input.text()
        self.radius_calculation = self.line_orbit_height_input.text()
        if self.radius_peryapse.isnumeric() and self.radius_apoapse.isnumeric() and self.radius_calculation.isnumeric():
            is_numeric = True
            print("Is_numeric = True")
            return self.radius_peryapse, self.radius_apoapse, self.radius_calculation
        else:
            is_numeric = False
            self.line_peryapse_input.clear()
            self.line_apoapse_input.clear()
            self.line_orbit_height_input.clear()
            print("Input error 2")
            self.label_result.setText(f"Input is not numeric")

    def get_data(self):
        self.g_constant = 6.6740831e-11
        if self.radio_earth.isChecked():
            self.mass = 5.97219e24
            self.radius = 6.371e6
        elif self.radio_moon.isChecked():
            self.mass = 7.342e22
            self.radius = 1.7374e6
        elif self.radio_sun.isChecked():
            self.mass = 1.9885e30
            self.radius = 6.96342e8

    def get_equation_orbital(self):
        Rp = self.radius + 1000 * int(self.radius_peryapse)
        Ra = self.radius + 1000 * int(self.radius_apoapse)
        Rc = self.radius + 1000 * int(self.radius_calculation)
        if Rc or Ra or Rp < -1*self.radius:
            self.label_result.setText(f"Entered radius lower than radius of primary body.")
            self.label_circ_orbit_inj_result.setText(f"You just tried to warp drive.")
        elif Rc > Ra:
            self.label_result.setText(f"Injection radius higher than apoapse.")
            self.line_orbit_height_input.clear()
        elif Rc < Rp:
            self.label_result.setText(f"Injection radius lower than peryapse.")
            self.line_orbit_height_input.clear()
        else:
            unit = 'm/s'
            a = (Rp + Ra)/2
            velocity = int(math.sqrt(self.g_constant * self.mass * ((2/Rc) - (1/a))))
            if velocity > 1000:
                velocity = velocity/1000
                unit = 'km/s'
            self.label_result.setText(f"Orbital velocity: {velocity} {unit}")
            self.label_circ_orbit_inj_result.clear()
            return Rp, Ra, Rc, a, velocity

    def get_equation_delta(self):
        Rp = self.radius + 1000 * int(self.radius_peryapse)
        Ra = self.radius + 1000 * int(self.radius_apoapse)
        Rf = self.radius + 1000 * int(self.radius_calculation)
        unit_delta = 'm/s'
        unit_circular = 'm/s'
        if Rf or Ra or Rp < -1*self.radius:
            self.label_result.setText(f"Entered radius lower than radius of primary body.")
            self.label_circ_orbit_inj_result.setText(f"You just tried to warp drive.")
            self.line_orbit_height_input.clear()
            self.line_apoapse_input.clear()
            self.line_peryapse_input.clear()
            return

        if self.radio_peryapse.isChecked():
            a = (Rp + Ra) / 2
            velocity_one = int(math.sqrt(self.g_constant * self.mass * ((2 / Rp) - (1 / a))))
            a = (Rp + Rf) / 2
            velocity_two = int(math.sqrt(self.g_constant * self.mass * ((2 / Rp) - (1 / a))))
            delta_v = velocity_two - velocity_one
            if delta_v > 1000:
                delta_v = delta_v/1000
                unit_delta = "km/s"
            self.label_result.setText(f"Delta V: {delta_v} {unit_delta}")
            a = (Rp + Rf) / 2
            velocity_three = int(math.sqrt(self.g_constant * self.mass * ((2 / Rf) - (1 / a))))
            a = (Rf + Rf) / 2
            velocity_four = int(math.sqrt(self.g_constant * self.mass * ((2 / Rf) - (1 / a))))
            into_circ = velocity_four - velocity_three
            if into_circ > 1000:
                into_circ = into_circ/1000
                unit_circular = "km/s"
            self.label_circ_orbit_inj_result.setText(f"Circular orbit: {into_circ} {unit_circular}")
            return delta_v, into_circ

        else:
            a = (Rp + Ra) / 2
            velocity_one = int(math.sqrt(self.g_constant * self.mass * ((2 / Ra) - (1 / a))))
            a = (Ra + Rf) / 2
            velocity_two = int(math.sqrt(self.g_constant * self.mass * ((2 / Ra) - (1 / a))))
            delta_v = velocity_two - velocity_one
            if delta_v > 1000:
                delta_v = delta_v / 1000
                unit_delta = "km/s"
            self.label_result.setText(f"Delta V: {delta_v} {unit_delta}")
            a = (Ra + Rf) / 2
            velocity_three = int(math.sqrt(self.g_constant * self.mass * ((2 / Rf) - (1 / a))))
            a = (Rf + Rf) / 2
            velocity_four = int(math.sqrt(self.g_constant * self.mass * ((2 / Rf) - (1 / a))))
            into_circ = velocity_four - velocity_three
            if into_circ > 1000:
                into_circ = into_circ / 1000
                unit_circular = "km/s"
            self.label_circ_orbit_inj_result.setText(f"Circular orbit: {into_circ} {unit_circular}")
            return delta_v, into_circ

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Orbital mechanics calculator"))
        self.group_box_mode.setTitle(_translate("MainWindow", "Select calculator mode"))
        self.radio_orbital_v.setText(_translate("MainWindow", "Orbital velocity"))
        self.radio_delta_v.setText(_translate("MainWindow", "Delta V"))
        self.group_box_primary.setTitle(_translate("MainWindow", "Select primary body"))
        self.radio_earth.setText(_translate("MainWindow", "Earth"))
        self.radio_moon.setText(_translate("MainWindow", "Moon"))
        self.radio_sun.setText(_translate("MainWindow", "Sun"))
        self.group_box_injection.setTitle(_translate("MainWindow", "Injection at:"))
        self.radio_peryapse.setText(_translate("MainWindow", "Peryapse"))
        self.radio_apoapse.setText(_translate("MainWindow", "Apoapse"))
        self.group_box_variables.setTitle(_translate("MainWindow", "Input variables"))
        self.label_peryapse.setText(_translate("MainWindow", "Peryapse (km):"))
        self.label_apoapse.setText(_translate("MainWindow", "Apoapse (km):"))
        self.label_orbit_height.setText(_translate("MainWindow", "Calculation orbit (km):"))
        self.push_button_calculate.setText(_translate("MainWindow", "Calculate"))
        self.label_result.setText(_translate("MainWindow", ""))
        self.label_circ_orbit_inj_result.setText(_translate("MainWindow", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
