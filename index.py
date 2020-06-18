import csv          
import pandas as pd
import numpy as np
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QFileDialog
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from MainWindow import *
import ctypes #GetSystemMetrics

# Application Class
class Application(QMainWindow):
    #Método constructor de la clase
    def __init__(self, parent = None):
        #QMainWindow Start
        QMainWindow.__init__(self,parent)
        #Charge MainWindow 
        uic.loadUi("MainWindow.ui", self)
        #Title
        self.setWindowTitle("SUVECI")
        self.count = 1
        #Agree new item
        self.btn_charge.clicked.connect(self.getfile)
        self.btn_process.clicked.connect(self.processfile)
    #Eliminar un item
    #self.lenguajes.removeItem(0)
    
    # Function in order to charge the files
    def getfile(self):
        self.options = QFileDialog.Options()
        #self.options |= QFileDialog.DontUseNativeDialog
        #fileName, _ = QFileDialog.getOpenFileName(self,"Open File", "","All Files (*);;CSV Files (*.csv)", options=options)
        self.fileNames, _ = QFileDialog.getOpenFileNames(self,"Open File", "","CSV Files (*.csv);;All Files (*)", options=self.options)
        #fileNames, _ = QFileDialog.getSaveFileName(self,"Open File","","All Files (*);;CSV Files (*.csv)", options=options)
        if self.fileNames:
            print(self.fileNames)
            self.lenght = len(self.fileNames)-1
            print(self.lenght)
            while self.lenght >= 0:
                print(self.fileNames[self.lenght])
                self.label_file.setText("Your Files have been Charged: " + str(len(self.fileNames)))
                self.listWidget.addItem(self.fileNames[self.lenght])
                #for i in (self.fileNames[self.lenght].reverse()):
                   # if (i == '.' or i == '/'):
                    #    self.count = i
                    #    break
                #print(self.count)
                self.lenght -=1
            
    # Function in order to create the new files
    def processfile(self):
        if self.fileNames:
            self.lenght = len(self.fileNames)-1
            print(self.lenght)
            while self.lenght >= 0:
                print(self.fileNames[self.lenght])            # Show what file are created
                data = pd.read_csv(self.fileNames[self.lenght])            # File csv

                name = data['Name']           # Get data about Name
                state = data['State']           # Get data about State
                phone = data['Phone']         # Get data about Phone
                leng1 = int(len(name))          # lenght of data
                print(leng1)
                # Create a table with data 
                dfObj = pd.DataFrame(np.zeros((leng1, 48)),columns=['Name', 'Given Name', 'Additional Name', 'Family Name', 'Yomi Name', 'Given Name Yomi', 'Additional Name Yomi', 'Family Name Yomi', 'Name Prefix', 'Name Suffix', 'Initials', 'Nickname', 'Short Name', 'Maiden Name', 'Birthday', 'Gender', 'Location', 'Billing Information', 'Directory Server', 'Mileage', 'Occupation', 'Hobby', 'Sensitivity', 'Priority', 'Subject', 'Notes', 'Language', 'Photo', 'Group Membership', 'Phone 1 - Type', 'Phone 1 - Value', 'Address 1 - Type', 'Address 1 - Formatted', 'Address 1 - Street', 'Address 1 - City', 'Address 1 - PO Box', 'Address 1 - Region', 'Address 1 - Postal Code', 'Address 1 - Country', 'Address 1 - Extended Address', 'Organization 1 - Type', 'Organization 1 - Name', 'Organization 1 - Yomi Name', 'Organization 1 - Title', 'Organization 1 - Department', 'Organization 1 - Symbol', 'Organization 1 - Location', 'Organization 1 - Job Description'])
                dfObj['Name'] = name
                dfObj['Given Name'] = name
                dfObj['Additional Name'] = name
                dfObj['Family Name'] = name
                dfObj['Phone 1 - Value'] = phone
                dfObj['Address 1 - Formatted'] = state
                dfObj['Address 1 - Street'] = state
                dfObj.to_csv('new.csv', index=False,sep=',')
                #print(dfObj)
                dfObj.to_csv(self.fileNames[self.lenght]+"output.csv",index=False,sep=',')
                self.lenght -=1
                self.listWidget_2.addItem(self.fileNames[self.lenght]+"output.csv")

        for i  in range(101):
            self.process_bar.setValue(i)
            self.label_process.setText("Processing...")
        self.label_process.setText("Process Finished")
        self.process_bar.setValue(0)

if __name__ == "__main__": 
    app = QApplication(sys.argv)        #App Inicialization
    _Application = Application()        #Object Class
    _Application.show()                 #Show Window
    app.exec_()                         #Execute Aplication
    #sys.exit(app.exec_())