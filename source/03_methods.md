# Methods
## ARDCUBE
- Describing the main components used in this software project:
  - What is it, which role does it play and why was it chosen?

### pyroSAR
- Describing pyroSAR in general with reference to Truckenbrodt2019 & Truckenbrodt2019a
- Used in this project for:
  - processing ARD data (SAR)
  - generate SRTM DEM

### FORCE
- Describing FORCE in general with reference to Frantz2019
- Used in this project for:
  - downloading level-1 data (optical)
  - processing ARD data (optical)
  - defining gridding and organization of ARD data (both optical and SAR!)
  - defining data format of ARD data (both optical and SAR!)
  
- *Fig: Figure 2 from Frantz2019? Highlighting which part of the workflow is being used here and then just put the more detailed figures (3 & 4) for the Level 1 Archiving Suite (L1AS) and the Level 2 Processing System (L2PS) into appendix?*

### Open Data Cube
- Describing ODC in general with reference to ...
- Used in this project for:
  - organize/index metadata of the generated ARD in a PostgreSQL database
  - access to indexed ARD by querying the database and loading as Xarray dataset
    - Can then be used for analysis with Python tools (Xarray, Dask, ...)  

- *Fig: Schematic figure from [medium article](https://medium.com/opendatacube/what-is-open-data-cube-805af60820d7)?*
- *Fig: Schematic figure from [docs](https://datacube-core.readthedocs.io/en/latest/architecture/high_level.html#load-data)*

### Containerization
- Singularity!
- Short comparison to Docker and why Singularity was chosen instead

### Other
- Short description that Python was used for developing this framework, which combines the software components mentioned before
- Mention Conda, because environments are an important part
- Mention some main packages being used (e.g. sentinelsat, rasterio, fiona, configparse, ...?)



## PROOF OF CONCEPT
- **Thuringian Data Cube**

- Everything data related here, because the choice of data and processing is specific to this proof of concept and not ARDCube itself! (other projects could use different combination of data and process it differently!) 

### Study Area
- Thuringia (the **free** state!)

- *Fig: Germany with outline of Thuringia*

### Data
#### Optical satellite data
- Landsat 8
- Sentinel-2

#### Synthetic Aperture Radar satellite data  
- Sentinel-1

#### Auxiliary data
- Lidar 10m Digital Elevation Model

### Processing
#### Optical satellite data
- Processing with FORCE
  
#### Synthetic Aperture Radar satellite data
- Processing with pyroSAR (not by me)
  - Short description how it was processed
- Interim processing (by me)
  - Cropping

#### Gridding, Projection, data format, ...
- Aspects that are relevant to optical and SAR datasets

### High Performance Cluster
- Short description of Terrasense



## USECASE
- **Roda forest / drought**

### Concept / Motivation
- What is the plan and why was this usecase chosen?
- Drought 2018
- Impacts on forest?
  
### Study Area
- Roda forest
- Maybe reference that other studies have been done in this area by the department?

- *Fig: Roda forest area + Location in Thuringia*

### Data
- Subset of data described in *proof of concept* section

### Method
- kNDVI
- VV/VH ratio