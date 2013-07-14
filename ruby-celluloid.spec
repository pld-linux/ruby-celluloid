#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	celluloid
Summary:	Actor-based concurrent object framework for Ruby
Name:		ruby-%{pkgname}
Version:	0.14.1
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	0d31912e5b1a1d9fd233e9783e451bc9
URL:		https://github.com/celluloid/celluloid
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-benchmark_suite
BuildRequires:	ruby-guard-rspec
BuildRequires:	ruby-rake
BuildRequires:	ruby-rspec
%endif
Requires:	ruby-rubygems >= 1.3.6
Requires:	ruby-timers >= 1.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Celluloid enables people to build concurrent programs out of
concurrent objects just as easily as they build sequential programs
out of sequential objects.

%prep
%setup -q -n %{pkgname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
