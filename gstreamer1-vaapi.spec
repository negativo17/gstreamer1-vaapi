Name:           gstreamer1-vaapi
Epoch:          1
Version:        1.14.4
Release:        2%{?dist}
Summary:        GStreamer plugins to use VA API video acceleration
License:        LGPLv2+
URL:            https://cgit.freedesktop.org/gstreamer/gstreamer-vaapi

Source0:        https://gstreamer.freedesktop.org/src/gstreamer-vaapi/gstreamer-vaapi-%{version}.tar.xz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  glib2-devel >= 2.32
BuildRequires:  gstreamer1-devel >= 1.4.0
BuildRequires:  gstreamer1-plugins-bad-free-devel >= 1.4.0
BuildRequires:  gstreamer1-plugins-base-devel >= 1.4.0
BuildRequires:  libdrm-devel
BuildRequires:  libGL-devel
BuildRequires:  libtool
BuildRequires:  libudev-devel
BuildRequires:  libva-devel >= 1.1.0
BuildRequires:  libvpx-devel
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  wayland-devel

%description
A collection of GStreamer plugins to let you make use of VA API video acceleration
from GStreamer applications.

Includes elements for video decoding, display, encoding and post-processing
using VA API (subject to hardware limitations).

%package        devel-docs
Summary:        Developer documentation for GStreamer VA API video acceleration plugins
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

Provides:       gstreamer1-vaapi-devel = %{version}-%{release}
Obsoletes:      gstreamer1-vaapi-devel < 0.6.1-3

%description	devel-docs
The %{name}-devel-docs package contains developer documentation
for the GStreamer VA API video acceleration plugins

%prep
%autosetup -n gstreamer-vaapi-%{version}
sed -i -e 's/-Wno-portability 1.14/-Wno-portability 1.13/g' configure.ac

%build
autoreconf -vif
%configure --enable-static=no

%make_build

%install
%make_install

find %{buildroot} -name "*.la" -delete

%check
make check

%ldconfig_scriptlets

%files
%doc AUTHORS NEWS README
%license COPYING.LIB
%{_libdir}/gstreamer-1.0/*.so

%files devel-docs
%doc AUTHORS NEWS README
%doc %{_datadir}/gtk-doc

%changelog
* Sun May 17 2020 Simone Caronni <negativo17@gmail.com> - 1.14.4-2
- Rebuild for updated dependencies.

* Mon Nov 11 2019 Simone Caronni <negativo17@gmail.com> - 1.14.4-1
- Rebase to 1.14.4.

* Tue May 01 2018 Simone Caronni <negativo17@gmail.com> - 1:1.10.4-2
- Rebuild for updated dependencies.

* Wed Aug 16 2017 Simone Caronni <negativo17@gmail.com> - 1:1.10.4-1
- Update to 1.10.4.

* Wed Aug 17 2016 Simone Caronni <negativo17@gmail.com> - 1:0.7.0-1
- Initial import.
