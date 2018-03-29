import os
os.system("sudo systemctl enable myscrit.service")
os.system("sudo systemctl enable myscrit.timer")
os.system("sudo systemctl start myscrit.service")
os.system("sudo systemctl start myscrit.timer")
