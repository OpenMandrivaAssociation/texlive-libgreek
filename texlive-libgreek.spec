%global tl_name libgreek
%global tl_revision 75712

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Greek letters in math mode from Libertinus or Linux Libertine/Biolinum
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/libgreek
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/libgreek.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/libgreek.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/libgreek.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows LaTeX users (especially if using traditional
LaTeX/pdfLaTeX) to set the Greek letters in math mode using the glyphs
from the Libertinus Serif or Sans font via the font support files
provided by Bob Tennent's libertinus-type1 package. All Greek letters
are defined both in \...up and \...it variants. The style (ISO, TeX, or
French i.e. upright) can be modified midway in the document. A "legacy"
mode uses font support from the (obsolete) libertine-legacy package
which maps to the Linux Libertine or Biolinum fonts. This package is for
users who only want to customize Greek letters in math mode.

