# revision 27789
# category Package
# catalog-ctan /macros/latex/contrib/libgreek
# catalog-date 2012-09-23 17:25:02 +0200
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-libgreek
Version:	1.0
Release:	12
Summary:	Use Libertine or Biolinum Greek glyphs in mathematics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/libgreek
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/libgreek.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/libgreek.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/libgreek.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is for LaTeX users who wish to use the Libertine or
Biolinum font for the Greek letters in math mode. It is not
necessary to load the libertine package itself, but of course
the Linux-Libertine/Biolinum fonts and LaTeX support files must
have been installed.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/libgreek/libgreek.sty
%doc %{_texmfdistdir}/doc/latex/libgreek/README
%doc %{_texmfdistdir}/doc/latex/libgreek/libgreek.pdf
%doc %{_texmfdistdir}/doc/latex/libgreek/libgreekcheck.tex
#- source
%doc %{_texmfdistdir}/source/latex/libgreek/libgreek.dtx
%doc %{_texmfdistdir}/source/latex/libgreek/libgreek.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
