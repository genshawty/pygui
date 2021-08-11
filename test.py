self.pos = MainWindow.pos()
        self.tasks_container = dict()
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)
        self.exit_button.clicked.connect(lambda: MainWindow.close())
        self.hide_button.clicked.connect(lambda: MainWindow.showMinimized())
        self.task_creator.clicked.connect(lambda: self.tabs_widget.setCurrentIndex(0))
        self.tasks.clicked.connect(lambda: self.tabs_widget.setCurrentIndex(1))
        self.billing.clicked.connect(lambda: self.tabs_widget.setCurrentIndex(2))
        self.proxies.clicked.connect(lambda: self.tabs_widget.setCurrentIndex(4))
        self.settings.clicked.connect(lambda: self.tabs_widget.setCurrentIndex(3))

        
        self.add_taskBtn.clicked.connect(self.add_task)

        self.save_indicator.hide()

        self.retranslateUi(MainWindow)

        self.tabs_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

def add_task(self):
    data = dict()
    self.tasks_num += 1
    data['num'] = str(self.tasks_num)
    data['site'] = self.enter_site_combo.currentText()
    data['profile'] = self.enter_profile_combo.currentText()
    data['product'] = self.enter_product_input.text()
    data['size'] = self.enter_size_combo.currentText()
    data['proxy'] = self.enter_proxy_combo.currentText()
    item = QListWidgetItem(self.listWidget)
    item.setSizeHint(QSize(944, 40))
    data['item'] = item
    widget = taskWidget(item, data)
    widget.itemDeleted.connect(self.deleteTask)
    widget.itemEdited.connect(self.editTask)
    # Binding delete signal
    self.listWidget.setItemWidget(item, widget)

    self.tasks_container[self.tasks_num] = data

    del data

def deleteTask(self, item):
    row = self.listWidget.indexFromItem(item).row()
    item = self.listWidget.takeItem(row)
    self.listWidget.removeItemWidget(item)
    del item

def editTask(self, item):
    print(item)
    for t in self.tasks_container:
        if self.tasks_container[t]['item'] == item:
            break
    
    dialog = Ui_Dialog(self.tasks_container[t])
    center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
    dialog.move(center.x()-400, center.y()-275)
    if dialog.exec() == QDialog.Accepted:
        print('edited')
    else:
        print('cancelled')

class taskWidget(QWidget):
    itemDeleted = Signal(QListWidgetItem)

    def __init__(self, item, data, *args, **kwargs):
        super(taskWidget, self).__init__(*args, **kwargs)
        self._item = item
        self.num_row = QLabel(self)
        self.num_row.setObjectName(u"num_row")
        self.num_row.setGeometry(QRect(9, 9, 24, 24))
        self.num_row.setAlignment(Qt.AlignCenter)
        self.site_row = QLabel(self)
        self.site_row.setObjectName(u"site_row")
        self.site_row.setGeometry(QRect(50, 9, 91, 24))
        self.product_row = QLabel(self)
        self.product_row.setObjectName(u"product_row")
        self.product_row.setGeometry(QRect(150, 9, 161, 24))
        self.size_row = QLabel(self)
        self.size_row.setObjectName(u"size_row")
        self.size_row.setGeometry(QRect(330, 9, 61, 24))
        self.profile_row = QLabel(self)
        self.profile_row.setObjectName(u"profile_row")
        self.profile_row.setGeometry(QRect(405, 9, 81, 24))
        self.proxy_row = QLabel(self)
        self.proxy_row.setObjectName(u"proxy_row")
        self.proxy_row.setGeometry(QRect(500, 9, 60, 24))
        self.status_row = QLabel(self)
        self.status_row.setObjectName(u"status_row")
        self.status_row.setGeometry(QRect(580, 9, 191, 24))
        self.status_row.setAlignment(Qt.AlignCenter)
        self.start_row = QPushButton(self)
        self.start_row.setObjectName(u"start_row")
        self.start_row.setGeometry(QRect(781, 6, 26, 26))
        icon1 = QIcon()
        icon1.addFile(u"img/start.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.start_row.setIcon(icon1)
        self.start_row.setIconSize(QSize(26, 26))
        self.stop_row = QPushButton(self)
        self.stop_row.setObjectName(u"stop_row")
        self.stop_row.setGeometry(QRect(820, 6, 26, 26))
        icon2 = QIcon()
        icon2.addFile(u"img/stop.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.stop_row.setIcon(icon2)
        self.stop_row.setIconSize(QSize(26, 26))
        self.edit_row = QPushButton(self)
        self.edit_row.setObjectName(u"edit_row")
        self.edit_row.setGeometry(QRect(860, 6, 26, 26))
        icon3 = QIcon()
        icon3.addFile(u"img/pen.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.edit_row.setIcon(icon3)
        self.edit_row.setIconSize(QSize(26, 26))
        self.delete_row = QPushButton(self)
        self.delete_row.setObjectName(u"delete_row")
        self.delete_row.setGeometry(QRect(900, 6, 26, 26))
        self.delete_row.clicked.connect(self.deleteItem)
        icon4 = QIcon()
        icon4.addFile(u"img/trash.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_row.setIcon(icon4)
        self.delete_row.setIconSize(QSize(26, 26))
        self.num_row.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.site_row.setText(QCoreApplication.translate("MainWindow", data['site'], None))
        self.product_row.setText(QCoreApplication.translate("MainWindow", data['product'], None))
        self.size_row.setText(QCoreApplication.translate("MainWindow", data['size'], None))
        self.profile_row.setText(QCoreApplication.translate("MainWindow", data['profile'], None))
        self.proxy_row.setText(QCoreApplication.translate("MainWindow", data['proxy'], None))
        self.status_row.setText(QCoreApplication.translate("MainWindow", u"stopped", None))

    def deleteItem(self):
        self.itemDeleted.emit(self._item)
        

