%define oname iniparse
%define name python-%oname
%define version 0.4
%define release 4

Summary: INI parser for python
Name: %{name}
Version: %{version}
Release: %{release}
Url: http://code.google.com/p/iniparse/
Source: http://iniparse.googlecode.com/files/%{oname}-%{version}.tar.gz 
License: MIT
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch
BuildRequires: python-devel

%description
iniparse is a INI parser for Python which is:

 * Compatiable with ConfigParser: Backward compatible implementations of 
   ConfigParser, RawConfigParser, and SafeConfigParser are included that 
   are API-compatible with the Python standard library. They pass all the 
   unit tests in Python-2.4.4.
 * Preserves structure of INI files: Order of sections & options, indentation, 
   comments, and blank lines are preserved as far as possible when data is 
   updated.
 * More convenient: Values can be accessed using dotted notation 
   (cfg.user.name), or using container syntax (cfg['user']['name']).

It is very useful for config files that are updated both by users and by 
programs, since it is very disorienting for a user to have her config 
file completely rearranged whenever a program changes it. iniparse also 
allows making the order of entries in a config file significant, which is 
desirable in applications like image galleries.


%prep
%setup -q -n %oname-%version

%build
python setup.py build
#perl -pi -e 's|^#!python|#!/usr/bin/python|' easy_install.py setuptools/command/easy_install.py

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --prefix=$RPM_BUILD_ROOT/%_prefix 
rm -Rf $RPM_BUILD_ROOT/%_prefix/share/doc/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changelog LICENSE LICENSE-PSF README html/* 
%py_sitedir/%{oname}*


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4-3mdv2011.0
+ Revision: 667939
- mass rebuild

* Sun Nov 21 2010 Funda Wang <fwang@mandriva.org> 0.4-2mdv2011.0
+ Revision: 599400
- rebuild for py 2.7

* Sat Aug 14 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.4-1mdv2011.0
+ Revision: 569669
- update to new version 0.4

* Sun Apr 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.2-1mdv2010.1
+ Revision: 538756
- update to new version 0.3.2

* Tue Jun 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.1-1mdv2010.0
+ Revision: 384251
- update to new version 0.3.1

* Sun Dec 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.4-1mdv2009.1
+ Revision: 320596
- update to new version 0.2.4

* Sat Aug 16 2008 Michael Scherer <misc@mandriva.org> 0.2.3-1mdv2009.0
+ Revision: 272497
- import python-iniparse


