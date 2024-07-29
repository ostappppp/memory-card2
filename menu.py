from PyQt5.QtWidgets import *

def menu():
    window = QDialog()
    main_line = QVBoxLayout()

    add_btn = QPushButton("Добавити")
    quest_lbl = QLabel("Запитання")
    quest_ledt = QLineEdit()

    h1 = QHBoxLayout()
    h1.addWidget(quest_lbl)
    h1.addWidget(quest_ledt)
    main_line.addLayout(h1)

    right_lbl = QLabel("Правильна відповідь")
    right_ledt = QLineEdit()

    h2 = QHBoxLayout()
    h2.addWidget(right_lbl)
    h2.addWidget(right_ledt)
    main_line.addLayout(h2)

    incorrect_lbl = QLabel("Неравильна відповідь")
    incorrect_ledt = QLineEdit()

    h3 = QHBoxLayout()
    h3.addWidget(incorrect_lbl)
    h3.addWidget(incorrect_ledt)
    main_line.addLayout(h3)

    incorrect_lbl = QLabel("Неравильна відповідь")
    incorrect_ledt = QLineEdit()

    h4 = QHBoxLayout()
    h4.addWidget(incorrect_lbl)
    h4.addWidget(incorrect_ledt)
    main_line.addLayout(h3)

    incorrect_lbl = QLabel("Неравильна відповідь")
    incorrect_ledt = QLineEdit()

    h5 = QHBoxLayout()
    h5.addWidget(incorrect_lbl)
    h5.addWidget(incorrect_ledt)
    main_line.addLayout(h3)

    def add_func():
        new_quest = {
        "запитання": quest_ledt.text(),
        "Правильна відповідь": right_ledt.text(),
        "Не правильна відповідь1": incorrect_ledt.text(),
        "Не правильна відповідь2": "10",
        "Не правильна відповідь3": "8",
        }

    add_btn.questions.append(new_quest)
    main_line.addWidget(add_btn)


    window.setLayout(main_line)
    window.exec()