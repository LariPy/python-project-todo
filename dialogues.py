
"""
confirmation
pop up a window
ask "are you sure"
buttons "yes" and "no"
yes = returns true
no = returns false

"""

from PySide6.QtWidgets import (
    QMessageBox
)

def confirm(parent, title, message):
    result = QMessageBox.question(parent, title, message, QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
    return result == QMessageBox.StandardButton.Yes

def about(parent, title, message):
    QMessageBox.about(parent, title, message)