Name:		texlive-libgreek
Version:	1.0
Release:	1
Summary:	Use Libertine or Biolinum Greek glyphs in mathematics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/libgreek
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/libgreek.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/libgreek.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/libgreek.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package is for LaTeX users who wish to use the Libertine or
Biolinum font for the Greek letters in math mode. It is not
necessary to load the libertine package itself, but of course
the Linux-Libertine/Biolinum fonts and LaTeX support files must
have been installed.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/libgreek/libgreek.sty
%doc %{_texmfdistdir}/doc/latex/libgreek/README
%doc %{_texmfdistdir}/doc/latex/libgreek/libgreek.pdf
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
