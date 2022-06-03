#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Convert-ASN1
Version  : 0.33
Release  : 26
URL      : https://cpan.metacpan.org/authors/id/T/TI/TIMLEGGE/Convert-ASN1-0.33.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TI/TIMLEGGE/Convert-ASN1-0.33.tar.gz
Summary  : 'Convert between perl data structures and ASN.1 encoded packets'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Convert-ASN1-license = %{version}-%{release}
Requires: perl-Convert-ASN1-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
# Convert::ASN1
Convert::ASN1 is a perl library for encoding/decoding data using
ASN.1 definitions

%package dev
Summary: dev components for the perl-Convert-ASN1 package.
Group: Development
Provides: perl-Convert-ASN1-devel = %{version}-%{release}
Requires: perl-Convert-ASN1 = %{version}-%{release}

%description dev
dev components for the perl-Convert-ASN1 package.


%package license
Summary: license components for the perl-Convert-ASN1 package.
Group: Default

%description license
license components for the perl-Convert-ASN1 package.


%package perl
Summary: perl components for the perl-Convert-ASN1 package.
Group: Default
Requires: perl-Convert-ASN1 = %{version}-%{release}

%description perl
perl components for the perl-Convert-ASN1 package.


%prep
%setup -q -n Convert-ASN1-0.33
cd %{_builddir}/Convert-ASN1-0.33

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Convert-ASN1
cp %{_builddir}/Convert-ASN1-0.33/LICENSE %{buildroot}/usr/share/package-licenses/perl-Convert-ASN1/ea2cb01a9b84d75f46c0509059f09d42e670bcc4
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Convert::ASN1.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Convert-ASN1/ea2cb01a9b84d75f46c0509059f09d42e670bcc4

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
