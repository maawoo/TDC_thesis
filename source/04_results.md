# Thuringian Data Cube


## Implementation

With the help of the developed software tool ARDCube, the Thuringian Data Cube (TDC) was implemented on the HPC system Terrasense, which is used by the Earth Observation department at the Friedrich-Schiller-University Jena. The available computing resources on the selected node on Terrasense consist of 24 CPUs with a total of 48 threads, 500 GB RAM memory and an HDD file system. The following sections describe the implementation in reference to the ARDCube modules used. ...?


### Data Selection

For the initial implementation of the TDC, EO datasets were acquired for a selected area and timeframe. The spatial extent of the area of interest covers the Free state of Thuringia, located in central Germany (Figure @fig:thuringia), while a timeframe of 3 years was chosen for the temporal extent: from 2017-01-01 until 2019-12-31.

Based on the spatial and temporal extents, EO data for the optical satellites Landsat 8 and Sentinel-2A/B, were acquired using the *download_level1* module of ARDCube. Both Landsat 8 and Sentinel-2A/B carry multi-spectral sensors: OLI (Operational Land Imager) and MSI (MultiSpectral Instrument) for Landsat 8 and Sentinel-2A/B respectively, which work passively by collecting sunlight that is reflected back from the Earth. 

Furthermore, EO data for the Sentinel-1A/B satellites was already available on Terrasense for the same extents. In contrast to the optical satellites, Sentinel-1A/B use a C-band synthetic aperture radar (SAR) instrument to actively send and receive signals to collect information about the Earth's surface. The data was acquired in the Interferometric Wide Swath (IW) acquisition mode, for both ascending and descending orbits, and include both VH and VV polarisations.

![Free(!) state of Thuringia with Roda forest AOI.](source/figures/04_results_1__thuringia.png){#fig:thuringia width=100%}

Additional maps are available in APPENDIX X with the tiling schemes for Landsat 8 and Sentinel-2A/B level-1 acquisitions overlaid over the area of interest. Sentinel-1A/B on the other hand do not use a fixed tiling scheme. ESA regularly provides acquisition segments covering a period of 12 days each, which is not feasible to visualize in this case. However, exemplary scene layouts for ascending and descending orbits are also provided in APPENDIX X.


### Optical Satellite Data

The level-1 data acquired were processed to a level-2/ARD format using the *process_ard* module of ARDCube. In total 234 Landsat 8 scenes with a size of 247 GB, and 2200 Sentinel-2A/B scenes with a size of 1400 GB, formed the basis for this particular step of the TDC implementation.

The processing workflow of the FORCE L2PS module (see Figure @fig:force) can be customized with various processing parameters. In the case of processing data for the TDC, mostly default settings were chosen, as they are commonly used by the FORCE developers themselves to generate ARD [@FORCE-Docs]. Some of the more important parameters are listed in @tbl:force-params. 

To perform the topographic correction, as well as improving cloud/cloud-shadow detection and atmospheric correction, a Digital Elevation Model (DEM) is needed. A Lidar-derived DEM with 10 m spatial resolution for the entire extent of the Free state of Thuringia was provided by the Earth Observation department for this purpose. It is also important to note that no water vapor correction using an external water vapor database was performed as this option is only relevant for Landsat data, and in particular Landsat 4-7 [@Frantz2019a], which were not used for this initial implementation. Further details on the Improphe algorithm used for the processing step *Resolution Merge*, which is used to improve the spatial resolution of the 20 m Sentinel-2 bands to 10 m, is provided by @Frantz2016a.

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

Table: Important parameters! {#tbl:force-params}

FORCE L2PS uses a nested parallelization strategy and settings are highly depended on each system's setup. To choose appropriate settings in this regard, the advice given by @FORCE-Docs was followed and the processing of both datasets was performed on a Terrasense node using 12 processes with 2 threads each. Using this setup it took 1 hour and 45 minutes to process the Landsat 8 dataset, and 48 hours and 36 minutes for the Sentinel-2 dataset. A simple log file with additional information about the processing of each individual scene is output by FORCE. From these it was calculated that the actual average processing time for Landsat 8 scenes was 5 minutes and 24 seconds, whereas Sentinel-2 scenes took an average of 15 minutes and 52 seconds.

The resulting files for both datasets were written in the GeoTIFF format with band sequential (BSQ) interleaving, LZW compression and internal blocks for partial image access. The size of internal blocks depend on the specifications of the overall tiling grid, which is described in +@sec:projection. Generally, however, they are arranged as strips that are as wide as the size of each individual tile. 

Two GeoTIFF files were created for each scene: a multi-band GeoTIFF for the Bottom-of-Atmosphere (BOA) reflectance, and a single-band GeoTIFF for Quality Assurance Information (QAI). The bands of each BOA file contain data that is specific to the commonly used spectral wavelengths of optical EO sensors and are provided in a common spatial resolution. Metadata, including data that is specific to FORCE, was written into each file automatically during processing. Furthermore, to simplify the usage of data from multiple sensors the mapping of the internal bands was homogenized, which is shown in TABLE X (APPENDIX A) for the datasets used here. Additionally, TABLE Y (APPENDIX A) provides more details about the information contained in the QAI files.  

Considering all data format specifications described, the resulting size of the datasets after processing to an ARD format is 12.5 GB for Landsat 8 and 520 GB for Sentinel-2.


### SAR Satellite Data  

As mentioned in +@sec:data-selection, ascending and descending datasets for the Sentinel-1A/B satellites were provided by the Earth Observation department and were already processed to an ARD format as well. Through a Bash script that was also supplied for each scene, the individual steps of the original processing workflow could be retraced. In contrast to the workflow integrated in ARDCube, pyroSAR was utilized with the proprietary software GAMMA. In both cases, however, radiometrically terrain-corrected gamma nought backscatter data in accordance with the workflow presented by @Truckenbrodt2019 is produced. **Something something DEM.** The provided datasets had a volume of: 1494 scenes with a size of 460 GB, and 1218 scenes with a size of 404 GB for the ascending and descending datasets, respectively. 

To assure that these datasets are in the same geographic projection and tiling grid as the aforementioned optical datasets, the post-processing steps described in +@sec:modules were applied using the *process_ard* module. As a result of using the auxiliary FORCE module *force-cube*, some specifications related to the produced GeoTIFF file format are the same as described for the optical datasets, including compression algorithm, internal block size and BSQ encoding. The resulting scenes consist of two single-band GeoTIFF files, each containing the data specific to one of the polarisations: VV (Vertical send; Vertical receive) and VH (Vertical send; Horizontal receive). General metadata was provided as an additional XML file for each scene, and no additional, FORCE-specific metadata was written into the files during the post-processing steps.  

The combined size of ascending and descending datasets after all processing steps were performed is 229.5 GB.


### Projection & Tiling {#sec:projection}

Applying an appropriate geographic projection and tiling structure to ARD, is an important aspect to consider in the context of EODCs and subsequent time-series analysis of the data. FORCE has implemented a data cube structure and file organization, which is presented in more detail by @Frantz2019 (p. 2-3). The key elements of this concept are that all ARD products are reprojected into a common coordinate system, and organized in a grid system as non-overlapping tiles. As such, the following terminology has been defined by @Frantz2019:

- “Grid”: the spatial subdivision of the land surface in the target coordinate system
- “Tile”: a grid cell with a unique tile identifier, e.g., X0003_Y0002
- “Chip”: original images are partitioned/tiled into several chips by intersecting them with the grid 

Similar concepts have been applied to the production of Landsat ARD products [@Dwyer2018], while Sentinel-2 level-1 data is already distributed as gridded data. However, the Sentinel-2 tiling scheme, which uses Universal Transverse Mercator (UTM) zones, creates redundant data as tiles are overlapping, and can cause difficulties when analyzing large areas, as each UTM zone constitutes a different projection [@Roy2016].

For the processing of ARD via FORCE, multiple parameters related to projection and tiling can be specified. Furthermore, two grid systems are already implemented in FORCE as default options with predefined parameters: EQUI7, which consists of 7 equi-distant, continental projections, and GLANCE7 with 7 equal-area, continental projections.

The latter was applied to all datasets of the TDC as part of the ARD processing described in +@sec:optical-satellite-data and +@sec:sar-satellite-data. The resulting gridding of the AOI as square tiles with a size of 150 km each, is shown in @fig:glance.

![GLANCE7 grid over AOI.](source/figures/04_results_2__glance.png){#fig:glance width=100%}

The GLANCE7 grid was developed as part of the NASA MEaSUREs project GLobal LANd Cover and Estimation (GLANCE) designed by Boston University [@Friedl] and is based on the EQUI7 grid system proposed by @BauerMarschallinger2014. It uses Lambert Azimuthal Equal Area projections to minimize distortion for each of the seven continents and ensures that areas in an ARD product are in proportion to the actual areas on the Earth's surface. A similar equal-area projection has also been used by @Dwyer2018 for the Landsat ARD products. 


### ODC Indexing

With the *prepare_odc* module of ARDCube, the final implementation step for the TDC was performed. Hereby, ODC dataset documents were generated automatically for each dataset, and more accurately for each individual image chip after the aforementioned tiling was applied. Ultimately a total of 111 YAML files were generated for the Landsat 8 dataset, 222 for the Sentinel-2A/B dataset, as well as 333 for the ascending and 444 for the descending orbits of Sentinel-1A/B. 

Even though all Sentinel-1A/B GeoTIFF files were stored in the same directory, they have been indexed into the ODC as two seperate products by distinguishing between their orbit directions. Ultimately, this results in an easier usage of the data, as both datasets can still be combined in an analysis when needed. 

...?



## Utilization

- Some general information about the usage after the TDC was implemented on Terrasense
- ARDCube / 'User' environment
- PostgreSQL/ODC database container runs in background
- Jupyterlab server runs in background and can be accessed via SSH tunnel from external system
- Jupyterlab + Dask workspace


### Big Computation

- Obviously another name is needed for this section :)

- Everything related to the per pixel computation for the entire datasets (> 1 Tb size)
- Motivation:
  - Mainly just to test if anything is not working as expected when large datasets are used in analysis
  - Usefulness beyond that can be elaborated on in discussion (which was not really clear before doing the computations anyway)

- *Figs: Per pixel computations*   
  - Maybe just one optical (Sentinel-2) and one SAR (either ascending or descending) and rest in appendix?
  - Inkl highlight of interesting aspects (e.g., blobs in optical related to cloud mask... which can then be explained later on with related literature)
- Jupyter notebook available on Github


### Roda Usecase

#### Concept

- Motivation 
  - Drought 2018
  - Impacts on forest?
- Description of workflow
  - Jupyter notebook available on Github

#### Results

- *Fig: Median difference for 2018/2019 related to 2017 with an area of apparent degradation/drought impact and one without, highlighted*  
  - Zoom into the forest patch of interest and mark two points: (1) Degraded patch, (2) Non-degraded patch
- *Fig: Time-series plots of areas highlighted in figure before*  

- Individual figs for median NDVI 2017, 2018, 2019 in Appendix
