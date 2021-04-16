
# Introduction

Earth observation (EO) satellites have been producing diverse and consistent datasets that provide valuable information about the Earth's surface for multiple decades now. This continuously growing volume of data and its derived products supports the assessment and monitoring of global policy frameworks, such as the United Nations Sustainable Development Goals (SDGs) [@Anderson2017], contributes to the climate data records of several Essential Climate Variables (ECVs) [@Hollmann2013] and assists decision makers in the sustainable use of Earth's resources [@Eckman2012].

Access to this extensive volume of data has been as easy as ever, which can be emphasized with the two most important satellite data archives: the Landsat program by NASA and the United States Geological Survey (USGS), and the Copernicus program by the European Commission and the European Space Agency (ESA). A free and open access policy for Copernicus data has been agreed upon before the launch of the first Sentinel satellite in 2014 [@EuropeanCommission2013], with the expectation that it can result in positive social, environmental and economic impacts for the European Union [@PwC2019]. On the other hand, access to the Landsat archive, with some datasets starting as early as 1972, only changed to an open data policy in 2009, which subsequently resulted in a significant increase in usage as well as scientific and public value of this data [@Wulder2012].

The ever-increasing availability of petabytes of EO and other geospatial data has led to the designation of the term 'big Earth data' and started discussions about associated opportunities and challenges [@Guo2016] [@Boulton2018]. The characterization of big data challenges as 'Volume, Velocity and Variety' by Laney (2001) [@Laney2001] has also been adapted in context of big Earth data: 
>“Volume (e.g., data volumes have increased by 10 in the last 5 years); Velocity (e.g., Sentinel-2 is capturing a new image of a given place every 5 days); and Variety (e.g., different type of sensors, spatial/spectral resolutions)” [@Giuliani2019a, p.1]. 

Furthermore, these challenges inhibit the full potential of the data to be exploited by the average user, especially when many still rely on the traditional approach of downloading and processing the data on their local system. Limitations in file storage and computing resources make the analysis of EO time-series, even for small spatial scales, impracticable.

In the past few years, this demand for new and innovative solutions has promoted the emergence of various platforms that not only provide access to open and commercial EO data repositories, but also offer processing capabilities via cloud-based infrastructures. Notable examples include: Google Earth Engine [@Gorelick2017], Data and Information Access Services (DIAS) [xx], OpenEO [@Pebesma2017], the JRC Earth Observation Data and Processing Platform (JEODPP) [@Soille2018] and Sentinel Hub [15]. All of these cloud-based management and analysis platforms can represent viable alternatives to the traditional data-centric approach. However, no one-fits-all solution exists and the fact that most platforms either rely on proprietary, closed source software or necessitate the purchase of storage space and processing resources, can be an important drawback for some user groups.

Another innovative solution that gained popularity among the EO community in recent years, is the Open Data Cube (ODC). This open source software project is supported by institutions like Geoscience Australia, USGS and the Committee on Earth Observation Satellites (CEOS) [@Killough2018] and has been successfully deployed for several regions around the world, such as Australia [@Lewis2017], Switzerland [@Giuliani2017], Catalonia (Spain) [@Maso2019] and Taiwan [@Cheng2019]. These national and regional ODC deployments enable researchers and decision makers to efficiently retrieve information from EO datasets, while being in control of their own data management and analysis platform and how it is being implemented on their existing computational infrastructures.

@Giuliani2017 identified data access and data preparation as two major challenges for the implementation of Data Cubes, both of which regard the processing of Analysis Ready Data (ARD). ARD can be defined as “satellite data that have been processed to a minimum set of requirements and organized into a form that allows immediate analysis with a minimum of additional user effort and interoperability both through time and with other datasets” [@Lewis2018, p.2 / 7408?]. Currently, data providers are lacking behind in providing ARD products (e.g. available Landsat ARD only covers the United States [22]) and there is still a lack of agreement for best practices of ARD generation in the user community. However, progress in this regard is ongoing, both for optical [@Giuliani2018] and radar sensors [@Truckenbrodt2019]. Furthermore, new and innovative software tools for the generation of ARD are emerging [@Frantz2019].

According to the ODC initiative, the ODC is supposed to ease technical barriers related to the exploitation of EO data [@Killough2018]. At the present stage of development, this statement can only be deemed partially true as new users face a significant barrier in the initial technical setup, including figuring out a viable workflow for generating and feeding ARD to their ODC implementation. Nevertheless, the ODC vision is also highlighting the importance that new deployments can benefit from the "lessons learned" of prior deployments [@Killough2018].

The goal of this work is to:

- Implement a regional Open Data Cube for the German state of Thuringia
- Develop an automated workflow to download, process and index ARD, which
  - Uses established, open source software tools to facilitate reproducibility and
  - Harmonizes the data products for optimal time-series analysis
- Examine the potential and usability of this project by presenting 2-3 time-series analysis use cases

Therefore, contributing to the "lessons learned" aspect of the ODC vision (...?).

(Last paragraph: Overview of next chapters)

[15] https://www.sentinel-hub.com  
[22] https://www.usgs.gov/core-science-systems/nli/landsat/us-landsat-analysis-ready-data  
