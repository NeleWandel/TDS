API
===

.. toctree::

   API

Acquisition
---------

.. method:: ActivateAveraging(WaveformAmount)
| Enables the *averaging acquisition mode*. In this mode the oscilloscope averages all acquired values from multiple waveforms and create a waveform based on the averaged values. 
| The number of waveforms that will be analysed must be set by ``WaveformAmount``, with the smallest possible number being 1. The more waveforms shall be analysed the more accurate the result, but the longer the aquisition needs.
.. method:: ActivateEnvelopeMode(WaveformAmount)
| Enables the *envelope acquisition mode*. In this mode the oscilloscope creates a waveform by showing the peak range values of the data points from multiple waveform acquisitions.
| The number of waveforms that will be analysed must be set by ``WaveformAmount``, with the smallest possible number being 1. The more waveforms shall be analysed the more accurate the result, but the longer the aquisition needs.
.. method:: ActivateHiRes()
| Enables the *Hi Res acquisition mode*. In this mode the oscilloscope creates a value by averaging all acquired data points from one waveform.
| The amount of data points that are taken during the acquisition period can be set with the command :meth:`SetSampleSize`.
.. method:: ActivatePeakDetect()
| Enables the *peak detect acquisition mode*. In this mode the oscilloscope creates a vertical column that show off the highest and lowest value of all acquired data points from one waveform.
| The amount of data points that are taken during the acquisition period can be set with the command :meth:`SetSampleSize`.
.. method:: ActivateSampleMode()
| Enables the *sample acquisition mode*. In this mode the oscilloscope creates a waveform with the acquired data points from one waveform.
| The amount of data points that are taken during the acquisition period can be set with the command :meth:`SetSampleSize`.
.. method:: ActivateWFMDBMode()
| Enables the *waveform database mode*. In this mode the oscilloscope acquires threedimensional data from a waveform (amplitude, time, count). The count-value keeps track on how often a specific data point (amplitude + time) has been acquired. The data acquisition starts with a trigger and works the same as *sample mode*, but it compares multiple samples with each other.
| The amount of data points that are taken during the acquisition period can be set with the command :meth:`SetSampleSize`.
.. method:: Continually()
| Sets the aquisition type to continuous. In this state the acquisition continues until it is stopped by :meth:`StopAcquisition`.
.. method:: ModeInfo()
| Returns the current acquisition mode in the style: ``:ACQuire:MODe AVERAGE`` or ``ACQuire:MODe SAMPLE``
.. method:: SetEquivalentTimeSampling()
| 
.. method:: SetInterpolatedSampling()
| 
.. method:: SetRealTimeSampling()
| 
.. method:: SetSampleSize(amount)
| Sets the amount of samples that will be acquired during one acquisition period. 
.. method:: Single()
| Sets the aquisition type to single. In this state the aquisition stops automatically after one period.
.. method:: StartAcquisition()
| Starts acquiring data. 
| While changes are possible during an acquisition, it is recommended that all acquisition settings are properly set before starting the acquisition.
.. method:: StopAcquisition()
| Stops acquiring data.
.. method:: Wait()
| The oscilloscope waits with the execution of further commands until all acquisitions are done.

Calibration
-----------
Hard Copy and Export
--------------------

Mask
----

.. method:: AutoAdjustMaskOff()
| Turns off automatic optimising of the mask.
.. method:: AutoAdjustMaskOn()
| Turns on automatic optimising of the mask. This feature shifts the mask horizontally and vertically in order to minimise the signal hits.
Math
-----
Measurement
-----------
Trigger
-------
.. method:: DefineTrigger(trigger)
| Defines the actions that are taken upon trigger. The ``trigger`` can be any amount of commands, seperated by semicolons, up to 80 characters.
.. note:: A full list of all viable commands can be found in the `Online Programmer Manual <https://download.tek.com/manual/PHP014070web.pdf>`_.
.. method:: Trigger()
| Immediately executes all actions defined by :meth:`DefineTrigger`.
.. method:: TriggerLogic(logic)
.. method:: TriggerSetHoldoffTime(time)
Waveform Transfer
-----------------

Miscellaneous
-------------

.. method:: AutoSet()
| Automatically adjusts the vertical, horizontal and trigger controls in order to privide a stable display of the waveform on the oscilloscope.
| These changes can be undone by using the :meth:`Undo` command.
.. method:: Undo()
| Reverses all changes done by :meth:`AutoSet`. 
.. method:: Busy()
| Returns :const:`0` if the oscilloscope is currently not running the :meth:`StartAcquisition` command. Returns :const:`1` if the oscilloscope is acquiring data. 
.. method:: Calibration()
| Starts the auto calibration. 
.. note:: In order for this command to properly work it is recommended to wait around 20 minutes after turning the oscilloscope on. It might take a long time for the oscilloscope to self-calibrate. No other commands will be executed during this time.
.. method:: Channel(channelnumber)
| Sets the standard channel for all future commands. ``channelnumber`` may only be 1, 2, 3 or 4.
| Default value is ::const::`1`.
.. method:: ChannelAsSource()
| Sets the channel as source for all acquisitions. The channel can be set by :meth:`Channel`
| Other options are: :meth:`MathAsSource`, :meth:`RefAsSource` and :meth:`HistogramAsSource`
.. method:: ChannelOffset(offsetinmV)
.. method:: Clear()
| Clears the ``event queue``, ``standard event status register`` and the ``status byte register``. Does not affect the output queue. 
.. method:: ClockPolarityFall()
.. method:: ClockPolarityRise()
.. method:: CMIPulseFormExeDiagram()
.. method:: CMIPulseFormMinusOne()
.. method:: CMIPulseFormPlusOne()
.. method:: CMIPulseFormZero()

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
| Prints information and the identifaction code of the oscilloscope.
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
.. method:: Print()
.. method:: PrintFilePath(path)
.. method:: PulseFormExeDiagram()
.. method:: PulseFormMinusOne()
.. method:: PulseFormPlusOne()
.. method:: Recall(storagelocation)
| Sets all oscilloscope settings to a state that was saved via the :meth:`Save` command.
| ``storagelocation`` must range from 1 through 10.
.. method:: RefAsSource(waveform)
.. method:: RefIsAbsolute()
.. method:: RefIsPercent()
.. method:: ResetStatistics()
.. method:: ResetToFactorySettings()
| Resets the oscilloscope to the default settings. 
.. method:: Save(storagelocation)
| Saves the current settings of the oscilloscope to a storage location. These settings can be reapplied to the oscilloscope by using the :meth:`Recall`command.
| ``storagelocation`` must range from 1 through 10.
.. method:: SedLowRefPercent(percent)
.. method:: SetBitrate(rate)
.. method:: SetDate(day, month, year)
.. method:: SetHighRefAbsolute(volt)
.. method:: SetHighRefPercent(percent)
.. method:: SetImmediateMeasType(argument)

.. method:: SetLowRefAbsolute(volt)
.. method:: SetMathPos(y)
.. method:: SetMathScale(x)
.. method:: SetMathStorage(number)
.. method:: SetMeasType()
.. method:: SetMidRefAbsolute(volt)
.. method:: SetMidRefPercent(percent)

.. method:: SetThresholdHigh(volt)
.. method:: SetThresholdLow(volt)
.. method:: ShowAllMeasPara()
.. method:: ShowImmediateMeasPara()
.. method:: ShowMathPos()
.. method:: ShowMathScale()
.. method:: ShowMeasurementPara(x)

.. method:: StanDeviation()

.. method:: Unit()
.. method:: Unlock()
.. method:: UseMeasurement(x)
.. method:: Value()

.. method:: WaitForTrigger()
