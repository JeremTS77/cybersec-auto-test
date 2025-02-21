# CyberSec Scanner

CyberSec Scanner est un outil d'analyse de sécurité automatisé conçu pour identifier les vulnérabilités d'un domaine ou d'une IP en exécutant plusieurs tests :

- Scan rapide des ports avec **Nmap**
- Récupération des en-têtes HTTP
- Analyse des technologies utilisées avec **WhatWeb**
- Détection des vulnérabilités avec **Nikto**
- Scan de répertoires cachés avec **Gobuster**

Le projet génère une page web statique affichant les résultats des tests en temps réel.

## 🚀 Installation et exécution

### Prérequis
- Docker & Docker Compose installés

### Installation
Clone ce dépôt et lance le scanner avec :

```sh
# Cloner le dépôt
git clone https://github.com/ton-github/cybersec-scanner.git
cd cybersec-scanner
```

Avant de lancer le service, vous devez définir la cible à scanner. Pour cela, modifiez la variable `TARGET_DOMAIN` dans le fichier `docker-compose.yml` :
```yaml
environment:
  - TARGET_DOMAIN=example.com

# Construire et lancer les conteneurs
docker compose up --build -d
```

Le service sera accessible sur `http://localhost:9001`.

## 📋 Fonctionnalités

1. **Scan des ports** : Utilise `nmap` pour identifier les ports ouverts.
2. **Analyse HTTP** : Récupère les en-têtes HTTP pour identifier d'éventuels problèmes de sécurité.
3. **Détection de technologies** : WhatWeb analyse les frameworks et services utilisés.
4. **Recherche de vulnérabilités** : Nikto scanne les failles courantes.
5. **Scan des répertoires cachés** : Gobuster cherche des fichiers ou dossiers non protégés.
6. **Affichage en temps réel** : Résultats affichés via une page web statique.

## 🛠️ Développement
Si tu veux modifier ou améliorer le projet :

```sh
# Arrêter le conteneur
docker compose down

# Modifier le code
nano app.py  # ou autre fichier

# Relancer
docker compose up --build -d
```

## 📄 Licence
Ce projet est sous licence MIT. Tu peux l'utiliser, le modifier et le partager librement.

---

💡 **Idées d'amélioration ?** N'hésite pas à ouvrir une issue ou à proposer une pull request ! 😉


