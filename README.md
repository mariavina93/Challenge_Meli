# Challenge Meli

# 🌐 Tablero de Indicadores de Conectividad en Argentina

Este proyecto tiene como objetivo explorar la **evolución del acceso a internet y sus posibles causas** en Argentina a lo largo de los últimos años, utilizando datos de fuentes oficiales y herramientas de visualización accesibles.

---

## 📊 Herramienta de visualización utilizada

El análisis fue desarrollado y publicado en **Tableau Public**:

🔗 **[Ver tablero interactivo en Tableau Public →](https://public.tableau.com/app/profile/maria.vi.a2611/viz/Dashboard-IndicadoresArgentina/TablerodeIndicadoresArgentinos?publish=yes)**

---

## 🗂️ Estructura del repositorio

```
Challenge_Meli/
├── .github/
│   └── workflows/
│       └── update_csv.yml                       ← GitHub Action que actualiza el CSV automáticamente
├── arquitectura/
│   └── arquitectura.drawio                      ← (arquitectura editable editable)
│   └── arquitectura.png                         ← (Imagen de arquitectura)

├── dashboard/
│   └── Dashboard - Indicadores Argentina.twb    ← Tablero final
├── images/
│   └── mercado-libre.png                        ← logo png de mercado libre
│   └── worldbank.png                            ← logo png de worldbank
├── data/
│   └── indicadores_argentina.csv                ← Dataset actualizado desde la API del World Bank
├── scripts/
│   └── update_data.py                           ← Script Python que descarga y limpia los datos
└── README.md                                    ← Este archivo
```

---

## 🧠 Arquitectura utilizada

![Arquitectura referencial](https://github.com/mariavina93/Challenge_Meli/blob/main/arquitectura/arquitectura.png)

---

## ⚙️ Flujo de trabajo automatizado

1. 📡 El script `update_data.py` se conecta a la [API del World Bank](https://data.worldbank.org/)
2. 🔁 Cada semana, GitHub Actions actualiza automáticamente el archivo `indicadores_argentina.csv`
3. 📄 El dataset se sincroniza con Google Sheets, fuente directa en Tableau
4. 📊 Tableau Public consume estos datos y actualiza el dashboard

---

## 🔍 Indicadores analizados

- **Usuarios de internet (% de la población)** – `IT.NET.USER.ZS`
- **Suscripciones móviles por cada 100 habitantes** – `IT.CEL.SETS.P2`
- **PIB per cápita (USD)** – `NY.GDP.PCAP.CD`

---

## 📈 Visualizaciones destacadas

- **Evolución histórica de usuarios de internet**
- **Comparación con suscripciones móviles**
- **Crecimiento interanual**
- **KPIs del último año disponible**

---

## 📌 Conclusiones del análisis

- 📈 El acceso a internet en Argentina ha crecido de manera sostenida desde el año 2000, pasando de un 7% a más del 89% en 2023.
- 📱 Las suscripciones móviles crecieron incluso más rápido, llegando a más de 150 líneas por cada 100 personas, lo que indica usuarios con múltiples chips/dispositivos.
- 🔁 El crecimiento interanual más fuerte se registró en 2010, con un aumento del 11%.
- 📉 En los últimos años, el crecimiento se ha desacelerado, lo que podría indicar una etapa de madurez o saturación del acceso.
- 💡 Se observa una correlación visual con la expansión móvil, pero también una caída abrupta en suscripciones en el último dato disponible, posiblemente por cambio metodológico o reporte parcial.

---

## ✍️ Autor

Desarrollado por **María José Viña** como parte de un challenge de analítica y visualización para Mercado Libre utilizando datos del Banco Mundial desde el siguiente link.

🔗[API del World Bank](https://data.worldbank.org/) 

