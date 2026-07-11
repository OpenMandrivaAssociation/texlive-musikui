%global tl_name musikui
%global tl_revision 47472

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1
Release:	%{tl_revision}.1
Summary:	Easy creation of arithmetical restoration puzzles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/musikui
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/musikui.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/musikui.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package permits to easily typeset arithmetical restorations using
LaTeX. This package requires the graphicx package.

