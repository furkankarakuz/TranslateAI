from PyQt5.QtWidgets import QLabel, QPushButton, QApplication, QVBoxLayout, QDialog, QRadioButton, QGridLayout, QGroupBox, QButtonGroup, QTabWidget, QWidget, QListWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from circle_widget import CircleWidget
from device_process import Device
from model_process import Model
import sys


mp = Model()
dp = Device()
device_list = dp.get_device_list()

lang_list = ["TR-EN", "TR-ES", "TR-FR", "EN-TR", "EN-ES", "EN-FR", "ES-EN", "ES-FR", "FR-EN", "FR-ES"]


class MainDialog(QDialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)

        self.setWindowTitle("TranslateAI APP")
        self.setWindowIcon(QIcon("images/logo.png"))
        self.setFixedWidth(350)

        self.initUI()

    def initUI(self):
        self.main_box = QVBoxLayout()

        self.input_devices = QListWidget()
        self.input_devices.setSpacing(3)

        for device in device_list:
            self.input_devices.addItem(device[0])

        self.input_devices.currentRowChanged.connect(self.select_input_device)
        self.input_devices.setCurrentRow(0)

        self.lang_radio_group = QButtonGroup()
        radio_layout = QVBoxLayout()

        for index, lang in enumerate(lang_list):
            lang_radio = QRadioButton(lang)

            if index == 0:
                lang_radio.setChecked(True)

            self.lang_radio_group.addButton(lang_radio, index)
            radio_layout.addWidget(lang_radio)

        radio_layout.deleteLater()
        self.lang_radio_group.buttonClicked.connect(self.select_language)

        lang_tab = QTabWidget()
        lang_tab.tabBar().setExpanding(True)
        lang_tab.addTab(self.lang_tab(range(0, 3)), QIcon("images/TR.png"), "TR")
        lang_tab.addTab(self.lang_tab(range(3, 6)), QIcon("images/EN.png"), "EN")
        lang_tab.addTab(self.lang_tab(range(6, 8)), QIcon("images/ES.png"), "ES")
        lang_tab.addTab(self.lang_tab(range(8, 10)), QIcon("images/FR.png"), "FR")

        group_box1 = QGroupBox("Device", self)
        group_box1.setAlignment(Qt.AlignCenter)

        group_box2 = QGroupBox("Language", self)
        group_box2.setAlignment(Qt.AlignCenter)

        grid_box1 = QGridLayout()
        grid_box1.addWidget(self.input_devices, 0, 0)
        group_box1.setLayout(grid_box1)

        grid_box2 = QGridLayout()
        grid_box2.addWidget(lang_tab, 0, 0, 1, 2)
        group_box2.setLayout(grid_box2)

        self.download_model_button = QPushButton("Download Model", clicked=self.download_model)
        self.download_model_button.setMinimumHeight(30)

        self.record_button = QPushButton("Start Record", clicked=self.record)
        self.record_button.setMinimumHeight(30)
        self.record_button.setVisible(False)

        self.download_model_status = QLabel()
        self.record_status = QLabel()

        self.circle_widget = QLabel()

        main_widget_list = [group_box1, group_box2, self.download_model_button, self.download_model_status, self.record_button, self.record_status, self.circle_widget]

        for main_widget in main_widget_list:
            self.main_box.addWidget(main_widget)

        self.select_language()
        self.setLayout(self.main_box)

    def select_input_device(self, row):
        self.device_index = device_list[row][1]

    def lang_tab(self, range_list):
        part = QWidget()
        grid = QGridLayout()

        for index, widget in enumerate(range_list):
            grid.addWidget(self.lang_radio_group.button(widget), 0, index)

        part.setLayout(grid)
        self.update()
        return part

    def select_language(self):
        selected_language_id = self.lang_radio_group.checkedId()
        self.selected_language = self.lang_radio_group.button(selected_language_id).text()

        self.download_model_button.setText(f"{self.selected_language} - Use Model")
        self.record_button.setVisible(False)
        self.download_model_status.setVisible(False)
        self.record_button.setText("Stop Record")
        self.record()
        QApplication.processEvents()

    def download_model(self):
        self.record_button.setVisible(False)
        self.download_model_status.setVisible(True)
        self.download_model_status.setText(f"<center><h4> ⏳ {self.selected_language} Model is Loading ...</h4></center>")
        QApplication.processEvents()

        mp.select_model(self.selected_language.lower())
        dp.audio_language(self.selected_language.lower().split("-")[0])
        self.download_model_status.setText(f"<center><h4> ✅ {self.selected_language} Model is Ready </h4></center>")

        dp.device_use_model(mp.use_model())
        self.record_button.setVisible(True)
        self.record_button.setText("Start Record")
        QApplication.processEvents()

    def record(self):
        if self.record_button.text() == "Start Record":
            self.start_circle(self.device_index)
            dp.connect_device(self.device_index)

            QApplication.processEvents()
            self.record_button.setText("Stop Record")
            self.record_status.setText("<center><h4>🔴 Recording ...</h4></center>")

        else:
            try:
                self.stop_circle()
                dp.stop_connect()

                QApplication.processEvents()
                self.record_button.setText("Start Record")
                self.record_status.setText("")
            except:  # noqa 
                pass

    def start_circle(self, index):
        if isinstance(self.circle_widget, QLabel):
            self.main_box.removeWidget(self.circle_widget)
            self.circle_widget.deleteLater()
            self.circle_widget = CircleWidget(self.device_index)
            self.main_box.addWidget(self.circle_widget)

    def stop_circle(self):
        if isinstance(self.circle_widget, CircleWidget):
            self.circle_widget.stop()
            self.main_box.removeWidget(self.circle_widget)
            self.circle_widget.deleteLater()
            self.circle_widget = QLabel()
            self.main_box.addWidget(self.circle_widget)

            self.adjustSize()

    def closeEvent(self, event):
        self.stop_circle()
        event.accept()


app = QApplication(sys.argv)
app.setStyle("Fusion")

window = MainDialog()
window.setWindowFlags(window.windowFlags() & ~ Qt.WindowContextHelpButtonHint)
window.show()

sys.exit(app.exec())
