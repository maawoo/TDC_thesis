# Background

## Big Data & Innovation

Since the beginning of the current century, a majority of the world's technological capacity to store, communicate, and compute information has relied on digital formats [@Hilbert2011]. This has not only resulted in the amount of data growing continuously, but also the importance of 'Big Data' being realized in various fields of society, such as science, industry, and government [@WEF2012]. 

The arising challenges and opportunities of growing amounts of EO and geospatial data have already been important topics in the 1990s. Al Gore coined the term 'Digital Earth' in a speech in 1998, where he envisioned a digital representation of our Earth and how it could benefit society [@Gore1998]. In the same decade, the need for improved management strategies of spatial information have increasingly been recognized by administrations worldwide and resulted in the development of Spatial Data Infrastructures (SDIs) [@Schade2019].

As presented by @Guo2016 and @Boulton2018, challenges and opportunities related to the current era of 'Big Earth Data' are still being discussed two decades later. In the context of EO, 'Big Earth Data' is particularly being fueled by the open data policies of the Landsat program, which includes an archive of over 40 years of global EO data [@Wulder2019], and the Copernicus program with its family of Sentinel satellites [@Aschbacher2017]. Furthermore, new missions are soon to be launched [e.g., @Kellogg2020] and new sensor technologies are being developed [e.g., @Kampe2017]. The commercial EO sector on the other hand is striving to provide EO data that exceeds the spatial- and temporal resolution of publicly available data [e.g., @Farquharson2018].

The volume of publicly available EO and geospatial data keeps growing and the variety of spatial-, spectral- and temporal resolutions, data formats and standards, adds to the complexity of generating valuable information from this data. 

Innovative trends in the rapidly evolving information technology (IT) sector have frequently been adopted by the geospatial sector. @Diaz2012 investigated this subject in relation to the development of SDIs and named 'cloud computing' as an important trend. It describes a paradigm that allows individuals to access not only data that is being managed in a remote facility, but also applications and computing power, over the internet and on demand [@Foster2008]. 

@Sudmanns2020 describe a change in EO data analysis workflow that is suitable for dealing with large amounts of EO data, where analysis-ready datasets and appropriate tools for information production, are being provided in a cloud environment. They also describe that most professionals still rely on the 'traditional' workflow of downloading and processing datasets locally, however, cloud computing platforms such as Google Earth Engine [@Gorelick2017] have become more popular in recent years and enabled scientists to use EO data in unprecedented, global-scale studies [e.g., @Hansen2013]. 

As a consequence of these changing workflows and increasing volumes of open data being used for individual analyses, innovation is also happening in closely related areas. Data formats for example are evolving and being optimized for network-based access. In their work, @Durbin2020 compared the data formats GeoTIFF and NetCDF-4, two established standards in the domain of Earth Science, with their optimized equivalents Cloud-optimized GeoTIFF and Zarr. Furthermore, new specifications such as the SpatioTemporal Asset Catalog (STAC) are being developed to provide a standardized way of describing and indexing spatial data and thereby improving discoverability [@STAC2021].

In close relationship to open data and arguably an equally important driver of innovation is open source software, i.e., collaboratively developed software projects that can be used, changed, and distributed freely. @Coetzee2020 have reviewed the current state of open data and open source software in the context of the geospatial domain. They came to the conclusion that both “have changed the way in which geospatial data are collected, processed, analyzed, and visualized” and that they probably will be even more important in the future (p.24). 

A recent publication by @Abernathey2020 provides an interesting perspective on several of the aspects previously described while also considering reproducibility and FAIR Data Principles [@Wilkinson2016]. @Abernathey2020 suggest that the creation of cloud-native data repositories could be “a viable path forward to help data-intensive scientific fields overcome current infrastructure challenges” (p.10).



## Earth Observation Data Cubes

To address challenges related to 'Big Earth Data', new technological solutions have emerged in recent years. Besides cloud computing platforms like Google Earth Engine, there are an increasing number of software projects that in some way or another use the term 'Data Cube' and usually are open source. These projects can be categorized under the term Earth Observation Data Cubes (EODCs) and offer a new approach to store, organize and manage large volumes of analysis-ready EO data and thereby lowering the barrier for users to exploit the data to its full potential [@Killough2018]. 

The following section will...


### Concept

While EODCs have gained popularity in recent years, the underlying idea does not originate in the geospatial domain. Already in the early 1990s, data cubes of business and statistical data have been used in the context of Online Analytical Processing (OLAP) and the Business Intelligence domain. @Ariav1986 defined a data cube as a “three-dimensional and inherently temporal data construct where time, objects, and attributes are the primary dimensions of stored data” (p.1). The general notion that data cubes are multidimensional data structures which include some form of metadata attributes, can be transferred to the concept of data cubes in the geospatial domain. Technological developments related to OLAP data cubes, however, are not directly applicable, as EO data in the form of spatio-temporal rasters is typically densely populated rather than sparsely [@Baumann2018].    
 
...


- Short 'Intro' to data cubes in EO. Different initiatives, different interpretations of this concept, inconsistent use of terminology.
- At a basic/simplified level EODCs can be seen similar to fig1

*Fig: Schematic of an EO cube* (Kopp2019?)

- But more complex that this! Multiple publications that try to define important aspects of data cube systems in EO:

- Baumann2017 - The Datacube Manifesto
  - Spatio-Temporal Gridded Data
  - Treat All Axes Alike
  - Efficient Single-Step Multi-Dimensional Extraction
  - Fast Along All Axes
  - Adaptive, Transparent Partitioning
  - Flexible Access and Analysis Language
  
- Strobl2017 - The six faces of the data cube
  - Parameter Model
  - Data Representation
  - Data Organisation
  - Infrastructure
  - Access and Analysis
  - Interoperability

- Nativi2017
  - Data-Cube infrastructure model based on a set of viewpoints
  - purpose was to stress important interoperability and re-usability aspects that should be carefully considered when designing an Earth Data-Cube infrastructure
  - A set of interoperability views were introduced and characterized to facilitate the comprehension of the complexity of Data-Cube systems and the possible interoperability levels necessary for being part of larger ecosystems
  - This model aims to support and complement the ongoing discussion on the “cube” facets, initiated by the developers of some significant Data-Cube infrastructures (Strobl et al., 2017)


### Overview of related projects

- Short overview of existing projects / initiatives
  - Baumann2015 & Misev2019 / EarthServer & BigDataCube (using rasdaman as backend and relying on OGC coverages)
  - Mahecha2020 / Earth System Data Lab ()
  - Appel2019 / gdalcubes
  - Lewis2017 / ODC

- Distinction from platforms like GEE and Sentinel Hub
  - Lack of consensus/distinction ? -> confusing
    - [@Gomes2020]: No differentiation and using the general term 'Platforms for big EO Data Management and Analysis'
    - [@Giuliani2019]: Tries to differentiate between data cube and cloud-based processing facilities
- Some advantages / disadvantages being discussed in literature
  - Not a black box / not proprietary / no vendor lock-in in comparison to platforms like GEE

- openEO is kind of a connection between everything (Pebesma2017 & Schramm2021)

- Mahecha2020: Most of the data cube initiatives are, however, motivated by the need for accessing singular (very-)high-resolution data cubes, e.g. from satellite remote sensing or climate reanalysis, and not by the need for global multivariate data exploitation
- datacube approaches, involving Array Databases, systems with procedural (typically python) interfaces, array libraries, and more [Baumann2018]


### Open Data Cube

- History
- Short technical description (more detailed in method section)
- Overview of related literature and national/regional deployments 

*Table: ODC deployments and relevant publications*


## Analysis Ready Data

- What is ARD? (History, Definitions)
- Important aspects for SAR and optical data
- Why is it important?
- How can it be acquired at the moment?
- How can it be generated at the moment?
- Current developments / Future

---

bla

### Requirements for all sensors

### Optical sensors

### Radar sensors 
