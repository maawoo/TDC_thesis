# Appendix {.unnumbered}

## **Appendix A — TDC Implementation** {.unlisted .unnumbered}

![Sentinel-2A/B product tiling scheme and and acquisition orbit swaths over the Free State of Thuringia.](source/figures/10_appendix_1__tiling_s2.png){#fig:appendixfig_A1 width=100% tag="A-1" short-caption="Sentinel-2A/B product tiling scheme and acquisition orbit swaths."}

![Landsat 8 product tiling scheme over the Free State of Thuringia.](source/figures/10_appendix_2__tiling_l8.png){#fig:appendixfig_A2 width=100% tag="A-2" short-caption="Landsat 8 product tiling scheme."}

![Sentinel-1A/B example acquisition footprints for the ascending (A) and descending (B) orbits over the Free State of Thuringia.](source/figures/10_appendix_3__sar_footprints.png){#fig:appendixfig_A3 width=80% tag="A-3" short-caption="Sentinel-1A/B example acquisition footprints."}


\newpage

\footnotesize
| **Wavelength Designation** | **FORCE Level-2 (Landsat 4-8)** | **FORCE Level-2 (Sentinel-2A/B)** | **USGS Level-1 (Landsat 4/5/7)** | **USGS Level-1 (Landsat 8)** | **ESA Level-1 (Sentinel-2A/B)** |
|----------------------------|---------------------------------|-----------------------------------|----------------------------------|------------------------------|---------------------------------|
| BLUE                       | 1                               | 1                                 | 1                                | 2                            | 2                               |
| GREEN                      | 2                               | 2                                 | 2                                | 3                            | 3                               |
| RED                        | 3                               | 3                                 | 3                                | 4                            | 4                               |
| REDEDGE1                   | -                               | 4                                 | -                                | -                            | 5                               |
| REDEDGE2                   | -                               | 5                                 | -                                | -                            | 6                               |
| REDEDGE3                   | -                               | 6                                 | -                                | -                            | 7                               |
| BROADNIR                   | -                               | 7                                 | -                                | -                            | 8                               |
| NIR                        | 4                               | 8                                 | 4                                | 5                            | 8A                              |
| SWIR1                      | 5                               | 9                                 | 5                                | 6                            | 11                              |
| SWIR2                      | 6                               | 10                                | 7                                | 7                            | 12                              |

Table: FORCE level-2 output bands and mapping to original level-1 bands. Adapted from [@FORCE-Docs2; @Frantz2019]. {#tbl:appendixtab_A1 tag="A-1"}

\normalsize


\newpage

\footnotesize
| **Bit No.** | **Parameter Name**   | **Bit Comb.** | **Integer** | **State**                                           |
|-------------|----------------------|---------------|-------------|-----------------------------------------------------|
| 0           | Valid data           | 0             | 0           | valid                                               |
|             |                      | 1             | 1           | no data                                             |
| 1-2         | Cloud state          | 00            | 0           | clear                                               |
|             |                      | 01            | 1           | less confident cloud                                |
|             |                      | 10            | 2           | confident, opaque cloud                             |
|             |                      | 11            | 3           | cirrus                                              |
| 3           | Cloud shadow         | 0             | 0           | no                                                  |
|             |                      | 1             | 1           | yes                                                 |
| 4           | Snow                 | 0             | 0           | no                                                  |
|             |                      | 1             | 1           | yes                                                 |
| 5           | Water                | 0             | 0           | no                                                  |
|             |                      | 1             | 1           | yes                                                 |
| 6-7         | Aerosol state        | 00            | 0           | estimated (best quality)                            |
|             |                      | 01            | 1           | interpolated (mid quality)                          |
|             |                      | 10            | 2           | high (aerosol optical depth > 0.6)                  |
|             |                      | 11            | 3           | fill (global fallback, low quality)                 |
| 8           | Subzero              | 0             | 0           | no                                                  |
|             |                      | 1             | 1           | yes                                                 |
| 9           | Saturation           | 0             | 0           | no                                                  |
|             |                      | 1             | 1           | yes                                                 |
| 10          | High sun zenith      | 0             | 0           | no                                                  |
|             |                      | 1             | 1           | yes (sun elevation < 15°)                           |
| 11-12       | Illumination state   | 00            | 0           | good (IA < 55°, best quality for TC)                |
|             |                      | 01            | 1           | medium (IA 55°-80°, good quality for TC)            |
|             |                      | 10            | 2           | poor (IA > 80°, low quality for TC)                 |
|             |                      | 11            | 3           | shadow (IA > 90°, no TC applied)                    |
| 13          | Slope                | 0             | 0           | no (cosine correction applied)                      |
|             |                      | 1             | 1           | yes (enhanced C-correction applied)                 |
| 14          | Water vapor          | 0             | 0           | measured (best quality, only Sentinel-2)            |
|             |                      | 1             | 1           | fill (scene average, only Sentinel-2)               |

Table: FORCE level-2 per-pixel quality assurance information (QAI) description. IA = Incidence Angle; TC = Topographic Correction. Adapted from [@FORCE-Docs2; @Frantz2019]. {#tbl:appendixtab_A2 tag="A-2"}

\normalsize

\newpage
## **Appendix B — TDC Use Cases** {.unlisted .unnumbered}

![Number of valid observations between 2017-01-01 and 2019-12-31 for each available pixel of the Sentinel-1A/B ascending dataset.](source/figures/10_appendix_4__obs_s1_asc.png){#fig:appendixfig_B1 width=100% tag="B-1" short-caption="Per-pixel computation: Valid observations for Sentinel-1A/B ascending."}

![Number of clear-sky observations between 2017-01-01 and 2019-12-31 for each available pixel of the Landsat 8 dataset.](source/figures/10_appendix_5__obs_l8.png){#fig:appendixfig_B2 width=100% tag="B-2" short-caption="Per-pixel computation: Clear-sky observations for Landsat 8."}


![Difference of the median NDVI (Normalized Difference Vegetation Index) derived from the optical datasets for the summer periods (June, July, August) 2018 (A) and 2019 (B) relative to 2017. The maps are projected in the GLANCE7 EU grid [@Holden] with corresponding easting and northing coordinates.](source/figures/10_appendix_6__roda_ndvi_diff.png){#fig:appendixfig_B3 width=100% tag="B-3" short-caption="Roda forest: Median NDVI difference between summer periods 2018 and 2019 relative to 2017, separately."}

![Difference of the median SAR backscatter (descending orbit; VH polarization) for the summer periods (June, July, August) 2018 and 2019 relative to 2017. The maps are projected in the GLANCE7 EU grid [@Holden] with corresponding easting and northing coordinates.](source/figures/10_appendix_7__roda_vh_diff.png){#fig:appendixfig_B4 width=100% tag="B-4" short-caption="Roda forest: Median SAR backscatter (descending) difference between summer periods 2018/2019 relative to 2017."}

![Individual plots of median NDVI (Normalized Difference Vegetation Index) derived from the optical datasets for the summer periods (June, July, August) of 2017 (A), 2018 (B) and 2019 (C).](source/figures/10_appendix_8__roda_ndvi.png){#fig:appendixfig_B5 width=100% tag="B-5" short-caption="Roda forest: Individual plots of median NDVI for summer periods 2017, 2018 and 2019."}


![Individual plots of median SAR backscatter (ascending orbit; VH polarization) for the summer periods (June, July, August) of 2017 (A), 2018 (B) and 2019 (C).](source/figures/10_appendix_9__roda_vh.png){#fig:appendixfig_B6 width=100% tag="B-6" short-caption="Roda forest: Individual plots of median SAR backscatter (ascending) for summer periods 2017, 2018 and 2019."}
