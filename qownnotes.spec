#
# Spec file for package qownnotes for openSUSE Linux, Fedora Linux and CentOS 7
#
# Check for Linux distribution version numbers here:
# https://en.opensuse.org/openSUSE:Build_Service_cross_distribution_howto
#

Name: qownnotes
Version: 17.06.6
Release: alt1
License: GPL-2.0
Group: Office
Summary: Note-taking app and todo list manager with ownCloud/Nextcloud integration
Url: http://www.qownnotes.org/

BuildRequires: gcc gcc-c++ fdupes
#BuildRequires: qt5-qtbase
BuildRequires: qt5-base-devel
#BuildRequires: qt5-qtbase-gui
#BuildRequires:  qt5-qtwebkit-devel
#BuildRequires: qt5-qttools qt5-qttools-devel
BuildRequires: qt5-tools-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-declarative-devel
BuildRequires: qt5-xmlpatterns-devel
BuildRequires: desktop-file-utils
#Requires: qt5-qtsvg qt5-qtxmlpatterns
Packager: Konstantin Artyushkin <akv@altlinux.org>

Source: %name-%version.tar.xz

%description
QOwnNotes is the open source notepad and todo list manager, that works together with the default notes application of ownCloud.

So you are able to write down your thoughts with QOwnNotes and edit or search for them later from your mobile device (like with CloudNotes or the ownCloud/Nextcloud web-service.

The notes are stored as plain text files and are synced with ownCloud's/Nextcloud's file sync functionality. Of course other software, like Dropbox can be used too.

I like the concept of having notes accessible in plain text files, like it is done in the ownCloud notes app, to gain a maximum of freedom, but I was not able to find a decent desktop note taking tool or a text editor, that handles them well. Out of this need QOwnNotes was born.

www.qownnotes.org

Author
======
Patrizio Bekerle <patrizio@bekerle.com>

%prep
%setup
mkdir build
pushd build
%qmake_qt5 ..
popd

%build

pushd build
CFLAGS=$RPM_OPT_FLAGS CCFLAGS=$CFLAGS
%make_build
popd

%install
# install application
pushd build
install -D -m 0755 QOwnNotes %buildroot%_bindir/QOwnNotes
popd

# install visuals
install -D -m 0644 QOwnNotes.desktop %buildroot%_desktopdir/QOwnNotes.desktop
install -D -m644 "images/icons/128x128/apps/QOwnNotes.png" "%buildroot%_datadir/pixmaps/QOwnNotes.png"
for format in {16x16,24x24,32x32,48x48,64x64,96x96,128x128,256x256,512x512}; do
    install -D -m644 "images/icons/$format/apps/QOwnNotes.png" "%buildroot%_iconsdir/hicolor/$format/apps/QOwnNotes.png"
    done

install -D -m644 "images/icons/scalable/apps/QOwnNotes.svg" "%buildroot%_iconsdir/hicolor/scalable/apps/QOwnNotes.svg"

# install languages
install -d "%buildroot/%_datadir/QOwnNotes/languages/"
install -D -m644 languages/*.qm "%buildroot/%_datadir/QOwnNotes/languages/"

#fdupes %buildroot%prefix

%files
#doc LICENSE README.md CHANGELOG.md SHORTCUTS.md
#_bindir/QOwnNotes
#_pixmapsdir/QOwnNotes.png

#_iconsdir/hicolor/16x16/apps/QOwnNotes.png
#_iconsdir/hicolor/24x24/apps/QOwnNotes.png
#_iconsdir/hicolor/32x32/apps/QOwnNotes.png
#_iconsdir/hicolor/48x48/apps/QOwnNotes.png
#_iconsdir/hicolor/64x64/apps/QOwnNotes.png
#_iconsdir/hicolor/96x96/apps/QOwnNotes.png
#_iconsdir/hicolor/128x128/apps/QOwnNotes.png
#_iconsdir/hicolor/256x256/apps/QOwnNotes.png
#_iconsdir/hicolor/512x512/apps/QOwnNotes.png
#_datadir/QOwnNotes/languages/QOwnNotes_en.qm
#_datadir/QOwnNotes/languages/QOwnNotes_de.qm
#_datadir/QOwnNotes/languages/QOwnNotes_fr.qm
#_datadir/QOwnNotes/languages/QOwnNotes_pl.qm
#_datadir/QOwnNotes/languages/QOwnNotes_zh.qm
#_datadir/QOwnNotes/languages/QOwnNotes_ru.qm
#_datadir/QOwnNotes/languages/QOwnNotes_pt_BR.qm
#_datadir/QOwnNotes/languages/QOwnNotes_pt_PT.qm
#_datadir/QOwnNotes/languages/QOwnNotes_es.qm
#_datadir/QOwnNotes/languages/QOwnNotes_nl.qm
#_datadir/QOwnNotes/languages/QOwnNotes_hu.qm
#_datadir/QOwnNotes/languages/QOwnNotes_ja.qm
#_datadir/QOwnNotes/languages/QOwnNotes_it.qm
#_datadir/QOwnNotes/languages/QOwnNotes_ar.qm
#_datadir/QOwnNotes/languages/QOwnNotes_uk.qm
#_datadir/QOwnNotes/languages/QOwnNotes_cs.qm
#_datadir/QOwnNotes/languages/QOwnNotes_hr.qm
#_desktopdir/QOwnNotes.desktop

#dir %_iconsdir/hicolor/512x512/apps
#dir %_iconsdir/hicolor/256x256/apps
#dir %_iconsdir/hicolor/128x128/apps
#dir %_iconsdir/hicolor/96x96/apps
#dir %_iconsdir/hicolor/64x64/apps
#dir %_iconsdir/hicolor/48x48/apps
#dir %_iconsdir/hicolor/32x32/apps
#dir %_iconsdir/hicolor/24x24/apps
#dir %_iconsdir/hicolor/16x16/apps
#dir %_iconsdir/hicolor/512x512
#dir %_iconsdir/hicolor/256x256
#dir %_iconsdir/hicolor/128x128
#dir %_iconsdir/hicolor/96x96
#dir %_iconsdir/hicolor/64x64
#dir %_iconsdir/hicolor/48x48
#dir %_iconsdir/hicolor/32x32
#dir %_iconsdir/hicolor/24x24
#dir %_iconsdir/hicolor/16x16
#dir %_iconsdir/hicolor
#dir %_datadir/QOwnNotes/languages
#dir %_datadir/QOwnNotes

%changelog
* Tue Jun 27 2017 Konstantin Artyushkin <akv@altlinux.org> 17.06.6-alt1
- initial build for ALT Sisyphus

