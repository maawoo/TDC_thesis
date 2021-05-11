# Thuringian Data Cube

## Implementation

With the help of the developed software tool ARDCube, the Thuringian Data Cube (TDC) was implemented on the HPC system Terrasense, which is used by the Earth Observation department at the Friedrich-Schiller-University Jena. The following sections describe the implementation in reference to the ARDCube modules used. ... bla

- 48 cores / 500 GB RAM on the node

### Data Selection

For the initial implementation of the TDC, EO datasets were acquired for a selected area and timeframe. The spatial extent of the area of interest covers the Free state of Thuringia, located in central Germany (Fig x), while a timeframe of 3 years was chosen for the temporal extent: from 2017-01-01 until 2019-12-31.

Based on the spatial and temporal extents, EO data for the optical satellites Landsat 8 and Sentinel-2A/B, were acquired using the *download_level1* module of ARDCube. Both Landsat 8 and Sentinel-2A/B carry multi-spectral sensors: OLI (Operational Land Imager) and MSI (MultiSpectral Instrument) for Landsat 8 and Sentinel-2A/B respectively, which work passively by collecting sunlight that is reflected back from the Earth. 

Furthermore, EO data for the Sentinel-1A/B satellites was already available on Terrasense for the same extents. In contrast to the optical satellites, Sentinel-1A/B use a C-band synthetic aperture radar (SAR) instrument to actively send and receive signals to collect information about the Earth's surface. The data was acquired in the Interferometric Wide Swath (IW) acquisition mode, for both ascending and descending orbits, and include both VH and VV polarisations.

- *Fig: Thuringia with Roda AOI + Location in Germany as a small map in a corner*  

Additional maps are available in APPENDIX X with the tiling schemes for Landsat 8 and Sentinel-2A/B level-1 acquisitions overlaid over the area of interest. <!--Not for Sentinel-1 though... --> 


### Optical Satellite Data

The level-1 data acquired was then processed to a level-2/ARD format using the *process_ard* module of ARDCube. In total 234 Landsat 8 scenes with a size of 247 GB, and 2200 Sentinel-2A/B scenes with a size of 1400 GB, formed the basis for this particular step of the TDC implementation. 

- Some kind of table with information from FORCE logfiles?
- Tables for spectral bands and QAI product -> Appendix!

- Processing was successful without any major problems using 2 processes with 12 threads each
  - ~ time Landsat 8
  - ~ time Sentinel-2

- Size of resulting datasets


### SAR Satellite Data  

- Sentinel-1 (asc): 1494 scenes / 460 GB
- Sentinel-1 (desc): 1218 scenes / 404 GB

- General info about the SAR data and that it was already provided (but nevertheless processed using pyroSAR)
  - Sentinel-1
- Additional processing by me
  - Cropping based on AOI + datacubing FORCE

- Processing time?
- Size of resulting datasets


### Output Format

- Aspects related to all datasets
- Grid system / Non-overlapping tiles
  - Glance7!
- Data format
  - FORCE standard: GeoTIFF with internal tiling based on grid system
  - Relevant: [https://force-eo.readthedocs.io/en/latest/components/lower-level/level2/format.html#level2-format](https://force-eo.readthedocs.io/en/latest/components/lower-level/level2/format.html#level2-format)
- Metadata
  - Optical / FORCE metadata stored in GeoTIFF files
  - SAR metadata as additional files 
  - (Discussion!)
- ODC YAMLs
- *Fig: Glance7 grid* in appendix?
- Maybe split this into two sections?



## Utilization

- Some general information about the usage after the TDC was implemented on Terrasense
- ARDCube / 'User' environment
- PostgreSQL/ODC database container runs in background
- Jupyterlab server runs in background and can be accessed via SSH tunnel from Laptop (or other external system)
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


### Roda Usecase

#### Concept

- Motivation 
  - Drought 2018
  - Impacts on forest?
- Description of workflow
  - Jupyter notebook available on Github

#### Results

- *Fig: Median difference for 2018/2019 related to 2017 with an area of apparent degradation/drought impact and one without, highlighted*  
  - Trying to keep it simple here -> Individual figures in appendix
- *Fig: Time-series plots of areas highlighted in figure before*  
