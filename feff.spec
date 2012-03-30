Name:		feff
Version:	1.7
Release:	%mkrel 1
Summary:	Front-end for FFmpeg
Group:		Video
License:	GPLv3+
URL:		http://qt-apps.org/content/show.php/Feff?content=140298
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	qt4-devel
BuildRequires:	imagemagick
Requires:	ffmpeg

%description
FeFF is a front-end for FFmpeg written in Qt4.

%prep
%setup -q -n %{name}_source

%build
%qmake_qt4 %{name}.pro
%make

%install
%__rm -rf %{buildroot}

# install binary
%__mkdir_p %{buildroot}%{_bindir}
%__cp Bin/%{name} %{buildroot}%{_bindir}/%{name}

# install locales
%__mkdir_p %{buildroot}%{_datadir}/%{name}
%__cp Bin/*.qm %{buildroot}%{_datadir}/%{name}/

# create and install icons
for N in 16 32 48 64 128; do convert %{name}.ico -scale ${N}x${N}! $N.png; done
%__install -D 16.png -m 644 %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%__install -D 32.png -m 644 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%__install -D 48.png -m 644 %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%__install -D 64.png -m 644 %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
%__install -D 128.png -m 644 %{buildroot}%{_iconsdir}/hicolor/128x128/apps/%{name}.png

# XDG menu entry
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Type=Application
Name=FeFF
Comment=FFmpeg front-end
Icon=%{name}
Exec=%{name}
Terminal=false
Categories=AudioVideo;Video;
EOF

%clean
%__rm -rf %{buildroot}

%files
%doc Bin/HISTORY Bin/COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

