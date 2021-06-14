# Thuringian Data Cube

## Implementation

With the help of the developed software tool ARDCube the Thuringian Data Cube (TDC) was implemented on the HPC system TerraSense, which is used by the Department of Earth Observation at the Friedrich Schiller University Jena. It runs CentOS 7 as the operating system and the available computing resources on the selected node consist of four AMD Opteron 6348 processors that operate at 2.8 GHz by default and contain 12 single-threaded cores each. Moreover, 500 GB of computing memory and an HDD (Hard Disk Drive) file system are available. The following sections describe the implementation in reference to the ARDCube modules used.


### Data Selection

For the initial implementation of the TDC, EO datasets were acquired for a selected area and timeframe. The spatial extent of the area of interest covers the Free State of Thuringia, located in central Germany (Figure @fig:thuringia), while a timeframe of three years was chosen for the temporal extent: from 2017-01-01 until 2019-12-31.

Based on the spatial and temporal extents, EO data for the optical satellites Landsat 8 and Sentinel-2A/B, were acquired using the *download_level1* module of ARDCube. Both Landsat 8 and Sentinel-2A/B carry multispectral sensors: OLI (Operational Land Imager) and MSI (MultiSpectral Instrument) for Landsat 8 and Sentinel-2A/B respectively. They work passively by measuring particular parts of the electromagnetic spectrum that is emitted by the sun (i.a., infrared and visible light) and reflected back from the Earth.

Furthermore, EO data for the Sentinel-1A/B satellites was already available on TerraSense for the same extents. In contrast to the optical satellites, Sentinel-1A/B use a C-band SAR instrument to actively send and receive signals to collect information about the Earth's surface. The data was acquired in the Interferometric Wide Swath (IW) acquisition mode, for both ascending and descending orbits, and include both VH (Vertical transmit; Horizontal receive) and VV (Vertical transmit; Vertical receive) polarizations. 

![Extent of the Free State of Thuringia, including various characteristics (e.g., location in Germany, topography and the location of major cities). An area of the Roda forest is highlighted, which is of interest for the use case described in Section @sec:roda-forest-analysis. The map is projected in the GLANCE7 EU grid [@Holden] with corresponding easting and northing coordinates. An additional grid shows latitude and longitude coordinates of the commonly used WGS84 reference system (EPSG:4326).](source/figures/04_results_1__thuringia.png){#fig:thuringia width=100% short-caption="Extent and characteristics of the Free State of Thuringia."}

Additional maps are available in Appendix A with the tiling schemes for Sentinel-2A/B level-1 (Figure @fig:appendixfig_A1) and Landsat 8 (Figure @fig:appendixfig_A2) acquisitions overlaid over the area of interest. Sentinel-1A/B, on the other hand, do not use a fixed tiling scheme. ESA regularly provides acquisition segments covering a period of 12 days each, which is not feasible to visualize in this case. However, exemplary scene footprints for ascending and descending orbits are provided in Figure @fig:appendixfig_A3.

Hereinafter, references of Sentinel-2 and Sentinel-1, always include each mission's currently active satellites (i.e., Sentinel-1A and Sentinel-1B). Any reference to an *optical dataset* includes both Landsat 8 and Sentinel-2 data.


### Optical Satellite Data

The level-1 data acquired were processed to an ARD format using the *process_ard* module of ARDCube. In total, 234 Landsat 8 scenes with a size of 247 GB, and 2200 Sentinel-2 scenes with a size of 1400 GB formed the basis for this particular step of the TDC implementation.

The processing workflow of the FORCE L2PS module (Figure @fig:force) can be customized with various processing parameters. In the case of processing data for the TDC, mostly default settings were chosen, as they are commonly used by the FORCE developers themselves to generate ARD [@FORCE-Docs3]. Some of the more important parameters are listed in Table \ref{table:force-params}. 

To perform the topographic correction, as well as improving cloud and cloud shadow detection and atmospheric correction, a Digital Elevation Model (DEM) is needed. A DEM with 10 m spatial resolution for the entire extent of the Free State of Thuringia was provided by the Department of Earth Observation for this purpose, which has been derived from openly available LiDAR (Light Detection and Ranging) data [@GDITh]. The DEM was used in an uncompressed format to prevent a possible negative impact on processing performance [cf. @Alberti2018].  

No water vapor correction using an external water vapor database was performed, as this option is only relevant for Landsat data and in particular Landsat 4-7 [@Frantz2019a], which were not used for this implementation. The *Improphe* algorithm was used to improve the spatial resolution of the 20 m Sentinel-2 bands during the *Resolution Merge* processing step. Further details on the algorithm are provided by @Frantz2016a.

\begin{table}[h]
\caption[FORCE L2PS processing parameters used for the implementation
of the TDC.]{\label{table:force-params}FORCE L2PS parameters used to process Landsat 8 and Sentinel-2 scenes for the implementation of the TDC. BRDF = Bidirectional Reflectance Distribution Function; AOD = Atmospheric Optical Depth.}
\end{table}

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

FORCE L2PS uses a nested parallelization strategy and settings are highly depended on each system's setup. To choose appropriate settings in this regard, the advice given by @FORCE-Docs3 was followed and the processing of both datasets was performed on a TerraSense node using 12 processes with 2 threads each. Using this setup, it took 1 hour and 45 minutes to process the Landsat 8 dataset, and 48 hours and 36 minutes for the Sentinel-2 dataset. A simple log file with additional information about the processing of each individual scene is written by FORCE. From these it was calculated that the actual average processing time for Landsat 8 scenes was 5 minutes and 24 seconds, whereas Sentinel-2 scenes took an average of 15 minutes and 52 seconds. This difference is expected, because of the higher spatial resolution of the Sentinel-2 data and the additional *Resolution Merge* processing step. 

The resulting files for both datasets were written in the GeoTIFF format with band sequential (BSQ) interleaving, Lempel–Ziv–Welch (LZW) compression and internal blocks for partial image access. The size of internal blocks depends on the specifications of the overall tiling grid, which is described in Section @sec:projection. Generally, however, they are arranged as strips that are as wide as the size of each individual tile. Other GeoTIFF format settings, such as compression algorithm, are not easily changed as they are hard-coded in FORCE.

Two GeoTIFF files were created for each scene: a multi-band GeoTIFF for the Bottom Of Atmosphere (BOA) reflectance, and a single-band GeoTIFF for quality assurance information (QAI). The bands of each BOA file contain data that is specific to the commonly used spectral wavelengths of optical EO sensors and are provided in a common spatial resolution. Metadata, including data that is specific to FORCE, was written into each file automatically during processing. Furthermore, to simplify the usage of data from multiple sensors the mapping of the internal bands was homogenized, which is shown in Table \ref{table:appendixtab_A1} of Appendix A. Additionally, Table \ref{table:appendixtab_A2} provides more details about the information contained in the QAI files.  


### SAR Satellite Data  

As mentioned in Section @sec:data-selection, ascending and descending datasets for the Sentinel-1 satellites were provided by the Department of Earth Observation and already processed to an ARD format. Through a Bash script that was also supplied for each scene, the individual steps of the original processing workflow could be retraced. Instead of the software SNAP, which is used by the workflow integrated in ARDCube, here, the proprietary software GAMMA was used with pyroSAR to process the datasets. In both cases, however, radiometrically terrain-corrected gamma nought backscatter data in accordance with the workflows presented by @Truckenbrodt2019 are produced. The exact type and spatial resolution of the DEM used for processing could not be identified through the Bash scripts but were confirmed to have been sourced from SRTM 1 arcsecond (~30 m resolution) data. In total, 1494 scenes with a size of 460 GB, and 1218 scenes with a size of 404 GB for the ascending and descending datasets, respectively, were provided. 

To assure that the SAR datasets are in the same geographic projection and tiling grid as the optical datasets, the post-processing steps described in Section @sec:modules were applied using the *process_ard* module. As a result of using the auxiliary FORCE module *force-cube*, some specifications related to the produced GeoTIFF file format are the same as described for the optical datasets, including compression algorithm, internal block size and BSQ encoding. The resulting scenes consist of two single-band GeoTIFF files, each containing the data specific to one of the polarizations (VV and VH). General metadata was provided as an additional XML file for each scene, and no additional, FORCE-specific metadata was written into the files during the post-processing steps.  


### Projection & Tiling {#sec:projection}

Applying an appropriate geographic projection and tiling structure to ARD products is an important aspect to consider in the context of EODCs and subsequent time-series analysis of the data. FORCE has implemented a data cube structure and file organization, which is presented in more detail by @Frantz2019 (pp. 2-3). The key elements of this concept are that all ARD products are reprojected into a common CRS and organized in a grid system as non-overlapping tiles. As such, the following terminology has been defined by @Frantz2019 [p. 3]:

- “Grid”: the spatial subdivision of the land surface in the target CRS.
- “Tile”: a grid cell with a unique tile identifier, e.g., X0003_Y0002.
- “Chip”: original images are partitioned/tiled into several chips by intersecting them with the grid.

Similar concepts have been applied to the production of Landsat ARD products [@Dwyer2018], while Sentinel-2 level-1 data is already being distributed as gridded data. However, the Sentinel-2 tiling scheme uses Universal Transverse Mercator (UTM) zones, which is resulting in redundant data because of overlapping areas of the individual tiles. Further, it can cause difficulties when analyzing large areas, as each UTM zone constitutes a different projection [@Roy2016].

For the processing of ARD via FORCE, multiple parameters related to projection and tiling can be specified. Two grid systems are already implemented in FORCE as default options with predefined parameters: EQUI7, which consists of seven equi-distant, continental projections, and GLANCE7 with seven equal-area, continental projections. The latter was applied to all datasets of the TDC as part of the ARD processing described in Sections @sec:optical-satellite-data and @sec:sar-satellite-data. The resulting grid system for the TDC with square tiles covering 150 by 150 km each is shown in @fig:glance. 

![GLANCE7 EU grid over the spatial extent of the Free State of Thuringia (derived from @ATKIS2021 data). Each grid cell constitutes a non-overlapping tile covering 150 by 150 km and can be identified with a unique tile identifier.](source/figures/04_results_2__glance.png){#fig:glance width=100% short-caption="Tiling scheme of the Thuringian Data Cube."}

The GLANCE7 grid was developed as part of the NASA MEaSUREs project GLobal LANd Cover and Estimation (GLANCE) designed by Boston University [@Friedl] and is based on the EQUI7 grid system proposed by @BauerMarschallinger2014. It uses Lambert Azimuthal Equal Area projections to minimize distortion for each of the seven continents and ensures that areas in an ARD product are in proportion to the actual areas on the Earth's surface. More details about each continental grid is provided by @Holden. A similar equal-area projection has also been used by @Dwyer2018 for a Landsat ARD product. 


### Indexing

With the *prepare_odc* module of ARDCube, the final implementation step for the TDC was performed. Hereby, ODC dataset documents were generated automatically for each dataset, and more accurately for each individual image chip after the aforementioned tiling was applied. Ultimately, a total of 405 YAML files were generated for the Landsat 8 dataset, 1102 for the Sentinel-2 dataset, as well as 1580 for the ascending and 2349 for the descending Sentinel-1 datasets. This also includes a number of documents for very small image chips that were produced due to the tiling (e.g., tile *X0031_Y0025* in Figure @fig:glance). 

The generated YAML files were then indexed into the ODC database using command-line functions provided by the ODC Python package. In case of the Sentinel-1 ascending and descending datasets, all files are stored in the same directory structure. Both datasets were, however, indexed as two separate products by distinguishing between their orbit directions. Ultimately, this results in an easier usage of the data, as both datasets can still be combined in an analysis when needed.  



## Use Cases

After completing the implementation of the TDC on TerraSense, the usability was evaluated through computations encompassing the entire spatial and temporal extent of the TDC, as well as a smaller scale time-series analysis. The former is described in Section @sec:per-pixel-computations and the latter in Section @sec:roda-forest-analysis.

As mentioned in Section @sec:python-framework the conda *user* environment facilitates usage of the TDC. As a prerequisite, the containerized PostgreSQL database needs to run as a background process in order for the ODC Python package to access the indexed data. Furthermore, a JupyterLab server was started on TerraSense to provide an interactive working environment, which could then be accessed on an external system via a Secure Shell Protocol (SSH) tunnel that simply forwards the necessary port used by the JupyterLab server.  

All files related to the results presented in this section are also available in a public GitHub repository: [https://github.com/maawoo/TDC_use](https://github.com/maawoo/TDC_use).


### Per-pixel Computations

#### Concept

To identify any problems and possible bottlenecks in terms of disk and memory bandwidth on one hand, and to get a better understanding of the spatio-temporal characteristics of the datasets on the other, per-pixel computations were performed. Hereby, for each individual pixel of the entire spatial extent of the TDC, the sum of valid (SAR datasets) and clear-sky (optical datasets) observations are calculated by considering each pixel's time-series information. 

The calculation for the SAR datasets is rather straightforward, as only no data values need to be excluded or masked to get the sum of valid observations and only one of the polarization bands need to be considered as the coverage of valid data is expected to be the same. 

For optical datasets, on the other hand, an appropriate clear-sky mask needs to be created from the information provided by the QAI band. In this case, the masking tool of the ODC core Python package was used to create a Boolean mask from the QAI flag values listed in Table \ref{table:qai_flags}. The values are combined in a logical *AND* fashion, which means that pixels are only set to *True* if all conditions apply. The result is a Boolean array for the entire dataset, which is then used to calculate the sum of valid, clear-sky observations.

\setcounter{table}{1}

\begin{table}[h]
\caption[QAI flags used for the per-pixel computation of the optical datasets. A comprehensive list of QAI flags can be found in Table \ref{table:appendixtab_A2}]{\label{table:qai_flags}Quality Assurance Information (QAI) flags used to create a Boolean mask for the per-pixel computation of the optical datasets (Landsat 8, Sentinel-2).}
\end{table}

-----------------------------------------------------------
**QAI flag**                                **Value**                      
------------------------------------------ ----------------
Valid data                                   'valid'                             

Cloud state                                  'clear'                             

Cloud shadow                                 'no' / False                             
-----------------------------------------------------------


#### Performance Considerations

Some performance aspects need to be considered before large computations are performed. As described in Section @sec:odc_methods the Python package Dask is handling the parallelization of computations, and more specifically the distributed scheduler of Dask is used, as, amongst others, it provides access to a diagnostic dashboard and performance reports [@Dask-Docs_performance]. Two aspects in particular were evaluated by using the aforementioned per-pixel computation on a spatial subset of the Sentinel-1 ascending dataset: array chunk sizes and multi-threading. 

As described by @Rocklin2015, Dask uses NumPy-like arrays and blocked array algorithms internally. It can handle large computational problems efficiently by breaking up an array into smaller chunks, performing a computation per chunk and then aggregating all intermediate results. The arrangement (e.g., per dimension) and size of array chunks can affect performance and also depends on the algorithm used [@Dask-Docs_chunks]. In case of the per-pixel computation, for example, only the spatial dimensions need to be chunked as the algorithm requires all values along the temporal dimension. 

A simple test was performed by varying the chunk size as shown in Figure @fig:dask_chunks. The number of tasks that are needed to ultimately come to the same computational result is also shown for both arrays. As a result of quadrupling the chunk size from 500 by 500 (A) to 1000 by 1000 (B) pixels in the spatial dimensions, the number of tasks needed decreases significantly, which furthermore decreases the total duration of the computation from 449 seconds to 196 seconds. 

![Variation of the Dask chunk size for the same dataset and performed computation. The chunk size is adjusted for the spatial dimensions (x, y), while each chunk covers the entire extent of the available time dimension. An increase of chunk size from 500 by 500 (A) to 1000 by 1000 pixels (B) decreases the number of tasks needed to perform the computation.](source/figures/04_results_3__dask_chunks.png){#fig:dask_chunks width=85% short-caption="Per-pixel computation: Testing Dask chunk sizes."}

The second test concerns multi-threading, which is known as the ability of a single processor to follow multiple streams of execution concurrently [@Nemirovsky2013, p. 1]. Processors are also called *workers* in some cases, such as Dask, and streams are commonly known as *threads*. For the multi-threading test only the number of workers and threads per worker was varied, while the computation, data subset and chunk sizes remained identical. The diagnostic dashboard and reports provided by Dask can visualize the stream of individual tasks performed by each thread and thereby reveal inefficient use of computing resources. 

The task streams of 4 workers and 6 threads per worker (A), as well as 1 worker and 24 threads (B) are shown in Figure @fig:dask_task_stream. The coloration of tasks reveals that a certain amount of communication is needed when multiple workers are utilized (A). Additionally, the computation seems to happen in a sequential order, i.e., pixel values are loaded first and the aggregation along the time dimension and per chunk is being done at the end. When a single worker has access to all available threads (B), on the other hand, a more even distribution of tasks is apparent. Furthermore, the use of allocated computing resources is more efficient and a continuous usage is facilitated. This is also reflected in a faster computation time of 196 seconds as opposed to 270 seconds in case of the former.

![Variation of Dask multi-threading parameters for the same dataset and performed computation. In case of the data type and computation used here, the change from 4 workers with 6 threads each (A) to 1 worker managing all 24 threads (B), results in a more efficient and faster computation. Further information on Dask performance reports is provided by @Dask-Docs_performance.](source/figures/04_results_4__dask_task_streams.png){#fig:dask_task_stream width=100% short-caption="Per-pixel computation: Testing Dask multi-threading parameters."}

\newpage
#### Results {#sec:pp_obs_results}

Based on the performance considerations tested, the actual per-pixel observations were calculated for each dataset. The results for the Sentinel-1 (descending) and Sentinel-2 datasets are shown in Figure @fig:pp_obs_s1_desc and @fig:pp_obs_s2, respectively. Similar figures are available in Appendix B for the Sentinel-1 (ascending) (Figure @fig:appendixfig_B1) and Landsat 8 (Figure @fig:appendixfig_B2) datasets.

On a larger spatial scale the number of valid observations is mostly affected by the orbits of the initial level-1 datasets. This can be observed in all cases, with some regions of fewer observations overlapping between the different datasets. Additionally, the original overlapping UTM grid of the Sentinel-2 dataset can be identified due to a slightly higher number of observations along its edges (see Appendix A, Figure @fig:appendixfig_A1 for comparison). 

As expected, the Sentinel-1 datasets show a rather homogenous distribution of values. However, a closer look reveals clusters of pixels with lower numbers of valid observations in comparison to surrounding areas. Most clusters appear in urban areas, as highlighted in Figure @fig:pp_obs_s1_desc for the state capital Erfurt, and might be related to processing artifacts due to high backscatter values.

Smaller-scale patterns are apparent in both optical datasets, due to the cloud and cloud shadow mask used for the computation. Some particular patterns correspond to false positive cloud and cloud shadow detections of the modified FMask algorithm that is used during ARD processing [@Frantz2015; @Frantz2018]. Examples are highlighted as A and B in Figure @fig:pp_obs_s2. Various points located in urban or industrial areas are repeatedly flagged as cloud covered, which appear as circular areas of fewer observations because of the 300 m buffer chosen during processing (see Table \ref{table:force-params}) (A). In other areas the extent of water bodies is outlined due to false positive cloud shadow detections (B).

Other, larger-scale patterns seem to show a natural variation due to topography. As highlighted by C in Figure @fig:pp_obs_s2, the number of clear-sky observations in the Thuringian forest, which is situated at higher elevations than the rest of the region, is noticeably lower than in the Thuringian basin located to the northeast (see Figure @fig:thuringia for comparison).   

![Number of valid observations between 2017-01-01 and 2019-12-31 for each available pixel of the Sentinel-1A/B descending dataset. An area of the state captial Erfurt is highlighted (a), which shows clusters of pixels with a reduced number of valid observations in comparison to surrounding areas.](source/figures/04_results_5__obs_s1_desc.png){#fig:pp_obs_s1_desc width=100% short-caption="Per-pixel computation: Valid observations for Sentinel-1A/B descending."}

![Number of clear-sky observations between 2017-01-01 and 2019-12-31 for each available pixel of the Sentinel-2A/B dataset. Various areas are highlighted: (a) shows repeated false positive cloud detections that might appear in urban or industrial areas [@Frantz2018]; (b) shows repeated false positive cloud shadow detections that might appear over water bodies [@Frantz2015]; (c) is highlighting an area of the Thuringian forest with a reduced number of clear-sky observations, which is likely related to the topography of the region (see Figure @fig:thuringia).](source/figures/04_results_6__obs_s2.png){#fig:pp_obs_s2 width=100% short-caption="Per-pixel computation: Clear-sky observations for Sentinel-2A/B."}


\newpage
### Roda Forest Analysis

#### Motivation & Study Area

A further assessment of the usability of the TDC was performed through a time-series analysis that incorporates all available datasets. For this analysis the Roda forest was chosen, which is located to the southeast of the city of Jena (see Figure @fig:thuringia), and primarily contains coniferous, evergreen trees [@Thiel2016]. Figure @fig:roda_aoi shows the area in more detail with a forest cover layer from an official survey [@ATKIS2021] overlaid.

The motivation behind this analysis lies in the severe summer drought that Central European forests experienced in 2018. The drought was classified as climatically even more extreme than the millennial drought of 2003 and resulted in a significant increase of drought-induced tree mortality, as well as drought-legacy effects in 2019 [@Schuldt2020]. The temporal extent of the current implementation of the TDC is suitable to compare the years for which most of the drought effects are expected to be observed (2018 and 2019) to a reference year (2017). 

![Roda forest between the cities of Kahla in the northwest and Neustadt an der Orla in the southeast. A forest covered area of interest is highlighted, which is relevant for the subsequent analysis. The map is projected in the GLANCE7 EU grid [@Holden] with corresponding easting and northing coordinates.](source/figures/04_results_7__roda_aoi.png){#fig:roda_aoi width=85% short-caption="Roda forest: Overview of the area of interest."}

\newpage
#### Methodology

For the first part of the analysis, the Normalized Difference Vegetation Index (NDVI) [@Rouse1974] is calculated for all clear-sky observations of the Landsat 8 and Sentinel-2 datasets. The NDVI is a commonly used index to monitor vegetation health and is calculated using the following spectral bands: 

$NDVI = \frac{NIR - RED}{NIR + RED}$ {#eq:ndvi}

The Landsat 8 data is resampled using the Nearest Neighbor interpolation to the same 10 m pixel spacing as the Sentinel-2 dataset, thus creating an array of the same size and facilitating the merging of both arrays into a single NDVI dataset. As both datasets have slightly different acquisition times, no individual time steps get merged and the full temporal resolution is thereby retained. 

The merged NDVI dataset is used to calculate temporal aggregates for the summer periods (June, July and August) of each available year. Hereby, for each pixel the median value per summer period is calculated. The resulting aggregated rasters can then be compared, e.g., by calculating the difference between the rasters for the summer periods 2018 and 2019 to the raster of the reference year 2017. This enables a visual assessment of possible drought effects in the region of interest. A similar raster showing the described difference between summer periods is also calculated for the Sentinel-1 ascending dataset. Here, the cross-polarized (VH) backscatter data is used, as it generally highlights volume scattering, which typically occures in forest canopies.

For the second part of the analysis the aforementioned rasters are inspected to identify forest areas that show a significant decrease in NDVI and VH backscatter values, suggesting drought-related degradation. A pixel of apparent degradation, and one located in a more stable area are then selected to visualize the time-series of all available dataset values. 

#### Results {#sec:roda_results}

Figure @fig:roda_analysis_1 shows the results of the first part of the analysis. The resulting rasters are visualizing the cumulative difference (i.e., 2018 and 2019 combined) of median NDVI (A) and VH backscatter (B) relative to the summer period of 2017 and show very similar patterns overall. Some extensive areas, such as in the northwest corner, show a significant decrease in both NDVI and VH backscatter. However, as can be seen in Figure @fig:roda_aoi these areas are usually not covered by forest but likely used for agriculture, and are therefore not in the interest of this study. 

A particular region is highlighted for both rasters (a = NDVI; b = backscatter), which shows a forested area in the central part of the region of interest. Here, patches of apparent degradation can be observed and two pixels were selected for the visualization of the time-series, which are shown in Figure @fig:roda_analysis_2. Furthermore, an interesting feature is only visible in the highlighted area of the calculated backscatter difference (b), where the patches of apparent degradation seem to be accompanied by patches of increased values.

The time-series plots A and B in Figure @fig:roda_analysis_2 (points P1 and P2 in Figure @fig:roda_analysis_1, respectively) confirm the reasoning behind selecting these particular points and show different developments of the values over time. While all datasets visualized for point P2 seem to be rather stable throughout the observed timeframe, a significant decrease of NDVI values and a noticeable decrease of VH backscatter values can be observed for point P1 around May 2018. It should be noted that outlier values are likely to still be present in the NDVI time-series, especially for winter months. A seasonal variation of the backscatter signal can be observed in plot B, which is particularly apparent for the descending dataset. No seasonality is apparent in the NDVI time-series on the other hand. 

Additional figures can be found in Appendix B. Figure @fig:appendixfig_B3 shows the calculated NDVI difference for the summer periods 2018 and 2019 in reference to 2017 as separate plots. Figure @fig:appendixfig_B4 is the equivalent of Figure @fig:roda_analysis_1 (B) for the descending dataset. Lastly, Figures @fig:appendixfig_B5 and @fig:appendixfig_B6 show individual plots of median NDVI and backscatter for each summer period.

![Difference of the median NDVI (Normalized Difference Vegetation Index) derived from the optical datasets (A) and SAR backscatter (ascending orbit; VH polarization) (B) for the summer periods (June, July, August) 2018 and 2019 relative to 2017. A centrally located area is highlighted for both rasters, where two points (P1, P2) were selected for the time-series visualization (see Figure @fig:roda_analysis_2). The maps are projected in the GLANCE7 EU grid [@Holden] with corresponding easting and northing coordinates.](source/figures/04_results_8__roda_analysis_1.png){#fig:roda_analysis_1 width=100% short-caption="Roda forest: Median NDVI and SAR backscatter (ascending) difference between summer periods 2018/2019 relative to 2017."}

![Time-series plots for the points selected in Figure @fig:roda_analysis_1. Point P1 shows a decrease in both NDVI (Normalized Difference Vegetation Index) and backscatter values after May 2018, whereas the values for point P2 appear to be stable over the available timespan. The VH backscatter values were slightly smoothed by calculating the weekly mean. NDVI values that were used to calculate the median for each summer period (see Figure @fig:roda_analysis_1) are highlighted.](source/figures/04_results_9__roda_analysis_2.png){#fig:roda_analysis_2 width=100% short-caption="Roda forest: NDVI and SAR backscatter time-series plots for two selected points of interest."}
