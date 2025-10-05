# dashboard_defense_israel_avance.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Configuration de la page
st.set_page_config(
    page_title="Analyse Stratégique Avancée - Israël",
    page_icon="🇮🇱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé avancé
st.markdown("""
<style>
    .main-header {
        font-size: 2.8rem;
        background: linear-gradient(45deg, #0038B8, #FFFFFF, #0038B8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .metric-card {
        background: linear-gradient(135deg, #0038B8, #FFFFFF);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 0.5rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .section-header {
        color: #0038B8;
        border-bottom: 3px solid #FFFFFF;
        padding-bottom: 0.8rem;
        margin-top: 2rem;
        font-size: 1.8rem;
        font-weight: bold;
    }
    .idf-card {
        background: linear-gradient(135deg, #0038B8, #1E90FF);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    .airforce-card {
        background: linear-gradient(135deg, #1E90FF, #87CEEB);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .army-card {
        background: linear-gradient(135deg, #228B22, #32CD32);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .navy-card {
        background: linear-gradient(135deg, #000080, #4169E1);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .intel-card {
        background: linear-gradient(135deg, #8B0000, #FF0000);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .alliance-card {
        background: linear-gradient(135deg, #4B0082, #8A2BE2);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

class DefenseIsraelDashboardAvance:
    def __init__(self):
        self.branches_options = self.define_branches_options()
        self.programmes_options = self.define_programmes_options()
        self.military_capabilities = self.define_military_capabilities()
        self.alliance_projects = self.define_alliance_projects()
        
    def define_branches_options(self):
        return [
            "Israël - Vue d'Ensemble", "Forces de Défense Israéliennes (Tsahal)", 
            "Force Aérienne Israélienne", "Forces Terrestres", 
            "Marine Israélienne", "Renseignement Militaire (Aman)",
            "Alliances Stratégiques", "Coopérations Sécuritaires"
        ]
    
    def define_programmes_options(self):
        return [
            "Défense Anti-Missile (Dôme de Fer)", "Supériorité Aérienne", 
            "Renseignement Électronique", "Guerre Cyber Offensive",
            "Forces Spéciales", "Armement de Précision",
            "Coopération Régionale"
        ]
    
    def define_military_capabilities(self):
        return {
            "Forces de Défense Israéliennes (Tsahal)": {
                "budget": 24.3,
                "personnel": 646.5,
                "reservistes": 465,
                "divisions": 12,
                "equipements": "Merkava IV, Namer, Spike Missiles",
                "technologies": "Systèmes C4I, Drones, IA militaire"
            },
            "Force Aérienne Israélienne": {
                "budget": 8.7,
                "personnel": 34,
                "avions_combat": 362,
                "helicopteres": 125,
                "drones": 250,
                "equipements": "F-35I Adir, F-16I Sufa, F-15I Ra'am",
                "technologies": "Systèmes EW avancés, Cyber-défense aérienne"
            },
            "Forces Terrestres": {
                "budget": 6.2,
                "personnel": 133,
                "chars": 2600,
                "vehicules_blindes": 10000,
                "artillerie": 600,
                "equipements": "Chars Merkava, VCI Namer, Artillerie autonome",
                "technologies": "Systèmes de combat numériques, Drones tactiques"
            },
            "Marine Israélienne": {
                "budget": 2.8,
                "personnel": 9.5,
                "corvettes": 7,
                "sous_marins": 6,
                "patrouilleurs": 45,
                "equipements": "Classe Sa'ar 6, Classe Dolphin",
                "technologies": "Missiles navals Gabriel, Systèmes anti-missiles"
            },
            "Renseignement Militaire (Aman)": {
                "budget": 4.5,
                "personnel": 7,
                "capacites": "SIGINT, IMINT, HUMINT, CYBINT",
                "unites": "Unit 8200, Unit 504, Yaman",
                "technologies": "Cyber-renseignement, IA analytique"
            }
        }
    
    def define_alliance_projects(self):
        return {
            "Coopération USA-Israël": {"pays": "États-Unis", "type": "Soutien militaire", "statut": "Actif", "financement": "3.8 Md$/an"},
            "Dôme de Fer": {"pays": "Israël/USA", "type": "Défense anti-missile", "statut": "Opérationnel", "interceptions": "90%+"},
            "Arrow System": {"pays": "Israël/USA", "type": "Defense missile balistique", "statut": "Opérationnel", "portee": "Haute altitude"},
            "Exercice Juniper Cobra": {"pays": "USA/Israël", "type": "Exercice conjoint", "statut": "Biannuel", "effectifs": "5000+"},
            "Accords d'Abraham": {"pays": "EAU/Bahreïn/Maroc/Soudan", "type": "Normalisation", "statut": "Actif", "domaines": "Sécurité, Économie"},
            "Coopération Grèce-Chypre": {"pays": "Grèce/Chypre", "type": "Partage gaz/security", "statut": "Renforcement", "exercices": "Trident"}
        }
    
    def generate_advanced_data(self, selection):
        """Génère des données avancées et détaillées pour Israël"""
        annees = list(range(2000, 2028))
        
        config = self.get_advanced_config(selection)
        
        data = {
            'Annee': annees,
            'Budget_Defense_Mds': self.simulate_advanced_budget(annees, config),
            'Personnel_Milliers': self.simulate_advanced_personnel(annees, config),
            'PIB_Militaire_Pourcent': self.simulate_military_gdp_percentage(annees),
            'Exercices_Militaires': self.simulate_advanced_exercises(annees, config),
            'Readiness_Operative': self.simulate_advanced_readiness(annees),
            'Capacite_Dissuasion': self.simulate_advanced_deterrence(annees),
            'Temps_Mobilisation_Jours': self.simulate_advanced_mobilization(annees),
            'Exercices_Conjoints': self.simulate_joint_exercises(annees),
            'Developpement_Technologique': self.simulate_tech_development(annees),
            'Capacite_Aerienne': self.simulate_air_capacity(annees),
            'Couverture_AD': self.simulate_air_defense_coverage(annees),
            'Cooperation_Alliances': self.simulate_alliance_cooperation(annees),
            'Cyber_Capabilities': self.simulate_cyber_capabilities(annees),
            'Production_Armements': self.simulate_weapon_production(annees)
        }
        
        # Données spécifiques aux programmes
        if 'defense_missile' in config.get('priorites', []):
            data.update({
                'Interceptions_Dome_Fer': self.simulate_iron_dome_interceptions(annees),
                'Couverture_Defense_Missile': self.simulate_missile_defense_coverage(annees),
                'Systemes_AD_Deployes': self.simulate_ad_systems(annees)
            })
        
        if 'renseignement' in config.get('priorites', []):
            data.update({
                'Capacites_SIGINT': self.simulate_sigint_capabilities(annees),
                'Operations_Cyber': self.simulate_cyber_operations(annees),
                'Alertes_Prevention': self.simulate_early_warning(annees)
            })
        
        if 'innovation' in config.get('priorites', []):
            data.update({
                'Recherche_Defense': self.simulate_defense_research(annees),
                'Technologies_Emergentes': self.simulate_emerging_tech(annees),
                'Exportations_Armes': self.simulate_weapon_exports(annees)
            })
        
        if 'alliances' in config.get('priorites', []):
            data.update({
                'Exercices_USA': self.simulate_us_exercises(annees),
                'Partenariats_Strategiques': self.simulate_strategic_partnerships(annees),
                'Cooperation_Regionale': self.simulate_regional_cooperation(annees)
            })
        
        return pd.DataFrame(data), config
    
    def get_advanced_config(self, selection):
        """Configuration avancée avec plus de détails pour Israël"""
        configs = {
            "Israël - Vue d'Ensemble": {
                "type": "puissance_regionale_avancee",
                "budget_base": 24.3,
                "personnel_base": 646.5,
                "exercices_base": 85,
                "priorites": ["defense_missile", "renseignement", "innovation", "cyber", "alliances", "precision"],
                "doctrines": ["Dissuasion qualitative", "Défense active", "Frappe préemptive"],
                "objectifs": "Maintien de l'avantage qualitatif et sécurité nationale"
            },
            "Force Aérienne Israélienne": {
                "type": "suprematie_aerienne_regionale",
                "budget_base": 8.7,
                "personnel_base": 34,
                "priorites": ["avions_5e_gen", "drones", "cyber_aerien", "renseignement"],
                "capacites": ["F-35I Adir, F-16I Sufa", "Flotte de drones avancés", "Guerre électronique"],
                "doctrine": "Qualitative Military Edge"
            },
            "Renseignement Militaire (Aman)": {
                "type": "excellence_renseignement",
                "budget_base": 4.5,
                "personnel_base": 7,
                "priorites": ["cyberint", "sigint", "humint", "analyse_ia"],
                "capacites": ["Unit 8200", "Cyber-renseignement", "Surveillance régionale"],
                "doctrine": "Prévention et anticipation"
            },
            "Alliances Stratégiques": {
                "type": "cooperation_internationale",
                "budget_base": 3.8,
                "priorites": ["cooperation_usa", "normalisation_arabe", "partenariats_technologiques"],
                "projets": ["Dôme de Fer", "Arrow System", "Exercices conjoints"],
                "objectifs": "Renforcement des alliances stratégiques"
            }
        }
        
        return configs.get(selection, {
            "type": "branche_militaire",
            "personnel_base": 100,
            "exercices_base": 20,
            "priorites": ["defense_generique"]
        })
    
    def simulate_advanced_budget(self, annees, config):
        """Simulation avancée du budget avec variations géopolitiques"""
        budget_base = config.get('budget_base', 24.3)
        budgets = []
        for annee in annees:
            base = budget_base * (1 + 0.035 * (annee - 2000))
            # Variations selon événements géopolitiques
            if 2000 <= annee <= 2005:  # Seconde Intifada
                base *= 1.15
            elif 2006 <= annee <= 2007:  # Guerre du Liban
                base *= 1.20
            elif 2008 <= annee <= 2009:  # Opération Plomb Durci
                base *= 1.18
            elif 2012 <= annee <= 2014:  # Opérations diverses
                base *= 1.12
            elif annee >= 2020:  # Normalisation et nouvelles menaces
                base *= 1.25
            budgets.append(base)
        return budgets
    
    def simulate_advanced_personnel(self, annees, config):
        """Simulation avancée des effectifs"""
        personnel_base = config.get('personnel_base', 646.5)
        return [personnel_base * (1 + 0.008 * (annee - 2000)) for annee in annees]
    
    def simulate_military_gdp_percentage(self, annees):
        """Pourcentage du PIB consacré à la défense"""
        return [6.5 + 0.05 * (annee - 2000) for annee in annees]
    
    def simulate_advanced_exercises(self, annees, config):
        """Exercices militaires avec saisonnalité"""
        base = config.get('exercices_base', 85)
        return [base + 3 * (annee - 2000) + 5 * np.sin(2 * np.pi * (annee - 2000)/4) for annee in annees]
    
    def simulate_advanced_readiness(self, annees):
        """Préparation opérationnelle avancée"""
        readiness = []
        for annee in annees:
            base = 92  # Départ très élevé
            if annee >= 2006:  # Post-guerre du Liban
                base += 3
            if annee >= 2014:  # Expérience Gaza
                base += 2
            if annee >= 2020:  # Nouvelles doctrines
                base += 3
            readiness.append(min(base, 98))
        return readiness
    
    def simulate_advanced_deterrence(self, annees):
        """Capacité de dissuasion avancée"""
        deterrence = []
        for annee in annees:
            base = 88  # Départ élevé
            if annee >= 2007:
                base += 3  # Frappe syrienne
            if annee >= 2010:
                base += 4  # Cyber capacités
            if annee >= 2020:
                base += 3  # F-35 et nouvelles capacités
            deterrence.append(min(base, 95))
        return deterrence
    
    def simulate_advanced_mobilization(self, annees):
        """Temps de mobilisation avancé"""
        return [max(48 - 1.2 * (annee - 2000), 24) for annee in annees]
    
    def simulate_joint_exercises(self, annees):
        """Exercices conjoints avec alliés"""
        exercises = []
        for annee in annees:
            if annee < 2005:
                exercises.append(15)
            elif annee < 2010:
                exercises.append(25 + (annee - 2005))
            else:
                exercises.append(35 + 2 * (annee - 2010))
        return exercises
    
    def simulate_tech_development(self, annees):
        """Développement technologique global"""
        return [min(85 + 1.8 * (annee - 2000), 96) for annee in annees]
    
    def simulate_air_capacity(self, annees):
        """Capacité aérienne globale"""
        return [min(90 + 1.2 * (annee - 2000), 97) for annee in annees]
    
    def simulate_air_defense_coverage(self, annees):
        """Couverture de défense anti-aérienne"""
        return [min(75 + 2.0 * (annee - 2000), 95) for annee in annees]
    
    def simulate_alliance_cooperation(self, annees):
        """Coopération avec alliances"""
        return [min(70 + 1.5 * (annee - 2000), 90) for annee in annees]
    
    def simulate_cyber_capabilities(self, annees):
        """Capacités cybernétiques"""
        return [min(90 + 1.5 * (annee - 2000), 98) for annee in annees]
    
    def simulate_weapon_production(self, annees):
        """Production d'armements (indice)"""
        return [min(75 + 1.8 * (annee - 2000), 92) for annee in annees]
    
    def simulate_us_exercises(self, annees):
        """Exercices avec USA"""
        return [min(20 + 1.5 * (annee - 2000), 45) for annee in annees]
    
    def simulate_strategic_partnerships(self, annees):
        """Partenariats stratégiques"""
        return [min(50 + 2.0 * (annee - 2000), 85) for annee in annees]
    
    def simulate_regional_cooperation(self, annees):
        """Coopération régionale"""
        return [min(20 + 3.0 * (annee - 2020), 65) for annee in annees if annee >= 2020] + [10] * (2020 - min(annees))
    
    def simulate_iron_dome_interceptions(self, annees):
        """Taux d'interception Dôme de Fer"""
        return [min(75 + 2.5 * (annee - 2011), 95) for annee in annees if annee >= 2011] + [0] * (2011 - min(annees))
    
    def simulate_missile_defense_coverage(self, annees):
        """Couverture défense missile"""
        return [min(60 + 2.0 * (annee - 2000), 90) for annee in annees]
    
    def simulate_ad_systems(self, annees):
        """Systèmes de défense anti-missile déployés"""
        return [min(5 + 0.8 * (annee - 2000), 25) for annee in annees]
    
    def simulate_sigint_capabilities(self, annees):
        """Capacités SIGINT"""
        return [min(85 + 1.5 * (annee - 2000), 96) for annee in annees]
    
    def simulate_cyber_operations(self, annees):
        """Opérations cyber offensives"""
        return [min(80 + 2.0 * (annee - 2000), 95) for annee in annees]
    
    def simulate_early_warning(self, annees):
        """Alertes précoces réussies"""
        return [min(75 + 1.5 * (annee - 2000), 92) for annee in annees]
    
    def simulate_defense_research(self, annees):
        """Recherche défense"""
        return [min(88 + 1.2 * (annee - 2000), 96) for annee in annees]
    
    def simulate_emerging_tech(self, annees):
        """Technologies émergentes"""
        return [min(85 + 1.8 * (annee - 2000), 95) for annee in annees]
    
    def simulate_weapon_exports(self, annees):
        """Exportations d'armes (milliards USD)"""
        return [min(3 + 0.5 * (annee - 2000), 12.5) for annee in annees]
    
    def display_advanced_header(self):
        """En-tête avancé avec plus d'informations"""
        st.markdown('<h1 class="main-header">🇮🇱 ANALYSE STRATÉGIQUE AVANCÉE - ISRAËL</h1>', 
                   unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("""
            <div style='text-align: center; background: linear-gradient(135deg, #0038B8, #FFFFFF, #0038B8); 
            padding: 1rem; border-radius: 10px; color: #0038B8; margin: 1rem 0;'>
            <h3>🛡️ TSVAH - EXCELLENCE MILITAIRE ET TECHNOLOGIQUE</h3>
            <p><strong>Analyse multidimensionnelle des capacités de défense et de la stratégie régionale (2000-2027)</strong></p>
            </div>
            """, unsafe_allow_html=True)
    
    def create_advanced_sidebar(self):
        """Sidebar avancé avec plus d'options"""
        st.sidebar.markdown("## 🎛️ PANEL DE CONTRÔLE AVANCÉ")
        
        # Sélection du type d'analyse
        type_analyse = st.sidebar.radio(
            "Mode d'analyse:",
            ["Vue d'Ensemble Israël", "Analyse par Branche", "Alliances Stratégiques", "Scénarios Sécuritaires"]
        )
        
        if type_analyse == "Vue d'Ensemble Israël":
            selection = st.sidebar.selectbox("Niveau d'analyse:", self.branches_options)
        elif type_analyse == "Analyse par Branche":
            selection = st.sidebar.selectbox("Branche militaire:", ["Forces de Défense Israéliennes (Tsahal)", "Force Aérienne Israélienne", "Forces Terrestres", "Marine Israélienne", "Renseignement Militaire (Aman)"])
        elif type_analyse == "Alliances Stratégiques":
            selection = st.sidebar.selectbox("Programme stratégique:", self.programmes_options)
        else:
            selection = "Scénarios Sécuritaires"
        
        # Options avancées
        st.sidebar.markdown("### 🔧 OPTIONS AVANCÉES")
        show_regional = st.sidebar.checkbox("Contexte régional", value=True)
        show_alliances = st.sidebar.checkbox("Analyse des alliances", value=True)
        show_technical = st.sidebar.checkbox("Détails techniques", value=True)
        threat_assessment = st.sidebar.checkbox("Évaluation des menaces", value=True)
        
        # Paramètres de simulation
        st.sidebar.markdown("### ⚙️ PARAMÈTRES DE SIMULATION")
        scenario = st.sidebar.selectbox("Scénario:", ["Statut Quo Sécuritaire", "Conflit Régional Majeur", "Escalade Nord", "Opération Préemptive"])
        
        return {
            'selection': selection,
            'type_analyse': type_analyse,
            'show_regional': show_regional,
            'show_alliances': show_alliances,
            'show_technical': show_technical,
            'threat_assessment': threat_assessment,
            'scenario': scenario
        }
    
    def display_strategic_metrics(self, df, config):
        """Métriques stratégiques avancées"""
        st.markdown('<h3 class="section-header">🎯 TABLEAU DE BORD STRATÉGIQUE ISRAËL</h3>', 
                   unsafe_allow_html=True)
        
        derniere_annee = df['Annee'].max()
        data_actuelle = df[df['Annee'] == derniere_annee].iloc[0]
        data_2000 = df[df['Annee'] == 2000].iloc[0]
        
        # Première ligne de métriques
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
            <div class="metric-card">
                <h4>💰 BUDGET DÉFENSE 2027</h4>
                <h2>{:.1f} Md$</h2>
                <p>📈 {:.1f}% du PIB israélien</p>
            </div>
            """.format(data_actuelle['Budget_Defense_Mds'], data_actuelle['PIB_Militaire_Pourcent']), 
            unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="metric-card">
                <h4>👥 EFFECTIFS TOTAUX</h4>
                <h2>{:,.0f}K</h2>
                <p>⚔️ + {:.0f}K réservistes</p>
            </div>
            """.format(data_actuelle['Personnel_Milliers'], 465), 
            unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="idf-card">
                <h4>🛡️ DÔME DE FER</h4>
                <h2>{:.1f}%</h2>
                <p>🚀 Taux d'interception</p>
            </div>
            """.format(data_actuelle.get('Interceptions_Dome_Fer', 0)), 
            unsafe_allow_html=True)
        
        with col4:
            st.markdown("""
            <div class="alliance-card">
                <h4>🤝 COOPÉRATION USA</h4>
                <h2>{:.0f}%</h2>
                <p>🇺🇸 3.8 Md$/an d'aide militaire</p>
            </div>
            """.format(data_actuelle['Cooperation_Alliances']), 
            unsafe_allow_html=True)
        
        # Deuxième ligne de métriques
        col5, col6, col7, col8 = st.columns(4)
        
        with col5:
            reduction_temps = ((data_2000['Temps_Mobilisation_Jours'] - data_actuelle['Temps_Mobilisation_Jours']) / 
                             data_2000['Temps_Mobilisation_Jours']) * 100
            st.metric(
                "⏱️ Temps Mobilisation",
                f"{data_actuelle['Temps_Mobilisation_Jours']:.1f} jours",
                f"{reduction_temps:+.1f}%"
            )
        
        with col6:
            croissance_aerienne = ((data_actuelle['Capacite_Aerienne'] - data_2000['Capacite_Aerienne']) / 
                               data_2000['Capacite_Aerienne']) * 100
            st.metric(
                "✈️ Puissance Aérienne",
                f"{data_actuelle['Capacite_Aerienne']:.1f}%",
                f"{croissance_aerienne:+.1f}%"
            )
        
        with col7:
            if 'Couverture_Defense_Missile' in df.columns:
                croissance_defense = ((data_actuelle['Couverture_Defense_Missile'] - data_2000.get('Couverture_Defense_Missile', 60)) / 
                                   data_2000.get('Couverture_Defense_Missile', 60)) * 100
                st.metric(
                    "🎯 Couverture Anti-Missile",
                    f"{data_actuelle['Couverture_Defense_Missile']:.1f}%",
                    f"{croissance_defense:+.1f}%"
                )
        
        with col8:
            st.metric(
                "📊 Préparation Opérationnelle",
                f"{data_actuelle['Readiness_Operative']:.1f}%",
                f"+{(data_actuelle['Readiness_Operative'] - data_2000['Readiness_Operative']):.1f}%"
            )
    
    def create_comprehensive_analysis(self, df, config):
        """Analyse complète multidimensionnelle"""
        st.markdown('<h3 class="section-header">📊 ANALYSE MULTIDIMENSIONNELLE ISRAËL</h3>', 
                   unsafe_allow_html=True)
        
        # Graphiques principaux
        col1, col2 = st.columns(2)
        
        with col1:
            # Évolution des capacités principales
            fig = go.Figure()
            
            capacites = ['Readiness_Operative', 'Capacite_Dissuasion', 'Cyber_Capabilities', 'Cooperation_Alliances']
            noms = ['Préparation Opér.', 'Dissuasion Strat.', 'Capacités Cyber', 'Coopération Alliances']
            couleurs = ['#0038B8', '#FFFFFF', '#1E90FF', '#228B22']
            
            for i, (cap, nom, couleur) in enumerate(zip(capacites, noms, couleurs)):
                if cap in df.columns:
                    fig.add_trace(go.Scatter(
                        x=df['Annee'], y=df[cap],
                        mode='lines', name=nom,
                        line=dict(color=couleur, width=4),
                        hovertemplate=f"{nom}: %{{y:.1f}}%<extra></extra>"
                    ))
            
            fig.update_layout(
                title="📈 ÉVOLUTION DES CAPACITÉS STRATÉGIQUES ISRAËL (2000-2027)",
                xaxis_title="Année",
                yaxis_title="Niveau de Capacité (%)",
                height=500,
                template="plotly_white",
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Analyse des capacités technologiques
            tech_data = []
            tech_names = []
            
            if 'Developpement_Technologique' in df.columns:
                tech_data.append(df['Developpement_Technologique'])
                tech_names.append('Développement Techno.')
            
            if 'Cyber_Capabilities' in df.columns:
                tech_data.append(df['Cyber_Capabilities'])
                tech_names.append('Capacités Cyber')
            
            if 'Production_Armements' in df.columns:
                tech_data.append(df['Production_Armements'])
                tech_names.append('Production Armements')
            
            if tech_data:
                fig = make_subplots(specs=[[{"secondary_y": True}]])
                
                for i, (data, nom) in enumerate(zip(tech_data, tech_names)):
                    fig.add_trace(
                        go.Scatter(x=df['Annee'], y=data, name=nom,
                                 line=dict(width=4)),
                        secondary_y=(i > 0)
                    )
                
                fig.update_layout(
                    title="🚀 AVANCÉE TECHNOLOGIQUE - ÉVOLUTION COMPARÉE",
                    height=500,
                    template="plotly_white"
                )
                st.plotly_chart(fig, use_container_width=True)
    
    def create_regional_analysis(self, df, config):
        """Analyse régionale avancée"""
        st.markdown('<h3 class="section-header">🌍 ENVIRONNEMENT RÉGIONAL ISRAËL</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Architecture sécuritaire régionale
            st.markdown("""
            <div class="idf-card">
                <h4>🏛️ ARCHITECTURE SÉCURITAIRE RÉGIONALE</h4>
                <p><strong>Alliances:</strong> Soutien américain inconditionnel, Accords d'Abraham</p>
                <p><strong>Menaces Directes:</strong> Iran, Hezbollah, Hamas, Syrie</p>
                <p><strong>Défenses:</strong> Dôme de Fer, Arrow, David's Sling, Barrière souterraine</p>
                <p><strong>Stratégie:</strong> Dissuasion qualitative, frappes préemptives, défense active</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Analyse des relations régionales
            st.markdown("""
            <div class="alliance-card">
                <h4>🌐 DYNAMIQUES RÉGIONALES</h4>
                <p><strong>Alliés:</strong> USA, Émirats Arabes Unis, Bahreïn, Grèce, Chypre</p>
                <p><strong>Adversaires:</strong> Iran, Hezbollah, Hamas, Syrie, Jihad Islamique</p>
                <p><strong>Neutres/Complexes:</strong> Jordanie, Égypte, Arabie Saoudite</p>
                <p><strong>Organisations:</strong> MENA, coopération gazière Est-Méditerranée</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Cartographie des menaces
            threats_data = {
                'Menace': ['Iran Nucléaire', 'Hezbollah (Roquettes)', 'Hamas (Gaza)', 
                          'Syrie (Conventionnel)', 'Cyber Attaques', 'Terrorisme'],
                'Distance_km': [1000, 120, 60, 70, 0, 0],
                'Capacite_Ennemie': [9, 8, 7, 6, 9, 6],
                'Niveau_Alerte': [9, 8, 7, 5, 8, 6]
            }
            threats_df = pd.DataFrame(threats_data)
            
            fig = px.scatter(threats_df, x='Distance_km', y='Capacite_Ennemie',
                           size='Niveau_Alerte', color='Menace',
                           title="🎯 CARTOGRAPHIE DES MENACES RÉGIONALES",
                           size_max=30)
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
            
            # Systèmes de défense
            defense_data = {
                'Système': ['Dôme de Fer', 'Arrow 2/3', "David's Sling", 'Barrière Gaza', 'Barrière Liban'],
                'Portée_km': [70, 100, 300, 0, 0],
                'Taux_Interception': [90, 90, 90, 95, 95],
                'Année_Déploiement': [2011, 2000, 2017, 2021, 2018]
            }
            defense_df = pd.DataFrame(defense_data)
            
            fig = px.bar(defense_df, x='Système', y='Taux_Interception',
                        title="🛡️ SYSTÈMES DE DÉFENSE ISRAÉLIENS",
                        color='Taux_Interception',
                        color_continuous_scale='blues')
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
    
    def create_branch_analysis(self, df, config):
        """Analyse des capacités par branche"""
        st.markdown('<h3 class="section-header">⚔️ CAPACITÉS PAR BRANCHE MILITAIRE</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Contributions des branches
            contributions_data = []
            for branche, data in self.military_capabilities.items():
                contributions_data.append({
                    'Branche': branche,
                    'Budget (Md$)': data['budget'],
                    'Personnel (K)': data['personnel'],
                    'Équipements Principaux': data.get('equipements', 'Non spécifié'),
                    'Technologies': data.get('technologies', 'Non spécifié')
                })
            
            contributions_df = pd.DataFrame(contributions_data)
            
            fig = px.bar(contributions_df, x='Branche', y='Budget (Md$)',
                        title="💰 RÉPARTITION BUDGÉTAIRE PAR BRANCHE",
                        color='Budget (Md$)',
                        color_continuous_scale='blues')
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Spécialisations stratégiques
            st.markdown("""
            <div class="airforce-card">
                <h4>🎯 SPÉCIALISATIONS STRATÉGIQUES</h4>
                <p><strong>Force Aérienne:</strong> Supériorité aérienne régionale, frappes de précision</p>
                <p><strong>Renseignement:</strong> Excellence cyber, SIGINT, surveillance régionale</p>
                <p><strong>Forces Terrestres:</strong> Mobilité, protection blindée, combat urbain</p>
                <p><strong>Marine:</strong> Contrôle gaz offshore, défense côtière, sous-marins stratégiques</p>
                <p><strong>Forces Spéciales:</strong> Opérations discrètes, contre-terrorisme</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Avantages comparatifs
            advantages_data = {
                'Domaine': ['Renseignement Cyber', 'Force Aérienne', 'Défense Anti-Missile', 
                           'Forces Spéciales', 'Guerre Électronique', 'Drones', 'Précision'],
                'Score_Israel': [10, 9, 10, 9, 10, 9, 10],
                'Score_Voisins': [4, 6, 3, 5, 4, 5, 4]  # Meilleurs voisins
            }
            advantages_df = pd.DataFrame(advantages_data)
            
            fig = go.Figure(data=[
                go.Bar(name='Israël', x=advantages_df['Domaine'], y=advantages_df['Score_Israel']),
                go.Bar(name='Meilleurs Voisins', x=advantages_df['Domaine'], y=advantages_df['Score_Voisins'])
            ])
            fig.update_layout(title="📊 AVANTAGES COMPARATIFS STRATÉGIQUES (0-10)",
                             barmode='group', height=400)
            st.plotly_chart(fig, use_container_width=True)
    
    def create_technical_analysis(self, df, config):
        """Analyse technique détaillée"""
        st.markdown('<h3 class="section-header">🔬 ANALYSE TECHNIQUE AVANCÉE</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Analyse des systèmes d'armes avancés
            systems_data = {
                'Système': ['F-35I Adir', 'Dôme de Fer', 'Arrow 3', 'Merkava IV', 
                           'Classe Sa\'ar 6', 'Système Trophy', 'Eitan APC'],
                'Portée/Puissance': [2200, 70, 2400, 0, 0, 0, 0],
                'Branche': ['Air Force', 'Défense', 'Défense', 'Armée', 'Marine', 'Armée', 'Armée'],
                'Statut': ['Opérationnel', 'Opérationnel', 'Opérationnel', 'Opérationnel', 'Opérationnel', 'Opérationnel', 'Développement']
            }
            systems_df = pd.DataFrame(systems_data)
            
            fig = px.scatter(systems_df, x='Portée/Puissance', y='Branche', 
                           size='Portée/Puissance', color='Branche',
                           hover_name='Système',
                           title="🚀 SYSTÈMES D'ARMES AVANCÉS D'ISRAËL",
                           size_max=30)
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Analyse de la supériorité technologique
            superiority_data = {
                'Domaine': ['Défense Anti-Missile', 'Drones de Combat', 'Guerre Cyber', 
                          'Renseignement SIGINT', 'Guerre Électronique', 'Armes de Précision'],
                'Avance_Annees': [15, 10, 8, 12, 10, 8],
                'Exportations_Mds': [2.5, 1.2, 1.8, 0.9, 0.7, 3.2]
            }
            superior_df = pd.DataFrame(superiority_data)
            
            fig = go.Figure()
            fig.add_trace(go.Bar(name='Avance (années)', x=superior_df['Domaine'], 
                                y=superior_df['Avance_Annees'],
                                marker_color='#0038B8'))
            fig.add_trace(go.Scatter(name='Exportations (Md$)', x=superior_df['Domaine'], 
                                   y=superior_df['Exportations_Mds'],
                                   yaxis='y2', mode='lines+markers',
                                   line=dict(color='#FFFFFF', width=3)))
            
            fig.update_layout(title="📈 SUPÉRIORITÉ TECHNOLOGIQUE ET EXPORTATIONS",
                             yaxis2=dict(title='Exportations (Md$)', overlaying='y', side='right'),
                             height=500)
            st.plotly_chart(fig, use_container_width=True)
            
            # Innovations en cours
            st.markdown("""
            <div class="alliance-card">
                <h4>🚀 INNOVATIONS TECHNOLOGIQUES EN COURS</h4>
                <p><strong>IA Militaire:</strong> Systèmes autonomes, analyse prédictive</p>
                <p><strong>Laser Tactique:</strong> Iron Beam pour défense anti-missile</p>
                <p><strong>Guerre Cyber:</strong> Unit 8200, capacités offensives avancées</p>
                <p><strong>Espace:</strong> Satellites Ofek, surveillance régionale</p>
                <p><strong>Robotique:</strong> Systèmes autonomes de combat</p>
            </div>
            """, unsafe_allow_html=True)
    
    def create_alliance_analysis(self, config):
        """Analyse des alliances stratégiques"""
        st.markdown('<h3 class="section-header">🤝 ANALYSE DES ALLIANCES STRATÉGIQUES</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Réseau d'alliances
            alliance_data = {
                'Alliance': ['USA-Israël', 'Accords Abraham (EAU)', 'Accords Abraham (Bahreïn)', 
                            'Grèce-Israël', 'Chypre-Israël', 'Coopération Jordanienne',
                            'Coopération Égyptienne', 'Inde-Israël'],
                'Niveau_Coopération': [10, 7, 6, 8, 8, 6, 5, 8],  # sur 10
                'Année_Début': [1948, 2020, 2020, 2010, 2010, 1994, 1979, 1992],
                'Domaines': ['Militaire', 'Économie/Sécurité', 'Économie/Sécurité', 'Énergie/Sécurité', 
                           'Énergie/Sécurité', 'Sécurité/Eau', 'Sécurité/Gaz', 'Militaire/Techno']
            }
            alliance_df = pd.DataFrame(alliance_data)
            
            fig = px.scatter(alliance_df, x='Année_Début', y='Niveau_Coopération',
                           size='Niveau_Coopération', color='Domaines',
                           title="🌐 RÉSEAU D'ALLIANCES STRATÉGIQUES",
                           size_max=30)
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Avantages des alliances
            st.markdown("""
            <div class="alliance-card">
                <h4>🏆 AVANTAGES STRATÉGIQUES DES ALLIANCES</h4>
                <p><strong>Soutien américain:</strong> 3.8 Md$/an d'aide militaire</p>
                <p><strong>Coopération régionale:</strong> Normalisation avec pays arabes</p>
                <p><strong>Partage technologique:</strong> Transfert de technologies avancées</p>
                <p><strong>Exercices conjoints:</strong> Juniper Cobra avec USA</p>
                <p><strong>Renseignement partagé:</strong> Collaboration Five Eyes étendue</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Domaines de coopération future
            future_coop_data = {
                'Domaine': ['Défense Anti-Missile Régionale', 'Guerre Cyber Collective', 
                           'Surveillance Spatiale', 'Guerre Électronique',
                           'Renseignement Artificiel', 'Exercices Conjoints Avancés'],
                'Potentiel': [8, 9, 7, 8, 9, 8]  # sur 10
            }
            future_coop_df = pd.DataFrame(future_coop_data)
            
            fig = px.bar(future_coop_df, x='Domaine', y='Potentiel',
                        title="🔮 POTENTIEL DE COOPÉRATION FUTURE",
                        color='Potentiel',
                        color_continuous_scale='blues')
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
    
    def create_threat_assessment(self, df, config):
        """Évaluation avancée des menaces"""
        st.markdown('<h3 class="section-header">⚠️ ÉVALUATION STRATÉGIQUE DES MENACES</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Matrice des menaces avancées
            threats_data = {
                'Type de Menace': ['Iran Nucléaire', 'Hezbollah (Liban)', 'Hamas (Gaza)', 
                                 'Syrie (Conventionnel)', 'Guerre Cyber Iranienne',
                                 'Terrorisme Transfrontalier', 'Crise Jérusalem',
                                 'Prolifération Missiles'],
                'Probabilité': [0.7, 0.8, 0.9, 0.6, 0.8, 0.7, 0.5, 0.8],
                'Impact': [0.9, 0.8, 0.7, 0.6, 0.7, 0.6, 0.8, 0.7],
                'Niveau_Preparation': [0.9, 0.8, 0.9, 0.7, 0.8, 0.9, 0.6, 0.8]
            }
            threats_df = pd.DataFrame(threats_data)
            
            fig = px.scatter(threats_df, x='Probabilité', y='Impact', 
                           size='Niveau_Preparation', color='Type de Menace',
                           title="🎯 MATRICE RISQUES - PROBABILITÉ VS IMPACT",
                           size_max=30)
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Capacités de réponse par domaine
            response_data = {
                'Scénario': ['Frappe Iranienne', 'Attaque Hezbollah', 'Escalade Gaza', 
                           'Conflit Syrie', 'Cyber Attaque Majeure', 'Crise Multifront'],
                'Force_Aerienne': [0.9, 0.8, 0.9, 0.8, 0.3, 0.8],
                'Defense_Anti_Missile': [0.8, 0.9, 0.9, 0.7, 0.2, 0.8],
                'Cybersécurité': [0.7, 0.6, 0.5, 0.4, 0.9, 0.6],
                'Forces_Terrestres': [0.4, 0.7, 0.6, 0.5, 0.2, 0.7]
            }
            response_df = pd.DataFrame(response_data)
            
            fig = go.Figure(data=[
                go.Bar(name='Force Aérienne', x=response_df['Scénario'], y=response_df['Force_Aerienne']),
                go.Bar(name='Défense Anti-Missile', x=response_df['Scénario'], y=response_df['Defense_Anti_Missile']),
                go.Bar(name='Cybersécurité', x=response_df['Scénario'], y=response_df['Cybersécurité']),
                go.Bar(name='Forces Terrestres', x=response_df['Scénario'], y=response_df['Forces_Terrestres'])
            ])
            fig.update_layout(title="🛡️ CAPACITÉS DE RÉPONSE PAR DOMAINE",
                             barmode='group', height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        # Recommandations stratégiques
        st.markdown("""
        <div class="alliance-card">
            <h4>🎯 RECOMMANDATIONS STRATÉGIQUES ISRAËL</h4>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1rem;">
                <div><strong>• Modernisation aérienne:</strong> F-35 supplémentaires, drones avancés</div>
                <div><strong>• Innovation technologique:</strong> Maintien de l'avance qualitative</div>
                <div><strong>• Renforcement anti-missile:</strong> Iron Beam, Arrow 4</div>
                <div><strong>• Cybersécurité offensive:</strong> Capacités de préemption</div>
                <div><strong>• Coopération régionale:</strong> Élargissement Accords d'Abraham</div>
                <div><strong>• Préparation multifront:</strong> Plans de contingence nord/sud</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def create_alliance_database(self):
        """Base de données des alliances stratégiques"""
        st.markdown('<h3 class="section-header">🤝 BASE DE DONNÉES DES ALLIANCES STRATÉGIQUES</h3>', 
                   unsafe_allow_html=True)
        
        alliance_data = []
        for nom, specs in self.alliance_projects.items():
            alliance_data.append({
                'Projet': nom,
                'Pays Participants': specs['pays'],
                'Type': specs['type'],
                'Statut': specs['statut'],
                'Détails': specs.get('financement', specs.get('interceptions', specs.get('portee', 'N/A')))
            })
        
        alliance_df = pd.DataFrame(alliance_data)
        
        # Affichage interactif
        col1, col2 = st.columns([2, 1])
        
        with col1:
            fig = px.treemap(alliance_df, path=['Type', 'Projet'],
                            title="🤝 CARTE DES ALLIANCES STRATÉGIQUES",
                            color='Type')
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("""
            <div class="alliance-card">
                <h4>📋 PROJETS STRATÉGIQUES</h4>
            """, unsafe_allow_html=True)
            
            for projet in alliance_data:
                st.markdown(f"""
                <div style="background: rgba(255,255,255,0.1); padding: 0.5rem; margin: 0.2rem 0; border-radius: 5px;">
                    <strong>{projet['Projet']}</strong><br>
                    🌍 {projet['Pays Participants']} • 🎯 {projet['Type']}<br>
                    📊 {projet['Statut']} • 📝 {projet['Détails']}
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    def run_advanced_dashboard(self):
        """Exécute le dashboard avancé complet"""
        # Sidebar avancé
        controls = self.create_advanced_sidebar()
        
        # Header avancé
        self.display_advanced_header()
        
        # Génération des données avancées
        df, config = self.generate_advanced_data(controls['selection'])
        
        # Navigation par onglets avancés
        tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
            "📊 Tableau de Bord", 
            "🔬 Analyse Technique", 
            "🌍 Contexte Régional", 
            "⚔️ Branches Militaires",
            "⚠️ Évaluation Menaces",
            "🤝 Alliances Stratégiques",
            "💎 Synthèse Stratégique"
        ])
        
        with tab1:
            self.display_strategic_metrics(df, config)
            self.create_comprehensive_analysis(df, config)
        
        with tab2:
            self.create_technical_analysis(df, config)
        
        with tab3:
            if controls['show_regional']:
                self.create_regional_analysis(df, config)
        
        with tab4:
            self.create_branch_analysis(df, config)
        
        with tab5:
            if controls['threat_assessment']:
                self.create_threat_assessment(df, config)
        
        with tab6:
            if controls['show_alliances']:
                self.create_alliance_database()
        
        with tab7:
            self.create_strategic_synthesis(df, config, controls)
    
    def create_strategic_synthesis(self, df, config, controls):
        """Synthèse stratégique finale"""
        st.markdown('<h3 class="section-header">💎 SYNTHÈSE STRATÉGIQUE - ISRAËL</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="idf-card">
                <h4>🏆 AVANTAGES STRATÉGIQUES DÉCISIFS</h4>
                <div style="margin-top: 1rem;">
                    <div class="airforce-card" style="margin: 0.5rem 0;">
                        <strong>🚀 Excellence Technologique</strong>
                        <p>Supériorité cyber, défense anti-missile, renseignement électronique</p>
                    </div>
                    <div class="army-card" style="margin: 0.5rem 0;">
                        <strong>🎯 Avantage Qualitatif</strong>
                        <p>Personnel hautement qualifié, formation intensive, innovation permanente</p>
                    </div>
                    <div class="navy-card" style="margin: 0.5rem 0;">
                        <strong>🤝 Alliances Solides</strong>
                        <p>Soutien américain inconditionnel, normalisation régionale élargie</p>
                    </div>
                    <div class="intel-card" style="margin: 0.5rem 0;">
                        <strong>🔍 Renseignement Supérieur</strong>
                        <p>Unit 8200, capacités cyber avancées, surveillance régionale</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="alliance-card">
                <h4>🎯 DÉFIS STRATÉGIQUES</h4>
                <div style="margin-top: 1rem;">
                    <div class="alliance-card" style="margin: 0.5rem 0;">
                        <strong>🇮🇷 Menace Iranienne</strong>
                        <p>Programme nucléaire, missiles balistiques, proxies régionaux</p>
                    </div>
                    <div class="alliance-card" style="margin: 0.5rem 0;">
                        <strong>☢️ Prolifération Missiles</strong>
                        <p>Hezbollah (150k+ roquettes), Hamas, Jihad Islamique</p>
                    </div>
                    <div class="alliance-card" style="margin: 0.5rem 0;">
                        <strong>🌍 Isolement Démographique</strong>
                        <p>Population limitée, environnement régional hostile</p>
                    </div>
                    <div class="alliance-card" style="margin: 0.5rem 0;">
                        <strong>💻 Vulnérabilités Cyber</strong>
                        <p>Cible prioritaire des cyberattaques étatiques et non-étatiques</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Perspectives futures
        st.markdown("""
        <div class="metric-card">
            <h4>🔮 PERSPECTIVES STRATÉGIQUES 2027-2035</h4>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-top: 1rem;">
                <div>
                    <h5>🔄 TRANSFORMATION TECHNOLOGIQUE</h5>
                    <p>• IA militaire opérationnelle<br>• Systèmes laser de défense<br>• Drones de combat autonomes<br>• Supériorité cyber renforcée</p>
                </div>
                <div>
                    <h5>🤝 ÉLARGISSEMENT ALLIANCES</h5>
                    <p>• Normalisation avec Arabie Saoudite<br>• Coopération défense régionale<br>• Partenariats technologiques élargis<br>• Intégration économique MENA</p>
                </div>
                <div>
                    <h5>🛡️ NOUVELLES DOCTRINES</h5>
                    <p>• Défense active multidimensionnelle<br>• Frappes préemptives cyber<br>• Dissuasion qualitative avancée<br>• Coopération civilo-militaire</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Recommandations finales
        st.markdown("""
        <div class="idf-card">
            <h4>🎖️ RECOMMANDATIONS STRATÉGIQUES FINALES</h4>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1rem;">
                <div>
                    <h5>🛡️ MAINTIEN DE LA SUPÉRIORITÉ</h5>
                    <p>• Investissement continu dans la R&D de défense<br>
                    • Modernisation des capacités anti-missile<br>
                    • Renforcement des capacités cyber offensives<br>
                    • Maintien de l'avantage qualitatif aérien</p>
                </div>
                <div>
                    <h5>🌍 LEADERSHIP RÉGIONAL</h5>
                    <p>• Élargissement des Accords d'Abraham<br>
                    • Coopération sécuritaire avec partenaires arabes<br>
                    • Leadership technologique au Moyen-Orient<br>
                    • Promotion de la stabilité régionale</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Lancement du dashboard avancé
if __name__ == "__main__":
    dashboard = DefenseIsraelDashboardAvance()
    dashboard.run_advanced_dashboard()