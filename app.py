import streamlit as st
import math

# Configuración de la página
st.set_page_config(page_title="Sistema Experto - Procesamiento de Litio", layout="wide")

def base_datos_litio_streamlit():
    # Base de datos completa (tal cual la pasaste en las capturas)
    compuestos = {
        "Carbonato de Litio (Li2CO3)": {
            "Físicas": {"Densidad (ρ)": "2.11 g/cm³", "PM": "73.89 g/mol", "Estado": "Sólido", "Color": "Blanco", "Llama": "Rojo Carmín", "Fusión": "723 °C", "Ebullición": "1310 °C (Descomp.)", "Refracción": "1.428", "Granulometría": "90% < 100 μm", "Higroscopicidad": "Baja"},
            "Químicas": {"Reacción": "Li2CO3(s) ⇌ 2Li+(aq) + CO3^2-(aq)", "Kps": "8.15e-4", "Pitzer_beta0": 0.149, "Pitzer_beta1": 1.340, "Precipita": "Sí (Caliente)", "Error_Ideal": "20-30%"},
            "Térmicas": {"Cp": "1.34 J/g*K", "ΔH_dis": "-12.8 kJ/mol", "ΔH_reac": "-22.5 kJ/mol", "k": "0.85 W/m*K", "L_evap": "N/A", "T_descomp": ">1300°C", "Estabilidad": "Alta", "Expansión": "1.1e-5 K^-1", "Calor_cryst": "-15.2 kJ/mol", "Ec_Sol": "S(T)=-0.016T+1.54", "Sol_25C": "1.14 g/100mL"},
            "Transporte": {"μ": "N/A", "D": "1.02e-9 m²/s", "Cond_elec": "Alta (Fundido)", "Mov_ion": "4.01e-8 m²/V·s", "Num_transp": "0.38", "kL": "2.5e-5 m/s", "Sediment": "0.45 cm/s"}
        },
        "Cloruro de Litio (LiCl)": {
            "Físicas": {"Densidad (ρ)": "2.07 g/cm³", "PM": "42.39 g/mol", "Estado": "Sólido/Delincuescente", "Color": "Blanco", "Llama": "Rojo Carmín", "Fusión": "605 °C", "Ebullición": "1382 °C", "Refracción": "1.381", "Granulometría": "Cristales", "Higroscopicidad": "Extrema"},
            "Químicas": {"Reacción": "LiCl(s) → Li+(aq) + Cl-(aq)", "Kps": "Muy alto", "Pitzer_beta0": 0.1494, "Pitzer_beta1": 0.3074, "Precipita": "No", "Error_Ideal": "45-60%"},
            "Térmicas": {"Cp": "1.18 J/g*K", "ΔH_dis": "-37.0 kJ/mol", "ΔH_reac": "N/A", "k": "0.60 W/m*K", "L_evap": "20.5 kJ/mol", "T_descomp": "Estable", "Estabilidad": "Alta", "Expansión": "1.6e-4 K^-1", "Calor_cryst": "-35.5 kJ/mol", "Ec_Sol": "S(T)=0.35T+75.2", "Sol_25C": "84.5 g/100mL"},
            "Transporte": {"μ": "1.8 cP (Sol)", "D": "1.35e-9 m²/s", "Cond_elec": "10.5 S/m", "Mov_ion": "4.01e-8", "Num_transp": "0.33", "kL": "3.1e-5 m/s", "Sediment": "N/A"}
        },
        "Ácido Clorhídrico (HCl)": {
            "Físicas": {"Densidad (ρ)": "1.18 g/cm³ (37%)", "PM": "36.46 g/mol", "Estado": "Líquido (Gas dis.)", "Color": "Incoloro/Amarillento", "Llama": "N/A", "Fusión": "-26 °C", "Ebullición": "48 °C (37%)", "Refracción": "1.25", "Granulometría": "N/A", "Higroscopicidad": "Alta (Humos)"},
            "Químicas": {"Reacción": "HCl(g) + H2O → H3O+(aq) + Cl-(aq)", "Kps": "N/A", "Pitzer_beta0": 0.177, "Pitzer_beta1": 0.294, "Precipita": "No", "Error_Ideal": "15%"},
            "Térmicas": {"Cp": "2.43 J/g*K", "ΔH_dis": "-74.8 kJ/mol", "ΔH_reac": "N/A", "k": "0.45 W/m*K", "L_evap": "16.2 kJ/mol", "T_descomp": "N/A", "Estabilidad": "Alta", "Expansión": "N/A", "Calor_cryst": "N/A", "Ec_Sol": "S(T)=Henry's Law", "Sol_25C": "37% m/m"},
            "Transporte": {"μ": "1.9 cP", "D": "2.5e-9 m²/s", "Cond_elec": "Alta", "Mov_ion": "3.6e-7 (H+)", "Num_transp": "0.82", "kL": "N/A", "Sediment": "N/A"}
        },
        "Ácido Sulfúrico (H2SO4)": {
            "Físicas": {"Densidad (ρ)": "1.84 g/cm³", "PM": "98.08 g/mol", "Estado": "Líquido aceitoso", "Color": "Incoloro", "Llama": "N/A", "Fusión": "10 °C", "Ebullición": "337 °C", "Refracción": "1.44", "Granulometría": "N/A", "Higroscopicidad": "Muy Alta"},
            "Químicas": {"Reacción": "H2SO4 → H+ + HSO4-", "Kps": "N/A", "Pitzer_beta0": 0.205, "Pitzer_beta1": 0.550, "Precipita": "No", "Error_Ideal": "50%"},
            "Térmicas": {"Cp": "1.39 J/g*K", "ΔH_dis": "-880 kJ/kg", "ΔH_reac": "Variable", "k": "0.36 W/m*K", "L_evap": "511 kJ/kg", "T_descomp": "340°C", "Estabilidad": "Alta", "Expansión": "N/A", "Calor_cryst": "N/A", "Ec_Sol": "S(T)=Miscible", "Sol_25C": "100%"},
            "Transporte": {"μ": "26.7 cP", "D": "1.7e-9 m²/s", "Cond_elec": "Alta", "Mov_ion": "Variable", "Num_transp": "N/A", "kL": "N/A", "Sediment": "N/A"}
        },
        "Cloruro de Calcio (CaCl2)": {
            "Físicas": {"Densidad (ρ)": "2.15 g/cm³", "PM": "110.98 g/mol", "Estado": "Sólido", "Color": "Blanco", "Llama": "Rojo Ladrillo", "Fusión": "772 °C", "Ebullición": "1935 °C", "Refracción": "1.36", "Granulometría": "Pellets", "Higroscopicidad": "Muy Alta"},
            "Químicas": {"Reacción": "CaCl2 → Ca^2+ + 2Cl-", "Kps": "Muy alto", "Pitzer_beta0": 0.316, "Pitzer_beta1": 1.614, "Precipita": "No", "Error_Ideal": "40%"},
            "Térmicas": {"Cp": "0.67 J/g*K", "ΔH_dis": "-82.9 kJ/mol", "ΔH_reac": "N/A", "k": "0.55 W/m*K", "L_evap": "N/A", "T_descomp": "N/A", "Estabilidad": "Alta", "Expansión": "Variable", "Calor_cryst": "-12 kJ/mol", "Ec_Sol": "S(T)=0.4T+60", "Sol_25C": "74.5 g/100mL"},
            "Transporte": {"μ": "1.5 cP", "D": "1.2e-9 m²/s", "Cond_elec": "Alta", "Mov_ion": "6.1e-8 (Ca2+)", "Num_transp": "0.41", "kL": "Variable", "Sediment": "N/A"}
        },
        "Carbonato de Sodio (Na2CO3)": {
            "Físicas": {"Densidad (ρ)": "2.54 g/cm³", "PM": "105.99 g/mol", "Estado": "Sólido", "Color": "Blanco", "Llama": "Amarillo Intenso", "Fusión": "851 °C", "Ebullición": "Descompone", "Refracción": "1.485", "Granulometría": "Soda Ash", "Higroscopicidad": "Media"},
            "Químicas": {"Reacción": "Na2CO3 → 2Na+ + CO3^2-", "Kps": "Muy alto", "Pitzer_beta0": 0.151, "Pitzer_beta1": 1.556, "Precipita": "Reactivo (Precipitante)", "Error_Ideal": "30%"},
            "Térmicas": {"Cp": "1.04 J/g*K", "ΔH_dis": "-24.7 kJ/mol", "ΔH_reac": "N/A", "k": "0.55 W/m*K", "L_evap": "N/A", "T_descomp": "850°C", "Estabilidad": "Alta", "Expansión": "Variable", "Calor_cryst": "-18 kJ/mol", "Ec_Sol": "S(T)=0.5T+7", "Sol_25C": "30.7 g/100mL"},
            "Transporte": {"μ": "1.2 cP", "D": "1.0e-9 m²/s", "Cond_elec": "Alta", "Mov_ion": "5.19e-8", "Num_transp": "0.39", "kL": "N/A", "Sediment": "N/A"}
        },
        "Sulfato de Calcio (CaSO4)": {
            "Físicas": {"Densidad (ρ)": "2.96 g/cm³", "PM": "136.14 g/mol", "Estado": "Sólido", "Color": "Blanco", "Llama": "Rojo Ladrillo", "Fusión": "1450 °C", "Ebullición": "N/A", "Refracción": "1.52", "Granulometría": "Fino", "Higroscopicidad": "Baja"},
            "Químicas": {"Reacción": "CaSO4 ⇌ Ca^2+ + SO4^2-", "Kps": "4.93e-5", "Pitzer_beta0": 0.20, "Pitzer_beta1": 2.65, "Precipita": "Sí (Escalamiento)", "Error_Ideal": "70%+"},
            "Térmicas": {"Cp": "0.73 J/g*K", "ΔH_dis": "-1.1 kJ/mol", "ΔH_reac": "N/A", "k": "0.54 W/m*K", "L_evap": "N/A", "T_descomp": "1400°C", "Estabilidad": "Media", "Expansión": "Variable", "Calor_cryst": "-5 kJ/mol", "Ec_Sol": "S(T)=-0.002T+0.25", "Sol_25C": "0.21 g/100mL"},
            "Transporte": {"μ": "N/A", "D": "0.85e-9 m²/s", "Cond_elec": "Baja", "Mov_ion": "5.9e-8", "Num_transp": "0.45", "kL": "1.2e-5", "Sediment": "1.2 cm/s"}
        },
        "Dióxido de Carbono (CO2)": {
            "Físicas": {"Densidad (ρ)": "1.98 kg/m³ (Gas)", "PM": "44.01 g/mol", "Estado": "Gas", "Color": "Incoloro", "Llama": "Extintor", "Fusión": "-78 °C", "Ebullición": "-57 °C", "Refracción": "1.00", "Granulometría": "N/A", "Higroscopicidad": "N/A"},
            "Químicas": {"Reacción": "CO2 + H2O ⇌ H2CO3", "Kps": "Kp=1.45e-2", "Pitzer_beta0": 0.0, "Pitzer_beta1": 0.0, "Precipita": "Gas Carb.", "Error_Ideal": "5%"},
            "Térmicas": {"Cp": "0.84 J/g*K", "ΔH_dis": "-19.9 kJ/mol", "ΔH_reac": "N/A", "k": "0.016 W/m*K", "L_evap": "25.2 kJ/mol", "T_descomp": "N/A", "Estabilidad": "Alta", "Expansión": "3.4e-3 K^-1", "Calor_cryst": "N/A", "Ec_Sol": "S(T)=Henry Law", "Sol_25C": "0.145 g/100mL"},
            "Transporte": {"μ": "0.014 cP", "D": "0.16 cm²/s", "Cond_elec": "N/A", "Mov_ion": "N/A", "Num_transp": "N/A", "kL": "Alta", "Sediment": "N/A"}
        },
        "Hidróxido de Litio (LiOH)": {
            "Físicas": {"Densidad (ρ)": "1.46 g/cm³", "PM": "23.95 g/mol", "Estado": "Sólido", "Color": "Blanco", "Llama": "Rojo Carmín", "Fusión": "462 °C", "Ebullición": "924 °C", "Refracción": "1.46", "Granulometría": "Cristalino", "Higroscopicidad": "Alta"},
            "Químicas": {"Reacción": "LiOH → Li+ + OH-", "Kps": "N/A", "Pitzer_beta0": 0.13, "Pitzer_beta1": 0.32, "Precipita": "No", "Error_Ideal": "25%"},
            "Térmicas": {"Cp": "2.07 J/g*K", "ΔH_dis": "-23.5 kJ/mol", "ΔH_reac": "-47.3 kJ/mol", "k": "0.52 W/m*K", "L_evap": "N/A", "T_descomp": "924°C", "Estabilidad": "Media", "Expansión": "Variable", "Calor_cryst": "-12 kJ/mol", "Ec_Sol": "S(T)=0.05T+11.8", "Sol_25C": "12.8 g/100mL"},
            "Transporte": {"μ": "1.1 cP", "D": "1.0e-9 m²/s", "Cond_elec": "Alta", "Mov_ion": "4.01e-8", "Num_transp": "0.21 (Li+)", "kL": "N/A", "Sediment": "N/A"}
        },
        "Sulfato de Magnesio (MgSO4)": {
            "Físicas": {"Densidad (ρ)": "2.66 g/cm³", "PM": "120.37 g/mol", "Estado": "Sólido", "Color": "Blanco", "Llama": "N/A", "Fusión": "1124 °C", "Ebullición": "N/A", "Refracción": "1.56", "Granulometría": "Sales Epsom", "Higroscopicidad": "Alta"},
            "Químicas": {"Reacción": "MgSO4 → Mg^2+ + SO4^2-", "Kps": "Alto", "Pitzer_beta0": 0.22, "Pitzer_beta1": 3.34, "Precipita": "No", "Error_Ideal": "80%+"},
            "Térmicas": {"Cp": "0.82 J/g*K", "ΔH_dis": "-91.2 kJ/mol", "ΔH_reac": "N/A", "k": "0.48 W/m*K", "L_evap": "N/A", "T_descomp": "1124°C", "Estabilidad": "Alta", "Expansión": "Variable", "Calor_cryst": "-20 kJ/mol", "Ec_Sol": "S(T)=0.8T+25", "Sol_25C": "35.1 g/100mL"},
            "Transporte": {"μ": "1.4 cP", "D": "0.7e-9 m²/s", "Cond_elec": "Media", "Mov_ion": "5.5e-8", "Num_transp": "0.40", "kL": "N/A", "Sediment": "N/A"}
        },
        "Hidróxido de Calcio (Ca(OH)2)": {
            "Físicas": {"Densidad (ρ)": "2.21 g/cm³", "PM": "74.09 g/mol", "Estado": "Polvo", "Color": "Blanco", "Llama": "Rojo Ladrillo", "Fusión": "580 °C (Descomp.)", "Ebullición": "N/A", "Refracción": "1.57", "Granulometría": "<50 μm", "Higroscopicidad": "Baja"},
            "Químicas": {"Reacción": "Ca(OH)2 ⇌ Ca^2+ + 2OH-", "Kps": "5.5e-6", "Pitzer_beta0": 0.40, "Pitzer_beta1": 0.50, "Precipita": "Sí (Reactivo)", "Error_Ideal": "50%"},
            "Térmicas": {"Cp": "1.20 J/g*K", "ΔH_dis": "-16.7 kJ/mol", "ΔH_reac": "N/A", "k": "0.50 W/m*K", "L_evap": "N/A", "T_descomp": "580°C", "Estabilidad": "Baja", "Expansión": "Variable", "Calor_cryst": "-8 kJ/mol", "Ec_Sol": "S(T)=-0.001T+0.18", "Sol_25C": "0.16 g/100mL"},
            "Transporte": {"μ": "Variable (Lechada)", "D": "0.9e-9 m²/s", "Cond_elec": "Baja", "Mov_ion": "6.1e-8", "Num_transp": "0.25", "kL": "1.1e-5", "Sediment": "0.8 cm/s"}
        },
        "Ácido Bórico (H3BO3)": {
            "Físicas": {"Densidad (ρ)": "1.43 g/cm³", "PM": "61.83 g/mol", "Estado": "Sólido", "Color": "Blanco", "Llama": "Verde", "Fusión": "171 °C", "Ebullición": "300 °C", "Refracción": "1.33", "Granulometría": "Escamas", "Higroscopicidad": "Baja"},
            "Químicas": {"Reacción": "H3BO3 + H2O ⇌ [B(OH)4]- + H+", "Kps": "pKa=9.24", "Pitzer_beta0": 0.0, "Pitzer_beta1": 0.0, "Precipita": "No", "Error_Ideal": "0-5%"},
            "Térmicas": {"Cp": "1.31 J/g*K", "ΔH_dis": "+14.5 kJ/mol", "ΔH_reac": "N/A", "k": "0.40 W/m*K", "L_evap": "N/A", "T_descomp": "170°C", "Estabilidad": "Media", "Expansión": "Variable", "Calor_cryst": "12 kJ/mol", "Ec_Sol": "S(T)=0.2T+1", "Sol_25C": "5.7 g/100mL"},
            "Transporte": {"μ": "1.1 cP", "D": "1.1e-9 m²/s", "Cond_elec": "Baja", "Mov_ion": "N/A", "Num_transp": "N/A", "kL": "N/A", "Sediment": "N/A"}
        },
        "Hidróxido de Potasio (KOH)": {
            "Físicas": {"Densidad (ρ)": "2.04 g/cm³", "PM": "56.11 g/mol", "Estado": "Sólido", "Color": "Blanco", "Llama": "Violeta", "Fusión": "360 °C", "Ebullición": "1327 °C", "Refracción": "1.34", "Granulometría": "Lentejas", "Higroscopicidad": "Extrema"},
            "Químicas": {"Reacción": "KOH → K+ + OH-", "Kps": "Alto", "Pitzer_beta0": 0.13, "Pitzer_beta1": 0.32, "Precipita": "No", "Error_Ideal": "25%"},
            "Térmicas": {"Cp": "1.16 J/g*K", "ΔH_dis": "-57.1 kJ/mol", "ΔH_reac": "N/A", "k": "0.45 W/m*K", "L_evap": "N/A", "T_descomp": "Estable", "Estabilidad": "Alta", "Expansión": "Variable", "Calor_cryst": "-45 kJ/mol", "Ec_Sol": "S(T)=0.5T+100", "Sol_25C": "112 g/100mL"},
            "Transporte": {"μ": "1.3 cP", "D": "1.9e-9 m²/s", "Cond_elec": "Muy Alta", "Mov_ion": "7.6e-8 (K+)", "Num_transp": "0.27 (K+)", "kL": "N/A", "Sediment": "N/A"}
        }
    }

    st.title("🧪 SISTEMA EXPERTO MULTI-COMPUESTOS")
    st.header("Procesamiento de Litio")
    st.markdown("---")

    # Selector de compuesto
    lista_compuestos = list(compuestos.keys())
    seleccion = st.selectbox("Seleccione un compuesto para obtener el reporte técnico:", lista_compuestos)

    if seleccion:
        datos = compuestos[seleccion]
        
        # Cálculo dinámico de Pitzer (Lógica simplificada)
        I = 1.0
        b0 = datos["Químicas"].get("Pitzer_beta0", 0)
        b1 = datos["Químicas"].get("Pitzer_beta1", 0)
        gamma = math.exp(-0.51 * (math.sqrt(I)/(1+1.2*math.sqrt(I))) + I * b0 + I * b1)

        st.subheader(f"REPORTE TÉCNICO: {seleccion.upper()}")
        
        # Crear pestañas para organizar la información
        tab1, tab2, tab3, tab4 = st.tabs(["Físicas", "Químicas", "Térmicas", "Transporte"])

        with tab1:
            for k, v in datos["Físicas"].items():
                st.write(f"**{k}:** {v}")

        with tab2:
            st.info(f"**Coef. Actividad (Pitzer γ):** {gamma:.4f}")
            for k, v in datos["Químicas"].items():
                st.write(f"**{k}:** {v}")

        with tab3:
            for k, v in datos["Térmicas"].items():
                st.write(f"**{k}:** {v}")

        with tab4:
            for k, v in datos["Transporte"].items():
                st.write(f"**{k}:** {v}")

    st.markdown("---")
    st.caption("Desarrollado para análisis técnico en ingeniería química.")

if __name__ == "__main__":
    base_datos_litio_streamlit()

