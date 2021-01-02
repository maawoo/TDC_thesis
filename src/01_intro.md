
# Introduction

Earth observation (EO) satellites have been producing diverse and consistent sets of data about the Earth's surface for multiple decades now. This continuously growing volume of data and its derived products provide information that support the assessment and monitoring of global policy frameworks, such as the United Nations Sustainable Development Goals (SDGs) [1], contribute to the climate data records of several Essential Climate Variables (ECVs) [2] and assist decision makers in the sustainable use of Earth's resources [3].

Access to this extensive volume of data has been as easy as ever, which can be emphasized with the two most important satellite data archives: the Landsat program by NASA and the United States Geological Survey (USGS) and the Copernicus program by the European Commission and the European Space Agency (ESA). A free and open access policy for Copernicus data has been agreed upon before the launch of the first Sentinel satellite in 2014 [4], which is expected to result in positive social, environmental and economic impacts for the European Union [5]. On the other hand, access to the Landsat archive, with some datasets starting as early as 1972, only changed to an open data policy in 2009, which subsequently resulted in a significant increase in usage as well as scientific and public value of this data [6].

The ever increasing availability of petabytes of EO and other geospatial data has led to the designation of the term 'big Earth data' and started discussions about associated opportunities and challenges [7][8]. The characterization of big data challenges as 'Volume, Velocity and Variety' by Laney (2001) [9] has also been adapted in context of big Earth data: 'Volume (e.g., data volumes have increased by 10 in the last 5 years); Velocity (e.g., Sentinel-2 is capturing a new image of a given place every 5 days); and Variety (e.g., different type of sensors, spatial/spectral resolutions)' [10]. Furthermore, these challenges inhibit the full potential of the data to be exploited by the average user, especially when many still rely on the traditional approach of downloading and processing the data on their local system. Limitations in file storage and computing resources make the analysis of EO time-series, even for small spatial scales, impracticable.

In the past few years, this demand for new and innovative solutions has promoted the emergence of various platforms that not only provide access to open and commercial EO data repositories, but also offer processing capabilities via cloud-based infrastructures. Notable examples include: Google Earth Engine [11], Data and Information Access Services (DIAS) [12], OpenEO [13], the JRC Earth Observation Data and Processing Platform (JEODPP) [14] and Sentinel Hub [15]. All of these cloud-based management and analysis platforms can represent viable alternatives to the traditional data-centric approach. However, no one-fits-all solution exists and the fact that most platforms either rely on proprietary, closed source software or necessitate the purchase of storage space and processing resources, can be an important drawback for some user groups.

Another innovative solution that gained popularity among the EO community in recent years, is the Open Data Cube (ODC). This open source software project is supported by institutions like Geoscience Australia, USGS and Committee on Earth Observation Satellites (CEOS) [16] and has been successfully implemented for several regions around the world, such as Australia [17], Switzerland [18], Catalonia (Spain) [19] and Taiwan [20]. These national and regional ODC implementations enable researchers and decision makers to efficiently retrieve information from relevant EO datasets, while being in control of their own data management and analysis platform.

----

A major challenge for the implementation of Data Cubes is access to Analysis Ready Data (ARD). Like the name already implies, this data has already been preprocessed in a way that users can immediately start their analysis without having to spend time with data preperation beforehand. Recently progress has been made to define ARD for optical and Radar sensors for land applications (CARD4L). But there is still a lack of agreement for best practices of ARD generation, while data providers are lacking behind in providing ARD products. Currently, users/researchers are more or less stuck with traditional approaches of locally downloading and processing data or building their own solutions.

ARD is fundamental to the functioning of ODC implementations, but there is no common agreement between ODC users on a viable approach to automatically serve ARD to an ODC. While the ODC initiative says that ODC should lower barriers for users to exploit the full potential of EO, new ODC users face a huge barrier in trying to figure out what the best way of serving ARD to their cube is. Successful implementations only present their ARD solution in a limited way or not at all. Open source software exists that can process ARD in large volumes and because of their open nature, giving researchers the freedom/flexibility to process the data in a suitable way for their projects.

The goal of this project is to:

- Create a regional Open Data Cube for Thuringia = Thuringia Data Cube (TDC)
- Develop an automated workflow to generate ARD
  - Use established, open source tools to facilitate reproducibility (can easily be adapted for other regions)
  - Flexibility to download and process optical and SAR data of various sensors
  - Automatic indexing in ODC
- Highlight potential of the TDC/workflow by presenting 2-3 time-series analysis use cases

Overview of next chapters

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
