
# Introduction

Earth observation (EO) satellites have been producing diverse and consistent sets of data about the Earth's surface for multiple decades now. This continuously growing volume of data and its derived products provide information that support the assessment and monitoring of global policy frameworks, such as the United Nations Sustainable Development Goals (SDGs) [1], contribute to the climate data records of several Essential Climate Variables (ECVs) [2] and assist decision makers in the sustainable use of Earth's resources [3].

Access to this extensive volume of data has been as easy as ever, which can be emphasized with the two most important satellite data archives: the Landsat program by NASA and the United States Geological Survey (USGS) and the Copernicus program by the European Commission and the European Space Agency (ESA). A free and open access policy for Copernicus data has been agreed upon before the launch of the first Sentinel satellite in 2014 [4], which is expected to result in positive social, environmental and economic impacts for the European Union [5]. On the other hand, access to the Landsat archive, with some datasets starting as early as 1972, only changed to an open data policy in 2009, which subsequently resulted in a significant increase in usage as well as scientific and public value of this data [6].

The ever-increasing availability of petabytes of EO and other geospatial data has led to the designation of the term 'big Earth data' and started discussions about associated opportunities and challenges [7][8]. The characterization of big data challenges as 'Volume, Velocity and Variety' by Laney (2001) [9] has also been adapted in context of big Earth data: 'Volume (e.g., data volumes have increased by 10 in the last 5 years); Velocity (e.g., Sentinel-2 is capturing a new image of a given place every 5 days); and Variety (e.g., different type of sensors, spatial/spectral resolutions)' [10]. Furthermore, these challenges inhibit the full potential of the data to be exploited by the average user, especially when many still rely on the traditional approach of downloading and processing the data on their local system. Limitations in file storage and computing resources make the analysis of EO time-series, even for small spatial scales, impracticable.

In the past few years, this demand for new and innovative solutions has promoted the emergence of various platforms that not only provide access to open and commercial EO data repositories, but also offer processing capabilities via cloud-based infrastructures. Notable examples include: Google Earth Engine [11], Data and Information Access Services (DIAS) [12], OpenEO [13], the JRC Earth Observation Data and Processing Platform (JEODPP) [14] and Sentinel Hub [15]. All of these cloud-based management and analysis platforms can represent viable alternatives to the traditional data-centric approach. However, no one-fits-all solution exists and the fact that most platforms either rely on proprietary, closed source software or necessitate the purchase of storage space and processing resources, can be an important drawback for some user groups.

Another innovative solution that gained popularity among the EO community in recent years, is the Open Data Cube (ODC). This open source software project is supported by institutions like Geoscience Australia, USGS and the Committee on Earth Observation Satellites (CEOS) [16] and has been successfully deployed for several regions around the world, such as Australia [17], Switzerland [18], Catalonia (Spain) [19] and Taiwan [20]. These national and regional ODC deployments enable researchers and decision makers to efficiently retrieve information from EO datasets, while being in control of their own data management and analysis platform and how it is being implemented on their existing computational infrastructures.

Giuliani et al. (2017) [18] identified data access and data preparation as two major challenges for the implementation of Data Cubes, both of which regard the processing of Analysis Ready Data (ARD). ARD can be defined as "satellite data that have been processed to a minimum set of requirements and organized into a form that allows immediate analysis with a minimum of additional user effort and interoperability both through time and with other datasets" [21]. Currently, data providers are lacking behind in providing ARD products (e.g. available Landsat ARD only covers the United States [22]) and there is still a lack of agreement for best practices of ARD generation in the user community. However, progress in this regard is ongoing, both for optical [23] and radar sensors [24]. Furthermore, new and innovative software tools for the generation of ARD are emerging [25].

According to the ODC initiative, the ODC is supposed to ease technical barriers related to the exploitation of EO data [16]. At the present stage of development, this statement can only be deemed partially true as new users face a significant barrier in the initial technical setup, including figuring out a viable workflow for generating and feeding ARD to their ODC implementation. Nevertheless, the ODC vision is also highlighting the importance that new deployments can benefit from the "lessons learned" of prior deployments [16].

The goal of this work is to:

- Implement a regional Open Data Cube for the German state of Thuringia
- Develop an automated workflow to download, process and index ARD, which
  - Uses established, open source software tools to facilitate reproducibility and
  - Harmonizes the data products for optimal time-series analysis
- Examine the potential and usability of this project by presenting 2-3 time-series analysis use cases

Therefore, contributing to the "lessons learned" aspect of the ODC vision (...?).

(Last paragraph: Overview of next chapters)

----

[1] Anderson2017  
[2] Hollmann2013  
[3] Eckman2012  
[4] EuropeanCommission2013  
[5] PwC2019  
[6] Wulder2012  
[7] Guo2016  
[8] Boulton2018  
[9] Laney, D. (2001). 3D data management: Controlling data volume, velocity and variety. META group research note, 6(70), 1.
    https://studylib.net/doc/8647594/3d-data-management--controlling-data-volume--velocity--an...  
[10] Giuliani2019a (page 1)  
[11] Gorelick2017  
[12] https://www.copernicus.eu/sites/default/files/Copernicus_DIAS_Factsheet_June2018.pdf / https://earsc.org/dias-comparison  
[13] Pebesma2017  
[14] Soille2018  
[15] https://www.sentinel-hub.com  
[16] Killough2018  
[17] Lewis2017  
[18] Giuliani2017  
[19] Maso2019  
[20] Cheng2019  
[21] Lewis2018 (page 2 / 7408)  
[22] https://www.usgs.gov/core-science-systems/nli/landsat/us-landsat-analysis-ready-data  
[23] Giuliani2018  
[24] Truckenbrodt2019  
[25] Frantz2019
