from PySide6.QtWidgets import QWidget, QLabel,QMessageBox, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton
import requests, os
from PySide6.QtGui import QPixmap

from display_window import DisplayWindow



class SearchWindow(QWidget):
    
    def __init__(self):
        super().__init__()
       
        self.w = None        
        self.setFixedSize(850, 500)

        self.bg_img_label = QLabel(self)
        self.bg_img_label.setGeometry(0,0,850,500)
        self.bg_img_label.setStyleSheet("background-image: url('../assets/landing.jpg')")
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20) 
        self.textbox.setGeometry(50, 50, 280, 40)

        self.poke_url = "https://pokeapi.co/api/v2/pokemon/"      
        
        label1 = QLabel("Enter the name", self)
        label1.setGeometry(50, 5, 600, 70)

        enter_button = QPushButton("Search", self)
        enter_button.setGeometry(50, 300, 160, 43)
        enter_button.clicked.connect(self.data_fetch)  

        capture_button = QPushButton("Capture", self)
        capture_button.setGeometry(50, 350, 160, 43)
        capture_button.clicked.connect(self.capture_pokemon)

        display_button = QPushButton("Display", self)
        display_button.setGeometry(50, 400, 160, 43)
        display_button.clicked.connect(self.display_in_new_window)

    def data_fetch(self):
        self.clear_previous_pokemon_info()
        
        self.pokemon_name = self.textbox.text()
        print("Name: " + self.pokemon_name)
        res = requests.get(self.poke_url + self.pokemon_name)
        
        self.image_url = res.json()["sprites"]["other"]["home"]["front_default"]
        
        p_abilities = res.json()["abilities"]
        self.abilities_str = ''
        for i in range(len(p_abilities)):
            self.abilities_str = self.abilities_str + p_abilities[i]['ability']['name'] + ','
        self.abilities_str = self.abilities_str[:-1]
        print("Abilities: " + self.abilities_str)

        self.p_types = ''
        for i in range(len(res.json()["types"])):
            self.p_types = self.p_types + res.json()["types"][i]['type']['name'] + ','
        self.p_types = self.p_types[:-1]
        print("Types: " + self.p_types)

        print("Stats: ")
        stats = res.json()['stats']
        stat_dict = {item['stat']['name']: item['base_stat'] for item in stats}
        print(stat_dict)  

        self.bg_img_label.setHidden(True)
        self.pokemon_img = QLabel(self)
        pixmap = QPixmap()
        
        image_data = requests.get(self.image_url).content
        pixmap.loadFromData(image_data)
        self.pokemon_img.setPixmap(pixmap)
        self.pokemon_img.setGeometry(450,30,200,200) 
        self.pokemon_img.setScaledContents(True)
        self.pokemon_img.show() 

        self.name_label = QLabel("Name: " + self.pokemon_name, self)
        self.name_label.setGeometry(450,40,500,500)
        self.name_label.show()
        
        self.abilities_label = QLabel("Abilities: " + self.abilities_str, self)
        self.abilities_label.setGeometry(450,60,500,500)
        self.abilities_label.show()

        self.types_label = QLabel("Types: " + self.p_types, self)
        self.types_label.setGeometry(450,80,500,500)
        self.types_label.show()

        self.stats_label = QLabel("Stats:", self)
        self.stats_label.setGeometry(450,100,500,500)
        self.stats_label.show()

        self.hp_label = QLabel("Hp: " + str(stat_dict["hp"]), self)
        self.hp_label.setGeometry(450,120,500,500)
        self.hp_label.show()

        self.attack_label = QLabel("Attack: " + str(stat_dict["attack"]), self)
        self.attack_label.setGeometry(450,140,500,500)
        self.attack_label.show()

        self.defense_label = QLabel("Defense: " + str(stat_dict["defense"]), self)
        self.defense_label.setGeometry(450,160,500,500)
        self.defense_label.show()

        self.sa_label = QLabel("Special-attack: " + str(stat_dict["special-attack"]), self)
        self.sa_label.setGeometry(450,180,500,500)
        self.sa_label.show()

        self.sd_label = QLabel("Special-defense: " + str(stat_dict["special-defense"]), self)
        self.sd_label.setGeometry(450,200,500,500)
        self.sd_label.show()

        self.speed_label = QLabel("Speed: " + str(stat_dict["speed"]), self)
        self.speed_label.setGeometry(450,220,500,500)
        self.speed_label.show()

    def capture_pokemon(self):
        captured_poke_folder = "../captured/"
        fpath = captured_poke_folder + self.pokemon_name + ".png"
        file_exists = os.path.isfile(fpath)
        print("file exists? " + str(file_exists))
        if file_exists:
           
            msg = QMessageBox(self)
            msg.setWindowTitle("Error")
            msg.setText("Already Captured!")
            msg.exec()  
        else: 
            image_data = requests.get(self.image_url).content
            with open(fpath, "wb") as f:
                f.write(image_data) 

            msg = QMessageBox(self)
            msg.setWindowTitle("Success")
            msg.setText("Pokemon Successfully Captured!")
            msg.exec()    

    def display_in_new_window(self,checked):
        if self.w is None:
            self.w = DisplayWindow()
        self.w.show()

    def clear_previous_pokemon_info(self):
        try:
            self.pokemon_img.setParent(None)
            self.name_label.setParent(None)
            self.abilities_label.setParent(None)
            self.types_label.setParent(None)
            self.stats_label.setParent(None)
            self.hp_label.setParent(None)
            self.attack_label.setParent(None)
            self.defense_label.setParent(None)
            self.sa_label.setParent(None)
            self.sd_label.setParent(None)
            self.speed_label.setParent(None)
        except:
            print("not assigned yet")

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())
