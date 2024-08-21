from PySide6.QtCore import QSize, Qt, QPropertyAnimation, QRect, QEasingCurve
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication, QFrame, QHBoxLayout, QMainWindow, QPushButton,
    QStackedWidget, QVBoxLayout, QWidget, QSizePolicy
)

class SlideMenu(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Frame para os botões principais
        self.button_frame = QFrame()
        self.button_frame.setLayout(QVBoxLayout())
        self.button_frame.setMinimumWidth(150)
        self.layout.addWidget(self.button_frame)

        # Botões principais
        self.btn_ti = QPushButton("TI")
        self.btn_rh = QPushButton("RH")
        self.btn_capacita_pro = QPushButton("CAPACITAPRO")
        
        self.button_frame.layout().addWidget(self.btn_ti)
        self.button_frame.layout().addWidget(self.btn_rh)
        self.button_frame.layout().addWidget(self.btn_capacita_pro)

        # Frame para opções adicionais
        self.expandable_frame = QFrame()
        self.expandable_frame.setLayout(QVBoxLayout())
        self.expandable_frame.setStyleSheet("background-color: #2E2E2E; color: white;")
        self.expandable_frame.setMinimumWidth(150)
        self.expandable_frame.setMaximumHeight(0)  # Começa contraído
        self.layout.addWidget(self.expandable_frame)

        # Opções adicionais
        self.extra_content_btn1 = QPushButton("Opção 1")
        self.extra_content_btn2 = QPushButton("Opção 2")
        self.expandable_frame.layout().addWidget(self.extra_content_btn1)
        self.expandable_frame.layout().addWidget(self.extra_content_btn2)

        # Botão para expandir/contrair
        self.toggle_button = QPushButton("Ver Mais")
        self.toggle_button.clicked.connect(self.toggle_expand)
        self.layout.addWidget(self.toggle_button)

        # Layout de espaçamento
        self.layout.addStretch()

        # Animação
        self.animation = QPropertyAnimation(self.expandable_frame, b"maximumHeight")
        self.animation.setDuration(300)  # Tempo da animação (milissegundos)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)  # Curva de suavização

    def toggle_expand(self):
        if self.expandable_frame.height() == 0:
            # Expandir
            self.animation.setStartValue(0)
            self.animation.setEndValue(100)  # Ajuste conforme necessário
            self.toggle_button.setText("Ver Menos")
        else:
            # Contrair
            self.animation.setStartValue(self.expandable_frame.height())
            self.animation.setEndValue(0)
            self.toggle_button.setText("Ver Mais")

        self.animation.start()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menu Navigation App")
        self.setGeometry(100, 100, 800, 600)

        # Layout principal
        main_layout = QHBoxLayout()

        # Instanciando o SlideMenu
        self.slide_menu = SlideMenu()
        main_layout.addWidget(self.slide_menu)

        # QStackedWidget para páginas
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.create_page("TI"))
        self.stacked_widget.addWidget(self.create_page("RH"))
        self.stacked_widget.addWidget(self.create_page("CAPACITAPRO"))

        # Conectando os botões do SlideMenu aos widgets
        self.slide_menu.btn_ti.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        self.slide_menu.btn_rh.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        self.slide_menu.btn_capacita_pro.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))

        # Layout principal
        main_layout.addWidget(self.stacked_widget)

        # Widget central
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def create_page(self, name):
        """Cria uma página simples com um QLabel mostrando o nome."""
        page = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QPushButton(f"Conteúdo da página {name}"))
        page.setLayout(layout)
        return page

if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()
