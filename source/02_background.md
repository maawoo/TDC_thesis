# Background

## Big Data & Innovation

Since the beginning of the current century, a majority of the world's technological capacity to store, communicate, and compute information has relied on digital formats [@Hilbert2011]. This has not only resulted in the amount of data growing continuously, but also the importance of 'Big Data' being realized in various fields of society, such as science, industry, and government [@WEF2012]. 

The arising challenges and opportunities of growing amounts of EO and geospatial data have already been important topics in the 1990s. Al Gore coined the term 'Digital Earth' in a speech in 1998, where he envisioned a digital representation of our Earth and how it could benefit society [@Gore1998]. In the same decade, the need for improved management strategies of spatial information have increasingly been recognized by administrations worldwide and resulted in the development of Spatial Data Infrastructures (SDIs) [@Schade2019].

As presented by @Guo2016 and @Boulton2018, challenges and opportunities related to the current era of 'Big Earth Data' are still being discussed two decades later. In the context of EO, 'Big Earth Data' is particularly being fueled by the open data policies of the Landsat program, which includes an archive of over 40 years of global EO data [@Wulder2019], and the Copernicus program with its family of Sentinel satellites [@Aschbacher2017]. 

The volume of available EO and geospatial data keeps growing and the variety of spatial-, spectral- and temporal resolutions, adds to the challenge of generating valuable information from this data. New missions are soon to be launched [e.g., @Kellogg2020], new sensor technologies are being developed [e.g., @Kampe2017] and the commercial EO sector is striving to exceed the spatial- and temporal resolution of publicly available EO data [e.g., @Farquharson2018].

Innovative trends in the rapidly evolving information technology (IT) sector have frequently been adopted by the geospatial sector. @Diaz2012 investigated this subject in relation to the development of SDIs and named 'cloud computing' as an important trend. It describes a paradigm that allows individuals to access not only data that is being managed in a remote facility, but also applications and computing power, over the internet and on demand [@Foster2008]. 

@Sudmanns2020 describe a change in EO data analysis workflow that is suitable for dealing with large amounts of EO data, where analysis-ready datasets and appropriate tools for information production, are being provided in a cloud environment. They also describe that most professionals still rely on the 'traditional' workflow of downloading and processing datasets locally, however, cloud computing platforms such as Google Earth Engine (GEE) [@Gorelick2017] have become more popular in recent years and enabled scientists to use EO data in unprecedented, global-scale studies [e.g., @Hansen2013]. 

As a consequence of these changing workflows and increasing volumes of open data being used for individual analyses, innovation is additionally happening in closely related areas. Data formats for example are evolving and being optimized for network-based access. In their work, @Durbin2020 compared the data formats GeoTIFF and NetCDF-4, two established standards in the domain of Earth Science, with their optimized equivalents cloud-optimized GeoTIFF (COG) and Zarr. Furthermore, new specifications such as the SpatioTemporal Asset Catalog (STAC) are being developed to provide a standardized way of describing and indexing spatial data and thereby improving discoverability [@STAC2021].

In close relationship to open data and arguably an equally important driver of innovation is open source software, i.e., collaboratively developed software projects that can be used, changed, and distributed freely. @Coetzee2020 have reviewed the current state of open data and open source software in the context of the geospatial domain. They came to the conclusion that both “have changed the way in which geospatial data are collected, processed, analyzed, and visualized” and that open data and open source software will probably be even more important in the future (p.24). 

A recent publication by @Abernathey2020 provides a perspective on several of the aspects previously described, while also considering reproducibility and FAIR Data Principles [@Wilkinson2016]. @Abernathey2020 suggest that the creation of cloud-native data repositories could be “a viable path forward to help data-intensive scientific fields overcome current infrastructure challenges” (p.10).



## Earth Observation Data Cubes

To address challenges related to 'Big Earth Data', new technological solutions have emerged in recent years. Besides cloud computing platforms like GEE, there are an increasing number of software projects or implementations thereof in the geospatial domain, which in some way or another use the term 'Data Cube'. There still seems to be a lack of consensus in regard to the terminology, however, a number of recent publications are using Earth Observation Data Cube (EODC) as an umbrella term for these software projects and implementations [@Giuliani2019; @Kopp2019; @Ferreira2020]. According to @Killough2018, they offer a new approach to store, organize and manage large volumes of analysis-ready EO data and thereby lowering the barrier for users to exploit the data to its full potential. 

To better understand the fundamentals of EODCs, +@sec:concept provides a more comprehensive overview of the concept and how data cubes in EO are defined in literature. *@sec:software-ecosystem on the other hand provides an overview of important software projects and the Open Data Cube initiative in particular. 


### Concept

While EODCs have gained popularity in recent years, the underlying idea of data cubes does not originate in the geospatial domain. Already in the early 1990s, data cubes of business and statistical data have been used in the context of Online Analytical Processing (OLAP) and the Business Intelligence domain [@Nativi2017]. @Ariav1986 defined a data cube as “a three-dimensional and inherently temporal data construct where time, objects, and attributes are the primary dimensions of stored data” (p.1). 

The general notion that data cubes are multidimensional data structures, which include some form of metadata attributes, can be transferred to the concept of data cubes in the geospatial domain. Technological developments related to OLAP data cubes, however, are not directly applicable, as EO data in the form of spatio-temporal rasters is typically densely populated rather than sparsely [@Baumann2018]. A simplified visualization of a data cube structure of EO raster data is shown in figure 1.     

*Fig1: Schematic of an EO data cube* (DIY!) 

In response to inconsistent definitions and terminology, @Strobl2017 proposed a concept for data cubes in the geospatial domain that highlights several important aspects independently and thereby contributing to a more harmonized definition. Matching the cube analogy they identified six aspects, or rather faces, of the data cube. 

The work of @Strobl2017 builds on the conceptual view of the 'Datacube Manifesto' proposed by @Baumann2017. Furthermore, @Nativi2017 expand on the 'six faces' concept by introducing a set of modeling views with the goal of emphasizing the interoperability and reusability aspects of data cube infrastructures. However, in the following, only the six aspects identified by @Strobl2017 are briefly summarized and complemented with relevant publications:

**Parameter Model**  
The parameter model includes any metadata, parameterization and quality information that is necessary to understand what information is stored in each thematic layer of a data cube and facilitate further analysis. It remains a challenge to properly incorporate data of the same kind but from various origins (i.e., surface reflectance data from Sentinel-2 and Landsat 8) because of sensor related differences, as well as the variety of available processing tools and algorithms. This problem can be mitigated by using Analysis Ready Data (ARD) as endorsed by the Committee on Earth Observation Satellites (CEOS) [@Lewis2018]. The topic of ARD is presented in more detail in +@sec:analysis-ready-data. 

**Data Representation**    
Data representation refers to how each axes or dimension of the data cube is encoded. This includes spatial, temporal, spectral and thematic properties and can be specified by a set of metadata, such as range, interval, scale, and precision. The spatial dimension, for example, is encoded in the form of a grid system that is based on a geographic projection. The choice of an appropriate projection for the respective region of interest is important, as it can lead to considerable spatial distortion [@Steinwand1995]. 

**Data Organisation**  
This aspect covers how the data and its cell values are stored. In terms of raster data this can encompass data format (e.g., GeoTIFF, JPEG2000, Zarr), compression algorithm (e.g., Packbits, Deflate, LZW) and internal partitioning (e.g., Band Sequential, Band Interleaved by Pixel, Block Tiling). A comparison of several data formats in the context of cloud storage access can be found in @Durbin2020, while @Alberti2018 highlights the influence of compression algorithms in regard to the GeoTIFF format.

**Infrastructure**  
The infrastructure of storing large volumes of EO data, while ensuring rapid data access and transfer, is another important aspect to consider. EODCs can be implemented on local High Performance Computing (HPC) facilities, as demonstrated by @Lewis2017. Cloud computing and storage environments like Amazon Web Services (AWS) can also be a viable infrastructure option [@Ferreira2020a].

**Access and Analysis**  
To access and analyze the stored data, and to add new data products to the data cube, functionalities must be implemented within the infrastructure. The availability of these functionalities to end-users can be through APIs (Application Programming Interface). Several software layers (front-end & back-end) that serve different purposes, are also imaginable.

**Interoperability**  
The interoperability between different data cubes is a crucial aspect to prevent them to become 'silos of information'. Interoperability can be enabled through the use of widely-adopted geospatial standards, which are governed by the Open Geospatial Consortium (OGC) and the International Organization for Standardization (ISO). @Giuliani2019 emphasize the importance of this aspect.


### Software ecosystem

The ecosystem of EODC related projects is diverse and continuously growing. To begin with, it is important to distinguish between EODC related software projects, which usually are open source in nature, and cloud-based processing platforms, whose background is usually commercial. There are recent publications that compare both under an umbrella term [e.g., @Gomes2020], however, the distinction can clear up confusion among users and support the characterization of EODCs. @Giuliani2019 discuss several aspects in regard to this distinction and emphasize important limitations of cloud-based platforms that might not be apparent right away (e.g., vendor lock-in).    

The openEO API pursues the goal of providing a common ground for a variety of back-ends, including those previously mentioned, by connecting them via multiple APIs [@Pebesma2017]. The concept behind openEO, which uses a data cube model at its core, is also presented in a recent publication by @Schramm2021.

In the following, the Open Data Cube is described in more detail, as it is an important part of this thesis. A selection of other related EODC projects are briefly introduced in +@sec:other-projects.


#### Open Data Cube

- History
- Short technical description (more detailed in method section)
- Overview of related literature and national/regional deployments 

*Table: ODC deployments and relevant publications*


#### Other projects

**Earth Server & BigDataCube**

**Earth System Data Lab**

**gdalcubes**



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
