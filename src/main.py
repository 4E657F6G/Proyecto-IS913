import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QProgressBar
from PyQt5.QtCore import QTimer
from modules.codeManager import CodeManager
class WindowManager(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle('Traductor de Python a C++')
        self.setGeometry(100, 100, 400, 300)

        # Crear componentes de la interfaz de usuario
        self.label_text = QLabel('Ruta del archivo:')
        self.label_path = QLabel('')
        self.button_search = QPushButton('Examinar', self)
        self.button_search.clicked.connect(self.open_file_explorer)
        self.button_quit = QPushButton('Salir', self)
        self.button_quit.clicked.connect(self.salir_aplicacion)
        self.button_translate = QPushButton('Traducir ', self)
        self.button_translate.clicked.connect(self.translate)
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)

        # Diseño de la interfaz de usuario utilizando un diseño vertical
        layout = QVBoxLayout()
        layout.addWidget(self.label_text)
        layout.addWidget(self.label_path)
        layout.addWidget(self.button_search)
        layout.addWidget(self.button_translate)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.button_quit)
        self.setLayout(layout)

    def start_progress_bar(self):
        # Establecer el valor inicial de la barra de carga
        self.actual_value = 0
        self.progress_bar.setValue(self.actual_value)

        # Configurar el temporizador para actualizar la barra de carga cada 100 ms
        self.time.start(100)

    def update_progress_bar(self):
        # Actualizar el valor de la barra de carga
        self.actual_value += 1
        self.progress_bar.setValue(self.actual_value)

        # Detener la barra de carga después de 3 segundos (3000 ms)
        if self.actual_value >= 100:
            self.time.stop()

    def open_file_explorer(self):
        # Abrir el explorador de archivos y obtener la ruta del archivo seleccionado
        path_file, _ = QFileDialog.getOpenFileName(self, 'Seleccionar Archivo', '', 'Archivos (*.*)')

        # Actualizar la etiqueta de la ruta del archivo
        self.label_path.setText(path_file)

    def salir_aplicacion(self):
        # Cerrar la aplicación al hacer clic en el botón de salir
        app.quit()

    def translate(self):
        # Instanciación de CodeManager
        #print(self.label_path.text())
        codeManager = CodeManager(self.label_path.text())

        # Configurar temporizador para actualizar la barra de carga
        self.time = QTimer(self)
        self.time.timeout.connect(self.update_progress_bar)

        # Iniciar la barra de carga
        self.start_progress_bar()


if __name__ == '__main__':
    # Crear la aplicación
    app = QApplication(sys.argv)

    # Crear la instancia de la ventana
    window = WindowManager()

    # Mostrar la ventana
    window.show()

    # Ejecutar la aplicación
    sys.exit(app.exec_())
    
