from PySide6.QtCore import QCoreApplication, QPropertyAnimation, QRect, QEasingCurve, Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QStackedWidget,
                               QVBoxLayout, QLabel, QToolButton, QFrame, QHBoxLayout, QPushButton)

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        # Criando o widget central
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        # Criando o QStackedWidget
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(100, 100, 600, 400)

        # Criando as páginas
        self.page1 = QWidget()
        self.page2 = QWidget()
        self.page3 = QWidget()

        # Layout para as páginas
        layout1 = QVBoxLayout(self.page1)
        layout2 = QVBoxLayout(self.page2)
        layout3 = QVBoxLayout(self.page3)

        # Conteúdo das páginas
        layout1.addWidget(QLabel("Página 1"))
        layout2.addWidget(QLabel("Página 2"))
        layout3.addWidget(QLabel("Página 3"))

        # Adicionando as páginas ao QStackedWidget
        self.stackedWidget.addWidget(self.page1)
        self.stackedWidget.addWidget(self.page2)
        self.stackedWidget.addWidget(self.page3)

        # Criando a barra lateral fechada
        self.slide_bar_close = QFrame(self.centralwidget)
        self.slide_bar_close.setObjectName("slide_bar_close")
        self.slide_bar_close.setGeometry(QRect(0, 0, 81, 541))
        self.slide_bar_close.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.slide_bar_close.setFrameShape(QFrame.Shape.StyledPanel)
        self.slide_bar_close.setFrameShadow(QFrame.Shadow.Raised)

        # Criando a barra lateral expandida
        self.slide_bar_open = QFrame(self.centralwidget)
        self.slide_bar_open.setObjectName("slide_bar_open")
        self.slide_bar_open.setGeometry(QRect(-150, 0, 150, 541))  # Inicialmente fora da tela
        self.slide_bar_open.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.slide_bar_open.setFrameShape(QFrame.Shape.StyledPanel)
        self.slide_bar_open.setFrameShadow(QFrame.Shadow.Raised)

        # Adicionando widgets à barra lateral fechada
        self.toolButton = QToolButton(self.slide_bar_close)
        self.toolButton.setObjectName("toolButton")
        self.toolButton.setGeometry(QRect(30, 20, 22, 22))
        self.toolButton.setText("☰")

        self.logo_wbp = QLabel(self.slide_bar_close)
        self.logo_wbp.setObjectName("logo_wbp")
        self.logo_wbp.setGeometry(QRect(10, 10, 49, 16))

        self.rh_btn = QToolButton(self.slide_bar_close)
        self.rh_btn.setObjectName("rh_btn")
        self.rh_btn.setGeometry(QRect(10, 70, 41, 41))
        self.rh_btn.setStyleSheet("background-color: #00D576")
        self.rh_btn.setText("RH")

        self.TI_btn = QToolButton(self.slide_bar_close)
        self.TI_btn.setObjectName("TI_btn")
        self.TI_btn.setGeometry(QRect(10, 130, 41, 41))
        self.TI_btn.setStyleSheet("background-color: #00D576")
        self.TI_btn.setText("TI")

        self.capacitaPro_btn = QToolButton(self.slide_bar_close)
        self.capacitaPro_btn.setObjectName("capacitaPro_btn")
        self.capacitaPro_btn.setGeometry(QRect(10, 190, 41, 41))
        self.capacitaPro_btn.setStyleSheet("background-color: #00D576")
        self.capacitaPro_btn.setText("Cap")

        # Adicionando widgets à barra lateral expandida
        self.logo_wbp_2 = QLabel(self.slide_bar_open)
        self.logo_wbp_2.setObjectName("logo_wbp_2")
        self.logo_wbp_2.setGeometry(QRect(0, 10, 31, 16))

        self.label = QLabel(self.slide_bar_open)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(40, 10, 81, 16))
        self.label.setText("WBP ServerPRO")

        # Layout dos botões na barra lateral expandida
        self.layoutWidget = QWidget(self.slide_bar_open)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 140, 101, 24))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.ti_brn = QToolButton(self.layoutWidget)
        self.ti_brn.setObjectName("ti_brn")
        self.ti_brn.setStyleSheet("background-color: #00D576")
        self.ti_brn.setText("TI")
        self.horizontalLayout_2.addWidget(self.ti_brn)

        self.ti_text_btn = QLabel(self.layoutWidget)
        self.ti_text_btn.setObjectName("ti_text_btn")
        self.ti_text_btn.setText("TI")
        self.horizontalLayout_2.addWidget(self.ti_text_btn)

        self.layoutWidget_2 = QWidget(self.slide_bar_open)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 200, 101, 24))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.capacita_btn = QToolButton(self.layoutWidget_2)
        self.capacita_btn.setObjectName("capacita_btn")
        self.capacita_btn.setStyleSheet("background-color: #00D576")
        self.capacita_btn.setText("Cap")
        self.horizontalLayout_3.addWidget(self.capacita_btn)

        self.capacitaPro_btn_text = QLabel(self.layoutWidget_2)
        self.capacitaPro_btn_text.setObjectName("capacitaPro_btn_text")
        self.capacitaPro_btn_text.setText("CapacitaPRO")
        self.horizontalLayout_3.addWidget(self.capacitaPro_btn_text)

        # Conectando o botão da barra lateral para alternar entre estados
        self.toolButton.clicked.connect(self.toggle_sidebar)

        # Conectar os botões para trocar de página
        self.rh_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.TI_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.capacitaPro_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))

        # Inicializar a animação da barra lateral
        self.animation = QPropertyAnimation(self.slide_bar_open, b"geometry")
        self.animation.setDuration(300)  # Duração da animação em milissegundos
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)

    def toggle_sidebar(self):
        if self.slide_bar_open.geometry().x() < 0:
            self.animation.setEndValue(QRect(0, 0, 150, 541))
            self.slide_bar_close.setGeometry(QRect(150, 0, 81, 541))  # Atualiza a posição da barra fechada
        else:
            self.animation.setEndValue(QRect(-150, 0, 150, 541))
            self.slide_bar_close.setGeometry(QRect(0, 0, 81, 541))  # Atualiza a posição da barra fechada
        self.animation.start()

# Inicialização da aplicação
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
