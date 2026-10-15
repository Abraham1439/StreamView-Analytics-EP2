# Datos

| Archivo | Función | Dimensiones |
| --- | --- | --- |
| raw/netflix_movies_detailed_up_to_2025.csv | Fuente original de películas | 16.000 × 18 |
| raw/netflix_tv_shows_detailed_up_to_2025.csv | Fuente original de series | 16.000 × 16 |
| content_clean.csv | Fuente general para Looker Studio | 31.991 × 35 |
| content_financials.csv | Fuente del indicador financiero | 3.540 × 20 |
| diccionario_datos.csv | Descripción y tipos de las 55 columnas exportadas | 55 filas |
| origenes.json | Procedencia, dimensiones y SHA-256 de los dos originales | Metadatos |

Los originales permanecen intactos. Los dos CSV finales se regeneran al final del notebook,
después del EDA y las validaciones. Para Looker Studio solo se cargan `content_clean.csv`
y `content_financials.csv`; el diccionario y los metadatos son documentación.

Usar `content_id` como llave. `tmdb_id` puede repetirse entre películas y series.
`vote_average_x1000` y `popularity_x1000` se dividen por 1.000.
`roi_x1000000` se divide por 1.000.000 y representa ingresos/presupuesto, no utilidad neta.

`genre_main` es el primer género homologado. Las coproducciones se agrupan sin inventar
un país principal. `date_added` se conserva, pero no acredita incorporación a la plataforma.
Los años analizados son años de estreno y el extracto no representa todo el catálogo real.

