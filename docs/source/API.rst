API
===

.. toctree::

   API

Acquisition
---------
| With the commands of the acquisition group it is possible to set up the instruments signal aquisition as well as the way signals are processed into waveforms.

.. method:: Acquisition(acquiremode, mode=None, samplesize=None, WFamount=None, stop=None)
| Sets all the options for the acquisition. While it is possible to change these parameters during an ongoing acquisition, it is adviced to change them before starting the acquisition. Starting and stopping an acquisition must be done by :meth:`StartAcquisition` and :meth:`StopAcquisition`.
| 
| **Arguments**
| All arguments, except ``acquiremode`` are optional. 
| ``acquiremode``
| Enables the selected mode for aquiring data.
| Valid arguments are:
- :const:`sampling`
   - Enanbles sampling mode
- :const:`peakdetect`
   - Enables peak detect mode
- :const:`hires`
   - Enables HiRes mode
- :const:`averaging`
   - Enables averaging mode
- :const:`envelope`
   - Enables envelope mode
- :const:`wfmdb`
   - Enables WFMDB mode
| ``mode``
| Sets the wanted samplingmode to either real time, interpolated real time or equivalent time.
| Valid arguments are:
- :const:`RT`
- :const:`IT`
- :const:`ET`
| 
| ``samplesize``
| Sets the amount of waveform database points that the oscilloscope acquires for a single sequence acquisition. Must be a whole number.
| 
| ``WFamount``
| Sets the amount of waveforms that will be acquired for averaging and enveloping. Must be a whole number.
| If envelope mode is enabled, a waveform amount of :const:`0` corresponds to infinitely acquisations.
|
| ``stop``
| Defines whether the acquisition stops after a single sequence or repeats until stopped with :meth:`StopAcquisition`.
| Valid arguments are:
- :const:`repeat`
- :const:`single`
| 
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
.. method:: ProbeCalibration(channel=ch)
| Starts the auto calibration of the probe defined by ``channel``. The calibration can take up to a minutet and no other commands will be executed during that time.
| ``channel`` may range from :const:`1` through :const:`4`. If no channel is given, the system will use either the default channel 1 or the channel selected by :meth:`Channel` if that command had been used during the session.

Hard Copy and Export
--------------------
| The commands of the hard copy and export group allow the creation of data file copies. Export commands can format waveforms as data files.

.. method:: Export(filename=None, fileformat=None, inksaver=None, palette=None, fullscreen=None)
| Copies a waveform to a file that can be specified by ``filename``.
| **Arguments**
| All arguments are optional. Defining none of the arguments, exports with either the default settings or the settings used prior in that session.
| If ``filename`` is only the file name and not the directory the file will be saved in the default hard copy directory (usually ``C:\TekScope\Images\yourimage``)
| If ``filename`` is not specified the file will be saved in the default directory with the default name.
| Valid formats for ``fileformat`` are:
- :const:`BMP`
- :const:`JPEG`
- :const:`PNG`
| ``inksaver`` has three valid states:
- :const:`1`
   - Displays the display in the usual colors
- :const:`2`
   - Changes the background to white
- :const:`3`
   - Chooses colors that are well visible on a white background
| ``palette`` has three valid states:
- :const:`color` 
   - The exported file is in color
- :const:`gray`
   - The exported file is in grayscale
- :const:`baw`
   - The exported file is in black and white
| ``fullscreen`` has two valid states:
- :const:`off`
   - Hides all menu areas
- :const:`on`
   - Shows all menu areas
.. method:: Screenshot(filename=None, inksaver=None, palette=None, orientation=None, fullscreen=None)
| Creates a hardcopy screenshot of everything that can currently be seen on the oscilloscopes screen.
| The format is always BMP. Creation of a screenshot might take a few milliseconds, using a timer in between multiple screenshots is recommended.
| **Arguments**
| All arguments are optional. Defining none of the arguments, takes a screenshot with either the default settings or the settings used prior in that session.
| If ``filename`` is only the file name and not the directory the file will be saved in the default hard copy directory (usually ``C:\TekScope\Images\yourimage``)
| If ``filename`` is not specified the file will be saved in the default directory with the default name.
| ``inksaver`` has three valid states:
- :const:`1`
   - Displays the display in the usual colors
- :const:`2`
   - Changes the background to white
- :const:`3`
   - Chooses colors that are well visible on a white background
| ``palette`` has three valid states:
- :const:`color` 
   - The screenshot is in color
- :const:`gray`
   - The screenshot is in grayscale
- :const:`baw`
   - The screenshot is in black and white
| ``orientation`` has two valid states:
- :const:`1`
   - The screenshot will be captured in portrait mode
- :const:`2`
   - The screenshot will be captured in horizontal mode
| ``fullscreen`` has two valid states:
- :const:`off`
   - Hides all menu areas
- :const:`on`
   - Shows all menu areas

Histogram
---------

.. method:: Histogram(display=None, source=None, size=None, function=None, state=None, box=None, left=None, top=None, right=None, bottom=None)
| Sets up the histogram, defined by the arguments.
| **Arguments**
| All arguments are optional. Defining none of the arguments results in this command having no effect.
| ``display`` has three valid states:
- :const:`off`
   - Disables the display of the histogram, data will still be collected
- :const:`log`
   - The histogram display is turned on and set to logarithmic format
- :const:`lin`
   - The histogram display is turned on and set to linear format
| ``source`` sets the source for the histogram. The source may be either CH<x>, MATH<x> or REF<x>. 
| ``size`` is given in devisions and defines the size of the histogram. If the histogram is horizontal, the value may range from 0.1 to 8.0. In case the histogram is vertical, the range is 0.1 to 10.0.
| ``function`` defines whether the histogram is horizontal or vertical. There are two valid states:
- :const:`horizontal`
- :const:`vertical`
| ``state`` defines whether or not histogram calculations are activated. There are two valid states:
- :const:`ON`
- :const:`OFF`
| ``box`` defines the boundaries of the histogram has two valid arguments:
- :const:`coordinates`
- :const:`percent`
| If ``box`` is used ``left``, ``top``, ``right`` and ``bottom`` must be defined by either the waveform coordinates or the percentage coordinates. 
.. warning::
   Changing the histogram box results in a reset of the histogram data. Make sure to retrieve all wanted data with the :meth:`HistogramData` function before executing changes of the box.

.. method:: HistogramData()
| Returns all histogram data values as an ASCII list, separated by commas.
| A vertical histogram returns 200 values, a horizontal histogram returns 500 values.

.. method:: ResetHistogram()
| Clears all counts and statistics for the histogram.

Horizontal
----------
.. method:: FastFrame(source=None, count=None, refframe=None, length=None, mode=None, multiframes=None, multisource=None, frameamount=None, start=None)
| Sets up all FastFrame (also known as memory segmentation) parameters.
| All arguments are optional. Not defining any of the arguments results in this command being useless.
| **Arguments**
| ``source`` defines the reference source. Valid sources are CH<x>, MATH<x> and REF<x> with <x> being an number ranging from 1 through 4.
| ``count`` defines how many frames/segments the FastFrame mode acquires.
| ``refframe`` defines the reference frame number which is then used to calculate the time differences for the frames.
| ``length`` may range from :const`500` through :const:`400000` and defines the record length to the number of data points in each frame.
| ``mode`` can be either :const:`ALL` or :const:`LIVE`. In live mode adjusting a channel waveform leads to adjustment of all channel and math waveforms, as they get locked together. For example changing the reference frame from CH1 to frame 6 results in CH2, CH3, CH4, MATH1, MATH2, MATH3 and MATH 4 also using frame 6 as reference. All mode the same happens, but on top of that all REF waveforms also adjust to the selected frame.
| ``multiframes`` if turned :const:`on` the oscilloscope displays multiple overlaid frames. Turning on multiframe mode gives access to ``multisource``, ``frameamount`` and ``start``.
| ``multisource`` defines the source for the multiframe mode. This needs to be given, in order for ``frameamount`` and ``start`` to be accessible. Valid sources are CH<x>, MATH<x> and REF<x> with <x> being an number ranging from 1 through 4.
| ``frameamount`` defines the number of overlaying frames. 
| ``start`` defines the starting frame.
.. method:: FastFrameStart()
| Starts FastFrame acquisition.
.. method:: FastFrameStop()
| Stops FastFrame acquisition.
.. method:: Horizontal(rate=None, scale=None, units=None, position=None, resolution=None, roll=None)
| Sets the horizontal parameters of the oscilloscope.
| All arguments are optional.
| **Arguments**
| ``rate`` in samples for second. Sets the horizontal sample rate of the oscilloscope. Adjusting the rate leads to an automatic adjustment of the record length.
| ``scale`` in seconds per devision. Sets the horizontal scale, range is 2E-10 to 40 (200ps to 40s).
| ``units`` as a string. Sets the unit for the time base. 
| ``position`` in percent. Positions the chosen amout of the waveform to the left of the center. 
| ``resolution`` in data points per frame. The minimum is 500, maximum is 400000 if only one channel is in use, 200000 if two channels are in use and 100000 in case all four channels are in use.
| ``roll`` changes the roll mode status. This can be usefull for observing data samples at slow speeds. It has three valid states:
- :const:`AUTO`
- :const:`OFF`
- :const:`ON`
.. method:: TimeDelay(mode='seconds', time='0')
| Sets the horizontal time delay of the oscilloscope.
| ``mode`` can be either :const:`percent` or :const:`seconds`. 
| If ``mode`` is percent, time can be between :const:`1` and :const:`99`.
| If ``mode`` is seconds, time can be any amount in seconds.
| If ``time`` is :const:`0` time delay is turned off.

Mask
----
| Commands in the mask group allow for comparison of incoming waveforms with standard or user-defined masks. It is possible to set actions that the oscilloscope takes in case the waveform falls inside or outside the mask limits.

.. method:: AutoAdjustMaskOff()
| Turns off automatic optimising of the mask.
.. method:: AutoAdjustMaskOn()
| Turns on automatic optimising of the mask. This feature shifts the mask horizontally and vertically in order to minimise the signal hits.
.. method:: Mask(start=True, mask=None, source='CH1', display='ON', counting=None, wfmamount=None, highlights=None, inverted=None, margin=None, polatity=None, stoponfailure=None, failthreshold=None, failscreen=None, logfail=None, logwfm=None, repeat=None, delay=None, auto=None, hdelta=None, vdelta=None, digitalfilter=None, beep=None, failbeep=None)
| The mask function controlls 
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
| Disables the computing and display of the measurement selected by :meth:`UseMeasurement`.
.. method:: EnableCalcAndDisplay()
| Enables the computing and display of the measurement selected by :meth:`UseMeasurement`.
.. method:: HistogramAsSource()
| Selects a histogram as source for all single channel, delay and phase measurements.
.. method:: ImmediateChannelAsSource()
| Selects the channel defined by :meth:`Channel` as source for all immediate single channel, delay and phase measurements.
.. method:: ImmediateHistogramAsSource()
| Selects a histogram as source for all immediate single channel, delay and phase measurements.
.. method:: ImmediateMathAsSource()
| Selects the math definition defined by :meth:`SetMathStorage` as source for all immediate single channel, delay and phase measurements.
.. method:: ImmediateRefAsSource(waveform)
| Selects a reference waveform as source for all immediate single channel, delay and phase measurements.
| ``waveform`` may range from 1 through 4.
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
.. method:: Trigger(triggertype=None, mode=None, holdhofftime=None, triggerclass=None, CH1=None, CH2=None, CH3=None, CH4=None, function=None, triggerwhen=None, logicmin=None, logicmax=None, source=None, comm=None, bitrate=None, pulseform=None, eyetype=None, clock=None, clocksource=None, polarity=None, clockthreshold=None, setholdsource=None, threshold=None, settime=None, holdtime=None, width=None, low=None, high=None, edgecoupling=None, standard=None, level=None, CH1TH=None, CH2TH=None, CH3TH=None, CH4TH=None, dataformat=None, datapattern=None, timeout=None, timeouttime=None, deltatime=None, transition=None)

| Allows full controll of the trigger settings. All arguments are optional and not every argument is needed for every trigger type. All arguments ordered by ``triggertype`` can be found in the tabs below.
.. tabs::
   .. tab:: logic
   
      | Turns the trigger type to logic. In this state the oscilloscope starts a trigger event in case a defined logical situation occurs.
      | ``CH1``, ``CH2`` and ``CH3`` sets the logical input can be set to :const:`HIGH`, :const:`LOW` or :const:`x`. This specifies the logic that will be used when the trigger detects the trigger threshold level.
      | :const:`HIGH`specifies the logic high
      | :const:`LOW` specifies the logic low
      | :const:`x` specifies that it doesn't matter
      | Using the ``CH1TH``, ``CH2TH``, ``CH3TH`` and ``CH4TH`` arguments allow for setting the threshold for the respective channel in Volt.
      | ``triggerclass`` has three valid options that open up more options:
      .. tabs::
         .. tab:: pattern
         
            | ``CH4`` sets the logic input for channel 4. The logical input can be set to :const:`HIGH`, :const:`LOW` or :const:`x`.
            | ``triggerwhen`` specifies the condition under which the trigger will be generated. Valid states are:
            | :const:`true` (generates a trigger when the pattern becomes true)
            | :const:`false` (generates a trigger when the pattern becomes false)
            | :const:`less` (generates a trigger when the pattern becomes true for less than the duration set by ``logicmax``)
            | :const:`more` (generates a trigger when the pattern becomes true for longer than the duration set by ``logicmin``)
            | ``logicmax`` sets the duration in seconds that will be used as the time threshold for ``triggerwhen=less``
            | ``logicmin`` sets the duration in seconds that will be used as the time threshold for ``triggerwhen=more``
         .. tab:: state
         
         
         .. tab:: sethold
         
         
   .. tab:: communication
   
      | test
   .. tab:: edge
   
      | hbas 
   .. tab:: serial
   
      | hola
   .. tab:: pulse
   
      | kjasföskldsf.
      | jisaefioeslf
.. note:: A full list of all viable commands can be found in the `Online Programmer Manual <https://download.tek.com/manual/PHP014070web.pdf>`_.

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
| Reverses all changes done by :meth:`AutoSet`. This does affect any changes made after the automatic adjustment. 
.. method:: Busy()
| Returns :const:`0` if the oscilloscope is currently not running the :meth:`StartAcquisition` command. Returns :const:`1` if the oscilloscope is acquiring data. 
.. method:: Channel(channelnumber)
| Sets the standard channel for all future commands. ``channelnumber`` may only be :const:`1`, :const:`2`, :const:`3` or :const:`4`.
| Default value is :const:`1`.
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
