lib_LTLIBRARIES = libXvMC.la libXvMCW.la

libXvMC_la_SOURCES = \
         XvMC.c \
         XvMClibint.h

libXvMCW_la_SOURCES = \
	XvMCWrapper.c

libXvMC_la_LIBADD = @DEP_LIBS@
libXvMC_la_CFLAGS = @DEP_CFLAGS@

libXvMCW_la_LIBADD = @DEP_LIBS@
libXvMCW_la_CFLAGS =				\
	@DEP_CFLAGS@				\
	-DXVMC_CONFIGDIR=XConfigDir		\
	-DXVMC_SOVERSION=\"1.0\"		\
	-DXV_SOVERSION=\"1.0\"

libXvMC_la_LDFLAGS = -version-info 7:0:0 -no-undefined


