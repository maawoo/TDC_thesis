# Background

Short intro text explaining the structure of this section and why I start with SDIs (-> placing EODCs in a larger context!).


## EODC in context of Spatial Data Infrastructures

- Digital Earth concept (Gore 1999)
- Development of Spatial Data Infrastructures 
  - General concept (Rajabifard2002, Guo2020, Kotsev2020)
  - INSPIRE & GEOSS as examples (regional, global)
- Parallel development of storage and data access standards -> OGC / ISO
  - WMS, WFS, WPS, ...
- From Traditional SDIs towards new (IT) trends / rapid evolution of the sector!
  - Diaz et al. (2012)!
  - Cloud computing! (Manual of DE chapter 9!)
    - Also emergence of new data formats (COG, Zarr)
- Next generation SDIs (Gomes et al. 2020)
  - Online cloud computing platforms (e.g. GEE)
  - WCPS/WTSS based systems (e.g. Rasdaman/EarthServer)
  - Data Cube systems (e.g. ODC)
  - But lack of consensus in literature on categories/definitions/... -> Lines are blurred
    - Gomes et al. (2020): No differentiation and using the general term 'Platforms for big EO Data Management and Analysis'
    - Giuliani et al. (2019): Tries to differentiate between data cube and cloud-based processing facilities

---

Although the topic of 'big Earth data' is as current as ever, arising challenges in connection with growing amounts of EO and geospatial data were already recognized and discussed in the 1990s. Former Vice President of the United States Al Gore famously coined the term 'Digital Earth' in a speech given at the California Science Center in 1998, in which he envisioned a digital representation of our Earth as an opportunity to benefit from the “flood of georeferenced information” more efficiently (Gore, 1998). In the same decade, the need for improved management strategies of spatial information was increasingly recognized by administrations and communities worldwide and resulted in the development of Spatial Data Infrastructures (SDIs), which Rajabifard, Feeney & Williamson (2002) describe as being _“fundamentally about facilitation and coordination of the exchange and sharing of spatial data between stakeholders in the spatial data community.”_ (p. 12). In their work, a generic concept for SDIs is devised, which identifies people and data as one category and policy, access network and standards as a second category (Fig. 1). The former being fundamental and consistent, whereas the latter includes components that can be seen as very dynamic due to the rapid pace of technological developments.

[Fig. 1: SDI scheme by Rajabifard et al. (2002)]

This generic concept can be applied to current implementations of SDIs, like the INSPIRE Directive of the European Union (EU). This regional SDI is expected to be fully implemented in 2021 and aims to facilitate the sharing, access and policy-making of public spatial information across EU member states (INSPIRE, 2021). A brief history of the development of SDIs and major milestones in a global context is provided by Schade et al. (2019).

Concurrent to the advancement of SDIs, the technical foundations for storing and accessing geospatial data have been developed and standardized by the International Organization for Standardization (ISO) and the Open Geospatial Consortium (OGC). In relation to EO, the Geographic Tagged Image File Format (GeoTIFF) has been widely used as a storage format for raster data (OGC 2019). Furthermore, various interfaces have been developed that enable the discovery and access of geospatial data via web-services. These include Catalogue Services for the Web (CSW), Web Mapping Services (WMS) and Web Feature Services (WFS) for discovering, viewing and downloading data, respectively (Schade et al., 2019). Additionally, the processing of geospatial data has been possible via bla and bla. 

A shift towards new technological trends that often originate in the closely related and continuously developing IT sector, can be observed in today's geospatial sector, which is also fueled by the constantly growing amount of openly available EO and geospatial data. Traditional SDIs have been focusing on serving this data via aforementioned web-services with the expectation that further processing and extraction of useful information happens client-side. Sudmanns et al. (2020) argue that this approach is inefficient when dealing with large amounts of EO data, which has lead to an increased immobility of said data and the need for adequate, server-side processing and analysis tools. 

The work of Diaz et al. (2012) discusses several trends of the IT sector and their relevance to the development of SDIs. -> cloud computing as one important trend which originates in the IT sector! This has also led to the development of new, cloud-optimized data formats. For example COG instead of GeoTIFF and Zarr instead of netCDF / HDF5. 


## Earth Observation Data Cubes

- General overview / definitions
- Difference between EODCs and Cloud computing platforms like GEE
- Open Data Cube
- Other Data Cube projects (?)

---

- ODC
  - Describe everything BUT the current technical architecture!
  - Australian history
  - ODC Initiative
  - Notable regional / national deployments
  - Future (?) / Open Earth Alliance

- Other DC projects
  - Only giving an overview of notable / comparable projects; not comparing in detail because that would be too much
  - xcubes
  - Pangeo
  - Earth System Data Lab
  - Gdalcubes
  - EarthServer

---

### General

### ODC

### Other non-ODC projects


################################################################


# Analysis Ready Data

## History & Definition(s)

- Landsat
- CARD4L

## How to process ARD

No technical deep-dive! Only highlight most important / relevant. Maybe limit selection to only highlight open source and/or free software? FORCE & pyroSAR will be explained in method section in detail.

- Optical
  - [Maja](https://labo.obs-mip.fr/multitemp/maccs-how-it-works/)
  - LiMES
  - [FORCE](https://force-eo.readthedocs.io/en/latest/)
- SAR
  - GAMMA
  - SNAP
  - pyroSAR
  - ASF MapReady? (no Sentinel-1!)

https://www.orfeo-toolbox.org/  
QGIS, GRASS GIS ?
