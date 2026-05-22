import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configuration de la page du Dashboard
st.set_page_config(
    page_title="Dashboard IA - Sorel Tiokap",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 L'Adoption de l'Intelligence Artificielle dans le Monde")
st.write("Analyse interactive des indicateurs socio-économiques et technologiques par pays.")

# 2. Chargement des données
@st.cache_data
def load_data():
    return pd.read_csv("ia_adoption_clusters.csv")

try:
    df = load_data()
    
    # 3. Barre latérale de configuration
    st.sidebar.header("⚙️ Configuration")
    indicateur = st.sidebar.selectbox(
        "Sélectionnez un indicateur à analyser :",
        ['Global AI Score', 'GDP', 'Tool Adoption Rate', 'Avg Productivity Change (%)']
    )
    
    # 4. Organisation de l'espace en 2 colonnes pour les graphiques
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(f"📊 Distribution de : {indicateur} par Cluster")
        fig_hist = px.histogram(
            df, x=indicateur, color='Cluster', nbins=15,
            template='plotly_white', color_discrete_sequence=px.colors.qualitative.Set2
        )
        st.plotly_chart(fig_hist, use_container_width=True)
        
    with col2:
        st.subheader("📈 Corrélation : Richesse (PIB) vs Productivité")
        fig_scatter = px.scatter(
            df, x='GDP', y='Avg Productivity Change (%)',
            size='Global AI Score', color='Cluster', hover_name='country',
            template='plotly_white', color_discrete_sequence=px.colors.qualitative.Set2
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
        
    # 5. Carte du monde interactive
    st.subheader("🗺️ Cartographie Globale du Niveau d'Avancement en IA")
    fig_map = px.choropleth(
        df, locations='country', locationmode='country names',
        color='Global AI Score', color_continuous_scale='Viridis',
        labels={'Global AI Score': 'Score IA Global'},
        template='plotly_white'
    )
    fig_map.update_layout(height=500)
    st.plotly_chart(fig_map, use_container_width=True)

except Exception as e:
    st.error(f"Erreur de chargement. Vérifiez que 'ia_adoption_clusters.csv' est bien à la racine de votre GitHub. Détails : {e}")
