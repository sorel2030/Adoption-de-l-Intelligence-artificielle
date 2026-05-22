#  Analyse de l'Adoption de l'IA et de l'Impact Socio-Économique

##  Présentation du Projet
Ce projet a pour objectif d'analyser et de segmenter les pays selon leur niveau d'avancement, d'adoption technologique et d'impact économique lié à l'Intelligence Artificielle.

L'objectif final est de comprendre si des indicateurs macroéconomiques comme le PIB ou les gains de productivité permettent de prédire le score global de maturité en IA d'une nation.

##  Méthodologie & Approche Data
1. **Collecte & Nettoyage :** Fusion de 4 datasets (Global AI Index, Données de PIB, Taux d'Adoption des outils, Évolution de la productivité). Aggrégation des données pour éliminer les doublons de pays.
2. **Gestion du Data Leakage :** Cloisonnement strict des données (`train_test_split`) avant l'étape d'imputation des valeurs manquantes.
3. **Modélisation :** Test et évaluation d'une Régression Linéaire et d'un Random Forest Regressor.
4. **Clustering :** Segmentation des pays en 3 profils distincts via l'algorithme K-Means après standardisation.

##  Résultats des Modèles (Performances Réelles)
Suite à la correction de la fuite de données, les modèles prédictifs affichent des performances réalistes, démontrant que le score d'IA global dépend de facteurs plus complexes que la simple richesse économique :
*   **Régression Linéaire :** $R^2 \approx 0.06$ | RMSE $\approx 19.86$
*   **Random Forest :** $R^2 \approx 0.04$ | RMSE $\approx 20.16$

## Technologies Utilisées
*   **Langage :** Python (Pandas, NumPy, Scikit-Learn)
*   **Visualisation :** Plotly Express, Streamlit
*   **Environnement :** Google Colab, Git / GitHub
