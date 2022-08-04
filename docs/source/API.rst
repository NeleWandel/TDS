API
===

.. toctree::

   API

Acquisition
---------
| With the commands of the acquisition group it is possible to set up the instruments signal aquisition as well as the way signals are processed into waveforms.

.. method:: Acquisition(acquiremode, mode=None, samplesize=None, WFamount=None, stop=None, fast=None)
| Sets all the options for the acquisition. While it is possible to change these parameters during an ongoing acquisition, it is adviced to change them before starting the acquisition. Starting and stopping an acquisition must be done by :meth:`StartAcquisition` and :meth:`StopAcquisition`.
| 
| All arguments, except ``acquiremode`` are optional. 
| ``acquiremode`` enables the selected mode for aquiring data.
| Valid arguments are:
- :const:`sampling` (Enanbles sampling mode)
- :const:`peakdetect` (Enables peak detect mode)
- :const:`hires` (Enables HiRes mode)
- :const:`averaging` (Enables averaging mode)
- :const:`envelope` (Enables envelope mode)
- :const:`wfmdb` (Enables WFMDB mode)
| 
| ``mode`` sets the wanted samplingmode to either real time (:const:`RT`), interpolated real time (:const:`IT`) or equivalent time (:const:`ET`).
| 
| ``samplesize`` sets the amount of waveform database points that the oscilloscope acquires for a single sequence acquisition. Must be a whole number.
| 
| ``WFamount`` sets the amount of waveforms that will be acquired for averaging and enveloping. Must be a whole number.
| If envelope mode is enabled, a waveform amount of :const:`0` corresponds to infinitely acquisations.
|
| ``stop`` defines whether the acquisition stops after a :const:`single` sequence or :const:`repeat` until stopped with :meth:`StopAcquisition`.
| 
| ``fast`` determines whether fast acquisition mode is turned :const:`on` or :const:`off`.
.. method:: StartAcquisition()
| Starts acquiring data. 
| While changes are possible during an acquisition, it is recommended that all acquisition settings are properly set before starting the acquisition.
.. method:: StopAcquisition()
| Stops acquiring data.

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
| 
| All arguments are optional. Defining none of the arguments, exports with either the default settings or the settings used prior in that session.
| If ``filename`` is only the file name and not the directory the file will be saved in the default hard copy directory (usually ``C:\TekScope\Images\yourimage``)
| If ``filename`` is not specified the file will be saved in the default directory with the default name.
| Valid formats for ``fileformat`` are:
- :const:`BMP`
- :const:`JPEG`
- :const:`PNG`
| 
| ``inksaver`` has three valid states:
- :const:`1` (Displays the display in the usual colors)
- :const:`2` (Changes the background to white)
- :const:`3` (Chooses colors that are well visible on a white background)
| 
| ``palette`` has three valid states:
- :const:`color` (The exported file is in color)
- :const:`gray` (The exported file is in grayscale)
- :const:`baw` (The exported file is in black and white)
| 
| ``fullscreen`` has two valid states:
- :const:`off` (Hides all menu areas)
- :const:`on` (Shows all menu areas)

.. method:: Screenshot(filename=None, inksaver=None, palette=None, orientation=None, fullscreen=None)
| Creates a hardcopy screenshot of everything that can currently be seen on the oscilloscopes screen.
| The format is always BMP. Creation of a screenshot might take a few milliseconds, using a timer in between multiple screenshots is recommended.
| All arguments are optional. Defining none of the arguments, takes a screenshot with either the default settings or the settings used prior in that session.
| If ``filename`` is only the file name and not the directory the file will be saved in the default hard copy directory (usually ``C:\TekScope\Images\yourimage``)
| If ``filename`` is not specified the file will be saved in the default directory with the default name.
| 
| ``inksaver`` has three valid states:
- :const:`1` (Displays the display in the usual colors)
- :const:`2` (Changes the background to white)
- :const:`3` (Chooses colors that are well visible on a white background)
| 
| ``palette`` has three valid states:
- :const:`color` (The screenshot is in color)
- :const:`gray` (The screenshot is in grayscale)
- :const:`baw` (The screenshot is in black and white)
| 
| ``orientation`` has two valid states:
- :const:`1` (The screenshot will be captured in portrait mode)
- :const:`2` (The screenshot will be captured in horizontal mode)
| 
| ``fullscreen`` has two valid states:
- :const:`off` (Hides all menu areas)
- :const:`on` (Shows all menu areas)

Histogram
---------
| Commands of the histogram group control the histogram options and data.
.. method:: Histogram(display=None, source=None, size=None, function=None, state=None, box=None, left=None, top=None, right=None, bottom=None)
| Sets up the histogram, defined by the arguments.
| All arguments are optional. Defining none of the arguments results in this command having no effect.
| ``display`` has three valid states:
- :const:`off` (Disables the display of the histogram, data will still be collected)
- :const:`log` (The histogram display is turned on and set to logarithmic format)
- :const:`lin` (The histogram display is turned on and set to linear format)
| ``source`` sets the source for the histogram. The source may be either CH<x>, MATH<x> or REF<x>. 
| ``size`` is given in devisions and defines the size of the histogram. If the histogram is horizontal, the value may range from 0.1 to 8.0. In case the histogram is vertical, the range is 0.1 to 10.0.
| ``function`` defines whether the histogram is :const:`horizontal` or :const:`vertical`.
| ``state`` defines whether histogram calculations are :const:`ON` or :const:`OFF`.
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
| Commands of the horizontal group control the time bases of the oscilloscope.
.. method:: FastFrame(source=None, count=None, refframe=None, length=None, mode=None, multiframes=None, multisource=None, frameamount=None, start=None)
| Sets up all FastFrame (also known as memory segmentation) parameters.
| All arguments are optional. Not defining any of the arguments results in this command being useless.
| ``source`` defines the reference source. Valid sources are CH<x>, MATH<x> and REF<x> with <x> being an number ranging from 1 through 4.
| ``count`` defines how many frames/segments the FastFrame mode acquires.
| ``refframe`` defines the reference frame number which is then used to calculate the time differences for the frames.
| ``length`` may range from :const:`500` through :const:`400000` and defines the record length to the number of data points in each frame.
| ``mode`` can be either :const:`ALL` or :const:`LIVE`. In live mode adjusting a channel waveform leads to adjustment of all channel and math waveforms, as they get locked together. For example changing the reference frame from CH1 to frame 6 results in CH2, CH3, CH4, MATH1, MATH2, MATH3 and MATH 4 also using frame 6 as reference. All mode the same happens, but on top of that all REF waveforms also adjust to the selected frame.
| ``multiframes`` if turned :const:`on` the oscilloscope displays multiple overlaid frames. Turning on multiframe mode gives access to ``multisource``, ``frameamount`` and ``start``.
| ``multisource`` defines the source for the multiframe mode. This needs to be given, in order for ``frameamount`` and ``start`` to be accessible. Valid sources are :const:`CH<x>`, :const:`MATH<x>` and :const:`REF<x>` with <x> being an number ranging from 1 through 4.
| ``frameamount`` defines the number of overlaying frames. 
| ``start`` defines the starting frame.
.. method:: FastFrameStart()
| Starts FastFrame acquisition.
.. method:: FastFrameStop()
| Stops FastFrame acquisition.
.. method:: Horizontal(rate=None, scale=None, units=None, position=None, resolution=None, roll=None)
| Sets the horizontal parameters of the oscilloscope.
| All arguments are optional.
| ``rate`` in samples for second. Sets the horizontal sample rate of the oscilloscope. Adjusting the rate leads to an automatic adjustment of the record length.
| ``scale`` in seconds per devision. Sets the horizontal scale, range is :const:`2E-10` to :const:`40` (200ps to 40s).
| ``units`` as a string. Sets the unit for the time base. 
| ``position`` in percent. Positions the chosen amout of the waveform to the left of the center. 
| ``resolution`` in data points per frame. The minimum is :const:`500`, maximum is :const:`400000` if only one channel is in use, :const:`200000` if two channels are in use and :const:`100000` in case all four channels are in use.
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

.. method:: DeleteUserMaskSeg(seg):
| Deletes the segment of the user mask defined by ``seg``.

.. method:: Mask(start=True, mask=None, source=None, display=None, counting=None, wfmamount=None, highlights=None, inverted=None, margin=None, polatity=None, stoponfailure=None, failthreshold=None, failscreen=None, logfail=None, logwfm=None, repeat=None, delay=None, auto=None, hdelta=None, vdelta=None, digitalfilter=None, beep=None, failbeep=None)
| The mask function creates, deletes and changes the mask.
| All arguments are optional.
| 
| ``start`` defines whether the mask starts the mask pass/fail testing.
| 
| ``mask`` allows input of a standard mask. A full list of all standard masks can be found on page 419 in the `Online Programmer Manual <https://download.tek.com/manual/PHP014070web.pdf>`_.
| 
| ``source`` sets the source that will be compared against the mask. This may be either :const:`CH<x>`, :const:`MATH<x>` or :const:`REF<x>` with x ranging from 1 through 4.
| 
| ``display`` turns the masks display on screen either :const:`ON` or :const:`OFF`. When turned off, mask counting, testing and autoset are not available.
| 
| ``counting`` turns the mask hit count state to either :const:`ON` or :const:`OFF`. ``display`` must be :const:`ON` to activate the mask counting.
| 
| ``wfmamount`` sets the amount of waveforms to test during a pass/fail test. (Default is 20)
| 
| ``highlights`` turns the highlighting of hits in a mask to either :const:`ON` or :const:`OFF`. If turned on, hits are highlighted in different colors than other waveform data.
| 
| ``inverted`` sets whether or not the mask is inverted. Valid states are :const:`OFF` (default) and :const:`ON`.
| 
| ``margin`` sets the mask margin in percent. Range is :const:`-50` to :const:`50` if no margin is set, it is turned off automatically.
| 
| ``polarity`` sets whether the pass/fail test tests :const:`positive` pulses, :const:`negative` pulses or :const:`both`. 
| 
| ``stoponfailure`` if turned :const:`ON` the oscilloscope stops acquiring data when a failure occurs during a pass/fail test. Turned :const:`OFF` is the default.
| 
| ``failthreshold`` sets the number of failed tested waveforms needed for the pass/fail testing status to change from passing to failing. If WfmDB mode is turned on, it sets the minimum number of hits needed to change the status from passing to failing.
| 
| ``failscreen`` if turned :const:`ON` the oscilloscope generates a screenshot as soon as the status changes to failing. :const:`OFF`turns this feature off. To change the screenshot settings use the :meth:`Screenshot` command beforehand. 
| 
| ``logfail`` if turned :const:`ON` the oscilloscope logs the current date and time to a file as soon as the status changes to failing. :const:`OFF`turns this feature off.
| 
| ``logwfm`` if turned :const:`ON`the oscilloscope copies waveform data from all active channels to files as soon as the status changes to failing. To creat a log of every violation set ``wfamount`` to :const:`1` and ``repeat`` to :const:`ON`.
| :const:`OFF`turns this feature off.
| 
| ``repeat`` if turned :const:`ON` the oscilloscope starts a new pass/fail test after completion.
| 
| ``delay`` in seconds, sets the amount of time the oscilloscope waits after starting a pass/fail test before actually testing. 
| 
| ``auto`` controlls whether auto adjustment is :const:`ON` or :const:`OFF`. Auto adjustment optimises the signal position within the mask in order to minimise hits.
| 
| ``hdelta`` in percent of a devision, defines how far the auto adjustment searches horizontally. 
| 
| ``vdelta`` in percent of a devision, defines how far the auto adjustment searches vertically.
| 
| ``digitalfilter`` turns the digital filter :const:`ON` or :const:`OFF`. The filter simulates optical hardware. 
| It runs on: OC1, OC3, OC12, OC48, FC133, FC266, FC531, FC1063, FC2125Draft, Gigabit Ethernet, Infiniband 2.5Gb, 1394b, 393Mb, 786.4 3Mb, 1.572 Gb.
| 
| ``beep`` if turned :const:`ON` the oscilloscope gives audible feedback on completion of the pass/fail test.
| 
| ``failbeep`` if turned :const:`ON` the oscilloscope gives audible feedback as soon as the status changes to failure.

.. method:: MaskHit()
| Returns the total amount of mask hits.

.. method:: ResetMaskHit()
| Resets the total amount of mask hits.

.. method:: UserMask(seg=None, points=None, amp=None, bit=None, hscale=None, htrigpos=None, patbits=None, presampbits=None, reclength=None, serialtrig=None, trigtosamp=None, voffset=None, vpos=None, vscale=None, width=None)
| Defines and changes the user mask. To use a standard mask, use the :meth:`Mask` command.
| All arguments are optional.
| 
| ``seg`` selects the segment that needs to be modified
| 
| ``points`` are X-Y coordinates that specify the user mask. Points always come in pairs with the horizontal (x) first and the vertical (y) afterwards seperated by commas. There need to be at least two pairs, that have to be listed counterclockwise. If only one pair is given, the segment is marked as undefined.
| **Example:** UserMask(seg=2, points='–2.3e-9, 44e-3,-2.5e-9, 47e-3, 1.2e-9, 44e-3')
| 
| ``amp`` sets the nominal pulse amplitude in volts.
| 
| ``bit`` sets the bitrate in bits per second.
| 
| ``hscale`` in seconds per devision, sets the horizontal resolution used to draw the mask.
| 
| ``htrigpos`` sets the nominal trigger position used to draw the mask as a fraction of the display width. The range is :const:`0.0` to :const:`1.0`.
| 
| ``patbits`` sets the number of bits used for serial trigger.
| 
| ``presampbits`` sets the number of bits before the pulse leading edge in the serial trigger pass/fail test.
| 
| ``reclength`` sets the nominal record length for pulse mask testing.
| 
| ``serialtrig`` sets the type of triggering used in pass/fail testing. Valid types are: :const:``AMI``, :const:``HDB3``, :const:``B3ZS``, :const:``B6ZS``, :const:``B8ZS``, :const:``CMI``, :const:``NRZ``, :const:``MLT3``, :const:``EDGE``.
| 
| ``trigtosamp`` in seconds, sets the time from the leading edge trigger position to the pulse bit sampling position.
| 
| ``voffset`` in volts, sets the vertical offset.
| 
| ``vpos`` in devisions, sets the vertical position of the input channels.
| 
| ``vscale`` in volts per devision, sets the vertical scale for the input channels.
| 
| ``width`` in seconds, sets the bit width.


Math
-----
| Commands of the math group allow for the creation of math-based waveforms. Up to four math based waveforms can be stored and displayed at the same time. :meth:`SetMathStorage` regulates which of the four possible math storages will be used by the other commands in the math group.

.. method:: DefineMath(equation)
| Sets a math based waveform. The equation may consist of waveforms (those can be taken from a channel, a reference or another math equation), measurements, scalar sources, functions, operands and numerical constants. The equation may consist of more than 100 characters. The equation will be saved to the place defined by :meth:`SetMathStorage`.
| Changes to any of the operands lead to changes of the output.
| Examples:
| DefineMath(Ch1+Ch2)
| DefineMath((Ch1-Meas1)/Meas2)
| DefineMath(Intg(Ch1-Avg(Ch1))
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
.. method:: CountMeas(m=meas)
| Returns the amount of values that have been obtained since the last statistical reset. Values that generated an error are not counted.
.. method:: Maximum(m=meas)
| Returns the maximum value found for the measurement defined by ``m`` from :const:`1` to :const:`8`. If ``m`` is not defined, the command will use the value set by :meth:`UseMeasurement` (default is :const:`1`).
.. method:: Mean(m=meas)
| Returns the mean value accumulated for the measurement defined by ``m`` from :const:`1` to :const:`8`. If ``m`` is not defined, the command will use the value set by :meth:`UseMeasurement` (default is :const:`1`).
.. method:: Measure(meastype=None, method=None, m=meas, statistics=None, weightvalue=None, state=None, source=None, source2=None, refmethod=None, high=None, low=None, mid=None, delay=None, edge1=None, edge2=None)
| ``m`` defines the measurement from :const:`1` to :const:`8`. If ``m`` is not defined, the command will use the value set by :meth:`UseMeasurement` (default is :const:`1`)
| 
| ``method`` sets the method used to calculate the 0% and 100% reference level. The valid states are:
- :const:`histogram` (High and low reference levels are set to the most common values above/below the mid point. Best choice for examining pulses.)
- :const:`mean` (High and low reference levels are set to mean values above/below the mid point. Best choice for examining eye patterns)
- :const:`minmax` (High and low reference levels are set to the highest/lowest value of the waveform record.)
| 
| ``delay`` sets the starting point and direction for a measurement. It can be either :const:`forwards` (starting at the beginning of the waveform) or :const:`backwards` (starting at the end of the waveform).
| 
| ``statistics`` controlls the operation and display of statistics. Statistics can be either turned :const:`off`, they can show :const:`all` statistics for all measurements or display the :const:`mean` of each measurement.
| 
| ``weightvalue`` sets the time constant for mean and standard deviation statistical accumulations.
| 
| ``state`` turns measurements :const:`off` or :const:`on`.
| 
| ``source`` sets the source to measure from. It can be :const:`CH<x>`, :const:`MATH<x>`, :const:`REF<x>` with <x> in the range of 1-4 or :const:`HIStogram`.
| 
| ``source2`` sets the sour ce to measure to (for phase or delay measurements). It can be :const:`CH<x>`, :const:`MATH<x>`, :const:`REF<x>` with <x> in the range of 1-4.
| 
| ``refmethod`` defines whether the reference levels are given in :const:`percent` or :const:`absolut` values.
| 
| ``high`` sets the high reference level in either percent or absolute value depending on ``refmethod``.
| 
| ``low`` sets the low reference level in either percent or absolute value depending on ``refmethod``.
| 
| ``mid`` sets the mid reference level in either percent or absolute value depending on ``refmethod``.
| 
| ``edge1`` sets the slope of the edge for the waveform set by ``source``. Can be either :const:`rise` or :const:`fall`.
| 
| ``edge2`` sets the slope of the edge for the waveform set by ``source2``. Can be either :const:`rise` or :const:`fall`.
| 
| ``meastype`` defines the kind of measurement that takes place in the spot selected by ``m``. 
| Valid options are:
.. tabs::
   .. tab:: AMPlitude
   
      | Measures the amplitude of the selected waveform selected.
      | 
      | Amplitude = High - Low 
   .. tab:: AREa
   
      | Measures the voltage over time for the selected waveform in volt-seconds.
      | Area above the ground is positive, area below the ground is negative.
   .. tab:: BURst
   
      | Measures the duration of a burst.
   .. tab:: CARea
   
      | Measures the voltage over time for the first cycle of the selected waveform in volt-seconds.
      | Area above the reference point is positive, area below the reference point.
   .. tab:: CMEan
   
      | Measures the arithmetic mean for the first cycle of the selected waveform.
   .. tab:: CRMs
   
      | Measures the true root mean square voltage for the first cycle of the selected waveform.
   .. tab:: DELay
   
      | Measures the time between the reference amplitude points of the source and destination waveform.
   .. tab:: DISTDUty
   
      | Measures the time between the falling and rising edge of the eye pattern.
   .. tab:: EXTINCTDB
   
      | Measures the extinction ratio for an optical waveform in dB.
      | This only works for fast acquisition signals.
      | 
      | Extinction dB = 10 x (log 10 (High/Low)
   .. tab:: EXTINCTPCT
   
      | Measures the extinction ratio for an optical waveform in percent.
      | This only works for fast acquisition signals.
      | 
      | Extinction % = 100.0 x (Low/High)
   .. tab:: EXTINCTRATIO
   
      | Measures the extinction ratio for an optical waveform.
      | This only works for fast acquisition signals.
      | 
      | Extinction = (High/Low)
   .. tab:: EYEHeight
   
      | Measures the vertical opening of an eye diagram in volts.
   .. tab:: EYEWidth
   
      | Measures the horizontal opening of an eye diagram in seconds.
   .. tab:: FALL
   
      | Measures the time it takes a falling edge to fall from a high reference value (default 90%) to a low reference value (default 10%).
   .. tab:: FREQuency
   
      | Measures the first cycle of the selected waveform in order to form the frequency in Hz.
   .. tab:: HIGH
   
      | Measures the 100% level reference (topline) of the selected waveform.
   .. tab:: HITS
   
      | Measures the number of hits in/on the histogram box.
   .. tab:: LOW
   
      | Measures the 0% level reference (baseline) of the selected waveform.
   .. tab:: MAXimum
   
      | Measures the maximum amplitude of the selected waveform.
      | If ``method=histogram`` the highest voltage or time within the vertical or horizontal histogram.
   .. tab:: MEAN
   
      | Measures the arithmetic mean over the selected waveform.
      | If ``method=histogram`` the average of all aquired points within the histogram will be measured.
   .. tab:: MEDian
   
      | Measures the middle point of the histogram box, meaning that half of the acquired points within the histogram are greater in value, while the other half is less in value.
   .. tab:: MINImum
   
      | Measures the minimum amplitude of the selected waveform.
      | If ``method=histogram`` the lowest voltage or time within the vertical or horizontal histogram.
   .. tab:: NCROss
   
      | Measures the time from trigger point to first falling/negative edge for the selected waveform.
   .. tab:: NDUty
   
      | Measures the negative duty cycle on the first cycle of the selected waveform.
      | This is the ratio of the negative pulse width to the signal period, in percent.
      | 
      | Negative Duty Cycle = (Negative Width)/Period*100%
   .. tab:: NOVershoot
   
      | Measures the negative overshoot value for the selected waveform.
      | 
      | Negative Overshoot = (Low - Minimum) / Amplitude * 100%
   .. tab:: NWIdth
   
      | Measures the negative width for the first pulse in the selected waveform in seconds.
      | The negative width is the distance between the middle reference (default 50%) amplitude points of a negative pulse.
   .. tab:: PBASe
   
      | Measures the base value that will be used in extiction ratio measurements.
   .. tab:: PCROss
   
      | Measures the time from trigger point to first raising/positive edge for the selected waveform.
   .. tab:: PCTCROss
   
      | Measures the location of the eye crossing point in percent.
      | 
      | Crossing percent = 100 * ((EyeCrossingPoint - PBASe)/(PTOP - PBASe))
   .. tab:: PDUty
   
      | Measures the positive duty cycle on the first cycle of the selected waveform.
      | This is the ratio of the positive pulse width to the signal period, in percent.
      | 
      | Positive Duty Cycle = (Positive Width)/Period*100%
   .. tab:: PEAKHits
   
      | Measures the number of points in the largest bin of the histogram.
   .. tab:: PERIod
   
      | Measures the time required to complete the first cycle in a waveform in seconds.
   .. tab:: PHAse
   
      | Measures the phase difference between two waveforms in degrees (360° is equal to one waveform cycle).
   .. tab:: PK2Pk
   
      | Measures the amplitude peak to peak for the selected waveform.
      | If ``method=histogram`` the peak to peak for the histogram is selected instead.
   .. tab:: PKPKJitter
   
      | Measures the minimum and maximum values in the time locations of the cross point.
   .. tab:: PKPKNoise
   
      | Measures the peak to peak noise for the selected waveform. Uses the mid reference level.
   .. tab:: POVershoot
   
      | Measures the posaitive overshoot value for the selected waveform.
      | 
      | Positive Overshoot = (Maximum - High) / Amplitude * 100%
   .. tab:: PTOP
   
      | Measures the top value that is used for the extinction ratio measurement.
   .. tab:: PWIdth
   
      | Measures the positive width for the first pulse in the selected waveform in seconds.
      | The positive width is the distance between the middle reference (default 50%) amplitude points of a positive pulse.
   .. tab:: QFACtor
   
      | Measures the quality factor (ratio eyesize to noise) of the eye diagram.
   .. tab:: RISe
   
      | Measures the time it takes a rising edge to rise from a low reference value (default 90%) to a high reference value (default 10%).
   .. tab:: RMS
   
      | Measures the true root mean square voltage for the selected waveform.
   .. tab:: RMSJitter
   
      | Measures the variance in the time locations of the cross point.
   .. tab:: RMSNoise
   
      | Measures the root mean square noise amplitude at the mid reference level (default 50%) for the selected waveform.
   .. tab:: SIGMA1
   
      | Measures the percentage of points in the histogram that are within one standard deviation of the histogram mean.
   .. tab:: SIGMA2
   
      | Measures the percentage of points in the histogram that are within two standard deviations of the histogram mean.
   .. tab:: SIGMA3
   
      | Measures the percentage of points in the histogram that are within three standard deviations of the histogram mean.
   .. tab:: SIXSigmajit
   
      | Histogram Measurement only.
      | 6 * RMSJitter
      | RMSJitter is defined as one standard deviation at the cross point.
   .. tab:: SNRatio
   
      | Measures the signal to noise ratio.
   .. tab:: STDdev
   
      | Measures the standard deviation of all points within the histogram box.
   .. tab:: UNDEFINED
   
      | Default type. No measurement type is specifies. 
      | Once a measurement type has been chosen :const:`UNDEFINED` can be used to clear the argument again.
   .. tab:: WAVEFORMS
   
      | Measures the number of waveforms used to calculate the histogram.
   
.. method:: Minimum(m=meas)
| Returns the minimum value found for the measurement defined by ``m`` from :const:`1` to :const:`8`. If ``m`` is not defined, the command will use the value set by :meth:`UseMeasurement` (default is :const:`1`).

.. method:: UseMeasurement(x)
| Sets the storage number for every command in the measurement group. ``x`` must range from 1 through 8.
| Default storage is 1.
Status and Error
----------------
.. method:: Clear()
| Clears the event queue, standard event status register and the status byte register. Does not affect the output queue. 
.. method:: IsDone()
| Returns :const:`1` when all operations are finished.
.. method:: Wait()
| The oscilloscope waits with the execution of further commands until all acquisitions are done.
Trigger
-------
.. method:: Trigger(triggertype=None, mode=None, holdhofftime=None, triggerclass=None, CH1=None, CH2=None, CH3=None, CH4=None, function=None, triggerwhen=None, logicmin=None, logicmax=None, source=None, comm=None, bitrate=None, pulseform=None, eyetype=None, clock=None, clocksource=None, polarity=None, clockthreshold=None, setholdsource=None, threshold=None, settime=None, holdtime=None, width=None, low=None, high=None, edgecoupling=None, standard=None, level=None, CH1TH=None, CH2TH=None, CH3TH=None, CH4TH=None, dataformat=None, datapattern=None, timeout=None, timeouttime=None, deltatime=None, transition=None)

| Allows full controll of the trigger settings. All arguments are optional and not every argument is needed for every trigger type. All arguments ordered by ``triggertype`` can be found in the tabs below.
.. tabs::
   .. tab:: edge
   
      | Turns the trigger type to edge. In this state a trigger event is executed when a signal has a specified voltage level and direction.
      | 
      | ``edgesource`` defines the source. This can be either :const:`CH1`, :const:`CH2`, :const:`CH3`, :const:`CH4`, :const:`AUX` or :const:`line`.
      | AUX specifies that an external trigger is used. This must be connected via the auxiliary trigger input connector on the back of the oscilloscope.
      | line specifies that an AC line voltage is used.
      | 
      | ``edgecoupling`` sets the coupling type. Valid states are:
      - :const:`AC` (AC coupling)
      - :const:`DC` (DC coupling)
      - :const:`HFRej` (Removes high frequency components of the DC signal)
      - :const:`LFRej` (Removes low frequency components of the AC signal)
      - :const:`NOISErej` (Low sensitivity DC coupling. This option needs a higher signal amplitude to minimise false triggers)
      | 
      | ``edgeslope`` defines the slope. Valid states are:
      - :const:`rise` (triggers on a rising/positive signal edge)
      - :const:`fall` (triggers on a falling/negative signal edge)
   .. tab:: logic
   
      | Turns the trigger type to logic. In this state the oscilloscope starts a trigger event in case a defined logical situation occurs.
      | 
      | ``CH1``, ``CH2`` and ``CH3`` sets the logical input can be set to :const:`HIGH`, :const:`LOW` or :const:`x`. This specifies the logic that will be used when the trigger detects the trigger threshold level.
      - :const:`HIGH` specifies the logic high
      - :const:`LOW` specifies the logic low
      - :const:`x` specifies that it doesn't matter
      | 
      | Using the ``CH1TH``, ``CH2TH``, ``CH3TH`` and ``CH4TH`` arguments allow for setting the threshold for the respective channel in Volt.
      | 
      | ``level`` in Volt, sets the trigger level. Valid options are either any Volt amount or the preset trigger levels of :const:`ECL` (-1.3V) or :const:`TTL` (1.4V).
      | 
      | ``triggerclass`` has three valid states each with their own set of arguments:
      .. tabs::
         .. tab:: pattern
         
            | With pattern class activated, the oscilloscope generates a trigger event when the logical combinations of channel 1-4 are met.
            | 
            | ``CH4`` sets the logic input for channel 4. The logical input can be set to :const:`HIGH`, :const:`LOW` or :const:`x`.
            | 
            | ``triggerwhen`` specifies the condition under which the trigger will be generated. 
            | Valid states are:
            - :const:`true` (generates a trigger when the pattern becomes true)
            - :const:`false` (generates a trigger when the pattern becomes false)
            - :const:`less` (generates a trigger when the pattern becomes true for less than the duration set by ``logicmax``)
            - :const:`more` (generates a trigger when the pattern becomes true for longer than the duration set by ``logicmin``)
            | 
            | ``logicmax`` sets the duration in seconds that will be used as the time threshold for ``triggerwhen=less``
            | 
            | ``logicmin`` sets the duration in seconds that will be used as the time threshold for ``triggerwhen=more``
         .. tab:: state
            
            | With state class activated, the oscilloscope generates a trigger event when the channel 4 condition is met first and all of channel 1 through 3 conditions are met afterwards.
            | 
            | ``CH4`` sets the slope for channel 4. This can be either :const:`rise` or :const:`fall`.
            | 
            | ``triggerwhen`` specifies whether the trigger occurs when channel 1 through 3 conditions are met (true) or not met (false). The options are :const:`false` and :const:`true`.
         
         .. tab:: sethold
         
            | With sethold class activated, the oscilloscope generates a trigger event when setup and hold between data source and clock source are violated. 
            | 
            | ``setholdsource`` defines the channel that is used as the sethold data source and must be either :const:`1`, :const:`2`, :const:`3` or :const:`4`.
            | 
            | ``clocksource`` defines the channel that is used as the source of the clock and must be either :const:`1`, :const:`2`, :const:`3` or :const:`4`.
            | 
            | ``clockthreshold`` in Volt, defines the voltage threshold for the clock. 
            | 
            | ``threshold`` in Volt, defines the voltage threshold for the sethold data source.
            | 
            | ``settime`` in seconds, specifies the setup time for sethold violation triggering.
            | 
            | ``holdtime`` in seconds, specifies the hold time for sethold violation triggering.
         
   .. tab:: pulse
   
      | Turns the trigger type to pulse. In this state a trigger event is executed when a specified pulse is found.
      | 
      | ``triggerclass`` has five valid states each with their own set of arguments:
      .. tabs::
         .. tab:: glitch
            
            | With the glitch class activated, the oscilloscope executes a trigger event as soon as a pulse with a specified polarity and width is found.
            | 
            | ``polarity`` defines the polarity the pulse needs to trigger. Valid states are:
            - :const:`positive` (The oscilloscope only triggers when the pulse has a positive polarity)
            - :const:`negative` (The oscilloscope only triggers when the pulse has a negative polarity)
            - :const:`both` (The oscilloscope triggers for both cases)
            | 
            | ``triggerwhen`` defines whether the pulse needs to be :const:`wider` or :const:`narrower` than the defined ``width`` in order to trigger. 
            | 
            | ``width`` in seconds, defines the minimum or maximum width (depending on ``triggerwhen``) the pulse needs to have in order to trigger. 
         .. tab:: runt
            
            | With the runt class activated, the oscilloscope executes a trigger event as soon as a pulse crosses the first voltage threshold two times without crossing the second threshold.
            | 
            | ``width`` in seconds, defines the minimum width for a pulse to trigger, when ``triggerwhen`` is set to :const:`greater`.
            | 
            | ``polarity`` defines the polarity the pulse needs to trigger. Valid states are:
            - :const:`positive` (The oscilloscope only triggers when the pulse crosses the low threshold twice without crossing the high threshold)
            - :const:`negative` (The oscilloscope only triggers when the pulse crosses the high threshold twice without crossing the low threshold)
            - :const:`both` (The oscilloscope triggers for both cases)
            | 
            | ``threshold`` sets the upper and lower threshold to predefined values. The two options are :const:`TTL`, which sets the upper threshold to 1.8V and the lower to 800mV, and :const:`ECL`, which sets the upper threshold to -1.1V and the lower to -1.5V. With the ``high`` and ``low`` arguments, the thresholds can be set to user defined values.
            | 
            | ``high`` in Volt, sets the upper threshold.
            | 
            | ``low`` in Volt, sets the lower threshold.
            | 
            | ``triggerwhen`` defines whether the oscilloscope checks for the width of the pulse. The two valid states are:
            - :const:`any` (A pulse of any width can trigger, as long as the polarity is correct.)
            - :const:`greater` (The pulse must be wider than the amount set with ``width`` in order to trigger.)
         .. tab:: width
            
            | With the width class activated, the oscilloscope executes a trigger event as soon as a pulse with a specified polarity is found inside or outside a defined limit.
            | 
            | ``high`` in seconds, sets the upper trigger limit.
            | 
            | ``low`` in seconds, sets the lower trigger limit.
            | 
            | ``polarity`` specifies whether a pulse needs to be :const:`positive` or :const:`negative` for a trigger event to occur.
            | 
            | ``triggerwhen`` defines wether the the pulse must be detected :const:`outside` or :const:`within` the limit to execute a trigger event.
         .. tab:: transition
            
            | With the transition class activated, the oscilloscope executes a trigger event as soon as a pulse crosses two defined thresholds in the same direction within a defined time span.
            | 
            | ``deltatime`` in seconds, sets the timespan during which the pulse crosses need to occur.
            | 
            | ``polarity`` defines the polarity the pulse needs to trigger. Valid states are:
            - :const:`high` (The oscilloscope only triggers when the pulse first crosses the lower and then the higher threshold.)
            - :const:`low` (The oscilloscope only triggers when the pulse frist crosses the higher and then the lower threshold.)
            - :const:`both` (The oscilloscope triggers for both cases.)
            | 
            | ``threshold`` sets the upper and lower threshold to predefined values. The two options are :const:`TTL`, which sets the upper threshold to 1.8V and the lower to 800mV, and :const:`ECL`, which sets the upper threshold to -1.1V and the lower to -1.5V. With the ``high`` and ``low`` arguments, the thresholds can be set to user defined values.
            | 
            | ``high`` in Volt, sets the upper threshold.
            | 
            | ``low`` in Volt, sets the lower threshold.
            | 
            | ``triggerwhen`` defines whether the crossing of the pulse needs to be :const:`faster` or :const:`slower` than ``deltatime``.
         .. tab:: timeout
            
            | With the timeout class activated, the oscilloscope executes a trigger event as soon as a the pulses stop for a set amount of time.
            | 
            | ``polarity`` defines the polarity the pulse needs to trigger. Valid states are:
            - :const:`high` (The oscilloscope only triggers when the pulse edge stays high/positive during the required time out period.)
            - :const:`low` (The oscilloscope only triggers when the pulse edge stays low/negative during the required time out period.)
            - :const:`either` (The oscilloscope triggers for both cases.)
            | 
            | ``timeouttime`` in seconds, defines the time out period.
   .. tab:: comm
   
      | Turns the trigger type to communitcation. In this state a trigger events is executed when a defined communication signal is found.
      | 
      | ``comm`` defines the communication type. Valid states are:
      - :const:`CMI`
      - :const:`AMI`
      - :const:`HDB3`
      - :const:`B3ZS`
      - :const:`B6ZS`
      - :const:`B8ZS`
      | 
      | ``source`` defines the channel that shall be used as communication source. It must be eihter :const:`1`, :const:`2`, :const:`3` or :const:`4`.
      | 
      | ``standard`` defines the standard that shall be applied for the code and bit rate. A table of all viable standard settings can be found on page 646 in the `Online Programmer Manual <https://download.tek.com/manual/PHP014070web.pdf>`_.
      | 
      | ``bitrate`` defines the bits per seconds. This can be any positive number greater than one.
      | 
      | ``pulseform`` defines the pulseform. Valid states are:
      - :const:`plus` (sets the pulseform to plusone, this means the triggering occurs on a positive mark)
      - :const:`minus` (sets the pulseform to minusone, this means the triggering occurs on a negative mark)
      - :const:`eye` (constructs an eye diagram, this can be further specified by ``eyetype``)
      - :const:`zero` (the triggering occurs on a bit representing zero)
      | 
      | ``eyetype`` sets the source type for creating the eye pattern when pulseform=eye. Valid arguments are:
      - :const:`data` (The oscilloscope triggers and shifts in five units intervalls to form the eye pattern.)
      - :const:`clock` (The oscilloscope triggers randomly with respect to the data channel in order to form the eye pattern. No shifts occur.)
      - :const:`recovered` (The oscilloscope uses a phase locked loop on the recovered clock from the data signal. Triggers are random, no shift occurs.)
      | 
      | ``high`` sets the upper communication threshold.
      | ``low`` sets the lower communication threshold.
      | 
      | ``polarity`` sets the clock polarity to either :const:`rise` or :const:`fall`.

   .. tab:: serial
   
      | Turns the trigger type to serial. In this state a trigger event is executed when NRZ-encoded data providing a 32-bit serial word is found.
      | 
      | ``source`` sets the serial source. Source can be :const:`CH1` through :const:`CH4`.
      | 
      | ``standard`` sets the standard that identifies the code and bit rate. Following standards are valid:
      | :const:`OC1`, :const:`OC3`, :const:`OC12`, :const:`FC133`, :const:`FC266`, :const:`FC531`, :const:`FC1063`, :const:`FW139BS400B`, :const:`FW139BS800B`, :const:`ENET1250`, :const:`CUSTom`, :const:`RIO_500M`, :const:`RIO_750M`, :const:`RIO:1G`, :const:`RIO_SERIAL_1G`, :const:`VSROC192`
      | 
      | ``dataformat`` sets the format in which the serial signals are to be expected. Valid choices are :const:`hex` and :const:`binary`.
      | 
      | ``datapattern`` sets the serial pattern to trigger on. Default is :const:`XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX01`.
      | 
      | ``bitrate`` defines the bits per second. Valid range is :const:`1.5e6` to :const:`1.25e9`.
      | 
      | ``code`` any value other than None sets the signal code to NRZ.
      | 
      | ``clocksource`` defines the source of the clock. Can be either :const:`CH1` to :const:`CH4` or :const:`RECOVered`.
      | 
      | ``clock`` sets the clock level in Volt. Level may range from :const:`-9.9e37` to :const:`9.9e37`.
      | 
      | ``polarity`` sets the polarity of the clock to either :const:`rise` or :const:`fall`.

.. method:: TriggerB(state=None, source=None, count=None, time=None, level=None, slope=None)
| Controlls the secondary trigger.
| 
| ``state`` sets the trigger activity to either :const:`ON` or :const:`OFF`.
| 
| ``source`` sets the source for the B trigger. It can be either :const:`AUX` or :const:`CH1` to :const:`CH4`.
| 
| ``count`` sets the amount of :meth:`Trigger` events that must occur before trigger B triggers an event.
| ``time`` sets the time period that must pass after a :meth:`Trigger` event for trigger B to trigger an event. 
| ``time`` and ``count`` cannot be active at the same time.
| 
| ``level`` in Volt, sets the trigger level. Valid options are either any Volt amount or the preset trigger levels of :const:`ECL` (-1.3V) or :const:`TTL` (1.4V).
| 
| ``slope`` sets the slope to either :const:`rise` where the trigger occurs on the rising/positive edge of a signal or :const:`fall` where the trigger occurs on the falling/negative edge of a signal.

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
.. method:: Busy()
| Returns :const:`0` if the oscilloscope is currently not running the :meth:`StartAcquisition` command. Returns :const:`1` if the oscilloscope is acquiring data. 
.. method:: Channel(channelnumber)
| Sets the standard channel for all future commands that have a ``channel`` argument. ``channelnumber`` may only be :const:`1`, :const:`2`, :const:`3` or :const:`4`.
| Default value is :const:`1`.
.. method:: Date()
| Returns the current date of the oscilloscope. 
| The date can be adjusted by using :meth:`SetDate`
.. method:: Header(status='off')
| Turns the headers of the oscilloscope either :const:`on` or :const:`off`
| Turning them off results in the oscilloscope returning only the values.
| Example:
| Header off: ``100``
| Header on: ``:ACQUIRE:NUMAVG 100``
.. method:: Identify()
| Returns information and the identifaction code of the oscilloscope.
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
.. method:: Undo()
| Reverses all changes done by :meth:`AutoSet`. This does affect any changes made after the automatic adjustment. 
.. method:: Unlock()
| Enables all frontpanel buttons and knobs on the oscilloscope, after they have been locked by :meth:`Lock`
