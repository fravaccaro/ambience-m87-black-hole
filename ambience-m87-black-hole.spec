Name:          ambience-m87-black-hole
Version:       0.0.1
Release:       2
Summary:       M87's black hole
Group:         System/Tools
Vendor:        fravaccaro
Distribution:  SailfishOS
Requires:      sailfish-version >= 3.0.0
BuildArch:     noarch
Packager:      fravaccaro <fravaccaro@jollacommunity.it>
URL:           https://github.com/fravaccaro/ambience-m87-black-hole
License:       GPLv3

%description
An ambience celebrating the first image of a black hole, found in the center of the galaxy M87.

%files
%defattr(-,root,root,-)
/usr/share/ambience/*

%post
chmod 755 /usr/share/ambience/{name}
chmod 755 /usr/share/ambience/{name}/images
chmod 755 /usr/share/ambience/{name}/sounds
chmod 644 /usr/share/ambience/{name}/*.*
chmod 644 /usr/share/ambience/{name}/images/*.*
chmod 644 /usr/share/ambience/{name}/sounds/*.*
systemctl-user restart ambienced.service

%postun
if [ $1 = 0 ]; then
    // Do stuff specific to uninstalls
rm -rf /usr/share/ambience/{name}
systemctl-user restart ambienced.service
else
if [ $1 = 1 ]; then
    // Do stuff specific to upgrades
echo "It's just upgrade"
systemctl-user restart ambienced.service
fi
fi

%changelog
* Thu Apr 11 2019 0.0.1
- First build.
