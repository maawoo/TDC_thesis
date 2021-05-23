# Thuringian Data Cube


## Implementation

With the help of the developed software tool ARDCube, the Thuringian Data Cube (TDC) was implemented on the HPC system TerraSense, which is used by the Department of Earth Observation at the Friedrich-Schiller-University Jena. The available computing resources on the selected node on TerraSense consist of four AMD Opteron 6348 processors that operate at 2.8 GHz by default and contain 12 single-threaded cores each. Moreover, 500 GB of computing memory and an HDD (Hard Disk Drive) file system are available. The following sections describe the implementation in reference to the ARDCube modules used.


### Data Selection

For the initial implementation of the TDC, EO datasets were acquired for a selected area and timeframe. The spatial extent of the area of interest covers the Free State of Thuringia, located in central Germany (Figure @fig:thuringia), while a timeframe of three years was chosen for the temporal extent: from 2017-01-01 until 2019-12-31.

Based on the spatial and temporal extents, EO data for the optical satellites Landsat 8 and Sentinel-2A/B, were acquired using the *download_level1* module of ARDCube. Both Landsat 8 and Sentinel-2A/B carry multi-spectral sensors: OLI (Operational Land Imager) and MSI (MultiSpectral Instrument) for Landsat 8 and Sentinel-2A/B respectively, which work passively by collecting sunlight that is reflected back from the Earth. 

Furthermore, EO data for the Sentinel-1A/B satellites was already available on TerraSense for the same extents. In contrast to the optical satellites, Sentinel-1A/B use a C-band Synthetic Aperture Radar (SAR) instrument to actively send and receive signals to collect information about the Earth's surface. The data was acquired in the Interferometric Wide Swath (IW) acquisition mode, for both ascending and descending orbits, and include both VH and VV polarizations.

![Extent of the Free State of Thuringia and location in Germany. The Roda forest is highlighted, which is an area of interest for +@sec:use-cases. The map is projected in UTM zone 32N (EPSG:25832), while the grid uses WGS84 (EPSG:4326) coordinates.](source/figures/04_results_1__thuringia.png){#fig:thuringia width=100%}

Additional maps are available in APPENDIX X with the tiling schemes for Landsat 8 and Sentinel-2A/B level-1 acquisitions overlaid over the area of interest. Sentinel-1A/B on the other hand do not use a fixed tiling scheme. ESA regularly provides acquisition segments covering a period of 12 days each, which is not feasible to visualize in this case. However, exemplary scene layouts for ascending and descending orbits are also provided in APPENDIX X.


### Optical Satellite Data

The level-1 data acquired were processed to a level-2/ARD format using the *process_ard* module of ARDCube. In total, 234 Landsat 8 scenes with a size of 247 GB, and 2200 Sentinel-2A/B scenes with a size of 1400 GB formed the basis for this particular step of the TDC implementation.

The processing workflow of the FORCE L2PS module (see Figure @fig:force) can be customized with various processing parameters. In the case of processing data for the TDC, mostly default settings were chosen, as they are commonly used by the FORCE developers themselves to generate ARD [@FORCE-Docs]. Some of the more important parameters are listed in Table @tbl:force-params. 

To perform the topographic correction, as well as improving cloud/cloud-shadow detection and atmospheric correction, a Digital Elevation Model (DEM) is needed. A LiDAR-derived DEM with 10 m spatial resolution for the entire extent of the Free State of Thuringia was provided by the Department of Earth Observation for this purpose. It is also important to note that no water vapor correction using an external water vapor database was performed as this option is only relevant for Landsat data, and in particular Landsat 4-7 [@Frantz2019a], which were not used for this initial implementation. Further details on the algorithm *Improphe*, which was used to improve the spatial resolution of the 20 m Sentinel-2 bands during the *Resolution Merge* processing step, is provided by @Frantz2016a.

-------------------------------------------------------------------------------
**Parameter**                                **Value**                      
------------------------------------------ ---------------- -------------------
Atmospheric Correction                        True                             

Topographic Correction                        True                             

BRDF Correction                               True                             

Adjacency Effect Correction                   True                             

Multiple Scattering Approximation             True                             

Water Vapor Correction                        Null/False      Landsat only    

Internal AOD Estimation                       True 

Cloud Buffer (m)                              300                              

Shadow Buffer (m)                             90                               

Snow Buffer (m)                               30                               

FMask Cloud Threshold                         0.225                            

FMask Shadow Threshold                        0.02                             

Resolution Merge                              Improphe        Sentinel-2 only 

Co-Registration                               Null/False      Sentinel-2 only 
-------------------------------------------------------------------------------

Table: FORCE L2PS parameters used to process Landsat 8 and Sentinel-2A/B scenes for the initial implementation of the TDC. BRDF = Bidirectional Reflectance Distribution Function; AOD = Atmospheric Optical Depth. {#tbl:force-params}

FORCE L2PS uses a nested parallelization strategy and settings are highly depended on each system's setup. To choose appropriate settings in this regard, the advice given by @FORCE-Docs was followed and the processing of both datasets was performed on a TerraSense node using 12 processes with 2 threads each. Using this setup, it took 1 hour and 45 minutes to process the Landsat 8 dataset, and 48 hours and 36 minutes for the Sentinel-2 dataset. A simple log file with additional information about the processing of each individual scene is written by FORCE. From these it was calculated that the actual average processing time for Landsat 8 scenes was 5 minutes and 24 seconds, whereas Sentinel-2 scenes took an average of 15 minutes and 52 seconds.

The resulting files for both datasets were written in the GeoTIFF format with band sequential (BSQ) interleaving, Lempel–Ziv–Welch (LZW) compression and internal blocks for partial image access. The size of internal blocks depends on the specifications of the overall tiling grid, which is described in +@sec:projection. Generally, however, they are arranged as strips that are as wide as the size of each individual tile. Other GeoTIFF format settings, such as compression algorithm, are not easily changed as they are hard-coded in FORCE.

Two GeoTIFF files were created for each scene: a multi-band GeoTIFF for the Bottom-of-Atmosphere (BOA) reflectance, and a single-band GeoTIFF for Quality Assurance Information (QAI). The bands of each BOA file contain data that is specific to the commonly used spectral wavelengths of optical EO sensors and are provided in a common spatial resolution. Metadata, including data that is specific to FORCE, was written into each file automatically during processing. Furthermore, to simplify the usage of data from multiple sensors the mapping of the internal bands was homogenized, which is shown in TABLE X (APPENDIX A) for the datasets used here. Additionally, TABLE Y (APPENDIX B) provides more details about the information contained in the QAI files.  


### SAR Satellite Data  

As mentioned in +@sec:data-selection, ascending and descending datasets for the Sentinel-1A/B satellites were provided by the Department of Earth Observation and already processed to an ARD format. Through a Bash script that was also supplied for each scene, the individual steps of the original processing workflow could be retraced. Instead of the software SNAP, which is used by the workflow integrated in ARDCube, here, the proprietary software GAMMA was used with pyroSAR to process the datasets. In both cases, however, radiometrically terrain-corrected gamma nought backscatter data in accordance with the workflow presented by @Truckenbrodt2019 is produced. The exact type of DEM and its spatial resolution could not be identified through the Bash scripts, but confirmed to have been sourced from SRTM (Shuttle Radar Topography Mission) 1 arcsecond (~30 m resolution) data. In total, 1494 scenes with a size of 460 GB, and 1218 scenes with a size of 404 GB for the ascending and descending datasets respectively, were provided. 

To assure that these datasets are in the same geographic projection and tiling grid as the aforementioned optical datasets, the post-processing steps described in +@sec:modules were applied using the *process_ard* module. As a result of using the auxiliary FORCE module *force-cube*, some specifications related to the produced GeoTIFF file format are the same as described for the optical datasets, including compression algorithm, internal block size and BSQ encoding. The resulting scenes consist of two single-band GeoTIFF files, each containing the data specific to one of the polarizations: VV (Vertical send; Vertical receive) and VH (Vertical send; Horizontal receive). General metadata was provided as an additional XML (Extensible Markup Language) file for each scene, and no additional, FORCE-specific metadata was written into the files during the post-processing steps.  


### Projection & Tiling {#sec:projection}

Applying an appropriate geographic projection and tiling structure to ARD, is an important aspect to consider in the context of EODCs and subsequent time-series analysis of the data. FORCE has implemented a data cube structure and file organization, which is presented in more detail by @Frantz2019 (p. 2-3). The key elements of this concept are that all ARD products are reprojected into a common coordinate system and organized in a grid system as non-overlapping tiles. As such, the following terminology has been defined by @Frantz2019:

- “Grid”: the spatial subdivision of the land surface in the target coordinate system.
- “Tile”: a grid cell with a unique tile identifier, e.g., X0003_Y0002.
- “Chip”: original images are partitioned/tiled into several chips by intersecting them with the grid.

Similar concepts have been applied to the production of Landsat ARD products [@Dwyer2018], while Sentinel-2 level-1 data is already distributed as gridded data. However, the Sentinel-2 tiling scheme, which uses Universal Transverse Mercator (UTM) zones, creates redundant data as tiles are overlapping, and can cause difficulties when analysing large areas, as each UTM zone constitutes a different projection [@Roy2016].

For the processing of ARD via FORCE, multiple parameters related to projection and tiling can be specified. Furthermore, two grid systems are already implemented in FORCE as default options with predefined parameters: EQUI7, which consists of seven equi-distant, continental projections, and GLANCE7 with seven equal-area, continental projections.

The latter was applied to all datasets of the TDC as part of the ARD processing described in +@sec:optical-satellite-data and +@sec:sar-satellite-data. The resulting grid system of square tiles with a size of 150 km each is shown in @fig:glance. 

![GLANCE7 grid over the extent of the TDC. Each grid cell constitutes a non-overlapping tile with a unique tile identifier.](source/figures/04_results_2__glance.png){#fig:glance width=100%}

The GLANCE7 grid was developed as part of the NASA MEaSUREs project GLobal LANd Cover and Estimation (GLANCE) designed by Boston University [@Friedl] and is based on the EQUI7 grid system proposed by @BauerMarschallinger2014. It uses Lambert Azimuthal Equal Area projections to minimize distortion for each of the seven continents and ensures that areas in an ARD product are in proportion to the actual areas on the Earth's surface. A similar equal-area projection has also been used by @Dwyer2018 for the Landsat ARD products. 


### ODC Indexing

With the *prepare_odc* module of ARDCube, the final implementation step for the TDC was performed. Hereby, ODC dataset documents were generated automatically for each dataset, and more accurately for each individual image chip after the aforementioned tiling was applied. Ultimately, a total of 111 YAML files were generated for the Landsat 8 dataset, 222 for the Sentinel-2A/B dataset, as well as 333 for the ascending and 444 for the descending Sentinel-1A/B datasets. 

Even though all Sentinel-1A/B GeoTIFF files were stored in the same directory, they have been indexed into the ODC as two separate products by distinguishing between their orbit directions. Ultimately, this results in an easier usage of the data, as both datasets can still be combined in an analysis when needed. 

...?



## Use Cases

After completing the implementation of the TDC on TerraSense, the functionality and usage was evaluated through computations encompassing the entire spatial and temporal extent of the TDC, as well as a smaller scale time-series analysis. 

As mentioned in +@sec:python-framework the conda *user* environment facilitates usage of the TDC. In addition, the containerized PostgreSQL database needs to run as a background process in order for the ODC Python package to access the indexed data. As a working environment a JupyterLab server was started on TerraSense, which could then be accessed on an external system via an SSH (Secure Shell Protocol) tunnel that forwards the necessary ports used by the database and the JupyterLab server.  

All files related to the results presented in this section are also available in a public Github repository: [https://github.com/maawoo/TDC_use](https://github.com/maawoo/TDC_use).


### Per-pixel Computations

To identify any problems and possible bottlenecks in terms of disk and memory bandwidth on one hand, and to get a better understanding of the spatio-temporal characteristics of the datasets on the other, per-pixel computations were performed. Hereby, for each individual pixel of the entire spatial extent of the TDC, the sum of valid observations are calculated by considering each pixel's time-series information. 

The calculation for SAR datasets is rather straightforward, as only no data values need to be excluded or masked to get the sum of valid observations and only one of the polarization bands need to be considered as the coverage of valid data should be the same. 

For optical datasets on the other hand, an appropriate clear-sky mask needs to be created from the information provided by the QAI band. In this case, the masking tool of the ODC core Python package was used to create a boolean mask from the QAI flag values listed in Table @tbl:qai_flags. The values are combined in a logical *AND* fashion, which means that pixels are only set to *True* if all conditions apply. The result is a boolean array for the entire dataset, which is then used to calculate the sum of valid observations.

-----------------------------------------------------------
**QAI flag**                                **Value**                      
------------------------------------------ ----------------
Valid data                                   'valid'                             

Cloud state                                  'clear'                             

Cloud shadow                                 False                             
-----------------------------------------------------------

Table: Quality Assurance Information (QAI) flags used to create a boolean mask for the per-pixel computation. {#tbl:qai_flags}

#### Performance Considerations

Some performance aspects need to be considered before large computations are performed. As described in +@sec:odc_methods the Python package Dask is handling the parallelization of computations, and more specifically the distributed scheduler of Dask is used, as, amongst others, it provides access to a diagnostic dashboard and performance reports. Two aspects in particular were evaluated by using the aforementioned per-pixel computation on a spatial subset of the Sentinel-1 ascending dataset: array chunk sizes and multi-threading. 

As described by @Rocklin2015, Dask uses NumPy-like arrays and blocked array algorithms internally. It can handle large computational problems efficiently by breaking up an array into smaller chunks, perform a computation per chunk and then aggregate all intermediate results. The arrangement (e.g., per dimension) and size of array chunks can affect performance and also depends on the algorithm used [@Dask-Docs_chunks]. In case of the per-pixel computation, for example, only the spatial dimensions need to be chunked as the algorithm requires all values along the temporal dimension. 

A simple test was performed by varying the chunk size as shown in @fig:dask_chunks. The number of tasks that are needed to ultimately come to the same computational result is also shown for both arrays. As a result of doubling the chunk size, the number of tasks needed decreases significantly, which furthermore decreases the total duration for the computation from 449 seconds to 196 seconds. 

![Chunk size comparison: A) 500x500; B) 1000x1000](source/figures/04_results_3__dask_chunks.png){#fig:dask_chunks width=75%}

The second test concerns multi-threading, which is known as the ability of a single processor to follow multiple streams of execution concurrently [@Nemirovsky2013, p. 1]. Processors are also called *workers* in some cases, such as Dask, and streams are commonly known as *threads*. For the multi-threading test only the number of workers and threads per worker was varied, while the computation, data subset and chunk sizes stayed the same. The diagnostic dashboard and reports provided by Dask can visualize the stream of individual tasks performed by each thread and thereby reveal inefficient use of computing resources. 

The task streams of 4 workers and 6 threads per worker, as well as 1 worker and 24 threads are shown in Figure @fig:dask_task_stream A and B, respectively. Overall it is apparent that the tasks are more evenly distributed when a single worker has access to all threads and that it facilitates continuous usage of their allocated computing resources. The coloration of tasks reveals that a certain amount of communication is needed when multiple workers are utilized. Additionally, the computation seems to happen in a sequential order, i.e., pixel values are loaded first and the aggregation along the time dimension and per chunk, being done at the end. Task stream B on the other hand shows a more efficient use of resources, which is reflected in the total duration of 196 seconds as opposed to 270 seconds in case of task stream A. 

![Task stream comparison. A) 4 workers/6 threads each; B) 1 worker/24 threads each](source/figures/04_results_4__dask_task_streams.png){#fig:dask_task_stream width=100%}

\newpage
#### Results {#sec:pp_obs_results}

Based on the performance considerations tested, the actual per-pixel observations were calculated for each dataset. The results for the Sentinel-1A/B (descending) and Sentinel-2A/B datasets are shown in Figure @fig:pp_obs_s1_desc and @fig:pp_obs_s2, respectively. Similar figures are available in APPENDIX X for the Landsat 8 and the Sentinel-1A/B (ascending) datasets.

On a larger spatial scale the number of valid observations is mostly affected by the orbits of the initial level-1 datasets. This can be observed in all cases, with some regions of fewer observations overlapping between the different datasets. Additionally, the original overlapping UTM grid of the Sentinel-2A/B dataset can be identified due to slightly higher number of observations along its edges (see APPENDIX ? for comparison). 

As expected, the Sentinel-1A/B datasets show a rather homogenous distribution of values. However, a closer look reveals clusters of pixels with lower numbers of valid observations in comparison to surrounding areas. Most clusters appear in urban areas, as highlighted in Figure @fig:pp_obs_s1_desc for the state capital Erfurt, and might be related to processing artifacts due to high backscatter values.

Smaller scale patterns are apparent in both optical datasets, due to the cloud/cloud-shadow-mask used for the computation. Some particular patterns correspond to false positive detections of the modified FMask algorithm that is used during ARD processing [@Frantz2015; @Frantz2018]. Examples are highlighted as A and B in Figure @fig:pp_obs_s2. Various points located in urban or industrial areas are repeatedly flagged as cloud covered and appear as circular areas of fewer observations because of the 300 m cloud-buffer chosen during processing (see Table @tbl:force-params) (A), while other areas outline the extent of water bodies due to false positive cloud-shadow detections (B). Other patterns seem to show a natural variation due to topography. As highlighted by C, the number of valid observations in the Thuringian forest, which is situated at higher elevations than the rest of the region, is noticeably lower than in the Thuringian basin located to the northeast.   

![Wird nochmal überarbeitet! Per pixel observations - Sentinel-1A/B Descending](source/figures/04_results_5__obs_s1_desc.png){#fig:pp_obs_s1_desc width=100%}

![Wird nochmal überarbeitet! Per pixel observations - Sentinel-2A/B](source/figures/04_results_6__obs_s2.png){#fig:pp_obs_s2 width=100%}


\newpage
### Roda Forest Analysis

A further assessment of the usability of the TDC was performed through a time-series analysis that incorporates all available datasets. For this analysis the Roda forest was chosen, which is located to the south-east of the city of Jena (see Figure @fig:thuringia), and primarily contains coniferous, evergreen trees [@Thiel2016]. Figure @fig:roda_aoi shows the area in more detail with a forest cover layer from the @ATKIS2021 survey overlaid.

The motivation behind this analysis lies in the severe summer drought that Central European forests experienced in 2018. The drought was classified as climatically even more extreme than the millennial drought of 2003 and resulted in a significant increase of drought-induced tree mortality, as well as drought-legacy effects in 2019 [@Schuldt2020]. The temporal extent of the current implementation of the TDC is suitable to compare the years for which most of the drought effects are expected to be observed (2018 & 2019) to a reference year (2017). 

![Roda forest between the cities of Kahla in the north-west and Neustadt an der Orla in the south-east. A forest cover layer is superimposed [@ATKIS2021]. Spatial reference system: GLANCE7 EU grid.](source/figures/04_results_7__roda_aoi.png){#fig:roda_aoi width=100%}


#### Methodology

For the first part of the analysis, the Normalized Difference Vegetation Index (NDVI) is calculated for all clear-sky observations of the Landsat 8 and Sentinel-2A/B datasets. The NDVI is a commonly used index to monitor vegetation health and is calculated using the following spectral bands: 

$NDVI = NIR - RED/NIR + RED$ {#eq:ndvi}

The Landsat 8 data is resampled using Nearest Neighbor interpolation to the same 10 m spatial resolution as the Sentinel-2A/B dataset, thus creating an array of the same size and facilitating the merging of both arrays into a single NDVI dataset. As both datasets have slightly different acquisition times, no individual time steps get merged and the full temporal resolution is retained. 

The merged NDVI dataset is used to calculate temporal aggregates for the summer periods (June, July and August) of each available year. Hereby, for each pixel the median value per summer period is calculated. The resulting aggregated rasters can then be compared, e.g., by calculating the difference between the rasters for the summer periods 2018 and 2019 to the raster of the reference year 2017. This enables a visual assessment of possible drought effects in the region of interest. A similar raster showing the described difference between summer periods is also calculated for the Sentinel-1A/B ascending dataset. Here, the cross-polarized (VH) backscatter data is used, as it generally highlights volume scattering, which is typical for the canopies of forests.

For the second part of the analysis the aforementioned rasters are inspected to identify forest areas that show a significant decrease in NDVI and VH backscatter values, suggesting drought-related degradation. A pixel of apparent degradation, and one located in a more stable area are then selected to visualize the time-series of all available values. 

#### Results {#sec:roda_results}

Figure @fig:roda_analysis_1 shows the results of the first part of the analysis. Both rasters, visualizing the difference of median NDVI and backscatter for the summer periods 2018 and 2019, relative to the reference year 2017, show very similar patterns. Some extensive areas show a significant decrease in both NDVI and VH backscatter for example. As can be seen in Figure @fig:roda, however, these are usually not covered by forest and are likely areas that are used agriculturally. Additional figures can be found in APPENDIX X, which show the difference for the summer periods 2018 and 2019 in reference to 2017 separately.  

A particular region is highlighted for both rasters, which shows a forested area in the central part of the region of interest. Here, patches of apparent degradation can be observed in both rasters and two pixels were selected for the visualization of the time-series, which are shown in Figure @fig:roda_analysis_2. The most striking difference between both time-series is a significant decrease of NDVI values and a noticeable decrease of VH backscatter values around May 2018 in case of plot A. The time-series of plot B, on the other hand, appears to be rather stable throughout. It also seems to show a seasonal variation of the backscatter signal, which does not seem to appear in the NDVI signal. 

![Difference of the median NDVI and ascending VH backscatter for the summer periods 2018 and 2019 relative to 2017. A centrally located area is highlighted for both rasters, where two pixels were selected for the time-series visualization (see Figure @fig:roda_analysis_2). Spatial reference system: GLANCE7 EU grid.](source/figures/04_results_8__roda_analysis_1.png){#fig:roda_analysis_1 width=100%}

![Time-series plots for the pixels selected in Figure @fig:roda_analysis_1. The VH backscatter values were smoothed by calculating the weekly mean. NDVI values that were used to calculate the median for each summer period are highlighted.](source/figures/04_results_9__roda_analysis_2.png){#fig:roda_analysis_2 width=100%}
