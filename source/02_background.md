# State of the Art

## Big Data & Innovation

Since the beginning of the current century, a majority of the world's technological capacity to store, communicate, and compute information has relied on digital formats [@Hilbert2011]. This has not only resulted in the amount of data growing continuously, but also the importance of big data being realized in various fields of society [@WEF2012]. 

The arising challenges and opportunities of growing amounts of EO and geospatial data have already been important topics in the 1990s. Al Gore coined the term *Digital Earth* in a speech in 1998, where he envisioned a digital representation of our Earth and how it could benefit society [@Gore1998]. In the same decade, the need for improved management strategies of spatial information has increasingly been recognized by administrations worldwide and facilitated the development of Spatial Data Infrastructures (SDIs) [@Schade2019].

As presented by @Guo2016 and @Boulton2018, challenges and opportunities related to the current era of big Earth data are still being discussed two decades later. In the context of EO, this era is particularly being fueled by the open data policies of the Landsat program, which includes an archive of over 40 years of global EO data [@Wulder2019], and the Copernicus program with its family of Sentinel satellites [@Aschbacher2017]. 

The volume of available EO and geospatial data keeps growing and the variety of spatial, spectral, and temporal resolutions adds to the challenge of generating valuable information from this data. New missions are soon to be launched [e.g., @Kellogg2020], new sensor technologies are being developed [e.g., @Kampe2017], and the commercial EO sector is striving to surpass the spatial and temporal resolution of publicly available EO data [e.g., @Farquharson2018].

Innovative trends in the rapidly evolving information technology (IT) sector have frequently been adopted by the geospatial sector. @Diaz2012 investigated this subject in relation to the development of SDIs and named *cloud computing* as an important trend. It describes a paradigm that allows individuals to access not only data that is being managed in a remote facility, but also applications and computing power over the internet and on demand [@Foster2008]. 

@Sudmanns2020 describe a change in EO data analysis workflows that is suitable for dealing with large amounts of EO data, where analysis ready datasets and appropriate tools for information extraction are being provided in a cloud environment. They also indicate that most professionals still rely on the traditional workflow of downloading and processing datasets locally. However, cloud computing platforms such as GEE [@Gorelick2017] have become more popular in recent years and enabled scientists to use EO data in unprecedented global-scale studies [e.g., @Hansen2013]. 

As a consequence of these changing workflows and increasing volumes of open data being used for analyses, innovation is also happening in closely related areas. Data formats, for example, are evolving and being optimized for network-based access. @Yee2020 compared the data formats GeoTIFF and NetCDF-4, which are two established standards in the domain of Earth Science, with their optimized equivalents Cloud Optimized GeoTIFF (COG) and Zarr. Furthermore, new specifications such as the SpatioTemporal Asset Catalog (STAC) are being developed to provide a standardized way of describing and indexing spatial data and thereby improving its discoverability [@STAC].

In close relationship to open data and arguably an equally important driver of innovation is open-source software, i.e., collaboratively developed software projects that can be used, changed, and distributed freely [@Corbly2014]. @Coetzee2020 have reviewed the current state of open data and open-source software in the context of the geospatial domain. They came to the conclusion that both “have changed the way in which geospatial data are collected, processed, analyzed, and visualized” (p. 24) and that the combination of open data and open-source software will probably play an even more important role in the future.



## Earth Observation Data Cubes

To address challenges related to big Earth data, new technological solutions have emerged in recent years. Besides cloud computing platforms like GEE, there is an increasing number of software projects in the geospatial domain that in some way or another use the term *Data Cube* and are usually open-source in nature.

There still seems to be a lack of consensus in regard to the exact terminology. However, a number of recent publications are using Earth Observation Data Cube (EODC) as an umbrella term for either such software projects or implementations thereof [e.g., @Giuliani2019; @Kopp2019; @Ferreira2020]. According to @Killough2018, they offer a new approach to store, organize, and manage large volumes of analysis ready EO data and thereby lower the barrier for users to exploit the data to its full potential. 

To better understand the fundamentals of EODCs, Section @sec:concept provides a more comprehensive overview of the concept and how data cubes in EO are defined in literature. Section @sec:software-ecosystem, on the other hand, gives an overview of important software projects and the Open Data Cube initiative in particular. 


### Concept

While EODCs have gained popularity in recent years, the underlying idea of data cubes does not originate in the geospatial domain. Already in the early 1990s, data cubes of business and statistical data have been used in the context of Online Analytical Processing (OLAP) and the domain of business intelligence [@Nativi2017]. @Ariav1986 defined a data cube as “a three-dimensional and inherently temporal data construct where time, objects, and attributes are the primary dimensions of stored data” (p. 499). 

The general notion that data cubes are multidimensional data structures, which include some form of metadata attributes, can be transferred to the concept of data cubes in the geospatial domain. Technological developments related to OLAP data cubes, however, are not directly applicable, as EO data in the form of spatio-temporal rasters is typically densely populated rather than sparsely [@Baumann2018, p. 288]. 

A simplified visualization of a data cube structure of EO raster data is shown in Figure @fig:eocube and a matching definition of EODCs as multidimensional arrays of dense raster data is provided by @Appel2019. Fundamentally, they are shaped by x (longitude; easting) and y (latitude; northing) as the spatial and time as the temporal dimension. Spectral bands or polarization for optical and Synthetic Aperture Radar (SAR) sensors, respectively, are a typical fourth dimension that is not visualized here.

![Simplified visualization of an EODC as a multidimensional array of dense raster data [@Kopp2019].](source/figures/02_background_1__Kopp2019_eocube.png){#fig:eocube width=50% short-caption="Simplified visualization of an EODC."}

In response to inconsistent definitions and terminology, @Strobl2017 proposed a concept that aimed to contribute to a more harmonized definition of what a data cube in the geospatial domain is. They highlight several distinct aspects that need to be considered when creating an EODC and in order to harness its full potential. Matching the cube analogy they identified six aspects, or rather faces, which hereafter are briefly summarized and complemented with relevant publications. The work of @Strobl2017 builds on the conceptual view of the Datacube Manifesto proposed by @Baumann2017. Moreover, @Nativi2017 further expand on the *six faces* concept by introducing a set of modeling views with the goal of emphasizing the interoperability and reusability aspects of data cube infrastructures.

**Parameter Model**  
To understand the information being stored in each dataset of an EODC and to facilitate analysis, the parameter model is describing the semantics of each cell value, which includes metadata, parameterization and quality information. Standardization and definition of important elements of the parameter model is done by organizations such as the Open Geospatial Consortium (OGC). However, it remains a challenge to properly incorporate data of the same kind but from various origins (e.g., surface reflectance data from Sentinel-2 and Landsat 8) because of sensor related differences, as well as the variety of available processing tools and algorithms. This problem can be mitigated by using ARD as endorsed by CEOS [@Lewis2018], which is presented in more detail in Section @sec:analysis-ready-data.

**Data Representation**    
Data representation refers to how each axis or dimension of the data cube is encoded. This includes spatial, temporal, spectral, and thematic properties and can be specified by a set of metadata, such as range, scale, and precision. The spatial dimension, for example, is encoded in the form of a grid system, which is based on a geographic projection. The choice of an appropriate projection for the respective region of interest is important, as it can lead to considerable spatial distortion [@Steinwand1995]. 

**Data Organisation**  
This aspect covers how the data and its cell values are stored. In terms of raster data this can encompass everything related to the data format (e.g., GeoTIFF, JPEG2000, Zarr), including compression algorithm (e.g., Packbits, Deflate, LZW) and internal partitioning (e.g., band sequential interleaving, block tiling). A comparison of several data formats in the context of cloud storage can be found in @Yee2020, while @Alberti2018 highlights the influence of compression algorithms in regard to the GeoTIFF format.

**Infrastructure**  
The infrastructure of storing large volumes of EO data, while ensuring rapid data access and transfer, is another important aspect to consider. EODCs can be implemented on local HPC facilities, as demonstrated by @Lewis2017. Cloud computing and storage environments like Amazon Web Services can also be a viable infrastructure option [e.g., @Ferreira2020a].

**Access and Analysis**  
Appropriate functionalities must be implemented within the infrastructure to access and analyze the stored data, and to add new data products to an EODC. The availability of these functionalities to end-users can be provided through APIs (Application Programming Interface), for example. Several software layers (front-end & back-end) that individually cover relevant aspects are also imaginable.

**Interoperability**  
The interoperability between different EODCs is a crucial aspect to prevent them from becoming silos of information. Interoperability can be enabled through the use of widely adopted geospatial standards, which are governed by the OGC and the International Organization for Standardization (ISO). The importance of this aspect is further emphasized by @Giuliani2019.


### Software Ecosystem  

The ecosystem of EODC related projects is diverse and continuously growing. To begin with, it is important to distinguish between EODC related, and usually open-source, software projects, and cloud-based processing platforms, whose background is usually commercial. There are recent publications that compare both under an umbrella term [e.g., @Gomes2020]. However, a differentiation of both can clear up confusion among users and support a comprehensible characterization of EODCs. @Giuliani2019 discuss several aspects in regard to this distinction and emphasize important limitations of cloud-based platforms that might not be apparent right away, such as the possibility of vendor lock-in.    

Also related but not fitting into either category is the openEO API, which pursues the goal of providing a common ground for a variety of back-ends, including those previously mentioned, by connecting them via a multilayered API [@Pebesma2017]. The concept behind openEO, which uses a data cube model at its core, is also presented in a recent publication by @Schramm2021.

In the following section, the Open Data Cube is described in more detail, as it plays an important role in the course of this work. An overview of other related EODC projects is provided in Section @sec:other-projects.

#### Open Data Cube {#sec:odc_background}

The Open Data Cube (ODC) project originates from the Australian Geoscience Data Cube (AGDC), which initially was developed with the objective to unlock the potential of 27 years of continuous EO data from the Landsat archive covering the entire continent of Australia [@Lewis2016]. Major improvements were implemented in the second version of the AGDC [@Lewis2017] and the project was renamed to ODC after long term support was ensured via governance structures [@Leith2018]. 

From a technical perspective, the ODC is an open-source software library to access, manage, and analyze large quantities of EO data that can be deployed in a flexible manner [@ODC-Docs1]. This is achieved through a database, a Python API and a set of command line tools. A more detailed description of the technical background can be found in Section @sec:odc_methods.

Besides being a freely available software library, ODC has developed into a community of people and supporting organizations. @Killough2018 presented the ODC initiative as part of the reorganization from AGDC to ODC, which is supported by the institutions originally responsible for the AGDC, namely Geoscience Australia and the Commonwealth Scientific and Industrial Research Organization (CSIRO), and additionally CEOS, USGS, and the Analytical Mechanics Associates (AMA). The aim of this initiative is to steward and contribute to the development of the ODC software architecture, thereby enabling its utilization around the world. 

In addition to the general ODC initiative, CEOS started a separate CEOS Data Cube initiative based on their goal to “improve data access, data preparation, and data analysis for all global users of satellite data” [@Killough2018, p. 8630]. In this context, the goal was defined to establish operational EODCs based on the ODC software library in 20 countries by 2022.

The Swiss Data Cube (SDC) was one of the first national EODCs and the lessons learned as described by @Giuliani2017 have been a valuable resource of information for subsequent deployments [e.g., @Asmaryan2019]. The SDC supports the Swiss government in environmental monitoring and reporting, and has been used to monitor the temporal and spatial evolution of snow cover in Switzerland [@Dhu2019, pp. 6-8].

Along with the SDC, the African Regional Data Cube (ARDC) was one of the first EODCs established as part of the CEOS Data Cube initiative. As the name suggests, the ARDC was initially regional in scale and encompassed the countries of Ghana, Kenya, Senegal, Sierra Leone, and Tanzania [@Killough2019]. Since then, the ARDC has developed into a continental-scale data infrastructure project called Digital Earth Africa [@DEAfrica]. According to a report by the WEF, the socio-economic benefits created through Digital Earth Africa could exceed $2bn per year by 2024 [@WEF2021]. 

Another important national EODC deployment that uses ODC at its core is the Brazil Data Cube (BDC) developed by Brazil’s National Institute for Space Research (INPE). The methodology of how the BDC was implemented is described in detail by @Ferreira2020. The BDC has already been used to develop new methods to map land use and cover changes [@Santos2021]. Moreover, all software products that are developed as part of the BDC are openly available [@BDC] and can be utilized by other projects of the ODC community.


#### Other Projects  

**EarthServer & BigDataCube**  
EarthServer, as presented by @Baumann2015, is one of the earliest developed EODC projects. Its approach to serve large volumes of EO data centers on the array database RasDaMan [@Baumann1998] and OGC coverage standards for access and processing, namely Web Map Service (WMS), Web Coverage Service (WCS) and Web Coverage Processing Service (WCPS). The insights gained from EarthServer were refined further with the BigDataCube project, which has been implemented by various public and commercial data providers (i.a., CODE-DE and cloudeo AG) to efficiently serve hundreds of terabytes of EO data [@Misev2019].

**gdalcubes**  
The setup of most EODC-related software is not trivial and can limit wider adoption of EODC technology. A project that aims to provide a solution to circumvents this obstacle, is the gdalcubes project [@Appel2019]. It uses on-demand data cubes that are only created when users perform computations on their data. As the name suggests, the widely used Geospatial Data Abstraction Library (GDAL) is a major component, which can handle a large variety of raster data formats [@Warmerdam2008]. The gdalcubes project is available as an open-source C++ library and a package for the programming language R. 

**Earth System Data Cube & Lab**  
@Mahecha2020 proposed the concept of Earth System Data Cubes (ESDC) that enable co-interpretation of EO and modelling data (e.g., from climate models). The dimensions of each ESDC, such as spatial, temporal, variable, and frequency, are treated alike and allow the execution of complex workflows by applying user-defined functions. The scientific programming languages Julia and Python are currently supported to work with ESDCs. Furthermore, the Earth System Data Lab [@ESDL] was introduced by @Mahecha2020, which provides access to curated and analysis ready ESDCs stored in a cloud environment.  

**xcube**  
Similar to ODC, the open-source project xcube is using the Python packages Xarray and Dask as its core packages [@xcube-Docs]. Beyond that, the conceptual direction of xcube is different, as it heavily relies on the data format Zarr to enable the creation of self-contained data cubes. These can then be published and used in the cloud, which has been implemented by the commercial Euro Data Cube service [@EDC2021]. 

**TileDB**  
TileDB is an open-source software system managed by Intel Labs and the Massachusetts Institute of Technology. It poses as a universal data engine and data management solution by providing not only a storage engine, but also a data model and data format [@TileDB-Docs]. TileDB can handle sparse and dense arrays of arbitrary dimensionality and therefore facilitates usage in a wide variety of large-scale scientific applications [@Papadopoulos2016]. An example on how TileDB can be used to manage large volumes of SAR data is given by @Barker2020.


## Analysis Ready Data {#sec:analysis-ready-data}

The aspect of having EO data that was consistently preprocessed and is suitable for time-series analysis is fundamental for the creation of EODCs. This aspect was described by @Strobl2017 as the first *face* of the data cube and the importance is further emphasized by how closely tied the term Analysis Ready Data (ARD) is being used in the context of EODCs [e.g., @Giuliani2017; @Baumann2018; @Killough2019]. When working with EO data, users typically have to deal with the difficulties of data access, data preparation and efficient analysis, all of which can be eased by the generation of ARD [@Giuliani2017, p. 102].

Currently, there still is an ongoing discussion about the definition of ARD and agreed specifications for the various satellite sensors available. The issue of ARD being interpreted differently by institutions and data providers is highlighted by @Sudmanns2020 in the context of data access. They come to the conclusion that the potential of ARD can be unlocked by “either finding a common understanding or communicating clearly the ARD’s differences, individual characteristics, and suitability for tasks” (p. 845). The CEOS Analysis Ready Data for Land initiative (CARD4L) presents an important step towards a consensus among EO data providers and users, which is further elaborated on in Section @sec:card4l.

Access to ARD products is improving continuously. The Landsat archive, for example, is being reprocessed into a tiered Collection 2 product inventory that is consistently calibrated over time [@Dwyer2018; @Masek2020] and effort is being made to create a harmonized Landsat 8 and Sentinel-2 product [@Claverie2018]. However, the creation of EODCs is still often linked to alternative approaches of generating ARD to meet specific project requirements [e.g., @Ferreira2020]. Some of these approaches are briefly described in Section @sec:generating-ard.

In the future, it will be necessary that the burden of generating ARD in a form that is suitable for as many users as possible lies on data providers who have the appropriate facilities to process large volumes of EO data [@Giuliani2019, p. 19]. Beyond the simple provision of ARD products, @Abernathey2020 argue that current infrastructure challenges of data-intensive scientific fields could be overcome by the combination of analysis-ready, cloud-optimized (ARCO) data repositories and scalable data-proximate computing (i.e., cloud computing).


### CARD4L

#### Initiative

Through the CARD4L initiative, CEOS is working to “enable non-expert users access to products that have been processed 'far enough' to be suitable for immediate analysis for a range of applications, while ensuring they are not too specific to only be used for particular topics or areas.” [@Lewis2018, p. 7407]. CARD4L aims to enable an increase of EODC usage and interoperability, and has set up a framework to achieve the initiative's goals consisting of three core components: Definition, Product Family Specification (PFS), and Product Alignment Assessment (PAA).

The non-prescriptive definition of CARD4L is as follows: “CEOS Analysis Ready Data for Land (CARD4L) are satellite data that have been processed to a minimum set of requirements and organized into a form that allows immediate analysis with a minimum of additional user effort and interoperability both through time and with other datasets.” [@Lewis2018, p. 7408]. 

An overview of the other two components, PFS and PAA, is also provided by @Lewis2018. The PFSs identify comparable and fundamental measurement types that are sensor-agnostic (e.g., surface reflectance), instead of the traditional approach of focusing on unique data streams produced by individual sensors. Moreover, requirements for the generation of ARD are defined by the PFSs. The PAAs on the other hand, are supposed to help data producers in self-assessing the alignment of their products with the CARD4L specifications. In addition, PAAs facilitate the provision of independent assessments and peer-reviews. 

#### Specifications  

The details provided by the PFSs can be used by data producers to identify which measures are necessary in order to deliver CARD4L compliant ARD to the users. These are further categorized as *Threshold* and *Target* requirements that provide specific information on the categories: general metadata, per-pixel metadata, radiometric and atmospheric corrections, and geometric corrections [@Siqueira2019].

Four PFSs are presently devised: Surface Reflectance (v5.0) and Surface Temperature (v5.0) for optical sensors, and Normalized Radar Backscatter (v5.0) and Polarimetric Radar (v3.0) for SAR sensors [@CARD4L]. A brief introduction of the Surface Reflectance and Normalized Radar Backscatter PFSs (SR-PFS and NRB-PFS, respectively) follows, as relevant ARD products are produced and used in this work. 

**General Metadata**  
At a basic level, both specifications require the provision of general metadata that allows users to assess if the dataset is suitable for their analysis. This includes information about the source data, such as temporal and spatial coverage, processing details, and other important attributes (e.g., spectral bands for SR-PFS, polarizations and orbit direction for NRB-PFS).

**Per-pixel Metadata**  
Both specifications also require per-pixel metadata that can be used to discriminate between individual observations. This includes commonly used masks for the SR-PFS (e.g., cloud and cloud shadow coverage). The NRB-PFS, on the other hand, specifies the requirement for a supplementary local incident angle image, which is based on the digital elevation model used for processing.

**Corrections**  
Geometric corrections are required to be performed for both specifications in order for measurements to be accurately geolocated and comparable through time. Other corrections, however, are sensor specific: radiometric and atmospheric corrections in case of the SR-PFS and radiometric terrain correction for the NRB-PFS, which result in surface reflectance and normalized backscatter intensity measurements, respectively.


### Processing methods {#sec:generating-ard}

The national and regional EODCs established in relation to the CEOS Data Cube initiative mentioned in Section @sec:odc_background have developed different approaches for generating their ARD products. To provide both the Swiss and the Armenian Data Cube with ARD, for example, the Live Monitoring of Earth Surface (LiMES) framework was utilized [@Giuliani2017; @Asmaryan2019], which is presented by @Giuliani2017a. Other approaches are described in detail, i.a., by @Lewis2017 for the AGDCv2 and by @Ferreira2020 for the BDC. 

Even though a variety of approaches are used, the common ground usually lies in open-source software and algorithms. Especially for optical sensors an extensive selection of peer-reviewed algorithms for radiometric and atmospheric corrections, as well as commercial and open-source software solutions, exist. Sen2Cor [@MainKnorn2017], for example, is commonly used to process Sentinel-2 data to a Level-2A Bottom Of Atmosphere (BOA) product, while @Lonjou2016 developed the MACCS-ATCOR joint algorithm (MAJA), which can be used to process both Sentinel-2 and Landsat 8 scenes. The 6S algorithm [@Vermote1997] is implemented in the open-source software ARCSI [@ARCSI-Software], which is able to handle a variety of optical sensors. And a software framework that not only focuses on the application of correction algorithms, but also on other important aspects when generating ARD for EODCs (e.g., appropriate tiling and gridding scheme), is the Framework for Operational Radiometric Correction for Environmental monitoring (FORCE) [@Frantz2019].  

In the context of SAR sensors on the other hand, the selection of algorithms to produce an NRB product is more uniform, and ultimately it is rather a choice of which software to use. Some alternatives include the open-source Orfeo Toolbox [@Inglada2009] and the proprietary GAMMA software [@GAMMA-Software]. ESA's Sentinel Application Platform [@SNAP] and more specifically its Sentinel-1 toolbox, is a widely adopted and freely available software to process data from various ESA and third-party SAR sensors. @Truckenbrodt2019 and @Ticehurst2019 have investigated the feasibility of generating Sentinel-1 ARD products using SNAP and GAMMA and came to a confirming conclusion in both cases.
