%define oname iniparse
%define name python-%oname
%define version 0.4
%define release %mkrel 1

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
