# Persistent Homology Rank Functions

<!-- Outline -->
## Outline

This repository contains data and code for computing single-parameter persistent homology rank functions and bi-parameter persistent homology rank invariants, also reproducing the figures and application results in the paper [``Computational Stability for Persistence
Rank Function Machine Learning"](cite).

Persistent homology is one of the most important tools in topological data analysis, studying how homological features of data persist over scale. Commonly, persistent homology is represented using the persistence diagram or the persistence barcode. However, these representations do not lend themselves naturally to statistical and machine learning algorithms. 

We explore the persistent homology rank functions as equivalent functional representations that are naturally suited to methods in functional data analysis, and can also be extended to the multiparameter setting.

<!-- Structure of the repository -->
## Structure of the repository
This repository is organised as follows:
- `HRV_Application:` 


## give credit to sources
To generate point clouds on tumour surface from CT scans see [this notebook](https://github.com/robinvndaele/TDA_LungLesion/blob/master/Scripts/TDAtumor.ipynb) from https://github.com/robinvndaele/TDA_LungLesion.




<!-- Package installation -->
## Package installation
Single parameter persistent homology rank functions can be computed both in [Julia](https://julialang.org/) and [Python](https://www.python.org/) and we compute two parameter persistent homology rank functions using [RIVET](https://rivet.readthedocs.io/en/latest/) in combination with python scripts. To run the ipython notebooks within this repository, we require the following libraries.

### Julia libraries 
Julia is a high-level, general-purpose dynamic programming language.
We compute single-parameter persistent homology using the [Ripserer](https://mtsch.github.io/Ripserer.jl/dev/) package and to reproduce the outputs in the [] notebook we also require the following packages:
- [CSV](https://csv.juliadata.org/stable/)
- [DataFrames](https://dataframes.juliadata.org/stable/)
- [Plots](https://docs.juliaplots.org/latest/tutorial/)
- [MultivariateStats](https://github.com/JuliaStats/MultivariateStats.jl)
- [Statistics](https://docs.julialang.org/en/v1/stdlib/Statistics/)
- [GLM](https://juliastats.org/GLM.jl/stable/)
- [StatBase](https://juliastats.org/StatsBase.jl/stable/)
- [Lathe](https://github.com/ChifiSource/Lathe.jl)
- [MLBase](https://github.com/JuliaStats/MLBase.jl)
- [ClassImbalance](https://juliapackages.com/p/classimbalance)
- [ROCAnalysis](https://github.com/davidavdav/ROCAnalysis.jl)
- [LIBSVM](https://github.com/JuliaML/LIBSVM.jl)
- [Random](https://docs.julialang.org/en/v1/stdlib/Random/)

### Python libraries:
Python is a high-level, versatile, and easy-to-read programming language widely used for various applications, including data analysis, machine learning.
We require from python the following packages:
- [numpy](https://numpy.org)
- [os](https://docs.python.org/3/library/os.html)
- [matplotlib](https://matplotlib.org/)
- [gudhi](https://gudhi.inria.fr/python/latest/)
- [math](https://docs.python.org/3/library/math.html)
- [random](https://docs.python.org/3/library/random.html)
- [ripser](https://ripser.scikit-tda.org/en/latest/)
- [persim](https://persim.scikit-tda.org/en/latest/)

### RIVET 
[RIVET](https://rivet.readthedocs.io/en/latest/) is a tool for computing two-parameter persistent homology and we provide code to compute the rank invariants from the RIVET outputs in the folder Compute_Biparameter_Rank_Invariant (these codes are built upon the original code for computing multiparameter persistence landscapes found [here](https://github.com/OliverVipond/Multiparameter_Persistence_Landscapes/tree/master))







<!-- References -->
## References
- [1]
- [2]









<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[julia-logo]: https://julialang.org/assets/infra/logo.svg
[julia-url]: https://julialang.org/


