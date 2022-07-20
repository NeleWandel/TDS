API
===

.. toctree::

   API


A
---

| ``AcquisitionState()`` 
| This command returns 0 if currently no acquisition takes place. Otherwise it returns 1.
| 
| ``ActivateAveraging(WaveformAmount)``
| *This command can be used before or during the data aquisition.*
| Enables the *averaging acquisition mode*. In this mode the oscilloscope averages all acquired values from multiple waveforms and create a waveform based on the averaged values. 
| The number of waveforms that will be analysed must be set by ``WaveformAmount``, with the smallest possible number being 1. The more waveforms shall be analysed the more accurate the result, but the longer the aquisition needs.
| 
| ``ActivateEnvelopeMode(WaveformAmount)``
| *This command can be used before or during the data acquisition.*
| Enables the *envelope acquisition mode*. In this mode the oscilloscope creates a waveform by showing the peak range values of the data points from multiple waveform acquisitions.
| The number of waveforms that will be analysed must be set by ``WaveformAmount``, with the smallest possible number being 1. The more waveforms shall be analysed the more accurate the result, but the longer the aquisition needs.
| 
| ``ActivateHiRes()``
| *This command can be used before or during the data acquisition.*
| Enables the *Hi Res acquisition mode*. In this mode the oscilloscope creates a value by averaging all acquired data points from one waveform.
| The ammount of data points that are taken during the acquisition period can be set with the command ``SetSampleSize(amount)``.
| 
| ``ActivatePeakDetect()``
| *This command can be used before or during the data acquisition.*
| Enables the *peak detect acquisition mode*. In this mode the oscilloscope creates a vertical column that show off the highest and lowest value of all acquired data points from one waveform.
| The ammount of data points that are taken during the acquisition period can be set with the command ``SetSampleSize(amount)``.
| 
| ``ActivateSampleMode()``
| *This command can be used before or during the data acquisition.*
| Enables the *sample acquisition mode*. In this mode the oscilloscope creates a waveform with the acquired data points from one waveform.
| The ammount of data points that are taken during the acquisition period can be set with the command ``SetSampleSize(amount)``.
| 
| ``ActivateWFMDBMode()``
| *This command can be used before or during the data acquisition.*
| Enables the *waveform database mode*. In this mode the oscilloscope acquires threedimensional data from a waveform (amplitude, time, count). The count-value keeps track on how often a specific data point (amplitude + time) has been acquired. The data acquisition starts with a trigger and works the same as *sample mode*, but it compares multiple samples with each other.
| The ammount of data points that are taken during the acquisition period can be set with the command ``SetSampleSize(amount)``.
| 
| ``AutoAdjustMaskOff()``
| Turns off automatic optimising of the mask.
| 
| ``AutoAdjustMaskOn()``
| Turns on automatic optimising of the mask. This feature shifts the mask horizontally and vertically in order to minimise the signal hits.
| 
| ``AutoSet()``
| Automatically adjusts the vertical, horizontal and trigger controls in order to privide a stable display of the waveform on the oscilloscope.
| These changes can be undone by using the ``Undo()`` command.
