# Background

## Big Data & Innovation

Since the beginning of the current century, a majority of the world's technological capacity to store, communicate, and compute information has relied on digital formats [@Hilbert2011]. This has not only resulted in the amount of data growing continuously, but also the importance of 'Big Data' being realized in various fields of society, such as science, industry, and government [@WEF2012]. 

The arising challenges and opportunities of growing amounts of EO and geospatial data have already been important topics in the 1990s. Al Gore coined the term 'Digital Earth' in a speech in 1998, where he envisioned a digital representation of our Earth and how it could benefit society [@Gore1998]. In the same decade, the need for improved management strategies of spatial information have increasingly been recognized by administrations worldwide and resulted in the development of Spatial Data Infrastructures (SDIs), like the INSPIRE Directive of the European Union. A brief history on this topic is provided by @Schade2019.

As presented by @Guo2016 and @Boulton2018, challenges and opportunities related to the current era of 'Big Earth Data' are still being discussed two decades later. In the context of EO, 'Big Earth Data' is particularly being fueled by the open data policies of the Landsat program, which includes an archive of over 40 years of global EO data [@Wulder2019], and the Copernicus program with its family of Sentinel satellites [@Aschbacher2017]. Furthermore, new missions are soon to be launched [e.g., @Kellogg2020] and new sensor technologies are being developed [e.g., @Kampe2017]. The commercial EO sector on the other hand is striving to provide EO data that exceeds the spatial- and temporal resolution of publicly available data [e.g., @Farquharson2018].

The volume of publicly available EO and geospatial data keeps growing and the variety of spatial-, spectral- and temporal resolutions, data formats and standards, adds to the complexity of generating valuable information from this data. 

Innovative trends in the rapidly evolving information technology (IT) sector have frequently been adopted by the geospatial sector. @Diaz2012 investigated this subject in relation to the development of SDIs and named 'cloud computing' as such an important trend. It describes a paradigm that allows individuals to access not only data that is being managed in a remote facility, but also applications and computing power, over the internet and on demand [@Foster2008]. 

@Sudmanns2020 describe a change in EO data analysis workflow that is suitable for dealing with large amounts of EO data, where analysis-ready datasets and appropriate tools for information production, are being provided in a cloud environment. They also describe that most professionals still rely on the 'traditional' workflow of downloading and processing datasets locally, however, cloud computing platforms such as Google Earth Engine [@Gorelick2017] have become more popular in recent years and enabled scientists to use EO data in unprecedented, global-scale studies [e.g., @Hansen2013]. 

As a consequence of these changing workflows and increasing volumes of open data being used for individual analyses, innovation is also happening in closely related areas. Data formats for example are evolving and being optimized for network-based access. In their work, @Durbin2020 compared the data formats GeoTIFF and NetCDF-4, two established standards in the domain of Earth Science, with their optimized equivalents Cloud-optimized GeoTIFF (COG) and Zarr. Furthermore, new specifications such as the SpatioTemporal Asset Catalog (STAC) are being developed to provide a standardized way of describing and indexing spatial data and thereby improving discoverability [@STAC2021].

In close relationship to open data and arguably an equally important driver of innovation is open source software, i.e., collaboratively developed software projects that can be used, changed, and distributed freely. @Coetzee2020 have reviewed the current state of open data and open source software in the context of the geospatial domain. They came to the conclusion that both “have changed the way in which geospatial data are collected, processed, analyzed, and visualized” and that they probably will be even more important in the future (p.24). 

A recent publication by @Abernathey2020 provides an interesting perspective on several of the aspects previously described while also considering reproducibility and FAIR Data Principles [@Wilkinson2016]. @Abernathey2020 suggest that the creation of cloud-native data repositories could be “a viable path forward to help data-intensive scientific fields overcome current infrastructure challenges” (p.10).



## Earth Observation Data Cubes

### Concept

- Strobl2017
- Nativi2017

- Ariav1986 - Concept existed before
- rasdaman, a pioneering technology that has coined the principle of queryable datacubes (https://link.springer.com/chapter/10.1007/978-3-642-77811-7_19) [@Misev2019]
- Earlier datacube approaches have focused on business oriented data introducing OLAP (Online Analytical Processing) https://link.springer.com/article/10.1023/A:1009726021843 [@Baumann2018]

- datacube approaches, involving Array Databases, systems with procedural (typically python) interfaces, array libraries, and more [Baumann2018]
- Next generation SDI [@Gomes2020]

*Fig: Schematic of an EO cube*


### Overview of related projects

- Short overview of existing projects / initiatives
  - Baumann2015 & Misev2019 / EarthServer & BigDataCube
  - Mahecha2020 / Earth System Data Lab
  - Appel2019 / gdalcubes
  - Lewis2017 / ODC
  - Sentinel Hub?
  - JEODPP?
  - Pebesma2017 & Schramm2021 / openEO?
- Distinction from platforms like GEE
  - Lack of consensus/distinction ? -> confusing
    - [@Gomes2020]: No differentiation and using the general term 'Platforms for big EO Data Management and Analysis'
    - [@Giuliani2019]: Tries to differentiate between data cube and cloud-based processing facilities
- Some advantages / disadvantages being discussed in literature
  - Not a black box / not proprietary / no vendor lock-in in comparison to platforms like GEE

- Mahecha2020: Most of the data cube initiatives are, however, motivated by the need for accessing singular (very-)high-resolution data cubes, e.g. from satellite remote sensing or climate reanalysis, and not by the need for global multivariate data exploitation


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
