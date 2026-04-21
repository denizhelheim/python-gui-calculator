import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QColor, QPalette


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.expression = ""
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Modern Hesap Makinesi")
        self.setGeometry(100, 100, 400, 550)
        self.setStyleSheet("background-color: #1e1e1e;")
        
        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(15, 15, 15, 15)
        
        # Display
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFont(QFont("Arial", 32, QFont.Bold))
        self.display.setStyleSheet("""
            QLineEdit {
                background-color: #2d2d2d;
                color: #00ff88;
                border: 2px solid #00ff88;
                border-radius: 10px;
                padding: 15px;
                selection-background-color: #00ff88;
            }
        """)
        self.display.setReadOnly(True)
        main_layout.addWidget(self.display)
        
        # Grid layout for buttons
        grid_layout = QGridLayout()
        grid_layout.setSpacing(8)
        
        # Button layout configuration: (row, col, text, color, width)
        buttons = [
            # Row 0: Operations
            (0, 0, "C", "#ff4444", 1),
            (0, 1, "DEL", "#ff6666", 1),
            (0, 2, "√", "#ff9999", 1),
            (0, 3, "÷", "#00ff88", 1),
            
            # Row 1
            (1, 0, "7", "#333333", 1),
            (1, 1, "8", "#333333", 1),
            (1, 2, "9", "#333333", 1),
            (1, 3, "×", "#00ff88", 1),
            
            # Row 2
            (2, 0, "4", "#333333", 1),
            (2, 1, "5", "#333333", 1),
            (2, 2, "6", "#333333", 1),
            (2, 3, "-", "#00ff88", 1),
            
            # Row 3
            (3, 0, "1", "#333333", 1),
            (3, 1, "2", "#333333", 1),
            (3, 2, "3", "#333333", 1),
            (3, 3, "+", "#00ff88", 1),
            
            # Row 4
            (4, 0, "0", "#333333", 2),
            (4, 2, ".", "#333333", 1),
            (4, 3, "=", "#00ff88", 1),
        ]
        
        for row, col, text, color, width in buttons:
            button = self.create_button(text, color)
            if width == 2:
                grid_layout.addWidget(button, row, col, 1, 2)
            else:
                grid_layout.addWidget(button, row, col)
        
        main_layout.addLayout(grid_layout)
        self.setLayout(main_layout)
        
        # Set window properties
        self.setWindowOpacity(0.98)

    def create_button(self, text, color):
        button = QPushButton(text)
        button.setFont(QFont("Arial", 18, QFont.Bold))
        button.setMinimumHeight(70)
        
        if text in ["+", "-", "×", "÷", "=", "√"]:
            button.setStyleSheet(f"""
                QPushButton {{
                    background-color: {color};
                    color: #1e1e1e;
                    border: none;
                    border-radius: 10px;
                    font-weight: bold;
                }}
                QPushButton:hover {{
                    background-color: {self.lighten_color(color)};
                    transform: scale(1.05);
                }}
                QPushButton:pressed {{
                    background-color: {self.darken_color(color)};
                }}
            """)
        else:
            button.setStyleSheet(f"""
                QPushButton {{
                    background-color: {color};
                    color: #00ff88;
                    border: 2px solid #444444;
                    border-radius: 10px;
                    font-weight: bold;
                }}
                QPushButton:hover {{
                    background-color: #444444;
                    border: 2px solid #00ff88;
                }}
                QPushButton:pressed {{
                    background-color: #1a1a1a;
                }}
            """)
        
        button.clicked.connect(lambda: self.on_button_click(text))
        return button

    def lighten_color(self, color):
        # Simple color lightening
        color_map = {
            "#ff4444": "#ff6666",
            "#ff6666": "#ff8888",
            "#ff9999": "#ffaaaa",
            "#00ff88": "#22ffaa"
        }
        return color_map.get(color, color)

    def darken_color(self, color):
        # Simple color darkening
        color_map = {
            "#ff4444": "#cc0000",
            "#ff6666": "#dd0000",
            "#ff9999": "#ee0000",
            "#00ff88": "#00cc66"
        }
        return color_map.get(color, color)

    def on_button_click(self, text):
        if text == "C":
            self.expression = ""
            self.display.setText("")
        elif text == "DEL":
            self.expression = self.expression[:-1]
            self.display.setText(self.expression)
        elif text == "=":
            self.calculate()
        elif text == "√":
            self.square_root()
        elif text == "×":
            self.expression += "*"
            self.display.setText(self.expression)
        elif text == "÷":
            self.expression += "/"
            self.display.setText(self.expression)
        else:
            self.expression += text
            self.display.setText(self.expression)

    def calculate(self):
        try:
            result = eval(self.expression)
            self.expression = str(result)
            self.display.setText(self.expression)
        except:
            self.display.setText("Hata!")
            self.expression = ""

    def square_root(self):
        try:
            if self.expression:
                result = math.sqrt(float(self.expression))
                self.expression = str(result)
                self.display.setText(self.expression)
        except:
            self.display.setText("Hata!")
            self.expression = ""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
