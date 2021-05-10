# Technical Implementation 

- Other chapter name? Technical *something*? ...Development? Implementation fits better for the Thuringian Data Cube as the implementation of everything described in this chapter
 


## Software Components


### pyroSAR

pyroSAR is an open source Python package [@pyroSAR2021] with the aim to provide a unified and scalable framework for the organization and processing of SAR satellite data. As described by @Truckenbrodt2019a, it consists of three main components: (1) identification and reading of SAR scenes from various missions, as well as the extraction and homogenization of metadata; (2) organization of the available information in a data archive, either as a SpatiaLite or a PostgreSQL database; (3) utilization of SNAP and GAMMA for data processing, and handling of any required ancillary data. 

Out of these, the functionality provided by the processing component was utilized for the development of the software tool. More specifically, to handle two particular tasks:

- Downloading of Digital Elevation Model (DEM) tiles and merging into a GeoTIFF mosaic 
- Processing of SAR scenes to an ARD product using the integrated SNAP API

Two auxiliary tools are offered by pyroSAR to create a DEM for an area of interest [@pyroSAR2021a]. First, all relevant tiles are obtained from one of various sources, such as the Shuttle Radar Topography Mission (SRTM) in 1 arcsecond (~30 m) or 3 arcsecond (~90 m) spatial resolution. The individual tiles are then merged and clipped to the extent of the area of interest. In addition to the processing of SAR scenes, the resulting DEM file can also be used in other workflows.

For the processing of SAR scenes, pyroSAR's SNAP API was chosen because of the open source availability of the SNAP software in comparison to the proprietary alternative GAMMA. Processing via the SNAP API is achieved by adapting XML workflows based on user input and then parsing them directly to SNAP's Graph Processing Tool (GPT) [@Truckenbrodt2019a]. The custom workflows can also be stored alongside the output files to facilitate the reproducibility of processing results.   

The feasibility to produce SAR backscatter products of an appropriate quality for time-series analysis was investigated by @Truckenbrodt2019. The study focused on producing ARD for the Sentinel-1 sensor and particularly in regard to EODCs. It came to an affirming conclusion, which further supports the methodology implemented in this work.


### FORCE

The Framework for Operational Radiometric Correction for Environmental monitoring, or FORCE in short, is an open source software project developed by @Frantz2021. The aim of FORCE is to provide a comprehensive solution for processing data from the Landsat and Sentinel-2 archives to ARD, and furthermore, higher-level products. 

The software components of FORCE are organized in the form of a level system: level-1 to automatically acquire scenes from data providers, level-2 for processing data to an ARD format, and level-3 for any higher-level processing (e.g., computation of best-available-pixel composites). The Level-1 Archiving Suite (L1AS) and the Level-2 Processing System (L2PS) are two of the main components of FORCE. They constitute an interconnected workflow, which is shown in Figure @fig:force and represents the functionality integrated into the developed software tool.    

![FORCE L1AS and L2PS workflows. Adapted from [@Frantz2019; @Frantz2021a]](source/figures/03_methods_1__force.png){#fig:force width=100%}

At first, the L1AS component is using provided parameters to query a cloud storage provider (Google Cloud Storage at the time of writing) and download any requested scenes. This workflow also checks for already existing scenes so only missing or new scenes are downloaded. A simple text file is the used to track the scenes and enqueue them for subsequent processing.

The L2PS component is using a processing workflow based on the framework presented by @Frantz2016. It includes a modified version of the Fmask code [@Zhu2012] for cloud masking and the generation of bit-wise quality assurance information (QAI), as well as a radiometric correction with radiative-transfer-based atmospheric correction [@Tanre1979; @Tanre1990]. Furthermore, the workflow includes the option to utilize one of three implemented algorithms to improve the spatial resolution of the 20 m Sentinel-2 bands ('Resolution merge'). Finally, the data is brought into a data cube appropriate format, i.e., reprojected and split into non-overlapping image chips based on a custom grid of rectangular tiles. A more comprehensive description of the processing workflow, including options not implemented here, can be found in @Frantz2019 and @Frantz2021a. Moreover, TABLE X and TABLE Y (appendix!) provide overviews for the homogenized spectral bands of the produced ARD products, and for the supplementary QAI product, respectively.   

In addition to the L1AS and L2PS components, some auxiliary modules of FORCE are utilized as well, namely 'force-tabulate-grid' and 'force-mosaic'. The former creates a KML (Keyhole Markup Language) file of the processing grid, and the latter automatically creates mosaics in the VRT (Virtual Raster Table) format for all image chips of the same date. Both outputs are for visualization purposes only. A third auxiliary module, 'force-cube', serves a more important task, as it is used to bring processed SAR data into the same data cube appropriate format mentioned above. Thereby the concurrent use of optical and SAR datasets in an EODC is facilitated.


### Open Data Cube

As described in CHAPTER X, at its core the Open Data Cube (ODC) is an open source software library aimed at the management and analysis of large volumes of EO data, which has successfully been leveraged to create EODCs of national [@Giuliani2017] and even continental scales [@Lewis2017]. The main technical components of ODC are a database for data management, and a Python based API to query and access the data. 

ODC currently uses a PostgreSQL database to catalog information about all EO data that is available for a given deployment. This allows large datasets to be queried (e.g., by time and location) initially without having to access the actual storage location [@Leith2018]. As described by @ODC2021, the process of cataloging information in the context of ODC is also called 'indexing' and is achieved in two separate steps as shown in Figure @fig:odc: 

![ODC indexing workflow. Adapted from [@ODC2021]](source/figures/03_methods_2__odc.png){#fig:odc width=100%}

First, a product definition document is manually created for a given dataset. It is stored in the YAML (YAML Ain't Markup Language) format and contains general information that is common for each scene of a dataset. This can include general metadata, storage information like CRS (Coordinate Reference System) and spatial resolution, as well as measurement descriptions. The measurement descriptions can also be extended from simply listing which spectral or polarization bands each scene includes, to providing bit-level descriptions of quality flags, such as the QAI bands generated by FORCE. This information can then be used during analysis to easily create masks to exclude undesirable pixel values (e.g., cloud covered pixels). An example product definition document can be found in APPENDIX X.  

During the second step, dataset definition documents are created for each individual scene in a given dataset. This step is also called 'data preparation' and can be automated using either an existing or a customized Python script. For each scene, metadata is extracted, which is specific for the given scene and also stored in a YAML file. Most importantly this includes storage location on the local file system, as well as acquisition time and georegistration information to enable temporal and spatial querying, respectively. Besides additional metadata, provenance can also be stored provided that the source dataset was indexed as well. An example dataset definition document can be found in APPENDIX Y.

In addition to indexing, it is also possible to 'ingest' datasets. This process converts indexed datasets to a new file format and structure, such as NetCDF. This can improve the efficiency of data access during analysis. However, this optional step was not explored further in the course of this work and based on responses in the ODC community, is not commonly being used anymore.   

After the database has been made aware of available datasets via the process of indexing product and dataset definition documents, it can be used to query and retrieve data for analysis. An open source Python package is available for this purpose [@ODC2020], which leverages the packages Xarray [@Hoyer2017] and Dask [@Rocklin2015] as two of its main dependencies. While Dask is providing a framework for parallel computing, Xarray is a toolkit for working with data that is structured as multi-dimensional arrays and closely integrated with the former. The combination of Xarray and Dask is also used in other projects that deal with large volumes of geoscientific data, such as Pangeo [@Pangeo2021].

When data is loaded into a Python environment it is organized as an Xarray Dataset including separate data variables for each requested band and appropriately labeled temporal and spatial dimensions [@ODC2021]. The execution of loading and computation in a 'lazy' manner is also supported, which means that data is only loaded and computed until actually needed. In combination with the 'chunking' of data into smaller portions, it is possible to run algorithms over very large EO datasets efficiently, even if the data itself does not fit into the system's memory. 

Some additional utilities are provided with the core Python package of ODC, like a masking tool to create boolean masks from bit-wise QAI products during analysis. More extensive collections of tools and algorithm examples are available in repositories created by users of the ODC community [e.g., @Krause2021]. Furthermore, a selection of applications have been developed that extend the functionality of ODC in various ways (https://www.opendatacube.org/data-cube-applications, last access: 08 May 2021).


### Containerization

Encapsulating a software environment, including its dependencies, system libraries, settings, and runtime code, so that it can be run on different computing environments reliably, is known as software containerization [@Docker2021]. The implementation of this aspect played an important role for various reasons: 

- Simplifying the setup process in general and for deployment on HPC (High Performance Computing) systems in particular.
- Avoiding possible issues related to the concurrent use of software components that rely on similar dependencies.
- Facilitating reproducibility by enabling a data processing workflow that can be replicated much easier than the alternative approach of not using containerized software components.

The containerization solution implemented here is Singularity, which is open source and was created with the motivation to provide a solution that is suitable for scientific applications on HPC systems [@Kurtzer2017]. Even though Docker is a containerization platform that is widely adopted in the IT sector, the requirement for high-level access privileges when running containers poses a security concern for HPC administrators [@Silver2017; @Kurtzer2017]. This issue is circumvented by Singularity with its container architecture as described by @Kurtzer2017. 

A Singularity container can be created from a definition file that provides a 'recipe' for what should be installed and included inside the container. Alternatively, they be created from existing Docker container images and the Docker registry, which in combination with the fact that the resulting containers exist as individual and moveable files, offers high flexibility. As shown by @Garofoli2019, Singularity can be used to create containerized scientific applications that are portable, scalable and ensure reproducible results.



## ARDCube

An open source software project called 'ARDCube' was developed, which integrates all components introduced in +@sec:software-components. It is hosted on Github (https://github.com/maawoo/ARDCube) and can be used by others without restrictions as stated in the MIT licence. An overview of all integrated components, as well as the main workflows managed by individual modules, is shown in Figure @fig:ardcube. The following sections will describe the most important aspects in more detail. Documents that are more specific, such as setup instructions, are provided in the Github repository. 

![ARDCube overview](source/figures/03_methods_3__ardcube.png){#fig:ardcube width=100%}


### Python Framework 

A variety of Python packages form the basic framework of ARDCube. They are utilized to manage the integrated software components and further extend on their functionality by enabling the automation of specific workflows. To manage these Python packages on the other hand, the package manager conda (https://conda.io, last access: 07 May 2021) is used. It offers the possibility to create self-contained environments that can include a custom selection of Python packages. In addition, these environments can easily be shared and replicated by others, which yet again facilitates reproducibility. 

Based on the prospect of how ARDCube could be used in the future (e.g., a university department), two user groups were identified and hence all packages are managed in two separate conda environments: 

- A 'maintainer' environment that includes all packages necessary for the automated workflows to download, process, and organize data.  
- A 'user' environment that includes packages necessary for analyzing the data and allows to be extended by users as required.

Some important packages used in the maintainer environment are introduced at relevant points in the course of the following sections. The user environment on the other hand is intended to be used more flexibly. At a very basic level, only the ODC Python package and its dependencies (see +@sec:open-data-cube) would be needed to access datasets that were indexed into an ODC database. However, other packages are recommended to be included. Jupyter Lab, for example, allows users to start interactive computing environments in a remote web browser, which can be very useful in the context of working on HPC systems. In the end, extending the environment is left to each user and can be as simple as packages for the visualization of results, or more advanced with packages such as numba [@Lam2015] that allow for the performance optimization of array based computations. 


### Parameterization & Usage

...

### Modules

- Concise descriptions of the main modules in relation to Figure @fig:ardcube

**download_level1**


**generate_ard**


**prepare_odc**

