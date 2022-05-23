FROM selenium/standalone-chrome:latest

RUN sudo apt-get update -y
RUN sudo apt install python3-pip -y
RUN sudo pip3 install selenium==4.1.3
# RUN sudo pip3 install -r requirements.txt

COPY main.py /home/seluser/main.py
COPY ./scrapack home/seluser/scrapack
COPY scrap.py /home/seluser/scrap.py

WORKDIR /home/seluser

ENTRYPOINT [ "python3", "main.py" ]
