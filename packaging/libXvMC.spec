%bcond_with x

Name:           libXvMC
Version:        1.0.8
Release:        0
License:        MIT
Summary:        X-Video Motion Compensation library
Url:            http://xorg.freedesktop.org/
Group:          System/Libraries

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXvMC
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libXvMC/
Source:         %{name}-%{version}.tar.bz2
Source1001: 	libXvMC.manifest
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xv)

%if !%{with x}
ExclusiveArch:
%endif

%description
X-Video Motion Compensation (XvMC), is an extension of the X video
extension (Xv) for the X Window System. The XvMC API allows video
programs to offload portions of the video decoding process to the GPU
video-hardware.

%package devel
Summary:        Development files for the X-Video Motion Compensation library
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
X-Video Motion Compensation (XvMC), is an extension of the X video
extension (Xv) for the X Window System. The XvMC API allows video
programs to offload portions of the video decoding process to the GPU
video-hardware.

This package contains the development headers for the library found
in %name.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%reconfigure
%autogen  --disable-static
make %{?_smp_mflags}

%install
%make_install

%remove_docs

%post  -p /sbin/ldconfig

%postun  -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%license COPYING
%{_libdir}/libXvMC*.so.1*

%files devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_includedir}/X11/*
%{_libdir}/libXvMC*.so
%{_libdir}/pkgconfig/xvmc.pc

%changelog
