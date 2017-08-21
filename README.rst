rbco.statcvswrapper
===================

Introduction
------------

rbco.statcvswrapper is an wrapper around StatCVS_ to make it more straightforward to use. It also
solves a problem: it corrects the encoding so accentuation is displayed correctly in the generated
reports.

Installing
----------

1. Download the StatCVS jar from its website.
2. Add an environment variable called ``STATCVS_JAR_PATH`` with the full path to the downloaded JAR.
   Example: ``export STATCVS_JAR_PATH=/home/rafaelb/statcvs.jar``. Normally you want to put this
   at the end of your ``~/.bashrc`` file.
3. Use Python's setuptools to install rbco.statcvswrapper. 
   Example: ``easy_install rbco.statcvswrapper``

Running
-------

1. Change into your working copy directory.
2. Do a ``cvs update``.
3. Run ``statcvs_wrapper .``.

This will issue the command to get the log from CVS, run StatCVS, correct the encoding of the 
report and open the report in Firefox.

.. References
   ----------

.. _StatCVS: http://statcvs.sourceforge.net/

