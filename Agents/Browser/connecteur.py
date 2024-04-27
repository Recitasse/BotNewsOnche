from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


# Chemin vers votre profil Firefox
profile_path = "/chemin/vers/votre/profil"

# Créer un objet FirefoxProfile en utilisant le chemin du profil
profile = FirefoxProfile(profile_path)

# Configuration des options de Firefox
options = Options()
options.headless = True  # Exécution en mode sans tête

# Initialisation du driver de Firefox avec le profil chargé
driver = webdriver.Firefox(firefox_profile=profile, options=options)