Name:           gstreamer1-vaapi
Version:        1.16.1
Release:        1%{?dist}
Epoch:          1
Summary:        GStreamer VA-API integration
License:        LGPLv2+
URL:            https://gstreamer.freedesktop.org/modules/gstreamer-vaapi.html

Source0:        https://gstreamer.freedesktop.org/src/gstreamer-vaapi/gstreamer-vaapi-%{version}.tar.xz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  glib2-devel >= 2.32
BuildRequires:  gstreamer1-devel >= %{version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{version}
BuildRequires:  gstreamer1-plugins-bad-devel >= %{version}
BuildRequires:  libtool
BuildRequires:  libvpx-devel
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
#BuildRequires:  pkgconfig(glesv3)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libva) >= 0.34.0
BuildRequires:  pkgconfig(libva-x11) >= 0.31.0
BuildRequires:  pkgconfig(libva-drm) >= 0.33.0
BuildRequires:  pkgconfig(libva-wayland) >= 0.33.0
BuildRequires:  pkgconfig(wayland-client) >= 1.0.2
BuildRequires:  pkgconfig(wayland-cursor) >= 1.0.2
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)

%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

VA-API-based decoder, encoder, postprocessing and video sink elements for
GStreamer.

%package        devel-docs
Summary:        Development documentation for the GStreamer VA-API integration
BuildArch:      noarch
Requires:       %{name}%{?isa} = %{?epoch}:%{version}-%{release}
Requires:       pkgconfig
# Fix for devel-docs not being noarch
Obsoletes:      %{name}-devel-docs < %{?epoch}:%{version}-1
Provides:       %{name}-devel-docs = %{?epoch}:%{version}-%{release}

%description    devel-docs
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains the development documentation for the GStreamer VA-API
integration.

%prep
%autosetup -n gstreamer-vaapi-%{version}

%build
autoreconf -vif
%configure --enable-static=no
%make_build

%install
%make_install
find %{buildroot} -name "*.la" -delete

%ldconfig_scriptlets

%files
%license COPYING.LIB
%doc AUTHORS NEWS README
%{_libdir}/gstreamer-1.0/*.so

%files devel-docs
%doc %{_datadir}/gtk-doc

%changelog
* Fri Dec 18 2020 Simone Caronni <negativo17@gmail.com> - 1:1.16.1-1
- First build for CentOS/RHEL 8.

* Mon Oct 23 2017 Simone Caronni <negativo17@gmail.com> - 1:1.12.3-1
- Update to 1.12.3.

* Thu Jul 20 2017 Simone Caronni <negativo17@gmail.com> - 1:1.12.2-1
- Update to 1.12.2.

* Sat Jun 24 2017 Simone Caronni <negativo17@gmail.com> - 1:1.12.1-1
- Update to 1.12.1.

* Sat May 13 2017 Simone Caronni <negativo17@gmail.com> - 1:1.12.0-1
- Update to 1.12.0.

* Wed Apr 19 2017 Simone Caronni <negativo17@gmail.com> - 1:1.11.90-1
- Update to 1.11.90.

* Mon Dec 05 2016 Simone Caronni <negativo17@gmail.com> - 1:1.10.2-1
- Update to 1.10.2.

* Mon Nov 28 2016 Simone Caronni <negativo17@gmail.com> - 1:1.10.1-1
- Update to 1.10.1.

* Thu Nov 10 2016 Simone Caronni <negativo17@gmail.com> - 1:1.10.0-1
- Update to 1.10.0.

* Thu Nov 03 2016 Simone Caronni <negativo17@gmail.com> - 1:1.9.2-1
- Update to 1.9.2.

* Wed Aug 17 2016 Simone Caronni <negativo17@gmail.com> - 1:1.9.1-1
- Update to 1.9.1.

* Mon Jul 25 2016 Simone Caronni <negativo17@gmail.com> - 1:1.8.2-2
- Fix devel-docs requirements, make subpackage noarch.

* Mon Jun 13 2016 Simone Caronni <negativo17@gmail.com> - 1:1.8.2-1
- First build.
