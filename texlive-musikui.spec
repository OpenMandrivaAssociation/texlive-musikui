Name:		texlive-musikui
Version:	47472
Release:	2
Summary:	Easy creation of "arithmetical restoration" puzzles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/musikui
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/musikui.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/musikui.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package permits to easily typeset arithmetical
restorations using LaTeX. This package requires the graphicx
package.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/musikui
%doc %{_texmfdistdir}/doc/latex/musikui

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
