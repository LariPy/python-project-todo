
"""
Dialogues
- confirm popup for confirming an action (such as Clear List)
- about popup for Help -> About, shows app version
"""

from PySide6.QtWidgets import (
    QMessageBox
)

def confirm(parent, title, message):
    result = QMessageBox.question(parent, title, message, QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
    return result == QMessageBox.StandardButton.Yes

def about(parent, title, message):
    QMessageBox.about(parent, title, message)