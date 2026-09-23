from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Менеджер задач")
        self.resize(500, 400)

        self.init_ui()
        self.connect_signals()
        self.update_counter()

    def init_ui(self):
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
        self.task_list = QListWidget()
        layout.addWidget(self.task_list)

        buttons_layout = QHBoxLayout()
        self.delete_button = QPushButton("Удалить")
        self.delete_marked_button = QPushButton("Удалить выполненные")
        self.clear_button = QPushButton("Очистить всё")
        buttons_layout.addWidget(self.delete_button)
        buttons_layout.insertWidget(1, self.delete_marked_button)
        buttons_layout.addWidget(self.clear_button)
        layout.addLayout(buttons_layout)
        self.counter_label = QLabel("Количество задач: 0")
        layout.addWidget(self.counter_label)

        center.setLayout(layout)

    def connect_signals(self):
        self.add_button.clicked.connect(self.add_task)
        self.task_input.returnPressed.connect(self.add_task)
        self.delete_button.clicked.connect(self.delete_task)
        self.delete_marked_button.clicked.connect(self.delete_marked_tasks)
        self.task_list.itemChanged.connect(self.update_counter)
        self.clear_button.clicked.connect(self.clear_tasks)

    def update_counter(self):
        cnt = self.task_list.count()
        marked = sum(
            1 for i in range(cnt)
                if self.task_list.item(i).checkState() == Qt.CheckState.Checked
        )
        self.counter_label.setText(f"Количество задач: {cnt} | Выполнено: {marked}")

    def delete_marked_tasks(self):
        rm_flag = False
        for i in range(self.task_list.count()-1,-1,-1):
            if self.task_list.item(i).checkState()==Qt.CheckState.Checked:
                self.task_list.takeItem(i)
                rm_flag=True
        if rm_flag:
            self.update_counter()
        else:
            QMessageBox.information(self,"Инфа",
                "Вы ещё не выполнили задачи, чтобы их удалять.")
        
    def clear_tasks(self):
        if self.task_list.count()==0:
            return
        ans= QMessageBox.question(self, "Очистка",
                        "Вы точно хотите удалить все задачи?")
        if ans == QMessageBox.StandardButton.Yes:
            self.task_list.clear()
            self.update_counter()

    def delete_task(self):
        r = self.task_list.currentRow()
        if r>=0:
            ans= QMessageBox.question(self, "Удаление",
                        "Вы хотите удалить указанную задачу?")
            if ans == QMessageBox.StandardButton.Yes:
                self.task_list.takeItem(r)
                self.update_counter()
        else:
            QMessageBox.warning(self, "Ошибка","Выберите задачу для удаления")


    def add_task(self):
        text = self.task_input.text().strip()
        if text:
            item = QListWidgetItem(text)
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            item.setCheckState(Qt.CheckState.Unchecked)
            self.task_list.addItem(item)
            # self.task_list.addItem(text)
            self.task_input.clear()
            self.update_counter()
        else:
            QMessageBox.warning(self, "Ошибка", "Введите название задачи")
