%define	name	feff
%define	version	1.9.1
%define	release	1
Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Front-end for FFmpeg
License:	GPLv3
URL:		http://qt-apps.org/content/show.php?content=140298#c404149
Source:		http://qt-apps.org/content/show.php?content=140298/%{name}-%{version}.tar.gz
Group:		Video
BuildRequires:	qt4-devel desktop-file-utils imagemagick
Requires:	ffmpeg 

%description
Front-end for FFmpeg written in QT4

%prep
%setup -q 
ln Bin/COPYING COPYING
ln Bin/HISTORY HISTORY

%build
%qmake_qt4 feff.pro
%make 

%install

# menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Categories=X-MandrivaLinux-Multimedia-Video;AudioVideo;Video;
Comment=Front-end for FFmpeg
Exec=feff
GenericName=feff
Icon=feff
Name=feff
StartupNotify=true
Terminal=false
Type=Application
EOF

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop 

#binaries
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 Bin/%{name} %{buildroot}%{_bindir}/

# icons
install -d -m755 $RPM_BUILD_ROOT%{_miconsdir}
convert %{name}.ico -resize 16x16 $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -d -m755 $RPM_BUILD_ROOT%{_iconsdir}
convert %{name}.ico -resize 32x32 $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -d -m755 $RPM_BUILD_ROOT%{_liconsdir}
convert %{name}.ico -resize 48x48 $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
# lang
install -d -m 755 %{buildroot}%{_datadir}/%{name}
# .ts needed for translations to be dropped in the future.
install -m 755  %{name}_*.ts %{buildroot}%{_datadir}/%{name}/
install -m 755  Bin/feff_*.qm %{buildroot}%{_datadir}/%{name}/


%files 
%defattr(-, root, root, -)
%doc HISTORY COPYING
%{_datadir}/%{name}/*.ts
%{_datadir}/%{name}/feff_*.qm
%{_bindir}/%{name}
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/applications/%{name}.desktop

