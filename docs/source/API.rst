API
===

.. autosummary::
   :toctree: generated

A
---

| ``AcquisitionState()`` 
| This command returns 0 if currently no acquisition takes place. Otherwise it returns 1.
| 
| ``ActivateAveraging(WaveformAmount)``
| This command can be used before or during the dataaquisition.
| Enables the *Averaging Acquisition Mode*. In this mode the oscilloscope averages all acquired values from multiple waveforms. 
| The number of Waveforms must be set by ``WaveformAmount``, with the smallest possible number being 1. The more waveforms shall be analysed the more accurate the result, but the longer the aquisition needs.
