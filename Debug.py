"""
Большие кнопки большим парням!!!
"""

import sys
from PySide2 import QtCore, QtGui, QtWidgets
from ui import Ui_Dialog

counter = 0
fit_counter = 0
temp_counter = 0

def main():
    # Create application
    app = QtWidgets.QApplication(sys.argv)
    # Create Form and UI
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()

    # Hook Logic
    def plus_one():
        print("plus clicked")
        global counter
        global fit_counter
        counter = counter + 1
        fit_counter = fit_counter + 0.042
        setter = f"""Вопросов: {counter} Каллорий: {round(fit_counter, 2)}"""
        ui.result_label.setText(setter)

    def minus_one():
        print("minus clicked")
        global counter
        global fit_counter
        counter = counter - 1
        fit_counter = fit_counter + 0.042
        setter = f"""Вопросов: {counter} Каллорий: {round(fit_counter, 2)}"""
        ui.result_label.setText(setter)

    def edit_counter():
        print("set counter start clicked")
        global counter
        global fit_counter
        fit_counter = fit_counter + 0.042
        counter = ui.set_counter_line_edit.text()
        if counter.isdigit():
            counter = int(counter)
            setter = f"""Вопросов: {counter} Каллорий: {round(fit_counter, 2)}"""
            ui.result_label.setText(setter)

    def cancel():
        print("canceled")
        ui.result_label.setText("Эту херню я не делал. В пизду.")

    ui.plus_button.clicked.connect(plus_one)
    ui.minus_button.clicked.connect(minus_one)
    ui.set_counter.clicked.connect(edit_counter)
    ui.reset_counter.clicked.connect(cancel)


    # Run main loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


