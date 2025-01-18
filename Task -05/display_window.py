from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QApplication
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import os

class DisplayWindow(QWidget):
    def __init__(self):
        super().__init__()
      
        self.setWindowTitle("Image Viewer")
        self.setFixedSize(850, 500)
      
        self.image_dir = os.path.join(os.path.dirname(__file__), "..", "captured")
        self.image_files = [f for f in os.listdir(self.image_dir) if f.lower().endswith('.png')]
        self.current_index = 0
        
        if not self.image_files:
            raise FileNotFoundError("No PNG images found in the 'captured' directory.")

        next_button = QPushButton("Next", self)
        next_button.setGeometry(500, 400, 200, 40)
        next_button.clicked.connect(self.show_next_image)
        
        previous_button = QPushButton("Previous", self)
        previous_button.setGeometry(100, 400, 200, 40)
        previous_button.clicked.connect(self.show_previous_image)

        self.pokemon_img = QLabel(self)
        self.pokemon_img.setGeometry(200, 10, 400, 400) 
        self.pokemon_img.setScaledContents(True)

        self.image_name_label = QLabel(self)
        self.image_name_label.setGeometry(550, 150, 300, 200)  
        self.image_name_label.setStyleSheet("color: white; font-size: 32px; font-weight: bold;")
        self.image_name_label.setAlignment(Qt.AlignCenter) 
        
        self.show_image()

    def show_image(self):
        image_path = os.path.join(self.image_dir, self.image_files[self.current_index])
        pixmap = QPixmap(image_path)
        self.pokemon_img.setPixmap(pixmap) 
        image_name = os.path.splitext(self.image_files[self.current_index])[0]
        self.image_name_label.setText(image_name)

    def show_next_image(self):
        self.current_index = (self.current_index + 1) % len(self.image_files)
        self.show_image()

    def show_previous_image(self):
        self.current_index = (self.current_index - 1) % len(self.image_files)
        self.show_image()

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = DisplayWindow()
    window.show()
    sys.exit(app.exec())

