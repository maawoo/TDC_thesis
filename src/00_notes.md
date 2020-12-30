
# Outline

- Title page
- Table of contents
- Lists / Glossary
- Abstract
- **Introduction**
  - Thematic introduction / Outline of the problem
  - Importance and significance of the topic in a larger context
  - What exactly is the goal of this work?
  - Overview of what lies ahead
- **Background**
  - State of the art / Literature review
  - Subtopics?
    - Analysis Ready Data (ARD)
    - EO data cubes (EODC)
- **Methods**
- **Results**
- **Discussion**
- **Conclusion**
- Literature
- Appendix

----

# Introduction

**Roter Faden:**

Problem of big EO data (big picture) >> General solutions >> Specific solution (ODC) >> ARD is fundamental, but not easy >> Goal of my work

## Problem of big EO data

- Volume, Velocity & Variety
- Still hard for users to harness the full potential of EO
- Trend towards cloud solutions
- Traditional approach of processing locally is not feasible anymore for large volumes of EO data
- Even more data in the future... duh

## General solutions

- Cloud-based processing (GEE, DIAS, ...)
- Rasdaman, Pangeo, etc
- All have pros & cons; no 'one-fits-all' solution exists

## Specific Solution (ODC)

- Short intro to ODC (more detailed in Background section!)
- Examples of where it's already being used
- Open-source & potential for future (interoperability)

## ARD is fundamental

- No standards yet
- No easy access; DIY attitude in science / multiple ways and tools for processing
- In the ODC community there's also no clear approach; Different ARD strategies used for different ODC instances and sometimes not comprehensible how ARD was processed

## Goal of my work

- Use established python packages to generate ARD (both optical & SAR)
  - FORCE
  - pyroSAR
- Automate the process (download, processing, indexing to ODC) as easily as possible
- No vendor lock-in (there's always multiple sources to access raw data; software is open-source)

----

# Background

- ARD
- EODC

----

# Methods

- bla
