
# General

### ODC

[Documentation - ODC Core](https://datacube-core.readthedocs.io/en/latest/index.html)  
[Github - ODC Core](https://github.com/opendatacube/datacube-core)  
[Github - ODC Explorer](https://github.com/opendatacube/datacube-explorer)  
[Github - ODC Stats](https://github.com/opendatacube/datacube-stats)  
[Github - ODC Tools](https://github.com/opendatacube/odc-tools)  
[Github - CEOS Datacube UI](https://github.com/ceos-seo/data_cube_ui) 

[ODC Enhancement Proposals](https://github.com/opendatacube/datacube-core/wiki/enhancement-proposals) - Description of technical improvements for ODC Core  
[Workshop material 2019 - 'Bringing ODC into practice'](https://www.researchgate.net/profile/Gregory_Giuliani/publication/334634843_Bringing_Open_Data_Cube_into_Practice_-_Workshop_Material/links/5d3703c8299bf1995b42c774/Bringing-Open-Data-Cube-into-Practice-Workshop-Material.pdf)  
[ODC Youtube Channel](https://www.youtube.com/channel/UCZcdqejeGkDBK2nP-9TWshw/videos)

### Open Earth Alliance

[Website](https://www.openearthalliance.org/)  
[Description - 2020-2022 GEO Work Programme](https://www.earthobservations.org/documents/gwp20_22/OEA.pdf)  
[Presentation - 2020 PPT ](https://www.earthobservations.org/documents/pb/me_202009/PB-18-1-4-3_Open_Earth_Alliance.pdf)     
[Presentation - GEO Virtual Symposium 2020 Video](https://www.youtube.com/watch?v=DghO-dcJ3io)

### Notebooks

[Github - CEOS Datacube Notebooks](https://github.com/ceos-seo/data_cube_notebooks)  
[Github - Catapult UK Notebooks](https://github.com/SatelliteApplicationsCatapult/odc-hub)

### ARD / Data processing

https://github.com/ceos-seo/odc_manual_indexer
[Github - eo-datasets](https://github.com/GeoscienceAustralia/eo-datasets)  
[Github - SAR ARD Processing](https://github.com/opendatacube/radar)  -> [Ticehurst2019](https://doi.org/10.3390/data4030100)   
[Github - Optical ARD Processing](https://github.com/GeoscienceAustralia/wagl)

### Docker

[Github - Cube in a Box](https://github.com/opendatacube/cube-in-a-box)  
[Github - BDC Docker](https://github.com/brazil-data-cube/bdc-odc/tree/master/docker)  
[Github - Catapult UK ARD Docker Images](https://github.com/SatelliteApplicationsCatapult/ard-docker-images)  
[Github - Catapult UK ODC Product Docker Images](https://github.com/SatelliteApplicationsCatapult/odc-product-docker-images)  

# National / Regional ODC deployments

## Australia
### Related publications:

[Woodcock2018](https://doi.org/10.1109/IGARSS.2018.8519170) - *Accelerating Industry Innovation Using the Open Data Cube in Australia*   
[Lewis2017 (!)](https://doi.org/10.1016/j.rse.2017.03.015) - *The Australian Geoscience Data Cube — Foundations and lessons learned*  
[Lewis2016](https://doi.org/10.1080/17538947.2015.1111952) - *Rapid, high-resolution detection of environmental change over continental scales from satellite data – the Earth Observation Data Cube*  

### ARD workflow:  

Described in chapter 3 of Lewis2017 but their strategy has changed in the meantime. I assume that [this](https://github.com/GeoscienceAustralia/wagl) is their current approach for processing optical and [this](https://github.com/opendatacube/radar) for SAR data. 

### Resources:  

[Github](https://github.com/GeoscienceAustralia/digitalearthau)      
[Sandbox](https://app.sandbox.dea.ga.gov.au/hub/login)  
[Sandbox - Github](https://github.com/GeoscienceAustralia/dea-sandbox)  
[Notebooks](https://github.com/GeoscienceAustralia/dea-notebooks)  
[Notebooks - Docs](https://docs.dea.ga.gov.au/index.html)  
[Algorithm - Wofs](https://github.com/GeoscienceAustralia/wofs)  
[Algorithm - Fractional Cover](https://github.com/GeoscienceAustralia/fc)  
[Algorithm - SAR Flood Mapping](https://github.com/GeoscienceAustralia/dea-sar-flood-veg)  
[Algorithm - Waterbodies](https://github.com/GeoscienceAustralia/dea-waterbodies)

## Switzerland
### Related publications:

[Giuliani2020a](https://doi.org/10.1088/1755-1315/509/1/012021) - *The Swiss Data Cube: Earth Observations for monitoring Switzerland’s environment in space and time*  
[Giuliani2017 (!)](https://doi.org/10.1080/20964471.2017.1398903) - *Building an Earth Observations Data Cube: lessons learned from the Swiss Data Cube (SDC) on generating Analysis Ready Data (ARD)*  

### ARD workflow:

ARD generation is done via [LiMES](https://doi.org/10.1016/j.rse.2017.05.040), a framework that 'helps automating EO data discovery and (pre-)processing using interoperable service chains for transforming observations into information products suitable for monitoring environmental changes.'

Chapter 3.3 in Giuliani2017 (see above) describes which algorithms are being implemented in LiMES for Landsat ARD processing (e.g. Fmask for cloud detection), but the framework itself is **not open source**.

No information available about Sentinel (1 & 2) processing.

### Resources:
  
[Github](https://github.com/GRIDgva/SwissDataCube)  
[Website](https://www.swissdatacube.org/)  
[Viewer](https://www.swissdatacube.org/viewer)  
[Explorer](http://sdc.unepgrid.ch/)  
[Geoserver](https://geoserver.swissdatacube.org/geoserver/web/)  
[Presentation - GEO Virtual Symposium 2020 Video](https://www.youtube.com/watch?v=3EUt_Dlmosg)

## Brazil
### Related publications:

[Ferreira2020 (!)](https://doi.org/10.3390/rs12244033) - *Earth Observation Data Cubes for Brazil: Requirements, Methodology and Products*  
[Picoli2020](https://doi.org/10.5194/isprs-annals-V-3-2020-533-2020) - *CBERS Data Cube: A powerful technology for mapping and monitoring Brazilian biomes*

### ARD workflow:

Detailed information about data products and processing is available [here](https://brazil-data-cube.github.io/products.html).

### Resources:

[Github](https://github.com/brazil-data-cube)  
[Documentation](https://brazil-data-cube.github.io/index.html)  
[Website](http://brazildatacube.org/)  
[Viewer](http://brazildatacube.dpi.inpe.br/portal/explore)  
[Notebooks](https://github.com/brazil-data-cube/jupyter-gallery)  
[Presentation - GEO Virtual Symposium 2020 Video](https://www.youtube.com/watch?v=Lxc8xQ0bQNs)

## Austria
### Related publications:

[Augustin2019](https://doi.org/10.3390/data4030102) - *Semantic Earth Observation Data Cubes*

### ARD workflow:

Some information about which datasets are available for the *ACube* and how they have been processed can be found [here](https://acube.eodc.eu/xwiki/bin/view/2.%20Terminology/3.3.%20Datasets/).

### Resources:

ACube - Austrian Data Cube:  
[Website](https://acube.eodc.eu/)  
[Notebooks](https://github.com/eodcgmbh/ACube_notebooks)  
[Wiki](https://acube.eodc.eu/xwiki/bin/view/Main/)  
[Presentation - EGU 2020 Poster](https://presentations.copernicus.org/EGU2020/EGU2020-21575_presentation.pdf)

sen2cube - Sentinel-2 Semantic Data and Information Cube Austria:     
[Manual](https://manual.sen2cube.at/)  
[Storymap](https://storymaps.arcgis.com/stories/05c3980c712b4190b54f7ae3156ae61e)  

## Africa
### Related publications:

[Dhu2019 (!)](https://doi.org/10.3390/data4040144) - *National Open Data Cubes and Their Contribution to Country-Level Development Policies and Practices* -> Chapter 2.4.: *Using the African Regional Data Cube to Manage Urbanization in Tanzania*  
[Killough2019](https://doi.org/10.1109/IGARSS.2019.8898321) - *The Impact of Analysis Ready Data in the Africa Regional Data Cube*

### ARD workflow:

The African Regional Data Cube and the Australian Data Cube are tightly linked. For ARD generation the same repositories as mentioned above are probebly being used.

### Resources: 

[Explorer](https://explorer.digitalearth.africa/products/ga_ls8c_gm_2_annual/extents)  
[Viewer](http://maps.digitalearth.africa/)

## Armenia
### Related publications:

[Asmaryan2019](https://doi.org/10.3390/data4030117) - *Paving the Way towards an Armenian Data Cube*  

### ARD workflow:

The Armenian Data Cube is based on the Swiss Data Cube and also uses the LiMES framework to generate ARD.

### Resources:

[Viewer](http://datacube.sci.am/)

## Catalonia (Spain)
### Related publications:

[Maso2019](https://doi.org/10.3390/data4030096) - *A Portal Offering Standard Visualization and Analysis on top of an Open Data Cube for Sub-National Regions: The Catalan Data Cube Example*  

### ARD workflow:

Not really described in detail in Maso2019. From what I understand, they just used Sentinel-2 level 2A data (Bottom of Atmosphere Reflectance) from the Copernicus Open Access Hub and Landsat data from SatCat, which is a data portal that has been organizing Landat data for Catalonia.

### Resources:

[Github](https://github.com/joanma747/CatalanDataCube)  
[Viewer](http://datacube.uab.cat/cdc/)

## Taiwan
### Related publications:

[Cheng2019](https://doi.org/10.1109/IGARSS.2019.8898576) - *Open Data Cube (ODC) in Taiwan: The Initiative and Protocol Development*  

### ARD workflow:

Not described in detail in Cheng2019. Only very short description that preprocessing of Landsat-7 and -8 included spatial alignment, radiometric correction and pixel quality index.

### Resources:

[Explorer](https://twdc.colife.org.tw/) (Link is broken?)

## Colombia
### Related publications:

[ArizaPorras2017](https://link.springer.com/chapter/10.1007/978-3-319-66562-7_7) - *CDCol: A Geoscience Data Cube that Meets Colombian Needs*  
[Bravo2017](https://link.springer.com/chapter/10.1007/978-3-319-66562-7_17) - *Architecture for a Colombian Data Cube Using Satellite Imagery for Environmental Applications*  

### ARD workflow:

...

### Resources:

...

## Virginia (USA)
### Resources:  

[Website](https://www.data4va.org/)  
[Presentation - Video](https://www.youtube.com/watch?v=T8XTrMeJoX4)

## Mexico
### Related publications:

[Dhu2019 (!)](https://doi.org/10.3390/data4040144) - *National Open Data Cubes and Their Contribution to Country-Level Development Policies and Practices* -> Chapter 2.3.1.: *Overview of the Mexican Geospatial Data Cube*

## China
### Related publications:

[Yao2018](https://doi.org/10.1109/BGDDS.2018.8626825) - *China Data Cube (CDC) for Big Earth Observation Data: Lessons Learned from the Design and Implementation*

## Sweden

https://www.ri.se/en/what-we-do/projects/swedish-space-data-lab
