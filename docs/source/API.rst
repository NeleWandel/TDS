API
===

.. toctree::

   API


Acquisition
---------

.. method:: AcquisitionState()
| Returns :const:`0` if currently no acquisition takes place. Otherwise it returns :const:`1`.
| 
.. method:: ActivateAveraging(WaveformAmount)
| *This command can be used before or during the data aquisition.*
| Enables the *averaging acquisition mode*. In this mode the oscilloscope averages all acquired values from multiple waveforms and create a waveform based on the averaged values. 
| The number of waveforms that will be analysed must be set by ``WaveformAmount``, with the smallest possible number being 1. The more waveforms shall be analysed the more accurate the result, but the longer the aquisition needs.
| 
.. method:: ActivateEnvelopeMode(WaveformAmount)
| *This command can be used before or during the data acquisition.*
| Enables the *envelope acquisition mode*. In this mode the oscilloscope creates a waveform by showing the peak range values of the data points from multiple waveform acquisitions.
| The number of waveforms that will be analysed must be set by ``WaveformAmount``, with the smallest possible number being 1. The more waveforms shall be analysed the more accurate the result, but the longer the aquisition needs.
| 
.. method:: ActivateHiRes()
| *This command can be used before or during the data acquisition.*
| Enables the *Hi Res acquisition mode*. In this mode the oscilloscope creates a value by averaging all acquired data points from one waveform.
| The amount of data points that are taken during the acquisition period can be set with the command :meth:`SetSampleSize`.
| 
.. method:: ActivatePeakDetect()
| *This command can be used before or during the data acquisition.*
| Enables the *peak detect acquisition mode*. In this mode the oscilloscope creates a vertical column that show off the highest and lowest value of all acquired data points from one waveform.
| The amount of data points that are taken during the acquisition period can be set with the command :meth:`SetSampleSize`.
| 
.. method:: ActivateSampleMode()
| *This command can be used before or during the data acquisition.*
| Enables the *sample acquisition mode*. In this mode the oscilloscope creates a waveform with the acquired data points from one waveform.
| The amount of data points that are taken during the acquisition period can be set with the command :meth:`SetSampleSize`.
| 
.. method:: ActivateWFMDBMode()
| *This command can be used before or during the data acquisition.*
| Enables the *waveform database mode*. In this mode the oscilloscope acquires threedimensional data from a waveform (amplitude, time, count). The count-value keeps track on how often a specific data point (amplitude + time) has been acquired. The data acquisition starts with a trigger and works the same as *sample mode*, but it compares multiple samples with each other.
| The amount of data points that are taken during the acquisition period can be set with the command :meth:`SetSampleSize`.
| 
.. method:: SetSampleSize(amount)
| Sets the amount of samples that will be acquired during one acquisition period. 
| 
Mask
----

.. method:: AutoAdjustMaskOff()
| Turns off automatic optimising of the mask.
| 
.. method:: AutoAdjustMaskOn()
| Turns on automatic optimising of the mask. This feature shifts the mask horizontally and vertically in order to minimise the signal hits.
| 
Miscellanious
-------------

.. method:: AutoSet()
| Automatically adjusts the vertical, horizontal and trigger controls in order to privide a stable display of the waveform on the oscilloscope.
| These changes can be undone by using the :meth:`Undo` command.
| 
.. method:: Undo()
| Reverses all changes done by :meth:`AutoSet`. 
| 
.. method:: Busy()
| Returns :const:`0` if the oscilloscope is currently not running the :meth:`StartAcquisition` command. Returns :const:`1` if the oscilloscope is acquiring data. 
| 
.. method:: Calibration()
| Starts the auto calibration. 
.. note:: In order for this command to properly work it is recommended to wait around 20 minutes after turning the oscilloscope on. It might take a long time for the oscilloscope to self-calibrate. No other commands will be executed during this time.
| 
.. method:: Channel(channelnumber)
| Sets the standard channel for all future commands. ``channelnumber`` may only be 1, 2, 3 or 4.
| Default value is ::const::`1`.
| 
.. method:: ChannelAsSource()
| Sets the channel as source for all acquisitions. The channel can be set by :meth:`Channel`
| Other options are: :meth:`MathAsSource`, :meth:`RefAsSource` and :meth:`HistogramAsSource`
.. method:: ChannelOffset(offsetinmV)
.. method:: Clear()
.. method:: ClockPolarityFall()
.. method:: ClockPolarityRise()
.. method:: CMIPulseFormExeDiagram()
.. method:: CMIPulseFormMinusOne()
.. method:: CMIPulseFormPlusOne()
.. method:: CMIPulseFormZero()
.. method:: Continually()
.. method:: CountMeasures(x)
.. method:: Date()
.. method:: DefineMath(equation)
.. method:: DefineMathVariable(varnumber, varvalue)
.. method:: DefineTrigger(trigger)
.. method:: DisableCalcAndDisplay()
.. method:: EnableCalcAndDisplay()
.. method:: Export()
.. method:: ExportFileFormat(ff)
.. method:: ExportFilePath(path)
.. method:: HistogramAsSource()
.. method:: Identify()
.. method:: ImmediateChannelAsSource()
.. method:: ImmediateHistogramAsSource()
.. method:: ImmediateMathAsSource()
.. method:: ImmediateRefAsSource(waveform)
.. method:: ImmediateRefIsAbsolute()
.. method:: ImmediateRefIsPercent()
.. method:: ImmediateSetHighRefAbsolute(volt)
.. method:: ImmediateSetHighRefPercent(percent)
.. method:: ImmediateSetLowRefAbsolute(volt)
.. method:: ImmediateSetLowRefPercent(percent)
.. method:: ImmediateSetMidRefAbsolute(volt)
.. method:: ImmediateSetMidRefPercent(percent)
.. method:: ImmediateUnit()
.. method:: ImmediateValue()
.. method:: IsDone()
.. method:: Level()
.. method:: Lock()
.. method:: MathAsSource()
.. method:: MathDefinition()
.. method:: Maximum()
.. method:: Mean()
.. method:: MeasDealayEdge2(edge)
.. method:: MeasDelayDirect(direction)
.. method:: MeasDelayEdge1(edge)
.. method:: MeasImmediateDelayDirect(direction)
.. method:: MeasImmediateDelayEdge(edge)
.. method:: MeasImmediateDelayEdge2(edge)
.. method:: Minimum()
.. method:: ModeInfo()
.. method:: Print()
.. method:: PrintFilePath(path)
.. method:: PulseFormExeDiagram()
.. method:: PulseFormMinusOne()
.. method:: PulseFormPlusOne()
.. method:: Recall(storagelocation)
.. method:: RefAsSource(waveform)
.. method:: RefIsAbsolute()
.. method:: RefIsPercent()
.. method:: ResetStatistics()
.. method:: ResetToFactorySettings()
.. method:: Save(storagelocation)
.. method:: SedLowRefPercent(percent)
.. method:: SetBitrate(rate)
.. method:: SetDate(day, month, year)
.. method:: SetEquivalentTimeSampling()
.. method:: SetHighRefAbsolute(volt)
.. method:: SetHighRefPercent(percent)
.. method:: SetImmediateMeasType(argument)
.. method:: SetInterpolatedSampling()
.. method:: SetLowRefAbsolute(volt)
.. method:: SetMathPos(y)
.. method:: SetMathScale(x)
.. method:: SetMathStorage(number)
.. method:: SetMeasType()
.. method:: SetMidRefAbsolute(volt)
.. method:: SetMidRefPercent(percent)
.. method:: SetRealTimeSampling()
.. method:: SetSampleSize(pointamount)
.. method:: SetThresholdHigh(volt)
.. method:: SetThresholdLow(volt)
.. method:: ShowAllMeasPara()
.. method:: ShowImmediateMeasPara()
.. method:: ShowMathPos()
.. method:: ShowMathScale()
.. method:: ShowMeasurementPara(x)
.. method:: Single()
.. method:: StanDeviation()
.. method:: StartAcquisition()
.. method:: StopAcquisition()
.. method:: Trigger()
.. method:: TriggerLogic(logic)
.. method:: TriggerSetHoldoffTime(time)
.. method:: Unit()
.. method:: Unlock()
.. method:: UseMeasurement(x)
.. method:: Value()
.. method:: Wait()
.. method:: WaitForTrigger()
