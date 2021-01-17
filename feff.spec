Name:		feff
Version:	1.10.1
Release:	1
Summary:	Front-end for FFmpeg
License:	GPLv3
URL:		https://bitbucket.org/admsasha/feff/
Source:		https://bitbucket.org/admsasha/feff/downloads/feff-1.10.1.tar.gz
Group:		Video
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)

Requires:	ffmpeg 

%description
Front-end for FFmpeg written in Qt5

%prep
%autosetup -p1

%build
%qmake_qt5
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
