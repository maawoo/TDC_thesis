# Discussion

The following discussion is divided into three sections. Section @sec:usability-assessment discusses the usability of the initial implementation of the TDC in regard to the presented use cases and integrated datasets, while also mentioning some possible improvements that are readily available. Section @sec:implementation-assessment focuses on technical aspects of the implementation related to ARD in general and the Open Data Cube. Finally, Section @sec:outlook provides an outlook on how the ARDCube tool could be extended, as well as the possible usage of the TDC at the Department of Earth Observation at the University of Jena.  



## Usability Assessment

By carrying out the use cases described in Section @sec:use-cases the usability of the initial implementation of the TDC could be assessed and possible improvements identified. The computation of per-pixel observations were a particular important aspect of the assessment. Even though the calculation of the sum of valid observations is rather simple, the underlying logistics of such a computation is not. This is especially the case if a very large volume of data is involved, which furthermore, is heterogeneous in nature (i.e., variability in spatial and temporal coverage). Various factors, such as the specifications of the GeoTIFF data format, can have an influence on performance and in some cases lead to problems when a computation is performed at scale. 

Fortunately, no significant issues were apparent during the per-pixel computations of the TDC. In addition, some important aspects could be tested beforehand, which are relevant to the software library used to perform scalable computations in Python. No universal set of parameters exists that always results in the best performance. As the tests have demonstrated, however, the available resources can easily be used to diagnose problems and adjust parameters accordingly. The visualization of diagnostics and insights as an interactive dashboard is a great way to reduce abstractness and the sense of working with a *black box*.     

The results of computing valid observations per pixel for the entire extent of the TDC provide valuable information about the temporal and spatial characteristics of the datasets. On one hand, inappropriate parameterization during the processing of ARD can be identified, such as a too large buffer for cloud, cloud-shadow and snow detection. Optimal parameters should of course be determined beforehand by first processing a smaller subset of the dataset. However, a visualization of the end product can reveal inconsistencies in the underlying data that might otherwise remain unnoticed. Furthermore, it can be used in support of performing time-series analysis. An area of interest can, for example, be located in a region of significantly fewer observations due to the orbit paths of the EO satellites. In addition, valid data points might be removed unintentionally when applying masks derived from the QAI band, as the algorithm used during processing can include false-positive detections [@Frantz2015; @Frantz2018]. It is important to consider these aspects before conducting an analysis or at least being aware of possible impacts. Having access to this information prior to the analysis or being able to easily generate and visualize it for a particular study area can be very beneficial. 

The study area of the Roda forest is located in a region of fewer observations for the Sentinel-2A/B and descending Sentinel-1A/B datasets. Nevertheless, the amount of data points were sufficient to conduct the time-series analysis in the form that was intended and the potential of using the TDC could successfully be demonstrated.

The correlation between decreasing NDVI and VH backscatter values in some, presumably agricultural, areas (Figure @fig:roda_analysis_1), is difficult to quantify without having any information about the crop type and cultivation cycle and is not a focus of this use case. As already described in Section @sec:roda_results, the highlighted forest area contains patches that seem to have degraded over the observed timespan. Some of these patches are accompanied by increased VH backscatter values to the northeast, which correlates with the look direction of the ascending orbit pass of the Sentinel-1A/B satellites. This effect could be caused by the clearing of forest areas, as the backscatter increase might be due to a double-bounce mechanism along the newly created forest edge [@Villard2007]. Additionally, an opposite shadow effect can sometimes be observed, which has been utilized by @Bouvet2018 to detect deforestation. However, a shadow effect does not seem to be visible in this case.  

The significant decrease of NDVI values for point A (Figure @fig:roda_analysis_2) and continuously low values thereafter, further support the assumption that at least some of these patches have not simply degraded but rather been cleared. The timing of the sharp drop-off of the NDVI time-series at the beginning of May 2018 suggests that the clearing happened at the beginning of the 2018 drought [@Schuldt2020]. A reason for such a clearing could be to prevent the spread of a bark beetle infestation. Damage caused by insect infestations has developed into the main reason for logging in German forests [@Destatis2020] and other regions worldwide, hence increasing the need for monitoring solutions that use time-series information derived from EO data [@Hollaus2019; @FernandezCarrillo2020].

The lack of seasonality in the NDVI time-series for point B might indicate that a coniferous evergreen forest is present in the area [@She2015]. A seasonal variation of the VH backscatter time-series on the other hand is plausible as the signal is influenced by the water content of the foliage, which changes over the year according to water availability [@Dubois2020]. The ascending and descending signals appear to show a more pronounced division during the summer periods 2018 and 2019 in comparison to 2017. As the orbits pass over the area during different times of the day (late afternoon for ascending; early morning for descending orbit), the diurnal difference of the backscatter signals could indicate drought related water stress [@SteeleDunne2012] and needs to be investigated further.

- Appendix stuff -> possible drought legacy effects?

Data points from the Sentinel-2A/B and Landsat 8 datasets have been combined to calculate the median NDVI differences seen in Figure @fig:roda_analysis_1 (and APPENDIX!). This combined usage is not trivial, as both sensors cover slightly different spectral wavelengths. While effort is being made to create harmonized data products from both sensors [@Claverie2018; @Scheffler2020], ARD products that have been created with FORCE are not yet harmonized during processing. Therefore, this aspect needs to be considered when similar time-series analysis are conducted using the TDC and the appropriateness of aggregating data points from different datasets ultimately depends on the study objective.     

Currently, the Level-1C data products of the Sentinel-2 mission have a multi-temporal geometric uncertainty of around 12 m [@Gascon2017], which can be a negative influence on time-series analyses. While a geometric refinement is currently being implemented by ESA to improve the accuracy [@ESA2021], it is not clear if the reprocessing of past datasets is planned. A coregistration option has already been implemented into FORCE L2PS (see Figure @fig:force). @Rufin2020 describe the algorithm used in more detail, which ultimately leverages base images created from the Landsat 8 near-infrared band to improve the multi-temporal geometric uncertainty of the processed Sentinel-2 ARD product to an average of around 4.4 m. This processing option requires some preparation steps but is readily available in the version of FORCE utilized in this work. The quality of time-series can thus be improved for future analyses performed with the TDC by reprocessing the Sentinel-2A/B dataset.  

The Sentinel-1A/B datasets were already provided in an ARD format and have been processed using an SRTM 1 arcsecond DEM (see Section @sec:sar-satellite-data). As @Truckenbrodt2019 describe in their work, large discrepancies can sometimes be observed between different openly available DEM options, such as SRTM. This can affect the quality of the topographic normalization during processing and ultimately the time-series analysis of individual pixels. Similarly to the Sentinel-2A/B dataset, it might be worthwhile to reprocess the dataset to further improve the data quality in regard to time-series analysis. The LiDAR-derived DEM utilized during the processing of the Sentinel-2A/B and Landsat 8 datasets could be used after a similar quality assessement as described by @Truckenbrodt2019 has been performed.  

In conclusion, the usability of the current implementation of the TDC has successfully been demonstrated with the performed use cases. The quality of all datasets is appropriate for time-series analysis but could be further improved with readily available processing options and ancillary data. Access to the indexed ARD products via the ODC Python API works without any issues or additional preparation steps. For example, no reprojection and resampling of the data has to be performed during data loading as all datasets are stored in a common projection and the same non-overlapping tiling scheme. The utilization of a continental projection, such as GLANCE7, can be additionally advantageous in the future by facilitating interoperability with other study areas in the same region if the same projection is used.   

The existing ecosystem of Python packages surrounding the core packages Xarray and Dask is steadily growing and has been adopted by a variety of scientific fields and institutions [e.g., @EynardBontemps2019]. The aspect of adoption should not be neglected in connection with open-source software projects, as it can ensure long term support of development. Various packages in this ecosystem can pave the way to more advanced types of analyses than demonstrated here. The Dask extension dask-ml [@DaskML-Software], for example, provides access to scalable machine learning by leveraging the popular Python library Scikit-Learn [@Pedregosa2011]. Furthermore, packages that might not be directly related to the ecosystem can easily be integrated into an analysis, such as the Roda use case, to provide additional information like climatic time-series data from weather stations located in the study area [@Wetterdienst-Software]. 



## Implementation Assessment


### Analysis Ready Data

Processing optical and SAR data with the software components integrated in the ARDCube tool produces datasets that can directly be used in an analysis and hence be designated as ARD products. However, a formal assessment of how well these products comply with the current CARD4L specifications described in Section @sec:card4l, has neither been done in the course of this work, nor by the developers of FORCE or pyroSAR. However, @Truckenbrodt2019 acknowledge that this is a future goal along with a relevant extension of the pyroSAR software and at the time of writing the official CARD4L website already lists FORCE as an ARD resource.

Various aspects that are related to ARD were taken into account while developing the ARDCube tool and implementing the TDC, but were not actively adjusted or changed. For the data format of both optical and SAR datasets, for example, the current setup solely relies upon which GeoTIFF specifications are defined by FORCE for the output files. @Alberti2018 demonstrates that GeoTIFF specifications such as the compression algorithm can have a significant impact on read and write speeds, as well as the ratio of compression and therefore storage size. Moreover, the internal tiling of the files affects the performance of only accessing a small part of each file, which is done repeatedly when a time-series of a pixel is retrieved, for example. These aspects need to be considered when large volumes of EO data are supposed to be handled during an analysis. Furthermore, new raster data formats have emerged in recent times, including Cloud Optimized GeoTIFF (COG) and Zarr, which provide their own set of specifications, as well as advantages and disadvantages [@Yee2020]. 

In regard to the TDC, the current approach works quite well as demonstrated with the per-pixel computations (Section @sec:per-pixel-computations). Therefore, any changes of the data format need to be justified, as existing datasets and the processing workflows would need to be adjusted. There appears to be a lack of literature in this regard, so an assessment where different format options are compared in the same computational setup could be valuable.

Similar to the data format, the handling of metadata needs further consideration. As mentioned in Sections @sec:optical-satellite-data and @sec:sar-satellite-data, additional metadata is stored in each GeoTIFF file by FORCE, whereas the SAR datasets were provided with separate metadata files. At present, the ARDCube tool does not include any ancillary functionality or leverages relevant features provided by pyroSAR, for example, to organize the available metadata. Another layer of complexity is added by the ODC, which requires its own set of metadata files in the form of dataset documents (see Section @sec:odc_methods), which currently only contain necessary information to ensure that the ODC Python API is operable. 

The CARD4L specifications list *machine readability* as one of the minimum requirements in terms of the handling of metadata, which is satisfied in all cases mentioned. Nevertheless, a uniform solution to organize and easily access the metadata of all datasets would be desirable. The SpatioTemporal Asset Catalog (STAC) specification [@STAC] could provide a viable and standardized solution, which is planned to be implemented into the ODC in the near future [@ODC-Docs]. It uses a similar approach as already used by the ODC in the form of higher-level (*Product Definition* in ODC; *Collections* in STAC) and lower-level metadata documents (*Dataset Documents* in ODC; *Items* in STAC). Furthermore, the STAC specification is an open-source project that is already being supported by a large community with additional and openly available tools being developed, such as the STAC Browser [@STACBrowser-Software].

A final aspect to be briefly discussed is the availability of auxiliary data products, which are specified by CARD4L as *Per-Pixel Metadata*. The QAI band produced by FORCE for the optical datasets is one such product already used in the initial implementation of the TDC. It provides valuable information during analyses and can be used to filter a time-series for clear-sky observations as demonstrated in Section @sec:per-pixel-computations. For the SAR datasets on the other hand, no auxiliary data products have currently been created and integrated into the TDC. The Normalized Radar Backscatter PFS of CARD4L lists, amongst others, the provision of a local incident angle image as a minimum requirement. In addition, @Truckenbrodt2019 recommend that a map of geometrical distortion (e.g., layover and radar shadow) should also be provided. Both products can be created during processing with the current version of pyroSAR's SNAP API, which is used by the ARDCube tool.


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

- Advantage of using ODC instead of relying on something like GEE for example


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
