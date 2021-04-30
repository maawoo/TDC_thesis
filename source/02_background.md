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

In response to inconsistent definitions and terminology, @Strobl2017 proposed a concept for data cubes in the geospatial domain that highlights several important aspects independently and thereby contributing to a more harmonized definition. Matching the cube analogy they identified six aspects, or rather faces, of the data cube. (!)

The work of @Strobl2017 builds on the conceptual view of the 'Datacube Manifesto' proposed by @Baumann2017. Furthermore, @Nativi2017 expand on the 'six faces' concept by introducing a set of modeling views with the goal of emphasizing the interoperability and reusability aspects of data cube infrastructures. However, in the following, only the six aspects identified by @Strobl2017 are briefly summarized and complemented with relevant publications:

**Parameter Model**  
The parameter model includes any metadata, parameterization and quality information that is necessary to understand what information is stored in each thematic layer of a data cube and to facilitate further analysis. It remains a challenge to properly incorporate data of the same kind but from various origins (i.e., surface reflectance data from Sentinel-2 and Landsat 8) because of sensor related differences, as well as the variety of available processing tools and algorithms. This problem can be mitigated by using Analysis Ready Data (ARD) as endorsed by the Committee on Earth Observation Satellites (CEOS) [@Lewis2018]. The topic of ARD is presented in more detail in +@sec:analysis-ready-data. (!)

**Data Representation**    
Data representation refers to how each axes or dimension of the data cube is encoded. This includes spatial, temporal, spectral and thematic properties and can be specified by a set of metadata, such as range, interval, scale, and precision. The spatial dimension, for example, is encoded in the form of a grid system that is based on a geographic projection. The choice of an appropriate projection for the respective region of interest is important, as it can lead to considerable spatial distortion [@Steinwand1995]. 

**Data Organisation**  
This aspect covers how the data and its cell values are stored. In terms of raster data this can encompass data format (e.g., GeoTIFF, JPEG2000, Zarr), compression algorithm (e.g., Packbits, Deflate, LZW) and internal partitioning (e.g., Band Sequential, Band Interleaved by Pixel, Block Tiling). A comparison of several data formats in the context of cloud storage access can be found in @Durbin2020, while @Alberti2018 highlights the influence of compression algorithms in regard to the GeoTIFF format.

**Infrastructure**  
The infrastructure of storing large volumes of EO data, while ensuring rapid data access and transfer, is another important aspect to consider. EODCs can be implemented on local High Performance Computing (HPC) facilities, as demonstrated by @Lewis2017. Cloud computing and storage environments like Amazon Web Services (AWS) can also be a viable infrastructure option [@Ferreira2020a].

**Access and Analysis**  
To access and analyse the stored data, and to add new data products to the data cube, functionalities must be implemented within the infrastructure. The availability of these functionalities to end-users can be through APIs (Application Programming Interface). Several software layers (front-end & back-end) that serve different purposes, are also imaginable.

**Interoperability**  
The interoperability between different data cubes is a crucial aspect to prevent them to become 'silos of information'. Interoperability can be enabled through the use of widely-adopted geospatial standards, which are governed by the Open Geospatial Consortium (OGC) and the International Organization for Standardization (ISO). @Giuliani2019 emphasize the importance of this aspect.


### Software Ecosystem  

The ecosystem of EODC related projects is diverse and continuously growing. To begin with, it is important to distinguish between EODC related software projects, which usually are open source in nature, and cloud-based processing platforms, whose background is usually commercial. There are recent publications that compare both under an umbrella term [e.g., @Gomes2020], however, the distinction can clear up confusion among users and support the characterization of EODCs. @Giuliani2019 discuss several aspects in regard to this distinction and emphasize important limitations of cloud-based platforms that might not be apparent right away (e.g., vendor lock-in).    

The openEO API pursues the goal of providing a common ground for a variety of back-ends, including those previously mentioned, by connecting them via multiple APIs [@Pebesma2017]. The concept behind openEO, which uses a data cube model at its core, is also presented in a recent publication by @Schramm2021.

The Open Data Cube is described in more detail in the following section (+@sec:open-data-cube), as it is an important part of this thesis. A selection of other related EODC projects are briefly introduced in +@sec:other-projects.

#### Open Data Cube  

The Open Data Cube (ODC) project originates from the Australian Geoscience Data Cube (AGDC), which initially was developed with the objective to unlock the potential of 27 years of continuous EO data from the Landsat archive for the entire continent of Australia [@Lewis2016]. Major improvements were implemented in version 2 of the AGDC [@Lewis2017] and the project was renamed to ODC after long term support was ensured via governance structures [@Leith2018]. 

From a technical perspective, the ODC is an open source software library to access, manage, and analyse large quantities of EO data through a Python API and a set of command line tools that can be deployed in a flexible manner [@ODC2020]. A more detailed description of the technical background can be found in section xyz.

Besides being a freely available tool, ODC has developed into a community of people and supporting organizations. @Killough2018 presented the “ODC initiative” as part of the reorganisation from AGDC to ODC, which is supported by the institutions originally responsible for the AGDC, namely Geoscience Australia (GA) and the Commonwealth Scientific and Industrial Research Organization (CSIRO), as well as the Committee on Earth Observation Satellites (CEOS), Analytical Mechanics Associates (AMA), and the United States Geological Survey (USGS). The aim of this initiative is to steward and contribute to the development of the ODC software architecture, thereby enabling its utilization around the world. 

In addition to the general ODC initiative, CEOS started a separate “CEOS Data Cube” initiative based on their goal to “improve data access, data preparation, and data analysis for all global users of satellite data” [@Killough2018, p. 8630 ?]. In this context, the goal was defined to establish operational EODCs (based on the ODC tools) in 20 countries by 2022.

The Swiss Data Cube (SDC) was one of the first national EODCs and the “lessons learned” described by @Giuliani2017 have been a valuable resource of information for subsequent deployments [e.g., @Asmaryan2019]. The SDC supports the Swiss government in environmental monitoring and reporting, and has been used to monitor the temporal and spatial evolution of snow cover in Switzerland [@Dhu2019].

Along with the SDC, the African Regional Data Cube (ARDC) was one of the initial EODCs established as part of the CEOS Data Cube initiative. As the name suggests, the ARDC was regional in scale and encompassed the countries of Ghana, Kenya, Senegal, Sierra Leone, and Tanzania [@Killough2019]. Since then, the ARDC has developed into the continental-scale data infrastructure Digital Earth Africa (DE Africa; https://www.digitalearthafrica.org, last access: 26 April 2021). According to a report by the World Economic Forum (WEF), the socio-economic benefits created through DE Africa could exceed $2bn per year by 2024 [@WEF2021]. 

Another important national EODC deployment that uses ODC at its core, is the Brazilian Data Cube (BDC; http://brazildatacube.org, last access: 26 April 2021) developed by Brazil’s National Institute for Space Research (INPE). The methodology of how the BDC was implemented is described in detail by @Ferreira2020. The BDC has already been used to develop new methods to map land use and cover changes (LUCC) [@Santos2021] and been active in developing tools that can be useful for the ODC community (https://github.com/brazil-data-cube, last access: 26 April 2021). 

Mexico, Colombia, Spain/Catalonia & Taiwan

#### Other Projects  

**EarthServer & BigDataCube**  
EarthServer, as presented by @Baumann2015, is one of the earliest developed EODC projects. Its approach to serve large volumes of EO data centers on the Array Database RasDaMan [@Baumann1998] and OGC coverage standards for access and processing, namely WMS (Web Map Service), WCS (Web Coverage Service) and WCPS (Web Coverage Processing Service). The insights gained from EarthServer were refined further with the BigDataCube project (http://bigdatacube.org, last access: 25 April 2021), which has been implemented by various public and commercial data providers (i.a., CODE-DE and cloudeo AG) to efficiently serve hundreds of terabytes of EO data [@Misev2019].

**gdalcubes**  
As the setup of most other EODCs is not trivial, the gdalcubes project aims to provide a solution that lets users concentrate on the analysis rather than data management [@Appel2019]. This is achieved by on-demand data cubes, which are only created when users process their data. As the name suggests, the widely-used Geospatial Data Abstraction Library (GDAL) is a major component and can handle a large variety of raster data formats [@Warmerdam2008]. The gdalcubes project is available as an open source C++ library (https://github.com/appelmar/gdalcubes, last access: 25 April 2021) and an R package (https://github.com/appelmar/gdalcubes_R, last access: 25 April 2021). 

**Earth System Data Cube & Lab**  
@Mahecha2020 proposed the concept of Earth System Data Cubes (ESDC) that enable co-interpretation of EO and model data. The dimensions of each ESDC, such as spatial, temporal, variable, and frequency, are treated alike and allow the execution of complex workflows by applying user-defined functions. The scientific programming languages Julia and Python are currently supported to work with ESDCs. Furthermore, the Earth System Data Lab (ESDL; https://www.earthsystemdatalab.net, last access: 25 April 2021) was introduced by @Mahecha2020, which provides access to curated and analysis ready ESDCs stored in a cloud.  

**xcube**  
Similar to ODC, the open source project xcube is using the Python packages Xarray and Dask as its core packages (https://github.com/dcs4cop/xcube, last access: 25 April 2021). Beyond that, the conceptual direction of xcube goes into a different direction by heavily relying on the data format Zarr to enable the creation of self-contained data cubes. These can then be published and used in the cloud, as implemented by the Euro Data Cube service (https://www.eurodatacube.com, last access: 25 April 2021). 



## Analysis Ready Data (ARD)

The aspect of having EO data that was consistently pre-processed and is suitable for time-series analysis is fundamental for the creation of EODCs. This aspect was described by @Strobl2017 as the first “face” of the data cube and the importance is further emphasized by how closely tied the term “Analysis Ready Data” (ARD) is being used in the context of EODCs [e.g., @Giuliani2017; @Baumann2018a; @Killough2019]. When working with EO data, users typically have to deal with the difficulties of data access, data preparation and efficient analysis, all of which can be eased by the generation of ARD [@Giuliani2017, p. ...].

Currently, there is still an ongoing discussion about the definition of ARD and agreed specifications for the various satellite sensors available. The issue of ARD being interpreted differently by institutions and data providers is highlighted by @Sudmanns2020 in the context of data access. They come to the conclusion that the potential of ARD can be unlocked by “either finding a common understanding or communicating clearly the ARD’s differences, individual characteristics, and suitability for tasks” (p. 845). The CEOS Analysis Ready Data for Land initiative (CARD4L) presents an important step towards a consensus among EO data providers and users and is further elaborated on in +@sec:card4l-initiative. 

While definitions and specifications are one problem, the access to ARD is another. The USGS has started to produce an ARD product for part of its Landsat archive (Landsat 4 – 8) [@Dwyer2018]. However, the Landsat ARD product is still only available for land areas of the United States of America and the release of a global product is yet unknown. Because official sources lack the availability for ARD products, currently the creation of EODCs is inherently linked to alternative approaches of generating ARD. Some common approaches are described in +@sec:generating-ard. 

In the future, it is necessary that the burden of generating ARD in a form that is suitable for as many users as possible, lies on data providers, who have the appropriate facilities to process large volumes of EO data [@Giuliani2019]. Beyond the simple provision of ARD products, @Abernathey2020 argue that current infrastructure challenges of data-intensive scientific fields can be overcome by the combination of analysis-ready, cloud-optimized (ARCO) data repositories and scalable data-proximate computing.


### CARD4L Initiative

Through the CARD4L initiative, CEOS is working to “enable non-expert users access to products that have been processed 'far enough' to be suitable for immediate analysis for a range of applications, while ensuring they are not too specific to only be used for particular topics or areas.” [@Lewis2018, p.7407]. Thereby also fostering the use and interoperability of EODCs.

To achieve the initiative's goals, a framework was set up, which consists of three core components: Definition, Product Family Specification (PFS), and Product Alignment Assessment (PAA). The definition of CARD4L is supposed to be neither exclusive nor prescriptive: 

>“CEOS Analysis Ready Data for Land (CARD4L) are satellite data that have been processed to a minimum set of requirements and organized into a form that allows immediate analysis with a minimum of additional user effort and interoperability both through time and with other datasets.” [@Lewis2018, p. 7408]

@Lewis2018 also provide an overview of the other two components. On one hand, the PFSs identify comparable and fundamental measurement types, and provide requirements for the generation of ARD. Thus, the PFSs contrast the traditional approach of focusing on unique data streams produced by individual sensors. On the other hand are PAAs, which are supposed to help data producers in self-assessing the alignment of their products with the CARD4L specifications. In addition, PAAs facilitate the provision of independent assessments and peer-reviews.

#### Product Family Specifications  

The details provided by the PFSs can be used by data producers to identify which measures are necessary in order to deliver CARD4L compliant ARD to the users. These are further categorized as 'Threshold' and 'Target' requirements that provide specific information on: general metadata, per-pixel metadata, radiometric and atmospheric corrections, and geometric corrections [@Siqueira2019].

Four PFSs are presently devised: Surface Reflectance (v5.0) and Surface Temperature (v5.0) for optical sensors, and Normalized Radar Backscatter (v5.0) and Polarimetric Radar (v3.0) for synthetic aperture radar (SAR) sensors (https://ceos.org/ard, last access: 28 April 2021). A brief introduction of the Surface Reflectance and Normalized Radar Backscatter PFSs (SR-PFS and NRB-PFS, respectively) follows, as relevant ARD products are produced and used in this work. 

At a basic level, both specifications require the provision of *general metadata* that allows users to assess if the dataset is suitable for their analysis. This includes information about the source data, such as temporal and spatial coverage, processing details, and important attributes (e.g., spectral bands for SR-PFS, polarisations and orbit direction for NRB-PFS).

Both specifications also require *per-pixel metadata* that can be used to discriminate between individual observations. This includes commonly used masks for the SR-PFS (e.g., cloud and cloud-shadow coverage), whereas the NRB-PFS specifies the requirement for a supplementary Local Incident angle image, which is based on the Digital Elevation Model used for processing.

*Geometric corrections* are required to be performed for both specifications in order for measurements to be accurately geolocated and comparable through time. Other corrections, however, are sensor specific: *Radiometric and Atmospheric corrections* in case of the SR-PFS and *Radiometric Terrain correction* for the NRB-PFS, which result in surface reflectance and normalized backscatter intensity measurements, respectively.


### Generating ARD

The national and regional EODCs established in relation to the CEOS Data Cube initiative mentioned in +@sec:open-data-cube, have developed different approaches for generating their ARD products. To provide both the SDC and the Armenian Data Cube with ARD, for example, the Live Monitoring of Earth Surface (LiMES) framework was used [@Giuliani2017; @Asmaryan2019], which is presented in detail by @Giuliani2017a. Other approaches are described, i.a., by @Lewis2017 for the AGDCv2 and by @Ferreira2020 for the BDC. Moreover, all software products being developed for the BDC are openly available (https://github.com/brazil-data-cube, last access: 30 April 2021). 

Even though a variety of approaches are used, the common ground usually lies in open source software and algorithms. Especially for optical sensors the selection of peer-reviewed algorithms that can be used for radiometric and atmospheric corrections, as well as the generation of cloud masks, is large. To process Sentinel-2 data to a Level-2A Bottom-Of-Atmosphere (BOA) product, Sen2Cor is commonly used [@MainKnorn2017]. @Lonjou2016 describe the MACCS-ATCOR joint algorithm (MAJA), which can be used to process Sentinel-2 and Landsat 8 data. The Satellite Signal in the Solar Spectrum (6S) algorithm [@Vermote1997] is implemented by the Atmospheric and Radiometric Correction of Satellite Imagery software (ARCSI; https://github.com/remotesensinginfo/arcsi, last access: 30 April 2021), which is able to handle a variety of optical sensors. A software framework that not only focuses on the application of correction algorithms, but also on other important aspects for the generation of ARD for EODCs (e.g., an appropriate tiling/gridding scheme), is FORCE [@Frantz2019].  



- SAR
  - Gamma
  - SNAP

(Giuliani2019a)
Truckenbrodt et al. [35] and Ticehurst et al. [36] assessed
the feasibility of automatically producing analysis-ready radiometrically terrain-corrected (RTC)
Synthetic Aperture Radar (SAR) gamma nought backscatter data from Sentinel-1. Both studies
concluded that the European Space Agency (ESA) Sentinel Application Platform (SNAP) toolbox
(https://step.esa.int/main/toolboxes/snap/) is a valid solution for producing Sentinel-1 ARD products.
