# Discussion

Short intro text explaining the order of discussed topics...

## Usability Assessment

By carrying out the use cases described in Section @sec:use-cases the usability of the initial implementation of the TDC could be assessed and possible improvements identified. The computation of per-pixel observations were a particular important aspect of the assessment. Even though the calculation of the sum of valid observations is rather simple, the underlying logistics of such a computation is not. This is especially the case if a very large volume of data is involved, which furthermore, is heterogeneous in nature (i.e., variability in spatial and temporal coverage). Various factors, such as the specifications of the GeoTIFF data format, can have an influence on performance and in some cases lead to problems when a computation is performed at scale. 

Fortunately, no significant issues were apparent during the per-pixel computations of the TDC. In addition, some important aspects could be tested beforehand, which are relevant to the software library used to perform scalable computations in Python. No universal set of parameters exists that always results in the best performance. As the tests have demonstrated, however, the available resources can easily be used to diagnose problems and adjust parameters accordingly. The visualization of diagnostics and insights as an interactive dashboard is a great way to reduce abstractness and the sense of working with a *black box*.     

The results of computing valid observations per pixel for the entire extent of the TDC provide valuable information about the temporal and spatial characteristics of the datasets. On one hand, inappropriate parameterization during the processing of ARD can be identified, such as a too large buffer for cloud, cloud-shadow and snow detection. Optimal parameters should of course be determined beforehand by first processing a smaller subset of the dataset. However, a visualization of the end product can reveal inconsistencies in the underlying data that might otherwise remain unnoticed. Furthermore, it can be used in support of performing time-series analysis. An area of interest can, for example, be located in a region of significantly fewer observations due to the orbit paths of the EO satellites. In addition, valid data points might be removed unintentionally when applying masks derived from the QAI band, as the algorithm used during processing can include false-positive detections [@Frantz2015; @Frantz2018]. It is important to consider these aspects before conducting an analysis or at least being aware of possible impacts. Having access to this information prior to the analysis or being able to easily generate and visualize it for a particular study area can be very beneficial. 
 
---

The study area of the Roda forest is located in a region of fewer observations for the Sentinel-2A/B and descending Sentinel-1A/B datasets. Nevertheless, the amount of data points were sufficient to conduct the time-series analysis in the form that was intended and the potential of using the TDC could successfully be demonstrated.

The correlation between decreasing NDVI and VH backscatter values in some, presumably agricultural, areas (Figure @fig:roda_analysis_1), is difficult to quantify without having any information about the crop type and cultivation cycle and is not a focus of this use case. As already described in Section @sec:roda_results, the highlighted forest area contains patches that seem to have degraded over the observed timespan. Some of these patches are accompanied by increased VH backscatter values to the northeast, which correlates with the look direction of the ascending orbit pass of the Sentinel-1A/B satellites. This effect could be caused by the clearing of forest areas, as the backscatter increase might be due to a double-bounce mechanism along the newly created forest edge [@Villard2007]. Additionally, an opposite shadow effect can sometimes be observed, which has been utilized by @Bouvet2018 to detect deforestation. However, a shadow effect does not seem to be visible in this case.  

The significant decrease of NDVI values for point A (Figure @fig:roda_analysis_2) and continuously low values thereafter, further support the assumption that at least some of these patches have not simply degraded but rather been cleared. The timing of the sharp drop-off of the NDVI time-series at the beginning of May 2018 suggests that the clearing happened at the beginning of the 2018 drought [@Schuldt2020]. A reason for such a clearing could be to prevent the spread of a bark beetle infestation. Damage caused by insect infestations has developed into the main reason for logging in German forests [@Destatis2020] and other regions worldwide, hence increasing the need for monitoring solutions that use time-series information derived from EO data [@Hollaus2019; @FernandezCarrillo2020].

The lack of seasonality in the NDVI time-series for point B might indicate that a coniferous evergreen forest is present in the area [@She2015]. A seasonal variation of the VH backscatter time-series on the other hand is plausible as the signal is influenced by the water content of the foliage, which changes over the year according to water availability [@Dubois2020]. The ascending and descending signals appear to show a more pronounced division during the summer periods 2018 and 2019 in comparison to 2017. As the orbits pass over the area during different times of the day (late afternoon for ascending; early morning for descending orbit), the diurnal difference of the backscatter signals could indicate drought related water stress [@SteeleDunne2012] and needs to be investigated further.

- Appendix stuff -> possible drought legacy effects?

Data points from the Sentinel-2A/B and Landsat 8 datasets have been combined to calculate the median NDVI differences seen in Figure @fig:roda_analysis_1 (and APPENDIX!). This combined use is not trivial, as both sensors cover slightly different spectral wavelengths. While effort is being made to create harmonized data products from both sensors [@Claverie2018; @Scheffler2020], ARD products that have been created with FORCE are not yet harmonized during processing. Therefore, this aspect needs to be considered when similar time-series analysis are conducted using the TDC and the appropriateness of aggregating data points from different datasets ultimately depends on the study objective.     

The quality of time-series derived from the Sentinel-2A/B dataset of the TDC could be improved for future analyses. Currently, the Level-1C data products of the Sentinel-2 mission have a multitemporal geometric uncertainty of around 12 m [@Gascon2017]. While a geometric refinement is currently being implemented to improve the accuracy [@ESA2021], it is not clear if the reprocessing of past datasets is planned. A coregistration option has already been implemented into FORCE L2PS (see Figure @fig:force). @Rufin2020 describe the algorithm used in more detail, which ultimately leverages base images created from the Landsat 8 near-infrared band to improve the multitemporal geometric uncertainty of the processed Sentinel-2 ARD product to an average of around 4.4 m.

---

- ODC-core, Xarray, Dask already provide a lot of possibilities to work with the data
  - The ecosystem is huge and continues to grow
  - Other libraries that are not necessarily part of the ecosystem can still be integrated if needed (e.g., numba) or wetterdienst to plot weather data (for the Roda use case for example)
  - Also ML! (e.g., example in dea-notebooks)



## Implementation Assessment
### Analysis Ready Data

- To my knowledge no official FORCE or pyroSAR CARD4L assessments have been done. (I haven't done them either...) 
  - An assessment would be helpful in identifying any shortcomings in "analysis readiness"
  - In general there is little doubt in the quality of ARD production in both cases though...

Data Format
- Currently relies on FORCE defaults for the GeoTIFF specifications that were described
- A change in data format (e.g., internal tiling of GeoTIFFs as blocks instead of strips, which is also default for COGs) would mean additional post-processing steps
- Assessments for quality, performance and so on are needed before deciding on any format changes and need to be justified, because it already works pretty well as is... 

Metadata
- Same as data itself: reliance on how FORCE/pyroSAR handle it 
- Develop a better system for organization on top of FORCE/pyroSAR? Or fully adapt the solution of one of both? Or just leave it as is because in the end both forms are machine readable (which is a CARD4L requirement)
- Integration of pyroSAR Archive functionality?
- Completeness of metadata was not evaluated. (as mentioned already: CARD4L assessments)
- ODC Dataset Documents: currently only necessary metadata and nothing else is stored (e.g. in properties field), because there's currently no benefit in doing so. It would be stored twice (at least) -> data redundancy; and even if more metadata is needed in the YAMLs it is easy to add and regenerate the files...   

Data Products
- Auxiliary data: layover/shadow map, local incidence angle, ..? -> [@Truckenbrodt2019] 
- Test Lidar DEM? -> [@Truckenbrodt2019]


### Open Data Cube

- Once everything is integrated/setup it works great, but to get there is not as straightforward as is advertised in some cases/articles
- Docker  
  - Even though it's not really mentioned in Docs, multiple Docker projects exist... 
    - https://github.com/opendatacube: 2 repos and 1 subdirectory in the core repo!
    - Then there is Datacube On Demand which is described as open source by Giuliani et al but nowhere to be found?
    - In the end Singularity container and conda environment a great solution. It works, is scalable and no security issues!
- PostgreSQL database and YAML based indexing might not be the best solution
  - Both aspects are also considered by devs and likely changed in the future (other db backends / STAC)
    - https://github.com/opendatacube/datacube-core/wiki/enhancement-proposals  
    - However, probably not any time soon...
  - Pangeo tools & STAC (+ intake-stac, stacstack, ...) seems to be great alternatives that would be worth testing
    - A **lot** of development in this area!
    - ODC is moving in the same direction with STAC integration + already shares core components (Xarray + Dask; Jupyter)... in the future the lines might be even more blurred 
    - So question is what ODC can actually offer in comparison?
      - Pangeo is just a collection of tools (Geoscience in general, not just EO) -> some functionalities/preparation steps needed to work with EO data might be lacking 
      - datacube-core is solving exactely this (wrapping Xarray and using rasterio for reprojections etc)
  - Also xcube with their Zarr integration and also the same core libraries (Xarray+Dask) is very interesting!
- Community
  - Documentation is in some parts outdated/confusing for new users. e.g. Ingestion is still described in Docs but "not recommended" in Community?
  - Big open source projects should have a proper community space to ask questions/get help
    - Current solution less than ideal to say the least...
  - Since recently ODC has been a GEO community activity 
    - ODC Initiative -> Open Earth Alliance afaik?
    - https://www.openearthalliance.org/
  - And a OSGeo Community Project 
    - http://osgeo-org.1560.x6.nabble.com/The-Open-Data-Cube-Application-for-OSGeo-Community-Project-Status-td5484126.html
    - https://www.osgeo.org/projects/open-data-cube/
  - ... so maybe those problems can soon be solved! (nobody should expect the core devs to do everything :) )



## Outlook

(ARDCube)

- ARDCube reproducibility! E.g. ease the process of reproducing someone elses project from level-1 data to ARD processing and ODC indexing to the analysis itself
  - Sudmanns2020: "[...] reproducibility not only requires a certain type of data but also semantic annotation of workflows (Scheider, Ostermann, and Adams 2017). This ensures data stewardship, comprehensive data lineage and trust in results. Producers of products and services are asked to disseminate detailed documentation of the data and workflows together with their results."
  - Giuliani2019 & Giuliani2019a
  - Abernathy2020: "Reproducibility of data science projects requires open access to at least three elements: the code, the software environment, and the data."

(TDC)

- [More data!](https://media.giphy.com/media/xT0BKi1TLjmKiu1HGg/giphy.gif)
  - Temporal 
  - Other sensors: Landsat archive with FORCE, easy and ARDCube is ready! SAR data a bit more work needed. 
- Automation / Near Real Time data stream
  - ARDCube commands could be used with a cronjob on Terrasense for example
  - Also relevant from BIDS presentation: https://elib.dlr.de/137176/
- JupyterHub to manage multiple users and computing resources 
  - Würzburg EO department! https://datacube.remote-sensing.org/
  - https://ieeexplore.ieee.org/abstract/document/9387494 
- Utilization of already available ODC extensions/applications
  - https://www.opendatacube.org/data-cube-applications
  - E.g. Explorer, which could also be used as a base project to extend as needed/wanted -> Webapp
  - Gowda2020a
