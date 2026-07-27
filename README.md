# 🏠 Analyse des logements en Californie

Application interactive développée avec **Streamlit** permettant d'explorer et d'analyser le jeu de données **California Housing** à l'aide de statistiques descriptives et de visualisations graphiques.

## 📌 Présentation

Ce projet a été réalisé dans le cadre d'un cours de **Science des données**. Son objectif est d'explorer le jeu de données *California Housing* afin d'identifier les principaux facteurs influençant le prix des logements en Californie.

L'application offre une interface simple et interactive permettant de visualiser les données, d'effectuer des analyses statistiques et d'interpréter les résultats.

---

## ✨ Fonctionnalités

* 📂 Chargement automatique du jeu de données
* 🧹 Détection et traitement des valeurs manquantes
* 📋 Aperçu des données
* 📏 Calcul des statistiques descriptives
* 📊 Calcul de la variance
* 📈 Histogramme de la distribution des prix des logements
* 🌊 Répartition des logements selon la proximité de l'océan
* 🔥 Matrice de corrélation (Heatmap)
* 📉 Tableau des corrélations avec le prix des logements
* 📌 Graphique des corrélations
* 💰 Nuage de points entre le revenu médian et le prix des logements
* 📦 Boîte à moustaches des prix selon la proximité avec l'océan
* 📝 Rapport final résumant les principales observations

---

## 🛠️ Technologies utilisées

* Python
* Streamlit
* Pandas
* Matplotlib
* Seaborn
* NumPy

---

## 📂 Jeu de données

Le projet utilise le jeu de données **California Housing**, contenant des informations sur différentes zones résidentielles de Californie.

Les principales variables sont :

* Longitude
* Latitude
* Âge médian des logements
* Nombre total de pièces
* Nombre total de chambres
* Population
* Nombre de ménages
* Revenu médian
* Prix médian des logements
* Proximité avec l'océan

---

## 🚀 Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/votre-utilisateur/california-housing-analysis.git
```

### 2. Accéder au dossier

```bash
cd california-housing-analysis
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Lancer l'application

```bash
streamlit run app.py
```

---

## 📊 Contenu de l'application

### 🏠 Accueil

* Présentation du projet
* Aperçu du jeu de données

### 📄 Aperçu des données

* Nombre de lignes et de colonnes
* Types des variables
* Valeurs manquantes
* Doublons
* Variance
* Statistiques descriptives

### 📈 Visualisations

* Histogramme des prix des logements
* Répartition selon la proximité avec l'océan
* Corrélations avec le prix
* Matrice de corrélation
* Nuage de points (Revenu médian vs Prix)
* Boîte à moustaches selon la proximité avec l'océan

### 📝 Rapport

* Objectif de l'étude
* Nettoyage des données
* Principales observations
* Conclusion
* Recommandations

---

## 📈 Principales conclusions

* Le **revenu médian** est la variable la plus fortement corrélée au prix des logements.
* Les logements situés à proximité de l'océan présentent généralement des prix plus élevés.
* La localisation géographique joue un rôle important dans la valeur des logements.
* Certaines variables présentent des valeurs extrêmes pouvant influencer les analyses statistiques.

---

## 🔮 Améliorations futures

* Développer un modèle de prédiction du prix des logements.
* Ajouter des filtres interactifs pour explorer les données.
* Intégrer davantage d'indicateurs statistiques.
* Déployer l'application sur Streamlit Community Cloud.

---

## 👨‍💻 Auteur

**Salim Jouini**

Étudiant en Techniques de l'informatique
Institut Teccart — Montréal, Canada

---

## 📄 Licence

Ce projet a été réalisé à des fins pédagogiques dans le cadre d'un cours de Science des données.
