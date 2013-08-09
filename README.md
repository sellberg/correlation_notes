correlation_notes
=================

Jonas Sellberg || <sellberg@slac.stanford.edu><br>
Derek Mendez || <dermen@stanford.edu><br>
TJ Lane || <tjlane@stanford.edu><br>

We each have investigated many different sources of error in correlation scattering experiments (CXS), as well as many different ways to overcome those errors via data processing. For example, should one subtract the mean of each shot when correlating in the presence of significant beam pulse energy variation? This repository reflects a more systematic and thorough approach to dealing with those effects, and documents our perception for dealing with them.

--------------------------------------------------------------------------------

##Outline##

We plan on investigating at least two "systems", specifically simulations of (1) a sine wave in phi, and (2) gold nanoparticles. The best-estimate correlation (single molecule, good statistics) will be compared to correlation functions. Correction algorithms can be judged on these grounds.

###I. Introduction###

1. Stated goals of this paper
2. A brief introduction to CXS
3. Common notation for CXS experiments

###II. Different Statistical Estimators of the Correlation Function##

1. Normalization: shot-by-shot vs. ensemble
2. Mean Subtraction: shot-by-shot vs. ensemble

###III. Analysis of Sources of Error (SoE)###

1. Generic Noise
	- gaussian (e.g. Johnson) noise
	- photon poisson statistics

2. Beam Pulse Power
	- 10% gaussian fluctuations

3. Gaps
	- SSRL systematic gaps
	- 20% of pixels randomly masked (binomial distribution)

4. Gain
	- use statistics from LCLS single-pixel gain on each polar "pixel"
	- study LCLS non-linear gain

5. Number of molecules per shot
	- poisson statistics around lambda=50 molecules

6. Additive Background Errors
	- simulation of common mode effects on the CSPAD
	- a structured background, e.g. like a solvent

###IV. Effects on Real Data###

1. Combine effects from above
2. Provide realistic numbers for parameters used above
3. Discuss SSRL & LCLS real data

###V. Conclusions###

We will provide a general prescription based on combined effects

--------------------------------------------------------------------------------

##Datasets##

Gold?
Protein?

Where and what are these; how were they generated