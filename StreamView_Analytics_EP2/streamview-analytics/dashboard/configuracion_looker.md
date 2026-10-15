# Configuración de Looker Studio

## Fuentes

datos_limpios_ep2: data/content_clean.csv, 31.991 filas y 35 columnas.
financials_ep2: data/content_financials.csv, 3.540 filas y 20 columnas.
Llave de relación: content_id, nunca el tmdb_id sin prefijo. Las claves son únicas en ambas tablas.

## Tipos

Números: release_year, vote_count, vote_average_x1000, popularity_x1000, es_confiable, es_7_o_mas, es_alto_potencial, n_genres, n_countries, popularity_pct_tipo, release_period_years. En finanzas: budget, revenue, profit y roi_x1000000.
Texto: IDs, títulos, categorías, rating_confiable (Sí/No) y banderas financieras (Sí/No). country_iso2 puede usarse como código geográfico; excluir ZZ y las producciones sin país único en mapas.

## Fórmulas

- Valoración por fila: vote_average_x1000 / 1000.
- Popularidad por fila: popularity_x1000 / 1000.
- Catálogo total: COUNT_DISTINCT(content_id).
- Valoración promedio: AVG(vote_average_x1000) / 1000; filtro es_confiable = 1.
- Nota >=7: SUM(es_7_o_mas) / SUM(es_confiable), formato porcentaje.
- Popularidad promedio: AVG(popularity_x1000) / 1000.
- Popularidad mediana: MEDIAN(popularity_x1000) / 1000.
- Títulos evaluables: SUM(es_confiable).
- Alto potencial: SUM(es_alto_potencial).
- Alto potencial entre evaluables: SUM(es_alto_potencial) / SUM(es_confiable), formato porcentaje.
- Países de producción: COUNT_DISTINCT(country_main); filtro tipo_produccion = Un solo país.
- Ingresos/presupuesto mediano: MEDIAN(roi_x1000000) / 1000000; solo fuente financiera.

Los porcentajes no se multiplican por 100. Mostrar sin datos si el denominador es cero. No usar los campos antiguos vote_average_x100 o roi_x1000.

## Gráficos

Géneros: genre_main, conteo de títulos, desglose content_type, orden descendente. Países: country_main, conteo, filtro tipo_produccion = Un solo país. Treemap: language y conteo de títulos. El diseño propuesto usa Top 5 sin Otros; la exportación adjunta muestra más categorías. Confirmar el límite efectivo en el reporte publicado.
Valoración por año: release_year ascendente, content_type, media de Valoración, es_confiable = 1.
Popularidad por año: release_year ascendente, content_type, mediana de Popularidad, todos los títulos, sin filtro de votos.
Alto potencial por género: genre_main, conteo de candidatos o suma de es_alto_potencial.
Tabla: title_label, content_type y genre_main como dimensiones; Valoración y Popularidad con media, Votos con máximo; filtro es_alto_potencial = 1, orden por Votos descendente.

## Interacción

Filtros por content_type, genre_main, country_main, language y release_year. Probar IDs internos de campos entre las fuentes; compartir un nombre no garantiza el filtrado. Prueba obligatoria: Serie deja el indicador financiero sin datos. Mostrar la navegación de ambas páginas y probar Restablecer en modo consulta. No afirmar una prueba funcional solo a partir de la exportación PDF.

## Acceso

[enlace_dashboard.md](enlace_dashboard.md).
