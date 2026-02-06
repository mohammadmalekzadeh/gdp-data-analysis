# GDP Data Analysis

This project provides an exploratory and analytical study of global economic structures using GDP-related indicators for 181 countries, based on data from the World Bank and the IMF.

---

## 📊 Dataset
- **Countries:** 181
- **Sources:** World Bank, UN Data, IMF (WEO 2025)
- **Key Variables:**
  - GDP (Nominal)
  - GDP (Abbrev)
  - Population
  - GDP per Capita
  - GDP Growth Rate
  - Share of World GDP (%)

---

## 🔧 Methodology
- Data cleaning and preprocessing with **Python**
- Log-transformations for skewed economic variables
- Statistical tests:
  - Shapiro–Wilk normality test
  - Pearson and Spearman correlation analysis
- Visualization exclusively with **R**

---

## 📈 Key Analyses & Visualizations
- Distribution and boxplots of GDP, population, and growth
- Scatter plots with log–log scaling
- **LOWESS smoothing** for nonlinear relationships
- Pie and bar charts for GDP size categories
- Top‑10 GDP country comparison

---

## 🔍 Key Findings
- Log‑GDP follows an approximately normal distribution; most other variables are highly non‑normal
- GDP Growth is extremely right‑skewed, indicating global growth instability
- Strong linear relationship between **Log(GDP)** and **Log(Population)** (Pearson r ≈ 0.80)
- Near‑perfect monotonic relationship between **GDP size** and **Share of World GDP** (Spearman ρ ≈ 0.996), revealing exponential concentration
- Global economy is structurally concentrated in a small number of countries

---

## 🇮🇷 Case Study: Iran
- **GDP (2023):** ~$404B (Billion category, rank ~36)
- **Population:** ~90.6 million
- **GDP per capita:** Below global average
- **Growth rate:** Relatively high but volatile
- **Insight:** Large population provides scale, but productivity constraints limit global economic share

---

## 📌 Conclusions
Economic development is fundamentally **structural and nonlinear**. GDP size and population alone do not guarantee prosperity. Productivity, growth quality, and global integration play decisive roles in determining long‑term economic position.

---

## 📚 References
- World Bank Open Data – GDP, Population, GDP per Capita  
- IMF World Economic Outlook (WEO 2025)  
- UN Data  

---

## 🛠 Tools
- R and RStudio
- Python
   - NumPy
   - Pandas
   - SciPy

---