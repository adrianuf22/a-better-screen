#! /bin/sh

sudo rm /usr/local/bin/chcolor
sudo ln -s $(pwd)/bin/chcolor /usr/local/bin/chcolor

sudo rm /usr/local/bin/chres
sudo ln -s $(pwd)/bin/chres.py /usr/local/bin/chres

sudo chown $USER:$USER /usr/local/bin/chcolor -h
sudo chown $USER:$USER /usr/local/bin/chres -h

touch /home/$USER/.config/a-better-screen.cfg