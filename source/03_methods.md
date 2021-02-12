
# Radar

# Optical

## FORCE
### Data cubing

Spatial resolution:
- Landsat-8 = 30 m
- Sentinel-2 = 10 m
    - Resolution merging: IMPROPHE

Projection: 
- EPSG 25832
- Resampling = Cubic Convolution

Tiling:
- Tile size = 30000
- Block size = 3000

### Corrections

Radiometric:
- Atmospheric correction
  - DEM!
- Topographic correction
  - DEM!
- BRDF
- Adjacency effect
- Multiple scattering

https://doi.org/10.3390/rs10020352
https://doi.org/10.1109/TGRS.2016.2530856

Water Vapor:
- Nope
- http://doi.org/10.3390/rs11030257 
    - “The uncertainty and bias were progressively reduced from Landsat 5 over Landsat 7 to Landsat 8 (with the exception of SWIR2 uncertainty) up to the point that the use of the climatology only marginally influences surface reflectance for Landsat 8’s NIR and SWIR1;”

Aerosol Optical Depth:
- Default / Internal estimation

### Cloud Detection

https://doi.org/10.1016/j.rse.2018.04.046
https://doi.org/10.3390/rs13010137

- Default parameters
- DEM!

### Sentinel-2 Coregistration

https://doi.org/10.1109/LGRS.2020.2982245

- Creation of Landsat base images

### Data format

- GeoTIFF

## Other improvements?

