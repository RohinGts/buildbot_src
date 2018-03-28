binary:
    # we are not going to build anything

install:
	sudo cp final.sh /home/$(USER)/final.sh
	sudo cp myscrit.service /etc/systemd/system/myscrit.service
	sudo cp myscrit.timer  /etc/systemd/system/myscrit.timer
	sudo systemctl enable myscrit.timer
	sudo systemctl enable myscrit.service
	sudo systemctl start myscrit.timer myscrit.service
