# Registro de decisiones · Equipo 2

Decisiones de diseño del nodo y de la herramienta web, con su fecha y justificación. Las más recientes van al final.

| Fecha | Decisión | Justificación | Reto |
|---|---|---|---|
| 2026-10-02 | Se adopta el CT SCT-013-100 de **100 A / 1 V** en lugar de los de 20 A o 30 A. | Es el único que cubre el objetivo de proyectos de hasta 20 kW (≈ 22 kVA en fase dividida 110/220 V). Se acepta su menor sensibilidad a corrientes bajas (5 mV eficaces a 0,5 A). | R1 |
| 2026-10-02 | Se usa un CT por línea (L1 y L2). | La red residencial objetivo es de dos líneas y neutro; cada línea se mide por separado. | R1 |
| 2026-10-21 | El Reto 2 se centra solo en el **software** (módulo de dimensionamiento de la página web). | Acordado con el docente en la socialización del Reto 2. El hardware se retoma en el Reto 3. | R2 |
| 2026-10-19 | La tensión se mide con **un solo módulo ZMPT101B**, conectado entre líneas con caimanes. | Simplifica el montaje y el costo; el módulo aporta aislamiento galvánico mediante transformador. | R3 |
| 2026-10-19 | La etapa de acondicionamiento usa un **LM358** con dos seguidores. | Aísla la salida de los CT de la entrada del ADC del ESP32. | R3 |
| 2026-10-19 | El nodo se alimenta con **5 V DC por USB** y va en una carcasa aislante. | Fuente fácil de conseguir y montaje seguro para uso en interiores. | R3 |
| 2026-09-30 | Los materiales se compran en **Ferretrónica** (ferretronica.com). | Disponibilidad fuera de Santa Marta y entrega de 1 a 3 días hábiles. Aunque hubo retrasos por la transportista. Costo de los componentes del nodo: $140.000 (meta ≤ $150.000). | R3 |
| 2026-10-19 | En el Reto 3 se reportan **solo valores de diseño**; la medición se realiza dias antes del **viernes 23 de octubre de 2026**. | Criterio acordado con el docente. | R3 |
