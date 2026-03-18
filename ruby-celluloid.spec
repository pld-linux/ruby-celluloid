#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	celluloid
Summary:	Actor-based concurrent object framework for Ruby
Name:		ruby-%{pkgname}
Version:	0.18.0
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	https://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	e0318948364639db1431cb875486f073
URL:		https://github.com/celluloid/celluloid
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
%if %{with tests}
BuildRequires:	ruby-benchmark_suite
BuildRequires:	ruby-guard-rspec
BuildRequires:	ruby-rake
BuildRequires:	ruby-rspec
%endif
Requires:	ruby-rubygems >= 2.0.0
Requires:	ruby-timers < 5
Requires:	ruby-timers >= 4.1.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Celluloid enables people to build concurrent programs out of
concurrent objects just as easily as they build sequential programs
out of sequential objects.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE.txt CHANGES.md
%{ruby_vendorlibdir}/celluloid.rb
%{ruby_vendorlibdir}/celluloid
%{ruby_specdir}/celluloid-%{version}.gemspec
