FROM debian:latest

# Installer les dépendances système
RUN apt update && apt install -y \
    python3 python3-venv python3-pip \
    iputils-ping nmap curl whatweb gobuster \
    git unzip wget && \
    apt clean

# Installer Nikto manuellement
RUN git clone https://github.com/sullo/nikto /opt/nikto && \
    ln -s /opt/nikto/program/nikto.pl /usr/local/bin/nikto

# Installer SecLists pour remplacer wordlists
RUN mkdir -p /usr/share/wordlists && \
    wget -qO /tmp/seclists.zip https://github.com/danielmiessler/SecLists/archive/master.zip && \
    unzip /tmp/seclists.zip -d /usr/share/wordlists && \
    rm /tmp/seclists.zip

# Création de l’environnement virtuel
RUN python3 -m venv /venv && /venv/bin/pip install --upgrade pip

# Copier le code source
WORKDIR /app
COPY . .

# Installer les dépendances Python
RUN /venv/bin/pip install -r requirements.txt

# Exposer le port Flask
EXPOSE 9001

# Démarrer l’application
CMD ["/venv/bin/python3", "app.py"]

