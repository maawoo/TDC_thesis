# Methods

## Software Project

### pyroSAR

pyroSAR is a Python package initially developed by @Truckenbrodt2019a with the aim to provide a unified and scalable framework for the organization and processing of SAR satellite data. It consists of three main components: (1) identification and reading of SAR scenes from various missions, as well as the extraction and homogenization of metadata; (2) organization of the available information in a data archive as a SpatiaLite or PostgreSQL database; (3) integration of processing software, and handling of any required ancillary data. 

Out of these, the functionality provided by the processing component was implemented in the ARDCube project. More specifically, two particular tasks are handled:

- Download and preparation of a Digital Elevation Model from SRTM (Shuttle Radar Topography Mission) tiles in 1 arc-second (~30 m) spatial resolution
- Processing of Sentinel-1 SAR scenes to an ARD product using the integrated SNAP API

The latter task was investigated by @Truckenbrodt2019 in regard to the capability and usability of SNAP to produce SAR backscatter data of an appropriate quality for time-series analysis. Since the results of this study attest to the provision of reliable products, also regarding Sentinel-1 EODCs in particular, the workflow was integrated in ARDCube.

pyroSAR's open source nature and availability on Github (https://github.com/johntruckenbrodt/pyroSAR, last access: 03 May 2021) are other important aspects that strengthened the choice to include it as the main component to handle SAR processing.


### FORCE

The Framework for Operational Radiometric Correction for Environmental monitoring, or FORCE in short, is an open source software project developed by @Frantz2019. The aim of FORCE is to provide a comprehensive solution for processing data from the Landsat and Sentinel-2 archives to ARD products, and to even go beyond ARD by providing various higher-level processing modules. 


- Level-1 Archiving Suite (L1AS)
- Level-2 Processing Suite (L2PS)
- Auxiliary modules: force-tabulate-grid, force-cube & force-mosaic


*Fig: FORCE L1AS + FORCE L2PS* (DIY combination!)

- Open source and available on Github: https://github.com/davidfrantz/force 



### Open Data Cube

bla

- Leith2018, Lewis2017, ODC2021, Gomes2020
  
- Management of ARD products by indexing metadata YAML-files in a PostgreSQL database (with ODC schema)
  - CLI tools
- Access to the indexed ARD products via Python API (query database, load Xarray/Dask dataset)
- Additional functions already provided by database-core: masking!

- *Fig: Schematic figure from [medium article](https://medium.com/opendatacube/what-is-open-data-cube-805af60820d7)?*
- *Fig: Or schematic figure from [docs?](https://datacube-core.readthedocs.io/en/latest/architecture/high_level.html#load-data)*


### Containerization

- Singularity whoop!
- Very short comparison to Docker and why Singularity was chosen instead


### Python Framework 

- Short description that Python was used for developing this framework, which combines the software components mentioned before
- Conda, because environments are an important part
  - dev env
    - configparser
    - sentinelsat
    - spython
    - geopandas, fiona, rasterio
  - user env
    - datacube (odc), which already includes/builds on Xarray & Dask (core packages for working with the data as a user)
    - jupyterlab
    - ... (can be extended!)


---

Xarray is the interface for working with big datasets: it
provides a Pandas-like API for labelled n-dimensional
arrays and has backends for established and upcoming
self-describing community data file formats and access
protocols like netCDF, GeoTIFF, OPeNDAP, and Zarr.
Xarray transparently integrates Dask arrays and hence
enables users to easily scale their work to massively
parallel computations.

Dask is a library for parallel and distributed computing
that coordinates with Pythons existing scientific software 
ecosystem. In many cases, it offers users the ability to take 
existing workflows and quickly scale them
to much larger applications.

Jupyter: Jupyter notebooks and Jupyter Lab enable interactive computing and analysis from a web browser,
and JupyterHub adds multi-user support. Jupyter notebooks are quickly becoming the standard open-source
format for interactive computing not only in Python,
but also in languages such as Julia and R


## Proof of Concept
### Setup

- Terrasense HPC
- ARDCube user environment

Describing this part first could be a very good bridge to what was said in the chapter before! Especially regarding the user environment!


### Study Area
- Thuringia (the **free** state!)
- Roda forest AOI

- *Fig: Thuringia with Roda AOI + Location in Germany as a small map in a corner*


### Data
#### Optical satellite data

- General info about data
  - Landsat 8
  - Sentinel-2

- *Fig: Landsat 8 tiles overlayed over Thuringia*
- *Fig: Sentinel-2 tiles overlayed over Thuringia*

- Specific info about processing with FORCE
  - Also: Lidar DEM!

#### Synthetic Aperture Radar satellite data  

- General info about data
  - Sentinel-1

- *Fig: Sentinel-1 tiles overlayed over Thuringia*

- Processing with pyroSAR/GAMMA (not by me)
  - Short description how it was processed
- Interim processing (by me)
  - Cropping based on AOI + datacubing FORCE

#### Gridding, Projection, data format, and so on

- Aspects that are relevant to both datasets!

- *Fig: Glance7 grid?*


### Roda usecase
#### Motivation
- What is the plan and why was this usecase chosen?
- Drought 2018
- Impacts on forest?

#### Concept
- kNDVI
- VV/VH ratio
- ...
