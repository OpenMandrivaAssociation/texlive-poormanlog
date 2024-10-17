Name:		texlive-poormanlog
Version:	63400
Release:	2
Summary:	Logarithms and powers with (almost) 9 digits
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/poormanlog
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/poormanlog.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/poormanlog.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This small package (usable with Plain e-TeX, LaTeX, or others)
with no dependencies provides two fast expandable macros
computing logarithms in base 10 and fractional powers of 10.
They handle arguments of 9 digit tokens which stand for either
1 <= d.dddddddd < 10 (for the log) or 0.xxxxxxxxx (for powers
of 10). They achieve a precision of 1ulp for the logarithm and
2ulp for fractional powers of ten. Extension to other numerical
ranges has to be done by user, via own macros or some math
engine. The xintexpr package (at 1.3f) imports the poormanlog
macros as core constituents of its log10(), pow10(), log(),
exp() and pow() functions.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/generic/poormanlog
%doc %{_texmfdistdir}/doc/generic/poormanlog

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
