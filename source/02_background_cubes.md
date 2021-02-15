
# Background

Short intro text explaining the structure of this section and why I start with SDIs (-> placing EODCs in a larger context!).


## Spatial Data Infrastructures

- Digital Earth concept (Gore 1999)
- Spatial Data Infrastructures 
  - General (Rajabifard2002, Guo2020, Kotsev2020)
  - Traditional SDIs
  - Next generation SDIs
    - Cloud computing platforms (e.g. GEE)
    - Array Database systems + WCPS/WTSS (e.g. Rasdaman/EarthServer)
    - Data Cube systems (e.g. ODC)
  
---

- Abbildung für den Zusammenhang erstellen!

- Traditional vs Next Gen SDI
  - Regular raster data format (e.g. GeoTIFF)     + Database system (relational?)           + Providing data (client-side processing)
    - OGC Standards erwähnen
  - Cloud optimized data format (e.g. COG, Zarr)  + Cloud / distributed computing system    + Providing results (server-side processing)
    - STAC erwähnen

- Next Gen SDIs
  - Lines are kinda blurred between categories mentioned above because Data Cube and Array Database systems can also be deployed via cloud environments
  - Gomes et al. (2020): No differentiation and using the general term 'Platforms for big EO Data Management and Analysis'
  - Giuliani et al. (2019): Tries to differentiate between data cube and cloud-based processing facilities
  - -> Lack of consensus!

---

The challenges in connection to big EO and geospatial data were already recognized and discussed in the 1990s. Former Vice President of the United States Al Gore famously coined the term 'Digital Earth' in a speech given at the California Science Center in 1998, where he not only envisioned a digital representation of our Earth, but also how potential applications could help humankind take advantage of georeferenced information and suggested some key technologies needed for the realization of this vision (Gore, 1998). Gore also mentioned that initial focus should be on the integration of data from multiple, existing sources. 

At the same time, the need for improved management strategies of spatial information was increasingly recognized by administrations and communities worldwide and resulted in the development of Spatial Data Infrastructures (SDIs), which Rajabifard, Feeney & Williamson (2002) describe as being _“fundamentally about facilitation and coordination of the exchange and sharing of spatial data between stakeholders in the spatial data community.”_ (p. 12). They identify policy, access network and technical standards as dynamic, and people and data as consistent core components of SDIs, thereby devising a generic framework that can be applied to national, regional and global SDIs that have been developed in the last decades. 

[Figure of Rajabifard et al.'s diagram?]

This generic framework can be applied to national and regional SDIs that have been developed in the last decades. As an example, the INSPIRE Directive of the European Union aims to _”enable the sharing of environmental spatial information among public sector organisations, facilitate public access to spatial information across Europe and assist in policy-making across boundaries.”_ (INSPIRE, 2021). Also mention GEOSS in another sentence and highlight that the provision of geospatial data has gained importance! A brief history of the development of SDIs and major milestones is provided by Schade et al. (2019).  

Concurrent to the advancement of SDIs, technical foundations for the storage and access of geospatial data have been developed and standardized by the International Organization for Standardization (ISO) and the Open Geospatial Consortium (OGC). In terms of EO typical raster data, the storage format GeoTIFF has been widely used and for discovery and access of data via web-services, various interfaces have been developed by the OGC. These include Catalogue Services for the Web (CSW), Web Mapping Services (WMS) and Web Feature Services (WFS) for discovering, viewing and downloading data, respectively (Schade et al., 2019). 

Just as the geospatial sector is evolving rapidly due to an increasing availability of open data and continuous improvements of computational resources, a shift towards new data formats and the preference of users to more efficiently access useful information instead of the data itself can be observed. Traditional SDIs have been focusing on serving data via aforementioned web-services, so users can continue with further processing of the data and the subsequent extraction of useful information on their local systems. Bla bla cloud computing!

- Chapters 6 & 9 of Manual of Digital Earth!
- Diaz et al. 2020!
- Kotsev et al. 2012!



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
  - ?

---

[insert text here :)]