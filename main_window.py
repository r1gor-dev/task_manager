from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Менеджер задач")
        self.resize(500, 400)

        center= QWidget()
        self.setCentralWidget(center)
        layout = QVBoxLayout()

        self.task_label = QLabel("Новая задача:")
        layout.addWidget(self.task_label)

        
        input_layout= QHBoxLayout()
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Название задачи")
        self.add_button = QPushButton("Добавить")
        input_layout.addWidget(self.task_input)
        input_layout.addWidget(self.add_button)
        layout.addLayout(input_layout)
        self.tasK_list = QListWidget()
        layout.addWidget(self.tasK_list)

        buttons_layout = QHBoxLayout()
        self.delete_button = QPushButton("Удалить")
        self.clear_button = QPushButton("Очистить всё")
        buttons_layout.addWidget(self.delete_button)
        buttons_layout.addWidget(self.clear_button)
        layout.addLayout(buttons_layout)
        self.counter_label = QLabel("Количество задач: 0")
        layout.addWidget(self.counter_label)
        
        center.setLayout(layout)