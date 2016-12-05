Name:           gstreamer1-vaapi
Version:        1.10.2
Release:        1%{?dist}
Epoch:          1
Summary:        GStreamer VA-API integration
License:        LGPLv2+
URL:            https://gstreamer.freedesktop.org/modules/gstreamer-vaapi.html

Source0:        https://gstreamer.freedesktop.org/src/gstreamer-vaapi/gstreamer-vaapi-%{version}.tar.xz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  glib2-devel >= 2.32
BuildRequires:  gstreamer1-devel >= 1.10.0
BuildRequires:  gstreamer1-plugins-base-devel >= 1.10.1
BuildRequires:  gstreamer1-plugins-bad-devel >= 1.10.1
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
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)

%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  pkgconfig(libva-wayland) >= 0.33.0
BuildRequires:  pkgconfig(wayland-client) >= 1.0.2
BuildRequires:  pkgconfig(wayland-cursor) >= 1.0.2
BuildRequires:  pkgconfig(wayland-egl)
%endif

# We can't provide encoders or decoders unless we know what VA-API drivers
# are on the system. Just filter them out, so they're not suggested by
# PackageKit et al.
#global __provides_exclude gstreamer1\\(decoder|gstreamer1\\(encoder

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
%setup -q -n gstreamer-vaapi-%{version}

%build
autoreconf -vif
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -name "*.la" -delete

# rpmlint fixes
#find %{buildroot} -name "*.c" -exec chmod 644 {} \;
#find %{buildroot} -name "*.h" -exec chmod 644 {} \;

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{!?_licensedir:%global license %%doc}
%license COPYING.LIB
%doc AUTHORS NEWS README
%{_libdir}/gstreamer-1.0/*.so

%files devel-docs
# Take the dir and everything below it for proper dir ownership
%doc %{_datadir}/gtk-doc

%changelog
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
