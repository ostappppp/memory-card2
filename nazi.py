from PyQt5.QtWidgets import *

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
group = QGroupBox("Варіанти відповідей")
main_line = QVBoxLayout()

horizontal_line1 = QHBoxLayout
horizontal_line1.addWidget(menu_btn)
horizontal_line1.addStetch(1)
horizontal_line1.addWidget(relax_btn)
horizontal_line1.addWidget(timer_sbx)
horizontal_line1.addLayout(horizontal_line1)
main_line.addWidget(quest_lbl)

group_main_line  = QVBoxLayout
group_main_line.addWidget(var1_btn)
group_main_line.addWidget(var2_btn)
group_main_line.addWidget(var3_btn)
group_main_line.addWidget(var4_btn)
group.setLayout(group_main_line)
main_line.addWidget(group)
main_line.addWidget(quest_lbl)





window.setLayout(main_line)
window.show()
app.exec()