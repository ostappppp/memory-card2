from PyQt5.QtWidgets import *

import random

import database

import menu


app = QApplication([])
window = QWidget()
menu_btn = QPushButton("Меню")
relax_btn = QPushButton("Відпочинок")
timer_sbx = QSpinBox()
min_lbl = QLabel("Хвилини")
quest_lbl = QLabel("2+2")
var1_btn = QRadioButton("1")
var2_btn = QRadioButton("2")
var3_btn = QRadioButton("3")
var4_btn = QRadioButton("4")
answer_btn = QPushButton("Відповісти")
next_quest_btn = QPushButton("Наступне запитання")
res_lbl = QLabel("Результат")
group = QGroupBox("Варіанти відповідей")
main_line = QVBoxLayout()

horizontal_line1 = QHBoxLayout()
horizontal_line1.addWidget(menu_btn)
horizontal_line1.addStretch(1)
horizontal_line1.addWidget(relax_btn)
horizontal_line1.addWidget(timer_sbx)
main_line.addLayout(horizontal_line1)


main_line.addWidget(quest_lbl)

group_main_line = QVBoxLayout()
group_main_line.addWidget(var1_btn)
group_main_line.addWidget(var2_btn)
group_main_line.addWidget(var3_btn)
group_main_line.addWidget(var4_btn)
group_main_line.addWidget(res_lbl)
group.setLayout(group_main_line)

main_line.addWidget(group)
main_line.addWidget(answer_btn)
main_line.addWidget(next_quest_btn)

answears = [var1_btn, var2_btn,var3_btn, var4_btn]

def set_quest():
    random.shuffle(answears)
    current_question = database.questions[database.nomer]
    quest_lbl.setText(current_question["запитання"])
    answears[0].setText(current_question["Правильна відповідь"])
    answears[1].setText(current_question["Не правильна відповідь1"])
    answears[2].setText(current_question["Не правильна відповідь2"])
    answears[3].setText(current_question["Не правильна відповідь3"])
set_quest()
res_lbl.hide()
next_quest_btn.hide

def ans_func():
    if answears[0].isChecked():
        res_lbl.setText("Правильно")
    else:
        res_lbl.setText("Не правильно")
    answears[0].hide()
    answears[1].hide()
    answears[2].hide()
    answears[3].hide()
    res_lbl.show()
    next_quest_btn.show()
    answer_btn.hide()

def next_quest_func():
    answears[0].show()
    answears[1].show()
    answears[2].show()
    answears[3].show()
    res_lbl.hide()
    next_quest_btn.hide()
    answer_btn.show()
    database.nomer +=1
    set_quest()

next_quest_btn.clicked.connect(next_quest_func)
answer_btn.clicked.connect(ans_func)
menu_btn.clicked.connect(menu.menu)
window.setLayout(main_line)
window.show()
app.exec()