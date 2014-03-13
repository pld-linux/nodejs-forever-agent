%define		pkg	forever-agent
Summary:	HTTP Agent that keeps socket connections alive between keep-alive requests
Name:		nodejs-%{pkg}
Version:	0.5.2
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	04e9c413b8166eec5ed52e39d6e2bc10
URL:		https://github.com/mikeal/forever-agent
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTTP Agent that keeps socket connections alive between keep-alive
requests. Formerly part of nodejs-request, now a standalone module.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -pr index.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{nodejs_libdir}/%{pkg}
