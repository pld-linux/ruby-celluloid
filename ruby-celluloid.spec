#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	celluloid
Summary:	Actor-based concurrent object framework for Ruby
Name:		ruby-%{pkgname}
Version:	0.15.2
Release:	3
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	ceaf6e864471fa988290bd18b69dc799
URL:		https://github.com/celluloid/celluloid
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
%if %{with tests}
BuildRequires:	ruby-benchmark_suite
BuildRequires:	ruby-guard-rspec
BuildRequires:	ruby-rake
BuildRequires:	ruby-rspec
%endif
Requires:	ruby-rubygems >= 1.3.6
Requires:	ruby-timers < 1.2
Requires:	ruby-timers >= 1.1.0
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
%{ruby_vendorlibdir}/celluloid.rb
%{ruby_vendorlibdir}/celluloid
%{ruby_specdir}/celluloid-%{version}.gemspec
