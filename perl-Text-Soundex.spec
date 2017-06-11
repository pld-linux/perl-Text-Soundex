#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Text
%define		pnam	Soundex
%include	/usr/lib/rpm/macros.perl
Summary:	Text::Soundex - Implementation of the soundex algorithm
Summary(pl.UTF-8):	Text::Soundex - implementacja algorytmu soundex
Name:		perl-Text-Soundex
Version:	3.04
Release:	5
License:	free (see COPYING)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4630d47b42b92470df7b447984a71446
URL:		http://search.cpan.org/dist/Text-Soundex/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Soundex is a phonetic algorithm for indexing names by sound, as
pronounced in English. The goal is for names with the same
pronunciation to be encoded to the same representation so that they
can be matched despite minor differences in spelling. Soundex is the
most widely known of all phonetic algorithms and is often used
(incorrectly) as a synonym for "phonetic algorithm". Improvements to
Soundex are the basis for many modern phonetic algorithms. (Wikipedia,
2007)

This module implements the original soundex algorithm developed by
Robert Russell and Margaret Odell, patented in 1918 and 1922, as well
as a variation called "American Soundex" used for US census data, and
current maintained by the National Archives and Records Administration
(NARA).

The soundex algorithm may be recognized from Donald Knuth's
The Art of Computer Programming. The algorithm described by
Knuth is the NARA algorithm.

%description -l pl.UTF-8
Soundex to algorytm fonetyczny do indeksowania nazw według brzmienia w
języku angielskim. Celem jest, aby nazwy o tej samej wymowie miały
taką samą reprezentację, przez co mogą być dopasowane niezależnie od
niewielkich różnic w pisowni. Soundex to najbardziej znany algorytm
fonetyczny, zwykle używany (niewłaściwie) jako synonim algorytmu
fonetycznego. (Wikipedia angielska, 2007)

Ten moduł implementuje oryginalny algorytm soundex opracowany przez
Roberta Russella oraz Margaret Odell, opatentowany w 1918 i 1922, oraz
wariację o nazwie "soundex amerykański" używany dla danych ludności w
USA, obecnie zarządzany przez NARA (National Archives and Records
Administration).

Algorytm soundex można znaleźć w "The Art of Computer Programming"
Donalda Knutha. Algorytm opisany przez Knutha to algorytm NARA.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

# extract copyright information
%{__sed} -n -e '3,12p' Soundex.pm > COPYING

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING Changes
%{perl_vendorarch}/Text/Soundex.pm
%dir %{perl_vendorarch}/auto/Text/Soundex
%attr(755,root,root) %{perl_vendorarch}/auto/Text/Soundex/Soundex.so
%{_mandir}/man3/Text::Soundex.3pm*
