import sys
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setWindowTitle("Web Automation App")
        self.setGeometry(100, 100, 800, 600)
        
        layout = QVBoxLayout()

        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Enter Email")
        layout.addWidget(self.email_input)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Enter Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)
        
        self.run_button = QPushButton("Run Automation", self)
        self.run_button.clicked.connect(self.run_automation)
        layout.addWidget(self.run_button)
        
        self.status_label = QLabel("Status: Idle", self)
        layout.addWidget(self.status_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def run_automation(self):
        self.status_label.setText("Status: Running...")
        
        config = {
            "email": self.email_input.text(),
            "password": self.password_input.text(),
            "offerdetails": {
                "offername": "Sample Offer",
                "offerdisplay": "Sample Offer Display",
                "offerterms": "Terms and conditions here...",
                "offertype": "instant"
            },
            "discount": {
                "mov": "100",
                "discountworth": "10"
            }
        }

        options = webdriver.ChromeOptions()
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-setuid-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=options)
        driver.get('https://dashboard.razorpay.com/?screen=sign_in')
        
        try:
            # Perform login
            email_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="Email or Mobile Number"]'))
            )
            email_input.send_keys(config['email'])

            password_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="Password"]'))
            )
            password_input.send_keys(config['password'])

            # Add more automation steps as per your original script

            self.status_label.setText("Status: Completed")
        except Exception as e:
            self.status_label.setText(f"Status: Error - {str(e)}")
        finally:
            driver.quit()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
