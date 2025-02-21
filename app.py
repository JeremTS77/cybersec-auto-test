import os
import subprocess
import logging
from flask import Flask, send_file

app = Flask(__name__)

# Configuration des logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

TARGET_DOMAIN = os.getenv('TARGET_DOMAIN', 'localhost')
RESULTS_FILE = "static/results.html"

def command_exists(cmd):
    """Vérifie si une commande est disponible sur le système."""
    return subprocess.getoutput(f"command -v {cmd}") != ""

def run_command(command):
    """Exécute une commande et gère les erreurs."""
    try:
        result = subprocess.getoutput(command)
        return result if result else "Aucune sortie"
    except Exception as e:
        return f"Erreur : {e}"

def run_tests():
    results = {}

    logging.info(f"Lancement des tests sur {TARGET_DOMAIN}")

    tests = {
        "ping": "ping -4 -c 4 " + TARGET_DOMAIN if command_exists("ping") else "ping non installé",
        "nmap_quick": f"nmap --top-ports 40 {TARGET_DOMAIN}" if command_exists("nmap") else "nmap non installé",
        "http_headers": f"curl -L -A 'Mozilla/5.0' -I https://{TARGET_DOMAIN}" if command_exists("curl") else "curl non installé",
        "whatweb": f"whatweb {TARGET_DOMAIN}" if command_exists("whatweb") else "whatweb non installé",
        "nikto": f"nikto -h {TARGET_DOMAIN}" if command_exists("nikto") else "nikto non installé",
        "gobuster_dir": f"gobuster dir -u https://{TARGET_DOMAIN} -w /usr/share/wordlists/dirb/common.txt" if command_exists("gobuster") else "gobuster non installé",
        "robots_sitemap": f"curl -s --insecure https://{TARGET_DOMAIN}/robots.txt && curl -s --insecure https://{TARGET_DOMAIN}/sitemap.xml",
        "security_headers": f"curl -I -s https://{TARGET_DOMAIN} | grep -E 'X-Frame-Options|X-XSS-Protection|X-Content-Type-Options'"
    }

    for test, command in tests.items():
        logging.info(f"Exécution de {test}")
        results[test] = run_command(command)

    logging.info("Génération du fichier HTML des résultats.")
    generate_html(results)

def generate_html(results):
    with open(RESULTS_FILE, "w") as f:
        f.write("<html><head><title>CyberSec Scan Results</title>")
        f.write('<link rel="stylesheet" href="/static/styles.css"></head>')
        f.write("<body><h1>Résultats des tests de sécurité</h1><pre>")
        for test, output in results.items():
            f.write(f"<h2>{test}</h2><pre>{output}</pre>")
        f.write("</pre></body></html>")
    logging.info("Fichier HTML des résultats généré.")

@app.route('/')
def index():
    return send_file(RESULTS_FILE)

@app.route('/run')
def manual_run():
    run_tests()
    return send_file(RESULTS_FILE)

if __name__ == "__main__":
    logging.info("Serveur lancé sur http://localhost:9001")
    run_tests()
    app.run(host='0.0.0.0', port=9001, debug=True)

