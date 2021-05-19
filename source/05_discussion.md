# Discussion


## Use Cases

- Implementation is successful!
  - Includes both aspects: ARD and EODC/ODC
  - As proven by use cases...
- Per-pixel observations not just useful to test the implementation in general but also to get a better understanding of the datasets (both temporal & spatial)
  - Can reveal wrong parameterization during ARD processing
  - Time-series values might be lost due to false-positive cloud/cloud-shadow flags -> Needs to be considered!
  - Some regions have a lot fewer observations in multiple datasets, which can influence analysis -> Needs to be considered! 
- Roda analysis
  - Even though it lies in exactly one of the regions with fewer observations, this simplified analysis worked very well!
  - ... 
- In a more general sense: Some aspects need/should be always considered (+@sec:performance-considerations)
  - Available tools/resources are great however to find problems or improve performance in general -> Less abstract due to interactivity and visualization 
- ODC, Xarray, Dask already provide a lot of possibilities to work with the data
  - The ecosystem is huge and continues to grow
  - Other libraries that are not necessarily part of the ecosystem can still be integreated if needed (e.g., numba) 
  - ML!: https://github.com/GeoscienceAustralia/dea-notebooks/tree/develop/Real_world_examples/Scalable_machine_learning 


## Implementation
### ARD

- To my knowledge no official FORCE or pyroSAR CARD4L assessments have been done. (I haven't done them either...)
  - John: "No formal assessment was made of how far the workflows presented here meet the requirements of this guideline. This is considered as a future goal such that a user might eventually be able to select a certain level of analysis “readiness” in either software and conveniently process data accordingly"  
  - Should 
- Data
  - Currently relies on FORCE defaults for the GeoTIFF specifications that were described
  - A change in data format (e.g., internal tiling of GeoTIFFs as blocks instead of strips, which is also default for COGs) would mean additional post-processing steps
  - Assessments for quality, performance and so on are needed before deciding on any format changes and need to be justified, because it already works pretty well as is... 
- Metadata
  - Same as data itself: reliance on how FORCE/pyroSAR handle it 
  - Develop a better system for organization on top of FORCE/pyroSAR? Or fully adapt the solution of one of both? Or just leave it as is because in the end both forms are machine readable (which is a CARD4L requirement)
  - Integration of pyroSAR Archive functionality?
  - Completeness of metadata was not evaluated. (as mentioned already: CARD4L assessments)
  - ODC Dataset Documents currently only store metadata that is necessary for ODC and nothing else (e.g. in properties field), because there's currently no use / it would be stored twice (at least) -> data redundancy / and even if more metadata is needed in the YAMLs it is easy to add and regenerate the files...   


### ODC

- Once everything is integrated/setup it works great, but to get there is not as straightforward as is advertised in some cases/articles
- Docker  
  - Even though it's not really mentioned in Docs, some Docker projects exist... 
    - https://github.com/opendatacube: 2 repos and 1 subdirectory in the core repo!
    - Then there is Datacube On Demand which is described as open source by Giuliani et al but nowhere to be found?
    - In the end Singularity container and conda environment a simple solution that works and is scalable (HPC!)
- PostgreSQL database and YAML based indexing might not be the best solution
  - Both aspects are also considered by devs and likely changed in the future (other db backends / STAC)
    - https://github.com/opendatacube/datacube-core/wiki/enhancement-proposals  
    - However, probably not any time soon...
  - Pangeo tools & STAC (+ intake-stac, stacstack, ...) seems to be great alternatives that would be worth testing
    - A **lot** of development in this area!
    - ODC is moving in the same direction with STAC integration + already shares core components (Xarray + Dask as core components; Jupyter)... in the future the lines might be even more blurred 
    - So question is what ODC can actually offer in comparison?
      - Pangeo is just a collection of tools (Geoscience in general, not just EO) -> some functionalities/preparation steps needed to work with EO data and Xarray/Dask might be lacking 
      - datacube-core is doing exactely this (wrapping Xarray and using rasterio for reprojections etc)
  - Also xcube with their Zarr integration and also the same core libraries (Xarray+Dask)!
- Community
  - Documentation is in some parts outdated/confusing for new users. e.g. Ingestion is still described in Docs but "not recommended" in Community?
  - Big open source projects should have a proper community space to ask questions/get help
    - Current solution less than ideal to say the least...
  - Since recently ODC has been a GEO community activity 
    - ODC Initiative -> Open Earth Alliance afaik 
    - https://www.openearthalliance.org/
  - And a OSGeo Community Project 
    - http://osgeo-org.1560.x6.nabble.com/The-Open-Data-Cube-Application-for-OSGeo-Community-Project-Status-td5484126.html
    - https://www.osgeo.org/projects/open-data-cube/
  - ... so maybe those problems can soon be solved! (nobody should expect the core devs to do everything)



## Outlook

(ARDCube)

- ARDCube reproducibility! E.g. ease the process of reproducing someone elses project from level-1 data to ARD processing and ODC indexing to the analysis itself
  - Sudmanns2020: "[...] reproducibility not only requires a certain type of data but also semantic annotation of workflows (Scheider, Ostermann, and Adams 2017). This ensures data stewardship, comprehensive data lineage and trust in results. Producers of products and services are asked to disseminate detailed documentation of the data and workflows together with their results."
  - Giuliani2019 & Giuliani2019a
  - Abernathy2020: "Reproducibility of data science projects requires open access to at least three elements: the code, the software environment, and the data."

(TDC)

- [More data!](https://media.giphy.com/media/xT0BKi1TLjmKiu1HGg/giphy.gif)
  - Temporal 
  - Other sensors: Landsat archive with FORCE, easy and ARDCube is ready! SAR data a bit more work needed. 
  - Auxiliary data: layover/shadow map, local incidence angle, ..? -> [@Truckenbrodt2019] 
- Better data
    - WVDB integration (needs to be done anyway when other Landsat data is processed)
    - Co-registration of Sentinel-2 scenes -> https://ieeexplore.ieee.org/abstract/document/9387494
    - Test Lidar DEM? -> [@Truckenbrodt2019]
- Automation / Near Real Time data stream
  - ARDCube commands could be used with a cronjob on Terrasense for example
  - Also relevant from BIDS presentation: https://elib.dlr.de/137176/
- JupyterHub to manage multiple users and computing resources 
  - Würzburg EO department! https://datacube.remote-sensing.org/
  - https://ieeexplore.ieee.org/abstract/document/9387494 
- Utilization of already available ODC extensions/applications
  - https://www.opendatacube.org/data-cube-applications
  - E.g. Explorer, which could also be used as a base project to extend as needed/wanted -> Webapp
  - Gowda2020a
