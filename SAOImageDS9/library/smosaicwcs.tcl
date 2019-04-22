#  Copyright (C) 1999-2018
#  Smithsonian Astrophysical Observatory, Cambridge, MA, USA
#  For conditions of distribution and use, see copyright notice in "copyright"

package provide DS9 1.0

proc LoadSMosaicWCSFitsFile {hdr fn layer sys} {
    global loadParam

    set loadParam(file,type) fits
    set loadParam(file,mode) [list mosaic $sys]
    set loadParam(load,type) smmap
    set loadParam(file,name) $fn
    set loadParam(file,header) $hdr
    set loadParam(load,layer) $layer

    ProcessLoad
}

proc ProcessSMosaicWCSCmd {varname iname sock fn} {
    upvar $varname var
    upvar $iname i

    global loadParam
    global current

    set layer {}

    switch -- [string tolower [lindex $var $i]] {
	new {
	    incr i
	    CreateFrame
	}
	mask {
	    incr i
	    set layer mask
	}
	slice {
	    incr i
	    # not supported
	}
    }

    set opt [lindex $var $i]
    if {$opt != {}} {
	incr i
    } else {
	set opt wcs
    }

    if {$sock != {}} {
	# xpa
	if {0} {
	    # not supported
	} else {
	    LoadSMosaicWCSFile [lindex $var $i] [lindex $var [expr $i+1]] \
		$layer $opt
	}
    } else {
	# comm
	if {0} {
	    # not supported
	} else {
	    LoadSMosaicWCSFile [lindex $var $i] [lindex $var [expr $i+1]] \
		$layer $opt
	}
    }
    FinishLoad
}
