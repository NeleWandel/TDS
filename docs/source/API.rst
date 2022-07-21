API
===

.. toctree::

   API

Acquisition
---------
| With the commands of the acquisition group it is possible to set up the instruments signal aquisition as well as the way signals are processed into waveforms.

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
| Returns the current acquisition mode in the style: ``:ACQuire:MODe AVERAGE`` or ``:ACQuire:MODe SAMPLE``
.. method:: SetEquivalentTimeSampling()
| Sets the sampling method to equivalent time.
.. method:: SetInterpolatedSampling()
| Sets the sampling method to interpolated time.
.. method:: SetRealTimeSampling()
| Sets the sampling method to real time.
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
| With the commands of the calibration group it is possible to perform self-calibrations as well as probe-calibrations.

.. method:: Calibration()
| Starts the auto calibration. 
.. note:: In order for this command to properly work it is recommended to wait around 20 minutes after turning the oscilloscope on. It might take a long time for the oscilloscope to self-calibrate. No other commands will be executed during this time.

Hard Copy and Export
--------------------
| The commands of the hard copy and export group allow the creation of data file copies. Export commands can format waveforms as data files.

.. method:: Export()
| Copies a waveform to a file.
.. method:: ExportFileFormat(ff)
| Changes the file format in which :meth:`Export` will save the waveform.
| Valid formats for ``ff`` are:
- BMP
- JPEG
- PNG
.. method:: ExportFilePath(path)
| Sets the directory and file name under which the file will be saved.
| If ``path`` is only the file name the file will be saved in the default hard copy directory (usually ``C:\TekScope\Images\yourimage``)
.. method:: Screenshot()
| Creates a hardcopy screenshot of everything that can currently be seen on the oscilloscopes screen to the directory chosen by :meth:`ScreenshotFilePath`.
| The format is always BMP. Creation of a screenshot might take a few milliseconds, using a timer in between screenshots is recommended.
.. method:: ScreenshotFilePath(path)
| Sets the directory and file name under which the file will be saved.
| If ``path`` is only the file name the file will be saved in the default hard copy directory (usually ``C:\TekScope\Images\yourimage``)

Histogram
---------

Horizontal
----------


Mask
----
| Commands in the mask group allow for comparison of incoming waveforms with standard or user-defined masks. It is possible to set actions that the oscilloscope takes in case the waveform falls inside or outside the mask limits.

.. method:: AutoAdjustMaskOff()
| Turns off automatic optimising of the mask.
.. method:: AutoAdjustMaskOn()
| Turns on automatic optimising of the mask. This feature shifts the mask horizontally and vertically in order to minimise the signal hits.

Math
-----
| Commands of the math group allow for the creation of math-based waveforms. Up to four math based waveforms can be stored and displayed at the same time. :meth:`SetMathStorage` regulates which of the four possible math storages will be used by the other commands in the math group.

.. method:: DefineMath(equation)
| Sets a math based waveform. The equation may consist of waveforms (those can be taken from a channel, a reference or another math equation), measurements, scalar sources, functions, operands and numerical constants. The equation may consist of more than 100 characters. The equation will be saved to the place defined by :meth:`SetMathStorage`.
| Changes to any of the operands lead to changes of the output.
| Examples:
- DefineMath(Ch1+Ch2)
- DefineMath((Ch1-Meas1)/Meas2)
- DefineMath(Intg(Ch1-Avg(Ch1))
.. method:: DefineMathVariable(varnumber, varvalue)
| Defines a variable that can be used in :meth:`DefineMath`.
| `varnumber` must be a number ranging from 1 through 8 and defines the storage place of the variable.
| `varvalue` can be any value.
.. method:: MathDefinition()
| Returns the current definition for the math waveform stored in the storage selected by :meth:`SetMathStorage`
.. method:: SetMathPos(y)
| Sets the vertical position of the waveform defined by :meth:`DefineMath`. `y` can be either positive or negative and is given in divisions.
| Please make sure to leave a time of at least 0.5 seconds between computing the math definition and changing the vertical positioning, as autoscaling occurs directly after computing. Autoscaling will override any position changes. 
.. method:: SetMathScale(x)
| Sets the horizontal scale of the waveform defined by :meth:`DefineMath`. `x` can be either positive or negative and is given in volt, amper or watt per divisions.
| Viable ranges are from 100.0E-36 through 100.0E+36.
| Please make sure to leave a time of at least 0.5 seconds between computing the math definition and changing the vertical positioning, as autoscaling occurs directly after computing. Autoscaling will override any position changes. 
.. method:: SetMathStorage(number)
| Sets the storage number for every command in the math group. ``number`` must be either 1, 2, 3 or 4.
| Default storage is 1.
.. method:: ShowMathPos()
| Returns the current position set by :meth:`SetMathPos`.
.. method:: ShowMathScale()
| Returns the current scale set by :meth:`SetMathScale`.

Measurement
-----------
.. method:: CountMeasures()
| Returns the number of valid values accumulated by the measurement since the last statistical reset.
.. method:: DisableCalcAndDisplay()
.. method:: EnableCalcAndDisplay()
.. method:: HistogramAsSource()
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
.. method:: MathAsSource()
.. method:: Maximum()
.. method:: Mean()
.. method:: MeasDealayEdge2(edge)
.. method:: MeasDelayDirect(direction)
.. method:: MeasDelayEdge1(edge)
.. method:: MeasImmediateDelayDirect(direction)
.. method:: MeasImmediateDelayEdge(edge)
.. method:: MeasImmediateDelayEdge2(edge)
.. method:: Minimum()
.. method:: RefAsSource(waveform)
.. method:: RefIsAbsolute()
.. method:: RefIsPercent()
.. method:: ResetStatistics()
.. method:: ShowAllMeasPara()
.. method:: ShowImmediateMeasPara()
.. method:: ShowMeasurementPara(x)
.. method:: SetHighRefAbsolute(volt)
.. method:: SetHighRefPercent(percent)
.. method:: SetImmediateMeasType(argument)
.. method:: SetLowRefAbsolute(volt)
.. method:: SetLowRefPercent(percent)
.. method:: SetMeasType()
.. method:: SetMidRefAbsolute(volt)
.. method:: SetMidRefPercent(percent)
.. method:: StanDeviation()
.. method:: Unit()
.. method:: UseMeasurement(x)
| Sets the storage number for every command in the measurement group. ``x`` must range from 1 through 8.
| Default storage is 1.
.. method:: Value()

Trigger
-------
.. method:: ClockPolarityFall()
| Sets the trigger to activate on the falling/negative edge of a signal.
.. method:: ClockPolarityRise()
| Sets the trigger to activate on the rising/positive edge of a signal.
.. method:: CMIPulseFormEyeDiagram()
| Sets the trigger to construct an eye diagram.
.. method:: CMIPulseFormMinusOne()
| Sets the trigger to activate on a negative mark.
.. method:: CMIPulseFormPlusOne()
| Sets the trigger to activate on a positive mark.
.. method:: CMIPulseFormZero()
| Sets the trigger to activate on a bit representing zero.
.. method:: DefineTrigger(trigger)
| Defines the actions that are taken upon trigger. The ``trigger`` can be any amount of commands, seperated by semicolons, up to 80 characters.
.. note:: A full list of all viable commands can be found in the `Online Programmer Manual <https://download.tek.com/manual/PHP014070web.pdf>`_.
.. method:: Level()
| Sets the trigger level to 50% of the max/min value of the trigger input signal. The trigger source must pass this level in order to activate a trigger event.
.. method:: PulseFormEyeDiagram()
| Sets the trigger to construct an eye diagram.
.. method:: PulseFormMinusOne()
| Corresponds to the Isolated +1 on the front panel.
.. method:: PulseFormPlusOne()
| Corresponds to the Isolated -1 on the front panel.
.. method:: SetBitrate(rate)
| Sets the bit rate.
| ``rate`` is in bits per second and must be a positive number over one.
.. method:: SetThresholdHigh(volt)
| Sets the threshold high level. 
| ``volt`` is the new threshold level and must be given in volt.
.. method:: SetThresholdLow(volt)
| Sets the threshold low level.
| ``volt`` is the new threshold level and must be given in volt
.. method:: Trigger()
| Immediately executes all actions defined by :meth:`DefineTrigger`.
.. method:: TriggerLogic(logic)
.. method:: TriggerSetHoldoffTime(time)
.. method:: WaitForTrigger()
| Sets the trigger mode to ``normal``. In this mode a valid trigger event must occur before a trigger is generated.
Vertical
--------
.. method:: ChannelOffset(offset)
| Sets the vertical offset for the channel specified by :meth:`Channel`. ``offset`` needs to be written in mV.
| Depending on the vertical scale factor the range of the channel offset can be either ±100V, ±10V or ±1V.

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
.. method:: Channel(channelnumber)
| Sets the standard channel for all future commands. ``channelnumber`` may only be 1, 2, 3 or 4.
| Default value is ::const::`1`.
.. method:: ChannelAsSource()
| Sets the channel as source for all acquisitions. The channel can be set by :meth:`Channel`
| Other options are: :meth:`MathAsSource`, :meth:`RefAsSource` and :meth:`HistogramAsSource`
.. method:: Clear()
| Clears the ``event queue``, ``standard event status register`` and the ``status byte register``. Does not affect the output queue. 
.. method:: Date()
| Returns the current date of the oscilloscope. 
| The date can be adjusted by using :meth:`SetDate`
.. method:: Identify()
| Prints information and the identifaction code of the oscilloscope.
.. method:: Lock()
| Disables all frontpanel buttons and knobs on the oscilloscope, including the touchscreen.
| The command :meth:`Unlock` enables them again.
.. method:: Recall(storagelocation)
| Sets all oscilloscope settings to a state that was saved via the :meth:`Save` command.
| ``storagelocation`` must range from 1 through 10.
.. method:: ResetToFactorySettings()
| Resets the oscilloscope to the default settings. 
.. method:: Save(storagelocation)
| Saves the current settings of the oscilloscope to a storage location. These settings can be reapplied to the oscilloscope by using the :meth:`Recall` command.
| ``storagelocation`` must range from 1 through 10.
.. method:: SetDate(day, month, year)
| Changes the internal date of the oscilloscope. ``day`` and ``month`` must be two digits, ``year`` must be four digits.
.. method:: Unlock()
| Enables all frontpanel buttons and knobs on the oscilloscope, after they have been locked by :meth:`Lock`
