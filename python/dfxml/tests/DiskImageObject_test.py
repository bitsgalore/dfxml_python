#!/usr/bin/env python3

# This software was developed at the National Institute of Standards
# and Technology in whole or in part by employees of the Federal
# Government in the course of their official duties. Pursuant to
# title 17 Section 105 of the United States Code portions of this
# software authored by NIST employees are not subject to copyright
# protection and are in the public domain. For portions not authored
# by NIST employees, NIST has been granted unlimited rights. NIST
# assumes no responsibility whatsoever for its use by other parties,
# and makes no guarantees, expressed or implied, about its quality,
# reliability, or any other characteristic.
#
# We would appreciate acknowledgement if the software is used.

__version__ = "0.2.1"

import os
import sys
import logging

sys.path.append( os.path.join(os.path.dirname(__file__), "../.."))
import dfxml.objects as Objects

import libtest

_logger = logging.getLogger(os.path.basename(__file__))

def test_empty_object():
    dobj = Objects.DFXMLObject(version="1.2.0")
    diobj = Objects.DiskImageObject()
    dobj.append(diobj)

    # Do file I/O round trip.
    (tmp_filename, dobj_reconst) = libtest.file_round_trip_dfxmlobject(dobj)
    try:
        diobj_reconst = dobj_reconst.disk_images[0]
    except:
        _logger.debug("tmp_filename = %r." % tmp_filename)
        raise
    os.remove(tmp_filename)

def test_sector_size():
    dobj = Objects.DFXMLObject(version="1.2.0")
    diobj = Objects.DiskImageObject()
    dobj.append(diobj)

    diobj.sector_size = 2048

    # Do file I/O round trip.
    (tmp_filename, dobj_reconst) = libtest.file_round_trip_dfxmlobject(dobj)
    try:
        diobj_reconst = dobj_reconst.disk_images[0]
        assert diobj_reconst.sector_size == 2048
        assert diobj.sector_size == diobj_reconst.sector_size
    except:
        _logger.debug("tmp_filename = %r." % tmp_filename)
        raise
    os.remove(tmp_filename)
