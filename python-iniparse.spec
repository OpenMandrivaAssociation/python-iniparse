%define oname iniparse

Summary:	INI parser for python
Name:		python-%{oname}
Version:	0.4
Release:	5
License:	MIT
Group:		Development/Python
Url:		http://code.google.com/p/iniparse/
Source0:	http://iniparse.googlecode.com/files/%{oname}-%{version}.tar.gz 
BuildArch:	noarch
BuildRequires:	pkgconfig(python)

%description
iniparse is a INI parser for Python which is:

 * Compatiable with ConfigParser:	Backward compatible implementations of 
   ConfigParser, RawConfigParser, and SafeConfigParser are included that 
   are API-compatible with the Python standard library. They pass all the 
   unit tests in Python-2.4.4.
 * Preserves structure of INI files:	Order of sections & options, indentation, 
   comments, and blank lines are preserved as far as possible when data is 
   updated.
 * More convenient:	Values can be accessed using dotted notation 
   (cfg.user.name), or using container syntax (cfg['user']['name']).

It is very useful for config files that are updated both by users and by 
programs, since it is very disorienting for a user to have her config 
file completely rearranged whenever a program changes it. iniparse also 
allows making the order of entries in a config file significant, which is 
desirable in applications like image galleries.


%prep
%setup -qn %{oname}-%{version}

%build
python setup.py build
#perl -pi -e 's|^#!python|#!/usr/bin/python|' easy_install.py setuptools/command/easy_install.py

%install
python setup.py install --prefix=%{buildroot}/%{_prefix} 
rm -Rf %{buildroot}/%{_prefix}/share/doc/*

%files
%doc Changelog LICENSE LICENSE-PSF README html/* 
%{py_sitedir}/%{oname}*

