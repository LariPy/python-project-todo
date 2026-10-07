from PySide6.QtWidgets import (
    QApplication, QScrollArea, QWidget, QVBoxLayout, QLabel
)

app = QApplication([])

content = QWidget()
layout = QVBoxLayout(content)
for i in range(50):
    layout.addWidget(QLabel(f"Row {i}"))

scroll = QScrollArea()
scroll.setWidget(content)
scroll.setWidgetResizable(True)
scroll.resize(300, 400)
scroll.show()

app.exec()