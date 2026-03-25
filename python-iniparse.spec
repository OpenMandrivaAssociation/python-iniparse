%define module iniparse
%bcond tests 1

Name:		python-iniparse
Summary:	INI parser for Python
Version:	0.5.1
Release:	1
License:	MIT
Group:		Development/Python
URL:		https://github.com/candlepin/python-iniparse
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz
# NOTE	These patches are all merged upstream post-release of v0.5.1, we should be able to remove them for the next release > 0.5.1
# https://github.com/candlepin/python-iniparse/commit/ad3760fd2b8d4a1ed7c83134e4018968b0aa83bb
Patch0:	https://github.com/candlepin/python-iniparse/commit/ad3760fd2b8d4a1ed7c83134e4018968b0aa83bb.patch#/0.5.1-fix-release-versioning.patch
# This fixes building with py3.14
# https://github.com/candlepin/python-iniparse/pull/38/
Patch1:	https://github.com/candlepin/python-iniparse/commit/3267e724a2d5ce0dbd388f62d549d870b76cb0f4.patch#/0.5.1-avoid-the-multiprocessing-forkserver-method.patch
# https://github.com/candlepin/python-iniparse/commit/c5e2a69f0415238d9df2815e0c9f0f72f8467cd9
Patch2:	https://github.com/candlepin/python-iniparse/commit/c5e2a69f0415238d9df2815e0c9f0f72f8467cd9.patch#/0.5.1-fix-a-small-test-error.patch
# https://github.com/candlepin/python-iniparse/commit/d750fe18d3effea95f2f0b60e03b4a8a659b7ea1
Patch3:	https://github.com/candlepin/python-iniparse/commit/d750fe18d3effea95f2f0b60e03b4a8a659b7ea1.patch#/0.5.1-fix-test-warning-message.patch

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python-test
%endif
%rename python2-iniparse

%description
%{name} is a INI parser for Python which is:

Compatible with ConfigParser: Backward compatible implementations of
ConfigParser, RawConfigParser, and SafeConfigParser are included that
are API-compatible with the Python standard library.

Preserves structure of INI files: Order of sections & options, indentation,
comments, and blank lines are preserved as far as possible when data is updated.

More convenient: Values can be accessed using dotted notation (cfg.user.name),
or using container syntax (cfg['user']['name']).

It is very useful for config files that are updated both by users and by
programs, since it is very disorienting for a user to have her config file
completely rearranged whenever a program changes it. iniparse also allows
making the order of entries in a config file significant, which is desirable
in applications like image galleries.

%prep -a
# Remove executable bit from html file
chmod 644 html/index.html

%install -a
# Remove unwanted files, we package these ourselves where we want them.
rm -rf %{buildroot}%{_docdir}/%{module}-%{version}

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
%{__python3} runtests.py
%endif

%files
%doc Changelog README.md html/*
%license LICENSE LICENSE-PSF
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}*.*-info

