%define	oname	txsocksx

Name:		python2-%{oname}
Version:	1.13.0.3
Release:	2
Summary:	Twisted client endpoints for SOCKS{4,4a,5}
Source0:	http://pypi.python.org/packages/source/t/%{oname}/%{oname}-%{version}.tar.gz
License:	ISC
Group:		Development/Python
Url:		https://github.com/habnabit/txsocksx
BuildArch:	noarch
BuildRequires:	python2-setuptools

%description
|txsocksx| is SOCKS4/4a and SOCKS5 client 
endpoints for `Twisted`_ 10.1 or
greater. The code is available on 
github: https://github.com/habnabit/txsocksx.


%prep
%setup -q -n %{oname}-%{version}

%build
python2 setup.py build

%install
python2 setup.py install --root=%{buildroot}

%files
%doc COPYING
%doc README.rst
%doc requirements.txt
%doc version.txt
%{py2_puresitedir}/txsocksx/*.py*
%{py2_puresitedir}/txsocksx/test/*.py*
%{py2_puresitedir}/txsocksx*.egg-info
