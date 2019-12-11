%define oname iniparse

# Enable legacy Python 2 build
%bcond_without python2

Summary:	INI parser for Python
Name:		python-%{oname}
Version:	0.4
Release:	18
License:	MIT
Group:		Development/Python
Url:		https://pypi.python.org/pypi/iniparse/?
Source0:	http://iniparse.googlecode.com/files/%{oname}-%{version}.tar.gz 
Patch1:		python-iniparse-python3-compat.patch
Patch2:		fix-issue-28.patch
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
Requires:	python-six
Provides:	python3-%{oname} = %{EVRD}

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


%if %{with python2}
%package -n python2-%{oname}
Summary:	INI parser for Python 2 (legacy)
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2-setuptools
Requires:	python2-six

%description -n python2-%{oname}
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
%endif

%prep
%setup -qn %{oname}-%{version}
%patch1 -p0
%patch2 -p1

%if %{with python2}
mkdir ../%{oname}-%{version}-py2
cp -a . ../%{oname}-%{version}-py2
%endif

%build
python3 setup.py build

%if %{with python2}
pushd ../%{oname}-%{version}-py2
python2 setup.py build
popd
%endif

%install
python3 setup.py install --prefix=%{buildroot}%{_prefix}

%if %{with python2}
pushd ../%{oname}-%{version}-py2
python2 setup.py install --prefix=%{buildroot}%{_prefix}
popd
%endif

rm -Rf %{buildroot}%{_prefix}/share/doc/*

%files
%doc Changelog LICENSE LICENSE-PSF README html/* 
%{python3_sitelib}/%{oname}*

%if %{with python2}
%files -n python2-%{oname}
%doc Changelog LICENSE LICENSE-PSF README html/* 
%{python2_sitelib}/%{oname}*
%endif
