# Analyse de l'Adoption de l'IA dans le Monde (Clustering K-Means)

Ce projet analyse l'impact socio-économique et technologique de l'Intelligence Artificielle à travers 62 pays. À l'aide d'un algorithme de Machine Learning, les pays ont été segmentés en différents groupes (clusters) pour identifier les dynamiques mondiales de maturité technologique.

## Démo Interactive
L'application est déployée en direct sur Streamlit Community Cloud : 
👉 [Lien vers le Dashboard Interactif](https://projet-final-sci1402-64cz8chv8yod6amweechym.streamlit.app/)

## Méthodologie & Données
- **Données :** Indicateurs macroéconomiques (PIB, taux d'adoption des outils IA, score global d'avancement, et évolution de la productivité).
- **Méthode :** Nettoyage des données, normalisation, et application de l'algorithme **K-Means** (Scikit-Learn) pour segmenter les pays de manière optimale.
- **Résultat clé :** Une distinction nette apparaît entre les économies moteurs (fort PIB et investissement IA massif) et les pays en transition technologique, visible sur la cartographie interactive.

## 🛠️ Technologies utilisées
- **Python** (Pandas, NumPy, Scikit-Learn)
- **Visualisation :** Plotly Express (Cartographie choroplèthe, graphiques de dispersion)
- **Déploiement :** Streamlit

##  Perspectives d'amélioration
Si j'avais eu plus de temps, j'aurais intégré des données historiques sur 5 ans pour analyser l'évolution temporelle des clusters et prédire les trajectoires d'adoption des pays émergents.
