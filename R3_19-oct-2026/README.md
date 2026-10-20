# Reto 3 · Diseño del nodo de medición eléctrica

## Descripción

- Dos transformadores de corriente de núcleo partido SCT-013-100 (100 A / 1 V), uno por línea.
- Un módulo de tensión ZMPT101B, conectado entre líneas.
- Una etapa de acondicionamiento con dos seguidores (LM358).
- Un ESP32 que muestrea, calcula corriente, tensión y energía, y envía los registros por Wi-Fi.

```
CT L1 / CT L2  →  Conectores de CT  →  Acondicionamiento (LM358)  →  ESP32  →  Nube  →  Herramienta web
Caimanes L1 / L2  →  ZMPT101B  →  Acondicionamiento / ADC  →  ESP32
```

> **Alcance de este reto:** se entregan los **valores de diseño** del nodo, según lo acordado con el docente. La medición experimental se realizará el **viernes 23 de octubre de 2026**.

## Contenido de la carpeta

| Carpeta / archivo | Contenido |
|---|---|
| `Informe/` | Informe técnico estilo hoja de datos (máximo 2 páginas) |
| `Ficha_tecnica_interactiva/` | Ficha técnica interactiva con el modelo 3D del nodo (`Ficha_interactiva.html`) |
| `Modelo_3d/` | Capturas del modelo: vista exterior, interior y despiece |
| `Materiales/` | Lista de materiales con cantidades y precios (`Lista_de_materiales_Reto3.xlsx`) |
| `Avance/` | Avance de los Retos 1 a 3 (`avance_retos_1_a_3.md`) |
| `/Avance/DECISIONES.md` | Registro de decisiones de diseño con fecha |

## Cómo ver la ficha interactiva

1. Descargue `ficha_tecnica_interactiva/Ficha_interactiva.html`.
2. Ábralo en un navegador (Chrome, Edge o Firefox). No requiere instalación ni conexión.
3. Arrastre el modelo para girarlo, cambie entre **Exterior**, **Interior** y **Despiece**, y toque un componente para ver su descripción. El botón superior activa el modo noche.

## Costo del nodo

Los materiales se compraron en Ferretrónica (ferretronica.com). El detalle está en `Materiales/Lista_de_materiales_Reto3.xlsx`:

| Concepto | Valor (COP) |
|---|---|
| Componentes del nodo | $140.000 |
| Insumos de fabricación (baquela, cloruro férrico, estaño, jumpers) | $32.000 |
| Envío | $19.500 |
| **Total pagado** | **$191.500** |

Meta del proyecto: costo del nodo ≤ COP 150.000. Los componentes del nodo la cumplen con un margen de $10.000.

## Aportes del equipo

| Integrante | Aporte en el Reto 3 |
|---|---|
| Antony José Iguarán Fandiño | [completar] |
| Miguel Ángel Bernal López | [completar] |
| Niurka Lisseth Beltrán Vesga | [completar] |
| Nicolás Paz Mejía | [completar] |

## Referencias

1. Espressif Systems, *ESP32-WROOM-32 Datasheet*.
2. YHDC, ficha de la familia SCT013; hoja del transformador ZMPT101B.
3. Plan de retos PCD 2026-II, Equipo 2; tabla de especificaciones e informes de los Retos 1 y 2.
