import sys
import string
import random
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
    QComboBox, QSpinBox, QMessageBox
)
from PyQt5.QtCore import Qt


class PasswordGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()

        # Window setup
        self.setWindowTitle("Password Generator")
        self.setGeometry(100, 100, 400, 300)

        # Instructions Label for character types
        instruction_label = QLabel("Choose the type of characters for your password:")
        self.choice_combo = QComboBox()
        self.choice_combo.addItems([
            "1. Lowercase",
            "2. Uppercase",
            "3. Digits",
            "4. Special characters",
            "5. Apply all"
        ])

        # Label and SpinBox for password length
        length_label = QLabel("Enter the length of the password:")
        self.length_spinbox = QSpinBox()
        self.length_spinbox.setRange(1, 100)
        self.length_spinbox.setValue(10)  # Default length

        # Button to trigger password generation
        self.generate_button = QPushButton("Generate Password")
        self.generate_button.clicked.connect(self.generate_password)

        # Label to display the generated password
        self.display_label = QLabel("")
        self.display_label.setAlignment(Qt.AlignCenter)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(instruction_label)
        layout.addWidget(self.choice_combo)
        layout.addWidget(length_label)
        layout.addWidget(self.length_spinbox)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.display_label)

        self.setLayout(layout)

    def generate_password(self):
        # Get user choice from the ComboBox
        choice = self.choice_combo.currentIndex() + 1

        # Get password length from SpinBox
        length = self.length_spinbox.value()

        # Define character list based on user's choice
        charlist = ""
        if choice == 1:
            charlist = string.ascii_lowercase
        elif choice == 2:
            charlist = string.ascii_uppercase
        elif choice == 3:
            charlist = string.digits
        elif choice == 4:
            charlist = string.punctuation
        elif choice == 5:
            charlist = string.ascii_letters + string.digits + string.punctuation

        # Generate a password of the specified length using random characters from charlist
        password = ''.join(random.choice(charlist) for _ in range(length))

        # Display the generated password
        self.display_label.setText(f"Your password: {password}")


# Run the application
app = QApplication(sys.argv)
window = PasswordGeneratorApp()
window.show()
sys.exit(app.exec_())
