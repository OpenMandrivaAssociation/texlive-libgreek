Name:		texlive-libgreek
Version:	27789
Release:	1
Summary:	Use Libertine or Biolinum Greek glyphs in mathematics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/libgreek
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/libgreek.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/libgreek.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/libgreek.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
