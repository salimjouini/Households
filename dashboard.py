import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Analyse des logements",
    
    layout="wide"
)


@st.cache_data
def charger_donnees():
    return pd.read_csv("housing.csv")


try:
    data = charger_donnees()

except FileNotFoundError:
    st.error(
        "Le fichier housing.csv est introuvable. "
        "Place-le dans le même dossier que ton fichier Python."
    )
    st.stop()


missing_before = data.isnull().sum()


data["total_bedrooms"] = data["total_bedrooms"].fillna(
    data["total_bedrooms"].median()
)


st.sidebar.title("Analyse des logements")

menu = st.sidebar.selectbox(
    "Navigation",
    [
        "Accueil",
        "Aperçu des données",
        "Graphiques",
        "Rapport"
    ]
)


if menu == "Accueil":
    st.title("Analyse des prix des logements en Californie")

    st.write(
        """
        Cette application permet d'explorer le jeu de données
        California Housing et d'identifier les caractéristiques
        qui influencent le prix des logements.
        """
    )

    st.subheader("Aperçu des données")
    st.dataframe(data.head(), use_container_width=True)



elif menu == "Aperçu des données":
    st.header("Aperçu du jeu de données")

    st.subheader("Dimensions des données")

    col1, col2 = st.columns(2)

    col1.metric("Nombre de lignes", data.shape[0])
    col2.metric("Nombre de colonnes", data.shape[1])

    st.subheader("Les 5 premières lignes")
    st.dataframe(data.head(), use_container_width=True)

    st.subheader("Les 5 dernières lignes")
    st.dataframe(data.tail(), use_container_width=True)

    st.subheader("Types des données")
    st.dataframe(
        data.dtypes.astype(str).rename("Type").to_frame(),
        use_container_width=True
    )

    st.subheader("Valeurs manquantes avant le nettoyage")
    st.dataframe(
        missing_before.rename("Valeurs manquantes").to_frame(),
        use_container_width=True
    )

    st.subheader("Valeurs manquantes après le nettoyage")
    st.dataframe(
        data.isnull()
        .sum()
        .rename("Valeurs manquantes")
        .to_frame(),
        use_container_width=True
    )

    st.subheader("Nombre de doublons")
    st.write(data.duplicated().sum())

    st.subheader("Variance des variables numériques")
    st.dataframe(
        data.var(numeric_only=True)
        .rename("Variance")
        .to_frame(),
        use_container_width=True
    )

    st.subheader("Statistiques descriptives")
    st.dataframe(
        data.describe(),
        use_container_width=True
    )



elif menu == "Graphiques":
    st.header("Visualisations")

    
    st.subheader("Distribution des prix des logements")

    figure_hist, ax_hist = plt.subplots(figsize=(9, 6))

    ax_hist.hist(
        data["median_house_value"],
        bins=30,
        color="skyblue",
        edgecolor="black",
        density=True
    )

    
    moyenne = data["median_house_value"].mean()
    ecart_type = data["median_house_value"].std()

    xmin, xmax = ax_hist.get_xlim()

    x = np.linspace(xmin, xmax, 1000)

    p = (
        np.exp(
            -((x - moyenne) ** 2) / (2 * ecart_type ** 2)
        )
        / (ecart_type * np.sqrt(2 * np.pi))
    )

    ax_hist.plot(
        x,
        p,
        color="red",
        linewidth=2,
        label="Courbe normale"
    )

    ax_hist.set_title(
        "Histogramme de la distribution des prix des logements"
    )
    ax_hist.set_xlabel("Prix des logements")
    ax_hist.set_ylabel("Densité")
    ax_hist.legend()

    figure_hist.tight_layout()

    st.pyplot(figure_hist)
    plt.close(figure_hist)

    
    
    corr = data.corr(numeric_only=True)

    st.subheader("Corrélation avec le prix des maisons")

    correlation_prix = (
        corr["median_house_value"]
        .drop("median_house_value")
        .sort_values(ascending=False)
    )

    st.dataframe(
        correlation_prix
        .rename("Corrélation avec le prix")
        .to_frame(),
        use_container_width=True
    )

    # Graphique horizontal des corrélations
    figure_bar_corr, ax_bar_corr = plt.subplots(figsize=(9, 5))

    correlation_prix.sort_values().plot(
        kind="barh",
        ax=ax_bar_corr
    )

    ax_bar_corr.set_xlabel("Coefficient de corrélation")
    ax_bar_corr.set_ylabel("Attribut")
    ax_bar_corr.set_title(
        "Corrélation des attributs numériques avec le prix"
    )

    figure_bar_corr.tight_layout()

    st.pyplot(figure_bar_corr)
    plt.close(figure_bar_corr)

    
    st.subheader("Matrice de corrélation")

    figure_corr, ax_corr = plt.subplots(figsize=(11, 8))

    sns.heatmap(
        corr,
        cmap="coolwarm",
        annot=True,
        fmt=".2f",
        linewidths=0.5,
        ax=ax_corr
    )

    ax_corr.set_title(
        "Corrélation entre les variables numériques"
    )

    figure_corr.tight_layout()

    st.pyplot(figure_corr)
    plt.close(figure_corr)

    
    st.subheader("Prix des maisons selon le revenu médian")

    figure_income, ax_income = plt.subplots(figsize=(8, 6))

    sns.scatterplot(
        data=data,
        x="median_income",
        y="median_house_value",
        alpha=0.3,
        ax=ax_income
    )

    ax_income.set_xlabel("Revenu médian")
    ax_income.set_ylabel("Prix médian des maisons")
    ax_income.set_title(
        "Relation entre le revenu médian et le prix"
    )

    figure_income.tight_layout()

    st.pyplot(figure_income)
    plt.close(figure_income)

    
    st.subheader(
        "Prix des maisons selon la proximité avec l'océan"
    )

    figure_boxplot, ax_boxplot = plt.subplots(figsize=(10, 6))

    sns.boxplot(
        data=data,
        x="ocean_proximity",
        y="median_house_value",
        ax=ax_boxplot
    )

    ax_boxplot.set_xlabel("Proximité avec l'océan")
    ax_boxplot.set_ylabel("Prix médian des maisons")
    ax_boxplot.set_title(
        "Distribution des prix selon la proximité avec l'océan"
    )

    ax_boxplot.tick_params(axis="x", rotation=30)

    figure_boxplot.tight_layout()

    st.pyplot(figure_boxplot)
    plt.close(figure_boxplot)



elif menu == "Rapport":
    st.header("Rapport final")

    st.subheader("Objectif")

    st.write(
        """
        L'objectif de cette analyse est d'identifier les principales
        caractéristiques qui influencent le prix des logements en
        Californie.
        """
    )

    st.subheader("Nettoyage des données")

    st.write(
        """
        Les valeurs manquantes de la variable `total_bedrooms`
        ont été remplacées par la médiane de cette variable.
        """
    )

    st.subheader("Principales observations")

    st.write(
        """
        - Le revenu médian présente une relation positive importante
          avec le prix des logements.
        - Les logements situés près de l'océan ou de la baie ont
          généralement des prix plus élevés.
        - Les variables comme la population et le nombre total de
          chambres ont une relation linéaire plus faible avec le prix.
        - Certaines variables contiennent des valeurs extrêmes.
        """
    )

    st.subheader("Conclusion")

    st.write(
        """
        Le revenu médian et la localisation géographique semblent être
        les facteurs les plus importants dans la détermination du prix
        des logements. Toutefois, une corrélation ne signifie pas
        nécessairement qu'une variable cause directement une variation
        du prix.
        """
    )

    st.subheader("Recommandations")

    st.write(
        """
        - Accorder une grande importance à la localisation du logement.
        - Utiliser le revenu médian dans les modèles d'estimation.
        - Étudier séparément les différentes catégories de proximité
          avec l'océan.
        - Construire éventuellement un modèle de prédiction des prix.
        """
    )