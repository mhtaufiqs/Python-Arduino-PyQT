import sys, os, glob
from PyQt4 import QtCore, QtGui, uic
import serial, time, threading


qtCreatorFile = "LDR.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.pushButton_OpenSerial.clicked.connect(self.OpenSerial)
		self.pushButton_Exit.clicked.connect(self.AppExit)
		self.pushButton_LDR.pressed.connect(self.Sensor)
		
	def OpenSerial(self):
		if self.pushButton_OpenSerial.text()=='Open Serial':
			self.ser = serial.Serial("COM8", "9600", timeout=0.1)
			if self.ser.isOpen():
				self.pushButton_OpenSerial.setText('Close Serial')
				self.textEdit_LogMessage.append("Opening serial port... OK")
				
								
			else:
				self.textEdit_LogMessage.append("can not open serial port")
		else:
			if self.ser.isOpen():
				self.ser.close()
				self.pushButton_OpenSerial.setText('Open Serial')
				self.textEdit_LogMessage.append("Closing serial port... OK")
				
	def Sensor(self):
		self.bytesToRead = self.ser.inWaiting()
		if (self.bytesToRead > 0):
			rxdata = self.ser.read(self.bytesToRead)
			self.textEdit_LogMessage_2.append(str(rxdata.decode()))
			

	def AppExit(self):
		self.textEdit_LogMessage.setText("Exit application")
		sys.exit()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
	
