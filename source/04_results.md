# Thuringian Data Cube


## Implementation

- Some general information about the technical implementation
- Terrasense HPC
- ARDCube / 'Maintainer' environment


### Data

#### Coverage

- Temporal and spatial coverage of the data
- Amount and volume of level-1 scenes per dataset  

- *Fig: Thuringia with Roda AOI + Location in Germany as a small map in a corner*  

#### Optical Satellite Data

- General info about the optical data and how it was processed using FORCE
  - Landsat 8
  - Sentinel-2
- Tables for spectral bands and QAI product -> Appendix!
  - Relevant: [https://force-eo.readthedocs.io/en/stable/components/lower-level/level2/format.html#product-type](https://force-eo.readthedocs.io/en/stable/components/lower-level/level2/format.html#product-type)

- *Fig: Landsat 8 tiles overlayed over Thuringia* ?  
- *Fig: Sentinel-2 tiles overlayed over Thuringia* ?  

#### SAR Satellite Data  

- General info about the SAR data and that it was already provided (but nevertheless processed using pyroSAR)
  - Sentinel-1
- Additional processing by me
  - Cropping based on AOI + datacubing FORCE

- *Fig: Sentinel-1 tiles overlayed over Thuringia* ?  

#### Output Format

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
